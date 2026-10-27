# Growth system chain

This is an invoke-in-order playbook, not a workflow engine. Run stages sequentially. Within a stage, invoke only the specialist skills required by the current constraint and record why the others were skipped.

## Stage 0: route

**Skill:** `growth-strategist`

**Input:** ambiguous growth goal, current business context, available evidence.

**Output:** measurable outcome, constraint hypothesis, evidence gaps, and selected diagnostic.

**Gate:** do not prescribe tactics until the problem is expressed as a measurable constraint.

## Stage 1: baseline

**Skill:** `growth-audit`

Add `evidence-led-growth-audit` when a comprehensive report needs analytics and billing reconciliation, traceable sources, current claim checks, and final artifact verification.

**Input:** routed question plus available market, funnel, retention, revenue, and execution evidence.

**Output:** evidence-backed scorecard, largest constraint, data gaps, and ranked diagnostic work.

**Gate:** every material claim carries an evidence label; unknown layers remain unknown.

## Stage 2: measure

**Skill:** `marketing-tagging-audits`

**Condition:** tagging, consent, event provenance, or attribution quality is uncertain. Skip this stage when current evidence already establishes measurement quality, and record that basis.

**Input:** baseline questions, event definitions, consent requirements, and authorized browser, analytics, or tag-manager access.

**Output:** measurement evidence, source-to-destination event checks, consent observations, coverage limits, and unresolved gaps.

**Gate:** reports distinguish configured tags, observed requests, received events, and attributed outcomes. Material gaps limit downstream conclusions; a measurement audit does not authorize publishing changes.

## Stage 3: diagnose

Invoke as needed:

- `customer-research` for motivations, triggers, objections, and language;
- `channel-fit-diagnostic` for acquisition-channel viability;
- `power-user-curve` for engagement depth and cohort movement;
- `saas-unit-economics-audit` for CAC, LTV, payback, margin, and segment viability;
- `paid-analysis-review` for paid-channel claims, matched reporting windows, financial denominators, and attribution reconciliation;
- `conversational-ads-optimization` for conversational-ad delivery, eligibility, destination, tracking, and creative diagnosis.

Use the paid specialists only for an applicable paid-channel question. A diagnostic recommendation does not authorize a live change.

**Output:** one constraint brief with the strongest evidence, important unknowns, and decision implications.

**Gate:** choose one primary constraint. Do not average incompatible problems into a generic growth plan.

## Stage 4: roadmap

**Skill:** `growth-roadmap`

**Input:** outcome, baseline, constraint brief, resources, and decision horizon.

**Output:** one quarterly outcome, ranked hypotheses, sequenced experiments, dependencies, owners, and stop rules.

**Gate:** no roadmap item survives without a metric, owner, evidence level, and decision rule.

## Stage 5: design

Route by constraint:

- offer or monetization → `offer-design`;
- first-value failure → `onboarding-activation`;
- product-embedded acquisition → `product-led-acquisition`;
- sharing, invitation, or collaboration → `viral-loop`;
- structural retention → `retention-state`.

**Output:** a buildable intervention specification with mechanism, affected population, instrumentation, risks, and expected decision consequence.

**Gate:** the intervention must target the diagnosed constraint and fit current delivery capacity.

## Stage 6: test

**Skill:** `experiment-design`

**Input:** intervention specification and baseline evidence.

**Output:** decision-ready experiment with one primary metric, guardrails, exposure rules, analysis plan, and stop conditions.

**Gate:** instrumentation checks pass before exposure. High-risk changes retain an explicit human approval gate.

## Stage 7: execute

**Specialist:** `paid-media-creative-operations` for paid creative preparation, approved rollout, and delivery verification. For other interventions, use the relevant execution tools.

Execution happens through the product, analytics, messaging, advertising, content, or engineering tools available in the operator's environment.

**Input:** experiment specification and explicit execution scope, including approval for any live advertising writes.

The executing agent must:

1. honor the experiment's eligibility and authority boundaries;
2. record assignment and exposure;
3. verify the resulting state through an independent read;
4. stop on malformed data, missing approval, or guardrail breach;
5. write the result to the experiment record.

**Output:** verified execution result with changed objects, state readback, delivery evidence where applicable, and rollback or stop decisions.

**Gate:** an API success or completed task is not proof; verify the user-visible or system-visible outcome.

## Stage 8: operationalize

**Skill:** `marketing-loops`

**Input:** a useful, repeatable action supported by experiment or operating evidence.

**Output:** recurring loop specification with trigger, state, idempotency, approval boundary, verification, budgets, owner, and retirement rule.

**Gate:** do not automate an unproven tactic or an action with unresolved external-risk approvals.

## Stage 9: learn

Return results to:

- `growth-audit` to refresh the baseline and constraint;
- `growth-roadmap` to continue, revise, or stop the quarter's work;
- `growth-strategist` if the binding constraint changed.

Record the decision, evidence, and next action. Do not preserve a losing experiment as recurring work.

## Minimum chain artifacts

1. growth brief;
2. audit scorecard;
3. measurement evidence and unresolved gaps, when measurement review is needed;
4. constraint brief;
5. roadmap;
6. intervention specification;
7. experiment specification;
8. verified execution result;
9. loop specification, only for a winner;
10. decision record.
