---
name: experiment-design
description: "Turn a growth hypothesis into a decision-ready experiment with one primary metric, guardrails, exposure rules, and a precommitted analysis plan."
---

# Experiment Design

Use this skill when a growth recommendation needs causal evidence before rollout.

Do not run an experiment when the change is legally required, fixes a clear defect, has negligible downside, or cannot reach enough exposure to inform a decision.

## Inputs

- decision and proposed intervention;
- target population and eligibility rules;
- baseline metric and variance, when available;
- expected mechanism;
- operational, ethical, and technical risks;
- available exposure and test duration constraints.

## Procedure

1. **Write the decision.** State what will change after a positive, negative, or inconclusive result.
2. **Write the causal hypothesis.** Use: “For [population], changing [intervention] will affect [primary outcome] because [mechanism].”
3. **Choose one primary metric.** It must match the decision and be measurable during the test window.
4. **Add guardrails.** Cover user harm, quality, retention, margin, reliability, support load, and other plausible side effects.
5. **Define the unit.** Choose user, account, session, market, or time block. Prevent contamination between variants.
6. **Set eligibility and exposure.** Specify who enters, when assignment happens, and what counts as exposed.
7. **Choose the design.** Randomized control is preferred. Use geo, switchback, phased rollout, or matched comparison only when randomization is impractical, and state the weaker assumptions.
8. **Plan sample and duration.** Use baseline rate, minimum effect worth acting on, variance, power, and traffic. Include full business cycles and delayed outcomes.
9. **Precommit analysis.** Fix exclusions, metric definitions, segment cuts, stopping rules, and treatment of missing data before launch.
10. **Run an instrumentation check.** Verify assignment, exposure, metric logging, and variant behavior before admitting real participants.
11. **Interpret for action.** Report effect size and uncertainty, not just significance. Distinguish “no useful lift” from “not enough information.”
12. **Record the result.** Keep hypothesis, dates, variants, decision, caveats, and follow-up in a durable experiment record.

## Output contract

Return:

1. decision statement;
2. hypothesis and mechanism;
3. population, unit, eligibility, and exposure rule;
4. control and treatment definitions;
5. primary metric and guardrails;
6. minimum effect worth acting on;
7. sample and duration assumptions;
8. instrumentation and quality checks;
9. precommitted analysis and stop rules;
10. launch, rollback, and decision owners;
11. result template.

## Interpretation states

- **Ship:** useful effect with acceptable guardrails.
- **Reject:** harmful or clearly below the useful threshold.
- **Iterate:** mechanism shows promise but implementation failed or a specific bottleneck dominates.
- **Inconclusive:** uncertainty still spans materially different decisions.

## Guardrails

- Do not peek repeatedly and stop at the first favorable result.
- Do not change the primary metric after seeing data.
- Do not hide harmed segments behind an average lift.
- Avoid simultaneous tests that contaminate the same users or outcome.
- Do not use statistical significance as a substitute for economic value.
- Require explicit approval for experiments involving pricing, sensitive data, health, credit, employment, or other high-risk decisions.

## Handoffs

- missing baseline evidence → `growth-audit`;
- unclear customer mechanism → `customer-research`;
- economics interpretation → `saas-unit-economics-audit`;
- successful repeatable action → `marketing-loops`;
- quarterly reprioritization → `growth-roadmap`.
