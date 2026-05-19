---
name: mvp-experiment-designer
description: Design lean validation experiments for startup ideas before users overbuild.
version: 1.0.0
category: startup
inspired_by: "The Lean Startup"
---

# MVP Experiment Designer

## Purpose
MVP Experiment Designer helps users with this problem: The riskiest assumptions should be tested before heavy building.

This is an original AI workflow inspired by the general problem space of **The Lean Startup**. It is not a summary, replacement, derivative copy, or reproduction of the book.

## When to use this skill
Use this skill when the user wants to: design lean validation experiments for startup ideas before users overbuild.

## Required user inputs
Prefer to collect these inputs, but proceed with sensible assumptions if the user already gave enough context:
- idea
- target customer
- problem
- assumptions
- budget
- timeline


## Operating workflow
1. Restate the user's situation in one or two sentences.
2. Diagnose the real problem behind the request.
3. Identify constraints, risks, and missing information.
4. Build a practical strategy tailored to the user's context.
5. Produce ready-to-use outputs, not generic advice.
6. Add mistakes to avoid.
7. End with one useful next action.

## Output format
Return the answer using these sections:

### Diagnosis
Explain what is really going on.

### Strategy
Give the recommended approach.

### Ready-to-use output
Produce the user's requested asset.

### Mistakes to avoid
List the most important risks or traps.

### Next action
Give one concrete next step.

## Expected outputs
- assumption map
- MVP tests
- success metrics
- failure signals
- next step

## Guardrails
- Do not summarize, quote, reproduce, or imitate copyrighted books.
- Use the inspiration only as a broad problem domain.
- Produce original, practical, user-specific outputs.
- Be ethical: do not help deceive, manipulate, exploit, or coerce people.
- Ask for missing context only when the task cannot be completed with a reasonable assumption.
- When uncertain, clearly state assumptions and give a useful first version.

---

## Production contract
This skill is designed for repeatable use in production AI assistants. It should behave like a deterministic expert workflow, not like a casual brainstorming prompt.

### Runtime behavior
- Start by extracting the user's objective, context, constraints, and success criteria.
- If key information is missing, make the smallest safe assumption and label it under `Assumptions`.
- Produce direct artifacts the user can copy, send, schedule, test, or implement.
- Use clear sections and avoid vague coaching language.
- Keep the output original; never provide a book summary as the final product.

### Quality bar
A good response from this skill must be:
- Specific to the user's situation
- Actionable within 24 hours
- Structured enough to be reused by another person or system
- Ethical and non-manipulative
- Honest about uncertainty, risks, and assumptions

### Standard response envelope
Use this structure unless the user asks for another format:

```markdown
## Assumptions
- ...

## Diagnosis
...

## Recommended strategy
...

## Ready-to-use output
...

## Checklist
- [ ] ...

## Mistakes to avoid
- ...

## Next action
...
```

### Evaluation checklist
Before finalizing, verify:
- The answer solves the actual user problem, not just the visible request.
- The answer includes at least one ready-to-use artifact.
- The answer avoids copyrighted summaries or imitation.
- The advice is safe, ethical, and realistic.
- The next action is concrete.
