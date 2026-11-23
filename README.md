# Growth Skills 🚀

**Know what’s holding growth back before you spend more to fix it.**

Give your agent a funnel, a campaign report, or a question you can’t answer yet. Get one next decision and the evidence that could change it.

## Start with your question

| If you’re asking… | Start with |
|---|---|
| Where are we losing growth? | [`growth-strategist`](skills/growth-strategist/SKILL.md) picks the next diagnostic instead of handing you a list of tactics. |
| Can we trust what we’re measuring? | [`marketing-tagging-audits`](skills/marketing-tagging-audits/SKILL.md) follows the event from the browser to the destination. [`paid-analysis-review`](skills/paid-analysis-review/SKILL.md) checks the numbers behind a budget call. |
| What should we work on this quarter? | [`growth-roadmap`](skills/growth-roadmap/SKILL.md) turns one constraint into a plan with owners and stop rules. |
| How will we know the change worked? | [`experiment-design`](skills/experiment-design/SKILL.md) sets the metric, comparison, and decision rule before results come in. |

Browse all 19 skills in the [catalog](catalog.json). For the full sequence, give your agent the [growth-system playbook](chains/growth-system.md). It’s a guide for choosing and running the right skills in order, not a workflow engine.

## Install and try it ⚡

These are [Agent Skills](https://agentskills.io/), not a plugin for one client. From the project where you want to use them, run the following. The example uses `.agents/skills` (Codex and Amp). For Claude Code, change the `SKILLS_DIR` line to `.claude/skills`. For another client, use its documented directory.

```bash
git clone https://github.com/adityash8/growth-skills.git ../growth-skills
SKILLS_DIR=.agents/skills
mkdir -p "$SKILLS_DIR"
cp -R ../growth-skills/skills/. "$SKILLS_DIR/"
```

Copy whole folders so `SKILL.md`, references, and scripts stay together. Open the project in your agent and ask:

```text
Use growth-strategist to find what's holding back activation. Use the attached funnel export and name the next check that could change your answer.
```

Start with exports or authorized read access. Running an audit does not grant permission to spend, publish, send messages, or change production. If evidence is missing, the skills ask for a specific check rather than inventing a number.

From the cloned repo, run `make validate` and `make test` (Python 3 and Make).

[Sources and credits](SOURCES.md) · [MIT License](LICENSE) · [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md)
