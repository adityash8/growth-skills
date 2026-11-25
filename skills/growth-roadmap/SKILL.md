---
name: growth-roadmap
description: "Turn a diagnosed growth constraint into a focused quarterly plan with outcomes, experiments, owners, and decision rules."
---

# Growth Roadmap

Turn a growth constraint into a focused quarterly plan. For stalled or declining growth, triage first. If the constraint is unknown, prepare a provisional learning plan and a `growth-audit` handoff rather than inventing a diagnosis.

Do NOT use for a first full-funnel diagnosis (`growth-audit`), channel selection (`channel-fit-diagnostic`), or experiment methodology (`experiment-design`).

## Inputs and missing data

Use supplied context and exports first. Keep useful drafting moving when data is absent. Mark unknown values and owners `[placeholder]`; distinguish inferred stage or segment from supplied facts.

| Input | Evidence to use or request if missing |
|---|---|
| Outcome, quarter, stage, segment and motion | Business brief; distinguish freemium, trial and sales-led |
| Customer gains, losses and recurring revenue | Monthly account/revenue bridge: month, starting customers, new customers, churned customers, starting MRR, new MRR, expansion MRR, contraction MRR, churned MRR, ending MRR |
| Activation and conversion | Cohort export: signup date, account ID, segment, core-action event/time, paid date, observation window |
| Retention and expansion | Cohort revenue export: account ID, cohort, opening revenue, closing revenue, cancellations; cancellation observations |
| Candidate work, prior results and constraint | Existing audit, experiment results, supporting evidence |
| Owners, capacity, budget and commitments | Named available owners, hours per planning period, fixed work, dependencies and approved spending limits |

For every unknown measurement or expected delta, name the export or observation and required fields that would establish it. Never replace unknown baselines or deltas with zero. A proposed target can stand separately from an unknown baseline. Deliver provisional research or measurement work while dependent decisions remain provisional.

## Approval and evidence contracts

**Planning is not execution approval.** Prepare drafts and task-ready text immediately. Explicitly require human approval before live product edits, publication, campaign launches, spending, external tracker writes or irreversible actions. A roadmap, budget ceiling or inferred answer does not authorize execution. Never claim actions happened without verified execution.

**Label numbers at the claim.** Every substantive quantity in the delivered plan must be supplied, calculated with inputs and checked arithmetic, a benchmark with source and year, or a proposed estimate/hypothesis. Cover baselines, targets, expected key-result deltas, effort, hours, portfolio ratios and delivery confidence. A general estimates disclaimer is insufficient. Borrowed defaults retain their source and year; do not relabel a borrowed benchmark as an original estimate. Do not present historical cases as guaranteed lift.

## 1. Triage stalled or declining growth

When the business metric is flat or falling, use [stalled-growth triage](references/stalled-growth-triage.md).

Skip this step for an ordinary planning quarter. Otherwise check in order, stopping at the first evidenced failure; missing evidence stays unassessed:

1. **Logo churn:** are losses offsetting acquisition? Customer ceiling = new customers per month / monthly logo churn rate, using comparable periods and a decimal rate. A supplied zero churn rate means no finite ceiling; unknown churn means unknown ceiling.
2. **Pricing and positioning:** does the offer fit the segment's budget and value? Use win/loss observations.
3. **Expansion:** do retained accounts expand? Net revenue retention = closing revenue of the opening cohort / its opening revenue; exclude new customers and read logo loss alongside it.
4. **Channel saturation:** what evidence shows the current channels cannot scale? Prepare `channel-fit-diagnostic` when applicable.
5. **Need to grow:** what business outcome actually requires growth?

Choose the objective in this order:

- **Active decline:** arrest the decline with a core product or marketing fix. Identify the cause first. If tracking changed, correct the full comparison period and recheck whether decline remains. Check that the proposed fix offsets losses: new customers versus churned customers for account growth; new plus expansion MRR versus contraction plus churned MRR for revenue. More accounts need not mean more revenue.
- **Activation failure:** when most signups miss the defined core action, freeze acquisition-scale key results and focus on activation.
- Otherwise use the first failing question. When evidence is insufficient, choose a provisional learning objective.

Report the first failure or unassessed question, decline status, activation status, objective and constraints from other failures. Do not turn each failure into another competing objective.

## 2. Align outcomes and key results

Prefer one business outcome; keep at most three objectives. Force-rank Growth, Engagement and Monetization into one proposed order, marking leadership agreement pending when not supplied. State painful non-goals.

For each key result (KR), assign one known owner or `[placeholder]`, a baseline/window, target/horizon, measurement method and growth lever. The levers are acquisition, activation, retention, revenue per user, efficiency and capacity.

Choose the goal type from the main risk:

| Risk | Goal type |
|---|---|
| Unknown mechanism | Learning: research that yields a testable hypothesis |
| Missing tools or data | Capability: establish reliable measurement or an enabling capability |
| Known lever and tools | Output: a verifiable delivery the team controls |
| Uncertain strategic hypothesis | Outcome: a measurable test of the hypothesis |

Do not impose outcome deltas where the mechanism or baseline is unknown. Label KRs committed or stretch and label numerical delivery expectations as proposed or sourced. Explain how controlled team inputs should move the business result. Avoid task lists disguised as outcome KRs.

