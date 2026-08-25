---
name: growth-strategist
description: "Route ambiguous growth problems to the right diagnostic, identify the binding constraint, and define the next evidence-backed decision."
---

# Growth Strategist

Use this skill when the request is broad: growth stalled, the team has too many ideas, or the operator does not yet know which growth problem to solve.

## Inputs

Collect what exists; do not block on a perfect brief.

- business model and primary value event;
- current stage and target outcome;
- funnel or revenue trend by period;
- acquisition mix and rough economics;
- retention or repeat-use signal;
- known constraints, recent changes, and failed tests.

Mark every input as **observed**, **reported**, **estimated**, or **unknown**.

## Procedure

1. **Define the outcome.** Convert “grow” into one business result, a baseline, a target direction, and a time horizon. Reject task-shaped goals.
2. **Map the system.** Trace demand → acquisition → activation → retention → monetization. Include measurement quality and operating capacity as upstream constraints.
3. **Find the binding constraint.** Select the stage where improvement would change the business result now. Distinguish a real bottleneck from the easiest metric to access.
4. **Check evidence strength.** Prefer product and revenue data over anecdotes; prefer segmented trends over blended snapshots. If evidence is weak, design the smallest diagnostic before recommending a program.
5. **Route the work.** Choose one primary skill from the table below. Use a second only when it resolves a dependency.
6. **Set a decision rule.** State what evidence would confirm, reject, or change the chosen path.

## Routing

| Signal | Primary skill |
|---|---|
| Baseline is missing or several stages may be broken | `growth-audit` |
| Constraint is known but work is scattered | `growth-roadmap` |
| No acquisition channel has structural traction | `channel-fit-diagnostic` |
| Existing users could expose value to non-users | `product-led-acquisition` |
| Users receive value but do not accumulate reasons to stay | `retention-state` |
| Engagement depth is hidden by averages | `power-user-curve` |
| Spend can grow but economics are unclear | `saas-unit-economics-audit` |

## Output contract

Return:

1. **Decision:** the single constraint to attack now.
2. **Evidence:** facts supporting it, with confidence and gaps.
3. **System map:** each stage labeled healthy, constrained, or unknown.
4. **Primary diagnostic:** the routed skill and why it is next.
5. **Do not do:** one tempting initiative that should wait.
6. **Decision rule:** the result that changes the recommendation.

## Guardrails

- Do not return a tactic list when the constraint is unknown.
- Do not blame acquisition before checking activation and retention.
- Do not call a channel scalable from blended return on spend alone.
- Do not invent targets or benchmarks. Date and segment external references.
- Do not recommend simultaneous work across the whole funnel.
- Treat missing instrumentation as a finding, not permission to guess.
