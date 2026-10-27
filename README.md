# Growth Skills 🚀

Nineteen Agent Skills for growth people who are tired of "10 hacks to 10x your funnel". Each skill finds the one thing actually holding growth back, fixes that, tests it, and only puts the winners on repeat.

Facts and guesses stay apart. Benchmarks come with a date. Nothing spends money or ships to production without a human saying yes.

## The skills

### 🧭 Figure out what's broken

| Skill | Use it to... |
|---|---|
| `growth-strategist` | Turn a vague "growth is slow" into the next decision worth making |
| `growth-audit` | Score the whole growth system and get an evidence-backed baseline |
| `evidence-led-growth-audit` | Ship a full growth audit report where every number has a source |
| `marketing-tagging-audits` | Check that your pixels, GTM, conversion APIs and consent setup report the truth |
| `customer-research` | Pull real pains, triggers and objections out of interviews and reviews |
| `channel-fit-diagnostic` | Pick channels your product, market and pricing can actually support |
| `power-user-curve` | See how deep engagement really goes, cohort by cohort |
| `saas-unit-economics-audit` | Stress-test CAC, payback, margin and LTV by segment |
| `paid-analysis-review` | Fact-check paid media reports and decks before they move budget |
| `conversational-ads-optimization` | Test and scale ads inside AI chat products like ChatGPT |

### 🛠️ Fix it

| Skill | Use it to... |
|---|---|
| `growth-roadmap` | Turn one constraint into a focused quarterly plan |
| `offer-design` | Build an offer people want and you can actually deliver |
| `onboarding-activation` | Get new users to their first win faster |
| `product-led-acquisition` | Let the product show itself to people who don't use it yet |
| `viral-loop` | Measure and improve invites, sharing and collaboration |
| `retention-state` | Make the product more useful the longer someone uses it, without dark patterns |

### 🔁 Prove it and repeat it

| Skill | Use it to... |
|---|---|
| `experiment-design` | Turn a hunch into a test with one metric and a decision rule |
| `paid-media-creative-operations` | Roll out new ad creative in safe batches, with approvals and rollback |
| `marketing-loops` | Put proven plays on a schedule with state, approvals and stop rules |

## The chain

Want the full ride? [`chains/growth-system.md`](chains/growth-system.md) runs the skills in order:

```text
route → baseline → measure → diagnose → roadmap → design → test → execute → loop → learn
```

It's a playbook your agent follows, not a workflow engine. Stages only run when the current constraint needs them.

## Install

```bash
git clone https://github.com/adityash8/growth-skills.git
cp -R growth-skills/skills/growth-strategist ~/.claude/skills/
```

Copy whole skill folders (keep `references/` and `scripts/` inside). They work in any Agent Skills client: Claude Code (`~/.claude/skills/`), Codex (`~/.codex/skills/`), Cursor, and friends.

Start with `growth-strategist`. It routes to the rest.

## Use

```text
Follow the growth-system chain for this product. Stop at each gate when evidence is missing.
Audit our tracking before we trust last month's CAC.
Review this paid media deck. What is actually true?
```

## What this repo won't do

- Ship credentials or private integrations. Bring your own.
- Spend money, publish, message users or touch production on its own.
- Pretend a 2021 benchmark applies to your business.
- Replace your lawyer, accountant or statistician.

## Checks

```bash
make validate   # catalog, chain, frontmatter, size limits, secrets and privacy scan
make test
```

## Credits and license

Frameworks that shaped these skills are credited in [SOURCES.md](SOURCES.md). Everything here is written from scratch under the [MIT License](LICENSE). Want to contribute? Read [CONTRIBUTING.md](CONTRIBUTING.md). Found something sensitive? Use [SECURITY.md](SECURITY.md), not a public issue.

If a skill saves you a meeting, a star is appreciated. ⭐
