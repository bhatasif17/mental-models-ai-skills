# Integration Guide

## CLI usage

```bash
python -m skillpack list
python -m skillpack validate
python -m skillpack render negotiation-reply-coach
python -m skillpack prompt mvp-experiment-designer --text "My idea is..."
```

## App integration

Load a skill:

```python
from pathlib import Path
skill_prompt = Path("skills/sales/negotiation-reply-coach/SKILL.md").read_text()
```

Send `skill_prompt` as your system/developer instruction and pass the user's runtime input separately.

## Claude/Codex/Gemini

- Claude/Codex: point the assistant to the target `SKILL.md`.
- Codex: keep `AGENTS.md` in the repo root for repository behavior.
- Gemini: use `GEMINI.md` as project context and ask it to load a target skill folder.
