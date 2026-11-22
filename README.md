# Growth Skills 🚀

**Nineteen skills. One idea. Find what's holding you back, and fix it.** 🎯

Most growth advice is a list of hacks. Ten tricks. Twenty tactics. A hundred things to try.

That's not a strategy. That's a to-do list. 📋

Real growth is simpler. There is always one thing holding you back. Find it. Fix it. Test it. Then put what works on repeat. 🔁

That's what these skills do.

## 🧭 Find what's broken

| | Skill | What it does |
|---|---|---|
| 🧠 | [`growth-strategist`](skills/growth-strategist/SKILL.md) | Turns "growth is slow" into the one decision worth making next |
| 🩺 | [`growth-audit`](skills/growth-audit/SKILL.md) | Scores your whole growth system and gives you a baseline you can trust |
| 📑 | [`evidence-led-growth-audit`](skills/evidence-led-growth-audit/SKILL.md) | Writes a full audit report where every number has a source |
| 🏷️ | [`marketing-tagging-audits`](skills/marketing-tagging-audits/SKILL.md) | Checks that your pixels, GTM, conversion APIs and consent setup tell the truth |
| 🗣️ | [`customer-research`](skills/customer-research/SKILL.md) | Pulls real pains, triggers and objections out of interviews and reviews |
| 📡 | [`channel-fit-diagnostic`](skills/channel-fit-diagnostic/SKILL.md) | Picks the channels your product, market and pricing can actually support |
| 📈 | [`power-user-curve`](skills/power-user-curve/SKILL.md) | Shows how deep engagement really goes, cohort by cohort |
| 💰 | [`saas-unit-economics-audit`](skills/saas-unit-economics-audit/SKILL.md) | Stress-tests CAC, payback, margin and LTV by segment |
| 🔎 | [`paid-analysis-review`](skills/paid-analysis-review/SKILL.md) | Fact-checks paid media reports before they move budget |
| 💬 | [`conversational-ads-optimization`](skills/conversational-ads-optimization/SKILL.md) | Tests and scales ads inside AI chat products like ChatGPT |

## 🛠️ Fix it

| | Skill | What it does |
|---|---|---|
| 🗺️ | [`growth-roadmap`](skills/growth-roadmap/SKILL.md) | Turns one constraint into a focused quarterly plan |
| 🎁 | [`offer-design`](skills/offer-design/SKILL.md) | Builds an offer people want and you can actually deliver |
| 👋 | [`onboarding-activation`](skills/onboarding-activation/SKILL.md) | Gets new users to their first win, faster |
| 🪄 | [`product-led-acquisition`](skills/product-led-acquisition/SKILL.md) | Lets your product show itself to people who don't use it yet |
| 🌱 | [`viral-loop`](skills/viral-loop/SKILL.md) | Measures and improves invites, sharing and collaboration |
| 🏠 | [`retention-state`](skills/retention-state/SKILL.md) | Makes your product more useful the longer someone uses it. No dark patterns. |

## 🔁 Prove it. Then repeat it.

| | Skill | What it does |
|---|---|---|
| 🧪 | [`experiment-design`](skills/experiment-design/SKILL.md) | Turns a hunch into a test with one metric and one decision rule |
| 🎨 | [`paid-media-creative-operations`](skills/paid-media-creative-operations/SKILL.md) | Rolls out new ad creative in safe batches, with approvals and rollback |
| ⏱️ | [`marketing-loops`](skills/marketing-loops/SKILL.md) | Puts proven plays on a schedule, with state, approvals and stop rules |

## ⛓️ One more thing

The skills don't just work alone. They work as one chain. 🔗

[`chains/growth-system.md`](chains/growth-system.md) runs them in order:

```text
route → baseline → measure → diagnose → roadmap → design → test → execute → loop → learn
```

It's a playbook your agent follows, not a workflow engine. Each stage runs only when your current constraint needs it.

## 🚀 Install

These are [Agent Skills](https://agentskills.io/). Not a plugin for one app. They work in Claude Code, Codex, Amp, Cursor and any agent that reads skills. 🤝

Clone once, from the project where you want them:

```bash
git clone https://github.com/adityash8/growth-skills.git ../growth-skills
```

Then copy the whole skill folders, so their references stay together. The block uses `.agents/skills` for Codex and Amp. Change `SKILLS_DIR` to `.claude/skills` for Claude Code, or to the folder your agent uses.

```bash
(
  SKILLS_DIR=.agents/skills
  for source in ../growth-skills/skills/*; do
    target="$SKILLS_DIR/${source##*/}"
    if [ -e "$target" ] || [ -L "$target" ]; then
      printf 'Install stopped: %s already exists.\n' "$target" >&2
      exit 1
    fi
  done
  mkdir -p "$SKILLS_DIR" && cp -R ../growth-skills/skills/* "$SKILLS_DIR/"
)
```

If any skill name is already taken, nothing is copied. To replace installed skills, move the old folders to a backup outside the skills folder, then run the block again.

Start with `growth-strategist`. It knows where to send you next. Browse all 19 in the [catalog](catalog.json).

## 💬 Use it

Just ask.

```text
Use growth-strategist to find what's holding back activation. Use the attached funnel export and name the next check that could change your answer.
Follow the growth-system chain for this product. Stop at each gate when evidence is missing.
Audit our tracking before we trust last month's CAC.
Review this paid media deck. What is actually true?
```

## 🚫 What it will never do

Saying no is how you focus. So here's what we said no to:

- 🔐 Ship credentials or private integrations. Bring your own.
- 💸 Spend money, publish, message users or touch production on its own. A human says yes first.
- 🎲 Invent a number. If evidence is missing, it asks for the one check that would settle it.
- 📅 Pretend a 2021 benchmark applies to your business. Every benchmark comes with a date.
- ⚖️ Replace your lawyer, accountant or statistician.

## ✅ Checks

```bash
make validate   # catalog, chain, frontmatter, size limits, secrets and privacy scan
make test
```

## 📜 Credits and license

The frameworks that shaped these skills are credited in [SOURCES.md](SOURCES.md). Everything here is written from scratch under the [MIT License](LICENSE).

Want to help? Read [CONTRIBUTING.md](CONTRIBUTING.md). Found something sensitive? Use [SECURITY.md](SECURITY.md), not a public issue. 🛡️

If a skill saves you a meeting, a star is appreciated. ⭐
