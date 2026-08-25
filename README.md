# Growth Skills

Fourteen evidence-first Agent Skills that connect growth strategy to verified execution.

This repository is for operators who want a decision system, not a bag of tactics. The skills separate facts from assumptions, identify the binding constraint, design a focused intervention, test it, and operationalize only what works.

## Packs

Install only the pack you need. Every skill remains independently usable.

### Strategy and diagnosis

| Skill | Use it for |
|---|---|
| `growth-strategist` | Route an ambiguous growth problem and select the next diagnostic |
| `growth-audit` | Build an evidence-backed baseline across the growth system |
| `customer-research` | Extract pains, triggers, objections, alternatives, and decision criteria |
| `channel-fit-diagnostic` | Choose channels the product, market, and model can support |
| `power-user-curve` | Measure engagement depth and cohort movement |
| `saas-unit-economics-audit` | Test CAC, payback, margin, retention, and LTV by segment |
| `growth-roadmap` | Turn one constraint into a focused quarterly plan |

### Execution and learning

| Skill | Use it for |
|---|---|
| `offer-design` | Build a credible, deliverable commercial offer |
| `onboarding-activation` | Shorten the path to a measurable first-value event |
| `product-led-acquisition` | Expose product value to non-users through normal use |
| `viral-loop` | Measure and improve invitations, collaboration, and sharing loops |
| `retention-state` | Build ethical compounding value and switching costs |
| `experiment-design` | Convert an intervention into a decision-ready test |
| `marketing-loops` | Repeat proven actions with state, approvals, verification, and stop rules |

## Full growth-system chain

[`chains/growth-system.md`](chains/growth-system.md) connects the repository end to end:

```text
route
  → baseline audit
  → constraint-specific diagnosis
  → quarterly roadmap
  → intervention design
  → experiment
  → verified execution
  → recurring loop for winners
  → refreshed strategy
```

The chain is an invoke-in-order playbook, not a workflow engine. Conditional stages run only when the active constraint requires them. The machine-readable stage manifest is [`chains/growth-system.json`](chains/growth-system.json).

## Install

Clone the repository, then copy or symlink individual folders under `skills/` into the skill directory used by your Agent Skills-compatible client.

```bash
git clone https://github.com/<owner>/growth-skills.git
```

Common destinations include:

- Claude Code: `~/.claude/skills/`
- Codex: `~/.codex/skills/`
- Cursor: the configured skills directory
- OpenClaw: the configured skills directory

Install the strategy pack first. Add execution skills only when the agent must operate that part of the chain.

## Use

Invoke a skill by name, or start with the chain:

```text
Follow the growth-system chain for this product. Stop after each gate when evidence is missing.
```

Each skill defines:

- required inputs;
- an evidence-aware procedure;
- a concrete output contract;
- guardrails and stop conditions;
- handoffs to the next relevant skill.

## Non-goals

This repository does not:

- provide platform credentials or private integrations;
- assume access to a particular analytics or advertising vendor;
- auto-spend, publish, message users, or modify production systems;
- replace legal, privacy, finance, or statistical review;
- promise universal growth benchmarks;
- bundle imported marketing packs or client playbooks.

## Validation

```bash
make validate
make test
```

Validation checks catalog and chain parity, frontmatter, description and file-size limits, symlink escapes, common secret formats, and blocked private patterns. The test suite covers failure cases.

## Provenance and license

Repository-authored content is available under the [MIT License](LICENSE). Framework-level influences and the quotation policy are documented in [SOURCES.md](SOURCES.md). Third-party trademarks and source materials remain the property of their owners.

## Contributing and security

Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing a skill. Report sensitive findings through [SECURITY.md](SECURITY.md), not a public issue.
