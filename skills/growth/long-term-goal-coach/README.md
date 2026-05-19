# Long-Term Goal Coach

Convert long-term ambitions into skill milestones, deliberate practice, tracking, and resilience plans.

## Production use

This folder contains a complete portable AI skill:

- `SKILL.md` — system/operator prompt for AI assistants
- `skill.json` — machine-readable manifest
- `sample-input.json` — example runtime request
- `examples.md` — simple examples

## How to invoke

Ask your AI assistant:

```text
Use the skill in this folder: skills/growth/long-term-goal-coach/SKILL.md
Input: [paste your situation]
Return the standard response envelope.
```

## Integration contract

Load `SKILL.md` as the instruction prompt and send user data according to `sample-input.json`. Validate the folder with `python -m skillpack validate`.

## IP and safety

This is an original workflow inspired by the broad problem space of **Grit**. It is not a book summary or replacement.
