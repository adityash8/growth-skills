# Growth Skills

Eight evidence-first Agent Skills for diagnosing and planning product growth.

This repository is for operators who want a decision system, not a bag of tactics. The skills separate facts from assumptions, find the binding constraint, and produce a concrete next move with a measurement plan.

## Catalog

| Skill | Use it for |
|---|---|
| `growth-strategist` | Route an ambiguous growth question to the right diagnostic |
| `growth-audit` | Build an evidence-backed baseline across the full growth system |
| `growth-roadmap` | Turn a diagnosed constraint into a focused quarterly plan |
| `channel-fit-diagnostic` | Choose the acquisition channel the product can structurally support |
| `product-led-acquisition` | Design product mechanics that naturally create new users |
| `retention-state` | Build value that compounds with continued product use |
| `power-user-curve` | Measure engagement depth with L7 or L30 activity histograms |
| `saas-unit-economics-audit` | Test whether acquisition and retention economics can support growth |

## Install

Clone the repository, then copy or symlink the folders under `skills/` into the skills directory used by your Agent Skills-compatible client.

```bash
git clone https://github.com/<owner>/growth-skills.git
```

Examples of common destinations:

```bash
# Claude Code
cp -R growth-skills/skills/* ~/.claude/skills/

# Codex
cp -R growth-skills/skills/* ~/.codex/skills/
```

Other clients can load each `skills/<name>/SKILL.md` directly. No specific model, provider, analytics vendor, or connector is required.

## Use

Invoke a specific skill when you know the job:

```text
Use channel-fit-diagnostic to decide whether this product should lead with paid search, outbound, or product-led sharing.
```

Start with `growth-strategist` when the problem is still vague:

```text
Use growth-strategist to find why growth stalled and choose the next diagnostic.
```

Live data is optional. When data is unavailable, the skills label assumptions and request the smallest useful export instead of inventing precision.

## Quality bar

Every skill includes:

- required inputs;
- an ordered procedure;
- a concrete output contract;
- guardrails against common bad calls;
- handoffs to the next relevant skill.

Run the repository checks with:

```bash
make validate
make test
```

## Non-goals

- channel execution playbooks for ads, SEO, lifecycle messaging, or copywriting;
- private analytics integrations or account-specific instructions;
- universal benchmark targets detached from segment, model, and date;
- automatic spending, publishing, or account changes.

## License and sources

Repository-authored content is MIT licensed. The frameworks cited in `SOURCES.md`, along with associated names and trademarks, remain the property of their respective owners. Attribution does not imply endorsement.
