---
name: experiment-design
description: "Turn a growth hypothesis into a decision-ready experiment with one primary metric, guardrails, exposure rules, and a precommitted analysis plan."
---

# Experiment Design

Turn a growth hypothesis into a decision-ready experiment, or explain why a cheaper validation is more useful.

Do NOT use for tracking setup, idea ranking, variant copywriting, or offline model evaluations. For available adjacent work, use the handoffs below.

## Scope and evidence

- Use supplied context and exports first. Label measured evidence, calculations, assumptions, predictions and unknowns separately; never invent measurements, tool access, owners or dates.
- Mark missing inputs [placeholder]. Produce a useful draft now; missing validity-critical inputs block launch or a causal verdict.
- Historical examples and external benchmarks suggest hypotheses; they do not supply an account's baseline, expected lift, win rate or prior.
- Drafting does not authorize live actions. Require explicit approval before live edits, enrolling participants, changing allocation, rollout, publication or irreversible actions. Record launch, rollback and decision owners.
- Never test an implementation that violates law, privacy, customer trust or an ethical red line. A test cannot waive compliance. Compare compliant alternatives when feasible.

## Modes

| Request | Procedure |
|---|---|
| Single change, several changes, sample question or readout | Start with Step 0; use the plan and readout rules below |
| Program setup, testing culture, velocity or long-term holdouts | Use [the program guide](references/experimentation-program.md) |

## Inputs

Use the decision, proposed intervention, expected mechanism, population, eligible daily unique units, baseline metric and variance, assignment unit, allocation, outcome delay, minimum effect worth acting on, deadline, risks and available testing method.

If baseline or traffic is absent, show sample and duration formulas with [placeholder] inputs rather than borrowing benchmarks. Ask only for missing information needed to resolve the decision.

## Step 0: Test or validate another way

Return one verdict with a reason for every proposed change:

- **TEST:** a valid comparison can answer a decision in time, with acceptable risk and cost.
- **SHIP AND MEASURE:** a low-risk reversible change costs more to test than the decision is worth. Specify monitoring, harm thresholds, rollback and outcome-aligned windows; approval is still required before rollout.
- **VALIDATE CHEAPER:** use existing evidence, interviews, usability checks, a disclosed smoke test, concierge delivery or a prototype. Say what it can establish and what remains uncertain.
- **DON'T BUILD:** decision-relevant evidence or an ethical red line rules out this implementation. A non-significant or underpowered result cannot permanently disprove an idea.

Before choosing TEST, calculate feasibility from baseline, absolute and relative minimum detectable effect (MDE), alpha, planned power, unit, allocation, eligible exposure and outcome delay. Compare required sample plus representative business cycles and outcome maturity with the actual deadline. There is no universal traffic cutoff or maximum test length.

A mandatory fix does not need a test to justify compliance; testing feasible implementation alternatives may still help. A new product does not automatically rule out a control.

Only TEST continues to the design sections. For other verdicts, return the matching validation or monitoring plan. An unrandomized before/after read is observational; it does not isolate causality. Use a randomized holdout when feasible and adequately precise.

## Design and sample

1. Write the causal hypothesis from an observation, intervention, mechanism, population and outcome. Record what changes after a positive, negative or inconclusive result before launch.
2. Choose one primary metric tied to durable business value and agree whether higher or lower is better. Add secondary diagnostics and guardrails for harm, quality, retention, margin, reliability and support load. Define denominators, windows and harm actions.
3. Prefer one meaningful change. A coherent bundle can test a larger effect at low sample size, but cannot identify each component's contribution. Factorial designs need adequate sample for planned effects and interactions.
4. Choose the assignment and analysis unit; prevent contamination and keep returning users in the same variant. Repeated sessions from a few accounts are not independent accounts.
5. Define population, eligibility, assignment timing, control, treatment and actual exposure separately from conversion outcomes. Freeze exclusions and address differential missingness without post-treatment filtering.
6. Size for the actual split and design. Start with [sample sizing](references/sample-size-guide.md); it includes the independent binary-outcome formula, assumptions, duration and multiplicity rules. Clusters, rare events, unequal splits and sequential methods need design-specific calculations.
7. Use [low-sample designs](references/low-sample-testing.md) for B2B, geo experiments, switchbacks and interference; use [SEO designs](references/seo-experiments.md) for page or cluster assignment. Label nonrandomized comparisons observational and state their assumptions.
8. Precommit alpha, power, sample, observation window, missing-data treatment, exclusions, confirmatory segments, comparison family and stopping rule. A fixed-horizon test cannot stop at first significance. For early efficacy decisions, choose a valid sequential method and boundaries before launch; a Bayesian dashboard alone is insufficient.
9. Specify multiplicity control for variants, metrics and confirmatory segments. Bonferroni uses alpha/m; Holm compares sorted p-values with alpha/(m-i+1), stopping at the first failure. Recalculate sample for the method. Post-hoc segments are exploratory.
10. Record expected lift as a prediction, never an account fact. Include recurring costs and a next iteration for a supported win. Do not optimize for test volume by weakening validity.

