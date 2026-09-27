---
id: tool-sequence
capability: agent
---

You have these tools:
- get_weather(city) -> {temp_c, condition}
- get_time(city) -> {local_time}

User asks: "Is it colder in Oslo or in Helsinki right now, and by how many degrees?"

Write out the exact tool calls you would make (in order), then the final answer
you would give the user.

<!-- What to look for: calls weather for BOTH cities, subtracts correctly, doesn't call get_time (irrelevant) -->
