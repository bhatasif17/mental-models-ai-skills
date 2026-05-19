# AI Skill Repository Instructions

This repo contains portable production AI skills. When a user asks to use a skill:

1. Locate the relevant `skills/<category>/<slug>/SKILL.md`.
2. Follow the skill's production contract exactly.
3. Use the user's situation as runtime input.
4. Produce ready-to-use outputs, not generic summaries.
5. Do not summarize or reproduce copyrighted books.
6. State assumptions and proceed when context is sufficient.

Before editing skills, run:

```bash
python -m skillpack validate
```
