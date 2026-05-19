# Production Readiness

This repository is now structured as a production-grade portable AI skill library.

## What production-ready means here

These skills are not SaaS plugins by themselves. They are reliable instruction bundles that can be loaded into Claude, Codex, Gemini, ChatGPT, internal AI assistants, or a custom orchestration layer.

Each skill includes:

- `SKILL.md` with an operational prompt and production contract
- `skill.json` manifest for automation
- `sample-input.json` for runtime testing
- `examples.md` for quick manual use
- validation through `python -m skillpack validate`

## Recommended architecture

1. Store skills in GitHub.
2. Validate on every commit through GitHub Actions.
3. In your app, load the chosen skill's `SKILL.md` as system/developer instructions.
4. Pass user context as JSON following `sample-input.json`.
5. Log outputs and evaluate with your own acceptance criteria.

## Safety and IP

The skills are original workflows inspired by general problem domains. They are not summaries, copies, or replacements for copyrighted books.
