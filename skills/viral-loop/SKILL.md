---
name: viral-loop
description: "Measure, design, and improve product-embedded sharing loops using cohort attribution, step-level conversion, loop speed, and decay analysis."
---

# Viral Loop

Use this skill when product use can expose value to non-users through invitations, collaboration, shared artifacts, or referrals.

Do NOT use for channel selection (`channel-fit-diagnostic`), activation repair (`onboarding-activation`), retention repair (`retention-state`), or recurring messaging (`marketing-loops`). Do not manufacture sharing for a product with weak retention or no natural recipient value.

## Inputs

- product and user job;
- activation and retention evidence;
- share, invite, or collaboration surfaces;
- acquisition attribution and referral identifiers, if available;
- current funnel rates and abuse constraints.

State the selected mode and assumptions in one line. Use supplied exports or observations even without connected tools. Unknowns stay explicit: name the missing evidence and prepare a provisional specification rather than inventing metrics, tool calls, or execution.

**Live-action approval:** Prepare analyses, specifications and drafts now. Explicitly require user approval before any live tracking or dashboard edit, experiment or feature rollout, message send or schedule, reward activation, or irreversible action; checks passing are not approval. Never claim execution without tool evidence.

**Quantitative provenance:** Label every substantive number as supplied/reported/observed, calculated with its inputs, or estimated/hypothetical. This includes rates, costs, multipliers, effort, prioritization scores, expected changes in viral factor, benchmarks, proposed maturation and attribution windows, retention cuts, experiment settings and message caps. Proposed numeric choices are heuristics requiring validation, never measured facts; label them at the claim or table/section level. Dates, list ranks and mathematical constants need no label.

## Modes

- **Measure:** determine whether an existing loop causes meaningful acquisition.
- **Design:** create a loop that is native to the product's value.
- **Improve:** locate and repair the weakest conversion step.
- **Decay audit:** explain why a previously useful loop weakened.

## Procedure

1. **Run the prerequisite check.** Confirm quick time to value, a natural recipient benefit, and retention that is not collapsing. If evidence fails, stop loop expansion and route to `channel-fit-diagnostic`, `onboarding-activation`, or `retention-state` as appropriate. If evidence is missing, mark viability unverified and draft only a conditional plan.
2. **Name the loop.** Define the actor, action, recipient, recipient value, return path, and activation event.
3. **Choose the natural mechanic.** Prefer collaboration, utility, or valuable shared output. Before offering a reward, check whether retained users can actually use it, whether it pays for referrals that would have happened anyway, and whether the economics and abuse controls work.
4. **Instrument causality.** Persist a privacy-safe referrer or artifact identifier from exposure through activation. Separate caused users from users who merely arrived in the same period.
5. **Measure by cohort.** For each causing cohort, count activated users attributed to that cohort over a fixed maturation window. Report the window and attribution limits.
6. **Map the step funnel.** Measure exposure → open → landing → signup → activation → first retained action. Do not optimize aggregate sharing while one downstream step is broken.
7. **Measure speed and repetition.** Record time to first caused user, time between generations, and how often retained users create new exposures.
8. **Design at the value peak.** Place sharing after a completed outcome, useful collaboration event, or artifact creation—not before users experience value.
9. **Test one bottleneck.** Rank fixes by expected change in cohort viral factor, stating assumptions and uncertainty. If lift cannot be estimated, explain the missing evidence. Route the highest-priority change to `experiment-design` with a primary metric, guardrails, and stop rule; require explicit approval before launch.
10. **Audit decay.** Check novelty loss, audience saturation, platform changes, attribution loss, abuse controls, and retention decline.

## Core calculations

Use a cohort ratio. Specify whether the outcome is signup or activation and use the same definition in numerator and denominator. The activation-based version is:

```text
viral factor = activated users caused by cohort C / activated users in cohort C
```

Keep the causing cohort distinct from the users it causes. Compare cohorts over the same fixed maturation window and report generation depth. Separate initial users from later generations when assessing sustained spread. Deduplicate recipients and define attribution precedence when loops or referrers overlap; do not add overlapping loop counts.

"Virally acquired users / all signups in the same period" measures acquisition share, not cohort viral factor. If that is all the data supports, report the share and leave the cohort factor unavailable. Invite count × conversion can diagnose an invite funnel, but does not capture all loop types or repeated sessions.

When the factor is below 1 and assumptions are stable:

```text
acquisition multiplier = 1 / (1 - viral factor)
```

