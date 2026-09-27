#!/usr/bin/env python3
"""Our benchmark runner — runs evals/tasks.yaml against any model in the matrix.

Usage:
  python run.py --make-longctx          # generate the long-context filler prompt once
  python run.py --model kimi-k3                    # run all tasks, save raw outputs
  python run.py --model kimi-k3 --task code-01     # run one task
  python run.py --model kimi-k3 --api-model moonshotai/kimi-k3   # override platform model string
  python run.py --grade --model kimi-k3            # grade saved outputs, append results.yaml
  python run.py --grade --all --judge-model claude-sonnet-5  # grade everything, LLM judges via this model
  python run.py --report                           # standings table

Needs: OPENROUTER_API_KEY in env (one key reaches every provider).
No third-party deps — stdlib only (PyYAML expected; install with: pip install pyyaml).
"""
import argparse, json, os, re, sys, time, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent))  # allow importing repo-level helpers later

import yaml  # pip install pyyaml

TASKS = yaml.safe_load((ROOT / "tasks.yaml").read_text())["tasks"]
RESULTS_PATH = ROOT / "results.yaml"
OUTPUTS = ROOT / "outputs"
LONGCTX_PATH = ROOT / "prompts" / "longctx-01.txt"


def load_models():
    data = yaml.safe_load((ROOT.parent / "models.yaml").read_text())
    return {m["id"]: m for p in data["providers"] for m in p["models"]}


def chat(api_model: str, prompt: str, max_tokens: int = 4000) -> str:
    key = os.environ["OPENROUTER_API_KEY"]
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=json.dumps({
            "model": api_model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens,
        }).encode(),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.loads(r.read())["choices"][0]["message"]["content"]


def make_longctx():
    """~120K-token filler doc with one anchor phrase buried in the middle."""
    LONGCTX_PATH.parent.mkdir(exist_ok=True)
    anchor = "the anchor phrase is qz-7319-mango"
    filler = ("The committee reviewed the quarterly transportation logistics report. "
              "No action was required. ") * 19000
    mid = len(filler) // 2
    doc = filler[:mid] + "\n" + anchor + "\n" + filler[mid:]
    LONGCTX_PATH.write_text(doc)
    print(f"wrote {LONGCTX_PATH} (~{len(doc)//4} tokens est.)")


def get_prompt(task):
    if "prompt_file" in task:
        return LONGCTX_PATH.read_text()
    return task["prompt"]


def cmd_run(args):
    model = load_models()[args.model]
    api_model = args.api_model or args.model
    todo = [t for t in TASKS if not args.task or t["id"] == args.task]
    out_dir = OUTPUTS / args.model
    out_dir.mkdir(parents=True, exist_ok=True)
    for t in todo:
        print(f"[run] {args.model} / {t['id']} ...", flush=True)
        try:
            text = chat(api_model, get_prompt(t))
            (out_dir / f"{t['id']}.txt").write_text(text)
        except Exception as e:
            print(f"  ERROR: {e}")


def grade_output(task, output: str, judge) -> float:
    g = task["grader"]
    if g == "exact":
        return 1.0 if output.strip().lower() == task["answer"].strip().lower() else 0.0
    if g == "contains":
        return 1.0 if task["answer"].lower() in output.lower() else 0.0
    if g == "regex":
        return 1.0 if re.search(task["answer"], output, re.I | re.S) else 0.0
    if g == "judge":
        if not judge:
            raise SystemExit("judge grader needs --judge-model <id>")
        verdict = chat(judge, (
            f"Rubric:\n{task['rubric']}\n\n---\n\nModel output:\n{output}\n\n---\n\n"
            "Does the output satisfy the rubric? Reply with exactly PASS or FAIL."
        ), max_tokens=10)
        return 1.0 if verdict.strip().upper().startswith("PASS") else 0.0
    if g == "human":
        print(f"[human] grade {task['id']} manually: {OUTPUTS}")
        return None  # you fill results.yaml by hand
    raise ValueError(f"unknown grader {g}")


def cmd_grade(args):
    results = yaml.safe_load(RESULTS_PATH.read_text()) if RESULTS_PATH.exists() else {"runs": []}
    for model_id in ([args.model] if not args.all else sorted({p.parent.name for p in OUTPUTS.glob('*/*.txt')})):
        for t in TASKS:
            f = OUTPUTS / model_id / f"{t['id']}.txt"
            if not f.exists():
                continue
            score = grade_output(t, f.read_text(), args.judge_model)
            if score is None:
                continue
            results["runs"] = [r for r in results["runs"]
                               if not (r["model"] == model_id and r["task"] == t["id"])]
            results["runs"].append({
                "model": model_id, "task": t["id"], "capability": t["capability"],
                "score": score, "grader": t["grader"], "judge_model": args.judge_model,
                "date": time.strftime("%Y-%m"),
            })
            print(f"[grade] {model_id} / {t['id']} -> {score}")
    RESULTS_PATH.write_text(yaml.safe_dump(results, sort_keys=False, allow_unicode=True))


def cmd_report(_):
    if not RESULTS_PATH.exists():
        print("no results yet — run: python run.py --model <id> && python run.py --grade --model <id>")
        return
    runs = yaml.safe_load(RESULTS_PATH.read_text())["runs"]
    models = sorted({r["model"] for r in runs})
    tasks = [t["id"] for t in TASKS]
    cell = {(r["model"], r["task"]): r["score"] for r in runs}
    print(f"{'task':<12}" + "".join(f"{m[:18]:>20}" for m in models))
    for t in tasks:
        print(f"{t:<12}" + "".join(f"{cell.get((m, t), '—')!s:>20}" for m in models))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--make-longctx", action="store_true")
    p.add_argument("--model")
    p.add_argument("--task")
    p.add_argument("--api-model", help="platform model string override (default: repo id)")
    p.add_argument("--grade", action="store_true")
    p.add_argument("--all", action="store_true")
    p.add_argument("--judge-model")
    p.add_argument("--report", action="store_true")
    args = p.parse_args()
    if args.make_longctx:
        make_longctx()
    elif args.grade:
        cmd_grade(args)
    elif args.report:
        cmd_report(args)
    elif args.model:
        cmd_run(args)
    else:
        p.print_help()


if __name__ == "__main__":
    main()