## Launch and validity checks

Before launch, verify the implementation and tracking end to end in every variant, document green/red actions, confirm safety and ethical constraints, and obtain approval for the concrete live action.

During the test, monitor safety and technical failures, record concurrent changes, and keep variants, eligibility and analysis commitments stable. A safety stop does not declare an efficacy winner.

Block efficacy interpretation until these checks pass:

1. **Sample ratio mismatch (SRM):** test assignment counts against the planned split, then inspect exposure/logging. Use a prespecified diagnostic threshold, not the outcome p-value. Outcome counts need not be equal. A healthy split does not prove instrumentation is correct.
2. **Early technical review:** inspect errors, assignment, eligibility and exposure. Stop for harm or broken implementation under the safety plan.
3. **Surprising effects:** inspect denominators, bots, filters and instrumentation, comparing with measured history. A surprise is a reason to investigate, not proof of a bug.
4. **Metric direction:** verify polarity, denominator and outcome window against a trusted signal.
5. **Treatment delivery:** exercise both variants before trusting a null; a broken treatment does not invalidate the entire idea.

Record actual versus planned sample, exclusions, attrition, mature outcomes and any deviations. Reaching planned sample alone does not validate a design.

## Readout and decision

- Report effect size with uncertainty, including absolute percentage-point and relative changes for rates. MDE is a planning target, not a post-hoc significance threshold.
- A p-value is the probability, under the null and stated assumptions, of a statistic at least as extreme as observed. It is not the probability that the null is true, the result is random or the variant wins. A confidence interval describes long-run coverage, not a posterior win probability.
- Report actual precision. Planned power is not achieved power; observed-effect post-hoc power adds no evidence. Do not lower thresholds, change the primary metric or select favorable segments after seeing results.
- **Ship:** a valid result supports useful benefit with acceptable guardrails and economic value. Require approval before rollout.
- **Reject:** evidence supports harm or rules out decision-relevant benefit under the committed rule; keep control and record learning.
- **Iterate:** evidence identifies a specific implementation failure or mechanism worth a new test; distinguish that explanation from a confirmed finding.
- **Inconclusive:** uncertainty still spans materially different decisions. Consider more data, a different treatment or a reversible decision with monitoring. Non-significance is not equivalence; equivalence needs a planned design and interval inside its bounds.
- For mixed signals, check validity and predefined segments; do not hide harmed groups behind an average. Plan replication for borderline or high-stakes decisions rather than rerunning until significant.
- Compare incremental value and incremental running costs over the same period, including effect uncertainty and supported lifetime-value assumptions. Show any word-of-mouth factor separately with evidence or sensitivity bounds. A statistical win can lose money.
- Preserve traceable cohorts for delayed or fading effects. A short-term activity gain does not prove durable retention lift.

## Output contract

Use these line labels verbatim:

```text
TEST PLAN: [name]
Step 0 verdict: TEST | SHIP AND MEASURE | VALIDATE CHEAPER | DON'T BUILD, because [reason]
Hypothesis: Because [observation], we believe [change] will cause [outcome] for [audience]. We'll know when [metric].
If green: [action]   If red: [action]   Prediction: [expected lift, labelled prediction]
OEC / primary: [metric and direction]   Guardrails: [metrics, thresholds, actions]   Secondary: [metrics]
Design: [method, control and treatment]   Unit: [assignment and analysis]   Split: [allocation]
Sample: [per-arm sample, baseline, relative and absolute MDE, alpha, power, assumptions]   Duration: [window and outcome delay]
Validity plan: [eligibility, exposure, exclusions, missing data, SRM, early review, polarity, end-to-end QA, owners]
Net value: [incremental benefit and running cost over same period, break-even lift, separate word-of-mouth assumption]
Read rules: [stopping, multiplicity family/method, positive/negative/inconclusive actions, replication criteria]
Unknowns: [placeholder list]
Owners and approval: [launch, rollback and decision owners; live-action approval required]
```

For two or more changes, write one TEST PLAN header, a `Step 0 verdict:` line for every change (one line may cover changes sharing a verdict), then repeat Hypothesis through Read rules for each test. Include unknowns and owners per test where different.

For SHIP AND MEASURE replace design/sample lines with monitoring windows, rollback and any holdout design; label pre/post evidence observational. For VALIDATE CHEAPER specify the method, success criteria and remaining uncertainty. For DON'T BUILD explain the evidence or red line. Do not invent an experiment for a skipped change.

For completed tests return the [result record](references/test-templates.md) with validity status before efficacy, evidence, decision and remaining uncertainty.

## Handoffs

Route only the work needed and do not claim another skill ran without its output:

- Missing baseline or measurement evidence → `growth-audit`; tagging and event provenance checks → `marketing-tagging-audits`.
- Unclear customer mechanism → `customer-research`.
- Offer hypotheses → `offer-design`; onboarding hypotheses → `onboarding-activation`.
- Economic interpretation → `saas-unit-economics-audit`.
- Backlog ranking and reprioritization → `growth-roadmap`.
- Supported repeatable action → `marketing-loops`.
