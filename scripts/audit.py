#!/usr/bin/env python3
"""Monthly board health check — audits the repo against SCHEMA.md rules.

Run from the repo root:  python3 scripts/audit.py
Exit code 0 = clean, 1 = issues found. Prints an OK/ISSUES report.
"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
TAGS = {
    'reasoning', 'agent', 'computer-use', 'coding', 'voice', 'cheap-volume',
    'long-context', 'multilingual', 'instruction-following',
}
ENUMS = {
    'status': {'ga', 'preview', 'sunset'},
    'billing_unit': {'per_1m_tokens', 'per_image', 'per_second', 'per_minute',
                     'per_1k_chars', 'per_1m_chars'},
}
REQ = ['id', 'model', 'released', 'status', 'context_tokens', 'price_input',
       'price_output', 'input', 'output', 'tags', 'open_weights', 'best_for',
       'source_date']


def main():
    issues, ok = [], []
    data = yaml.safe_load((ROOT / 'models.yaml').read_text())

    ids = []
    for p in data['providers']:
        for x in p['models']:
            ids.append(x['id'])
            missing = [k for k in REQ if k not in x]
            if missing:
                issues.append(f"{x.get('id', '?')}: missing fields {missing}")
                continue
            x.setdefault('billing_unit', 'per_1m_tokens')
            if not re.fullmatch(r'[a-z0-9-]+', x['id']):
                issues.append(f"{x['id']}: id not kebab-case")
            bad_tags = set(x['tags']) - TAGS
            if bad_tags:
                issues.append(f"{x['id']}: tags outside SCHEMA set: {bad_tags}")
            for f, allowed in ENUMS.items():
                if x[f] not in allowed:
                    issues.append(f"{x['id']}: bad {f}={x[f]}")
            if not re.fullmatch(r'\d{4}(-\d{2})?', str(x['released'])):
                issues.append(f"{x['id']}: released format {x['released']}")
            if x['price_input'] is None and x['billing_unit'] == 'per_1m_tokens':
                issues.append(f"{x['id']}: token-billed model without a price")
    if len(ids) != len(set(ids)):
        dups = sorted({i for i in ids if ids.count(i) > 1})
        issues.append(f'duplicate ids: {dups}')
    else:
        ok.append(f'{len(ids)} unique model ids')

    readme = (ROOT / 'README.md').read_text()
    yaml_ids, readme_ids = set(ids), set(re.findall(r'\| (?:~~)?`([a-z0-9-]+)`', readme))
    # exclude inline-code mentions in Notes cells (e.g. `tts-1`, `deepseek-flash`)
    readme_ids = {i for i in readme_ids if f'`{i}`' in readme and
                  re.search(rf'^\| (?:~~)?`{re.escape(i)}`', readme, re.M)}
    if yaml_ids - readme_ids:
        issues.append(f'in models.yaml but not README: {sorted(yaml_ids - readme_ids)}')
    if readme_ids - yaml_ids:
        issues.append(f'in README but not models.yaml: {sorted(readme_ids - yaml_ids)}')
    if yaml_ids == readme_ids:
        ok.append('README tables and models.yaml in sync')

    res = (ROOT / 'evals' / 'results.md').read_text()
    res_models = set(re.findall(r'\| \d{4}-\d{2}-\d{2} \| ([a-z0-9.-]+) \|', res)) - {'model-id'}
    if res_models - yaml_ids:
        issues.append(f'results.md references unknown models: {sorted(res_models - yaml_ids)}')
    else:
        ok.append(f'evals observations reference only board ids ({len(res_models)} models)')

    pids = []
    for f in sorted((ROOT / 'evals' / 'prompts').glob('*.md')):
        if f.name == 'README.md':
            continue
        t = f.read_text()
        pid, cap = re.search(r'id:\s*(\S+)', t), re.search(r'capability:\s*(\S+)', t)
        if not pid or not cap:
            issues.append(f'{f.name}: missing frontmatter')
        else:
            pids.append(pid.group(1))
            if cap.group(1) not in TAGS:
                issues.append(f'{f.name}: capability outside tag set: {cap.group(1)}')
    if len(pids) == len(set(pids)):
        ok.append(f'{len(pids)} prompts, unique ids, valid capabilities')
    else:
        issues.append('duplicate prompt ids')

    print('== OK ==')
    for s in ok:
        print('  +', s)
    if issues:
        print('== ISSUES ==')
        for s in issues:
            print('  -', s)
        sys.exit(1)
    print('== NO ISSUES ==')


if __name__ == '__main__':
    main()
