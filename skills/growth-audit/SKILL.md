---
name: growth-audit
description: "Audit a product's growth system across measurement, market, acquisition, activation, retention, revenue, and execution."
---

# Growth Audit

Use this skill for a first evidence-backed baseline or when growth is stuck and the failure could sit in more than one part of the system.

## Inputs

Use available first-party data, public evidence, and operator context. Label gaps instead of waiting indefinitely.

- business model, audience, offer, and primary value event;
- revenue, customer, and funnel trends by period;
- acquisition volume, cost, and quality by channel;
- activation, retention, expansion, and churn by cohort or segment;
- measurement map and known tracking changes;
- current team capacity, dependencies, and recent experiments.

## Evidence scale

- **E0 — unknown:** no reliable evidence.
- **E1 — directional:** anecdote, public signal, or tiny sample.
- **E2 — observed:** one relevant first-party source.
- **E3 — corroborated:** multiple sources or repeated cohorts agree.

Recommendation confidence cannot exceed its evidence level.

## Procedure

1. **Normalize the frame.** Fix the period, currency, segment, funnel definitions, and primary outcome. Record tracking or pricing changes that break comparability.
2. **Audit measurement.** Check whether acquisition sources, value events, revenue, churn, and identity are measurable end to end. Flag silent denominator changes.
3. **Audit market and offer.** Test audience specificity, trigger, alternative, promise, proof, pricing logic, and whether the reachable market can support the outcome.
4. **Audit acquisition.** Compare channels on qualified volume, marginal cost, payback, saturation, and fit with product and model. Separate experiments from engines.
5. **Audit activation.** Identify the first value event, time to value, setup friction, and conversion by source and segment.
6. **Audit retention.** Use cohorts where possible. Separate voluntary churn, failed payment, weak habit, poor fit, and structural lack of recurring value.
7. **Audit revenue.** Review conversion, gross margin, expansion, contraction, concentration, and unit economics by segment.
8. **Audit execution.** Check ownership, experiment throughput, decision latency, engineering dependency, and whether old tests have usable conclusions.
9. **Rank constraints.** Score each finding on outcome impact, evidence, effort, reversibility, and dependency risk. Use ranges when evidence is weak.
10. **Choose one next move.** Recommend the narrowest diagnostic or experiment that can change the decision.

## Output contract

1. **Verdict:** the binding constraint and confidence.
2. **Scorecard:** seven layers labeled healthy, constrained, or unknown, each with evidence level.
3. **Top findings:** evidence → consequence → recommendation.
4. **Data gaps:** missing evidence that could reverse the verdict.
5. **Priority matrix:** now, next, later, and stop.
6. **Next diagnostic:** handoff to one specialist skill.

## Handoffs

- planning and ownership → `growth-roadmap`;
- acquisition structure → `channel-fit-diagnostic`;
- product-driven distribution → `product-led-acquisition`;
- retention architecture → `retention-state`;
- engagement depth → `power-user-curve`;
- economics → `saas-unit-economics-audit`.

## Guardrails

- Never hide an evidence gap behind a benchmark.
- Do not mix periods, segments, or attribution methods in one comparison.
- Do not call correlation causation after a launch or campaign.
- Do not assign fake owners or deadlines.
- Do not audit every layer at forensic depth. Go broad first, then route the constraint.