Treat the multiplier as a model, not a forecast. It assumes constant reproduction across generations and enough time for those generations. It has no finite interpretation at or above 1. Loop speed, retention, attribution error, and saturation can dominate it.

Track repeated contribution across retained sessions, not just the initial invite. Report time to the first caused user and time between generations beside the factor. A slow loop may contribute lifetime acquisition without changing the current period materially.

## Design and incentive checks

Choose a mechanic that benefits both sender and recipient:

| Type | Natural mechanism | Main constraint |
|---|---|---|
| Word of mouth | Users talk about a useful or remarkable outcome | Product quality; surveys and listening are proxies, not causal attribution |
| Invitation or collaboration | Another person improves or completes the task | Recipient reaches value quickly |
| Shared output or visible utility | Normal use exposes an artifact, link, or result | Useful recipient context and consent for visibility |
| Incentivized referral | A reward reinforces existing recommendations | Incremental economics, reward eligibility, and abuse controls |

Inventory shareable objects × recipients × placements before tuning a surface. Keep a copyable link available; preserve content context and attribution across signup, app opening, and installation. Treat each recipient step as a landing experience.

For a new network product, validate the core value and then spread within a bounded, dense cohort before expecting independent spread. Seeding is a test method, not evidence that the loop sustains itself. In marketplaces, name which side causes participation on the other and keep those cohorts separate.

Before proposing a reward, require evidence of existing recommendations, reachable peers, enough eligible users to matter, and an incentive the most active referrers can use. Check reward cost against lifetime contribution margin, payback, and paid acquisition cost using incremental users rather than every attributed referral. Include a stated cannibalization assumption. Missing economics or fraud evidence means no reward activation.

Test the cheapest way to collect a reward without creating value. Tie qualification to the revenue or value event; account for self-referrals, duplicate accounts and reversals. Prefer useful product value where it fits, and test rather than assume that larger rewards improve conversion. Route broader acquisition mechanics to `product-led-acquisition` and economic analysis to `saas-unit-economics-audit`.

## Bottleneck and decay diagnosis

Use measured per-step rates to locate the bottleneck; funnel multiplication is a diagnostic, not a substitute for cohort measurement. For shared content, model typical reach rather than exceptional posts. Improve reach, recipient engagement, activation, sharing, and retained sessions according to the observed constraint. Do not compensate for weak retention by increasing prompt pressure.

| Possible cause | Evidence to inspect | Conditional response |
|---|---|---|
| Novelty loss | Broad decline in response across segments | Test a more useful format or mechanism |
| Audience saturation | Repeated targets, existing accounts, lower conversion in later cohorts | Reduce repetition; diversify acquisition |
| Platform or attribution change | Dated break at a particular step or platform | Verify delivery rules and tracking before claiming behavioral decay |
| Retention leak | Users leave before contributing later exposures | Route to `retention-state` |
| Notification saturation | Lower opens as network size or send count grows | Propose a validated cap and ranking; route to `marketing-loops` |
| Network unraveling | Retention falls when close connections become inactive | Test useful solo value, not more messages |

A single large broadcast is not sustained viral spread. Check later attributed generations before calling a spike a loop. Untracked recommendations, organic acquisition share, and satisfaction surveys can support a hypothesis, but cannot establish a cohort factor alone.

## Output contract

Return:

1. prerequisite verdict;
2. loop map and recipient value;
3. attribution specification;
4. loop diagram as a step × rate table with missing data marked;
5. cohort factor, maturation window, and uncertainty;
6. primary bottleneck and ranked instrumentation or fixes, with expected change in viral factor or an explicit reason it is unavailable;
7. one experiment specification;
8. abuse, consent, and platform risks;
9. next handoff.

## Guardrails

- Never use unsolicited contact uploads or dark patterns to inflate the loop.
- Do not call viral share of signups a cohort viral factor.
- Do not claim causality when attribution only shows correlation.
- Protect recipient consent and minimize personal data.
- Do not assume a past platform mechanic still works; verify current rules.
- If incentives attract abuse or exceed incremental value, recommend pausing them; require approval before changing live rewards.

## Handoffs

- unclear channel fit → `channel-fit-diagnostic`;
- broader acquisition mechanics → `product-led-acquisition`;
- referral economics → `saas-unit-economics-audit`;
- weak activation → `onboarding-activation`;
- weak retention → `retention-state` and `power-user-curve`;
- test design → `experiment-design`;
- proven recurring optimization → `marketing-loops`;
- quarterly sequencing → `growth-roadmap`.

Name the concrete next deliverable and evidence passed to each relevant skill. Do not claim a handoff was executed without its output.