## 3. Diagnose gaps and choose a segment

Classify blockers as knowledge, capability, resource or execution gaps. Pick one priority segment with evidence of value, pain, retention and reachable demand. State assumptions when those observations are missing.

Check funnel counts, conversion, retention and economics for that segment and motion. Always state numerator, denominator and window; use comparable mature cohorts. Do not grade freemium with trial benchmarks, month-one churn with steady-state churn, or all-signup retention with paid retention. No suitable benchmark means ungraded, not healthy. Use `saas-unit-economics-audit` for unit economics.

Select the lever justified by the constraint: fix retention or activation leaks before acquisition scale; investigate positioning when visit-to-signup evidence supports it; test new channels when saturation is evidenced. With no diagnosed constraint, keep the sequence provisional pending `growth-audit`.

## 4. Build the strategy and capacity split

Write one strategic bet: intervention → behavior → leading signal → business outcome. Use up to three primary hypotheses, each with evidence and a disproof condition. Explain the approach, segment advantage, resources and success metric.

Split capacity by stage before assigning work. Starting examples, not universal rules: pre-product-market-fit about 90/10 new versus incremental; mature about 50/50 (both Duolingo, 2023). For other stages choose and label a proposed allocation or cite an applicable source. Explain adjustments; under decline, staff the core fix first.

Reserve investigation time, stability work and any longer-term loop research within available capacity. Show hours as well as ratios, and whether reserves are included in buckets, so allocations do not double-count effort. Give big bets a bounded learning phase and continue/kill signals before work starts. Do not promise immediate revenue from a new loop.

## 5. Sequence and prioritize the portfolio

Each item must trace task → project → strategy → KR. Include:

- Outcome and expected KR delta in the KR's unit before any priority score; if unknown, say so and name the evidence needed.
- One owner or `[placeholder]`, effort in person-time, dependencies, done criterion and decision date.
- For experiments: intervention, eligible population, primary metric, guardrails, observation window and a falsifiable prediction.
- Continue, revise and stop criteria defined before the test; prepare `experiment-design` for sample and stopping rules.

Prioritize by KR relevance, critical gaps, dependencies, expected impact range, evidence confidence, effort and resource availability. Never invent a scoring result. If the required scoring method is unavailable, provide a provisional dependency order with the missing evidence; do not fabricate precision. Keep deferred ideas visible.

Frame items as outcomes. Commit a release date only after evidence gives confidence in the solution. Put measurement and enabling work ahead of dependent tests, name parallel work and show what will be deferred to fit capacity.

## 6. Deliver and review

Use [the roadmap template](references/roadmap-template.md). Include the triage when applicable, alignment, KRs, segment, gaps, funnel diagnosis, strategy, capacity split, ranked project stack, dependencies, risks, decision rules, exclusions and handoffs.

Plan this quarter in detail and the next as outcome bullets, with sourced or proposed confidence. Keep distant technology-dependent plans broad and replan after a major capability change. In uncertain quarters, set accelerate/cut triggers per KR before the quarter begins.

Review weekly: KR confidence with its evidence, last week's result, next week's work and up to three top priorities. Replan when the constraint changes; stop work when its pre-agreed stop condition is met.

## Required handoffs

For every applicable route, deliver the concrete input, expected returned artifact and status `prepared, not executed` unless verified output was supplied. Unavailable tools mean a pending handoff, not an omitted one; dependent decisions stay provisional.

| Trigger | Skill and concrete input | Expected return |
|---|---|---|
| Unknown constraint or no full-funnel picture | `growth-audit`: context, funnel/revenue exports or missing fields, candidate ideas, capacity | Diagnosed constraint and action matrix |
| Severe unexplained churn | `customer-research`: churn/tenure cohorts, cancellation observations or missing research fields | Cause hypotheses and customer evidence |
| Most signups miss the core action | `onboarding-activation`: core action, signup/activation cohorts, observed friction | Activation intervention brief and measurement needs |
| Controlled tests | `experiment-design`: hypothesis, eligible population, baseline/variant, metric, guardrails, window | Feasible test, sample/stopping rules and analysis plan |
| Saturated channels | `channel-fit-diagnostic`: segment/motion, funnel findings, saturation evidence, candidates | Channel-fit verdict and bounded test |
| Uncertain unit economics | `saas-unit-economics-audit`: revenue/cohort data, acquisition costs, margins, definitions | Comparable economics and constraints |

For decline decomposition, prepare account and revenue bridges plus tracking/channel/budget changes for analysis before committing to a lever. For project scoring, supply the full KR-linked list, deltas or unknowns with evidence needs, effort, dependencies and capacity to the user's chosen prioritization process. These are pending analysis tasks, not claims that another skill ran.

## Final checks

- Does each project have a KR-unit delta or an explicit unknown with evidence needed?
- Are all substantive numbers labelled at the claim, with arithmetic checked?
- Are unknown baselines still unknown, and dependent decisions provisional?
- Do the capacity totals fit, with reserves counted once?
- Are handoff inputs, returns and pending status explicit?
- Is human approval required before live or irreversible actions?
