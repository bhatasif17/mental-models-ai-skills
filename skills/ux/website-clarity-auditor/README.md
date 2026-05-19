# Website Clarity Auditor

Audit a website or landing page for first-impression clarity, navigation, trust, CTA, and conversion friction.

## Production use

This folder contains a complete portable AI skill:

- `SKILL.md` — system/operator prompt for AI assistants
- `skill.json` — machine-readable manifest
- `sample-input.json` — example runtime request
- `examples.md` — simple examples

## How to invoke

Ask your AI assistant:

```text
Use the skill in this folder: skills/ux/website-clarity-auditor/SKILL.md
Input: [paste your situation]
Return the standard response envelope.
```

## Integration contract

Load `SKILL.md` as the instruction prompt and send user data according to `sample-input.json`. Validate the folder with `python -m skillpack validate`.

## IP and safety

This is an original workflow inspired by the broad problem space of **Don’t Make Me Think**. It is not a book summary or replacement.
