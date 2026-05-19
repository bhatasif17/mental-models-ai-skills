# Focus Block Designer

Design realistic deep-work schedules around energy, distractions, deadlines, and shallow-work batching.

## Production use

This folder contains a complete portable AI skill:

- `SKILL.md` — system/operator prompt for AI assistants
- `skill.json` — machine-readable manifest
- `sample-input.json` — example runtime request
- `examples.md` — simple examples

## How to invoke

Ask your AI assistant:

```text
Use the skill in this folder: skills/productivity/focus-block-designer/SKILL.md
Input: [paste your situation]
Return the standard response envelope.
```

## Integration contract

Load `SKILL.md` as the instruction prompt and send user data according to `sample-input.json`. Validate the folder with `python -m skillpack validate`.

## IP and safety

This is an original workflow inspired by the broad problem space of **Deep Work**. It is not a book summary or replacement.
