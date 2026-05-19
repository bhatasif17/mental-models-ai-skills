# Mental Models AI Skills

A production-ready library of 30 portable AI skills for productivity, sales, startup validation, marketing, UX, decision-making, finance, operations, and personal growth.

These are not book-summary bots. Each skill is an original AI workflow inspired by a broad, high-value problem domain.

## Quick start

```bash
unzip mental-models-ai-skills-production.zip
cd mental-models-ai-skills
python -m skillpack validate
python -m skillpack list
python -m skillpack render negotiation-reply-coach
```

## Repository contents

- `skills/` — 30 production-ready skill folders
- `skillpack/` — small CLI for listing, validating, and rendering skills
- `schemas/` — JSON schemas for manifests and runtime requests
- `tests/` — pytest checks for CI
- `.github/workflows/validate.yml` — GitHub Actions validation
- `docs/` — production and integration docs
- `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` — assistant context files

## Skill folder contract

Each skill contains:

- `SKILL.md` — operational prompt
- `skill.json` — machine-readable manifest
- `sample-input.json` — sample runtime payload
- `README.md` — usage notes
- `examples.md` — simple examples

## Use with an AI assistant

```text
Use the skill at skills/sales/negotiation-reply-coach/SKILL.md.
Follow its production contract.
Here is my input: [paste situation]
```

## Production status

Ready for GitHub, internal assistant use, prompt orchestration, and app integration. It is not a hosted SaaS product by itself.

## IP notice

The skills are original workflows inspired by general problem domains. They do not reproduce, summarize, or replace copyrighted books.
