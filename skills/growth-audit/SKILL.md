---
name: growth-audit
description: "Audit a product's growth system across measurement, market, acquisition, activation, retention, revenue, and execution."
---

# Growth Audit

Use this skill for a first evidence-backed baseline or when growth is stuck and the failure could sit in more than one part of the system. Go broad, then route the binding constraint to a specialist.

Do NOT use for quarterly planning (`growth-roadmap`), channel selection (`channel-fit-diagnostic`), or unit-economics grading (`saas-unit-economics-audit`).

## Inputs and access

Use available first-party data, public evidence, and operator context:

- product URL, business model, audience, offer, and primary value event;
- revenue, customer, and funnel trends by period;
- acquisition volume, cost, and quality by channel;
- activation, retention, expansion, and churn by cohort or segment;
- measurement map, privacy constraints, known tracking changes, and past tests;
- current team capacity, dependencies, and audit depth: quick or standard (default).

For an existing engagement, batch missing-access questions once and continue with what exists. Accept exports, screenshots, or walkthrough notes when integrations are unavailable. Never claim access or observations that were not available. Mark each missing internal layer `[DATA GAP]` and name the evidence that would unlock it.

For a prospect with no relationship or internal access, ask nothing: audit available public signals immediately. Mark internal layers `[DATA GAP — unlocks on engagement]`. If browsing is unavailable too, use supplied material and state the limit.

Read supplied prior audits and experiment results before recommending work. Cite prior failures and explain any reason to retry. Respect known privacy, regulatory, and capacity constraints; do not recommend tracking changes that conflict with them.

## Evidence and quantity rules

Use the public evidence scale consistently:

- **E0 — unknown:** no reliable evidence.
- **E1 — directional:** anecdote, public signal, or tiny sample.
- **E2 — observed:** one relevant first-party source.
- **E3 — corroborated:** multiple sources or repeated cohorts agree.

Recommendation confidence cannot exceed its evidence level. Before delivery, label every substantive quantity, including effort, impact assumptions, diagnostic thresholds, and benchmarks:

- **Supplied:** source and period.
- **Calculated:** formula and inputs.
- **Estimated/heuristic:** rationale and scope. Third-party traffic estimates belong here.
- **Unknown:** missing evidence needed to establish the value.

A clearly scoped table legend may label repeated values. Never invent an impact range to complete the matrix. When effect evidence is absent, report impact as unknown and state what would establish it. This overrides any request for numeric impact or confident wording. Conditional scenarios must show their assumptions and are not promised lift.

Verify external benchmarks against a dated, segment-matched source. Reverify snapshots older than six months or omit them. Match currency, period, denominator, cohort maturity, business model, and attribution method before comparing. Separate correlation from causation. Small samples are directional; label any diagnostic cutoff as a heuristic with its rationale rather than a universal fact.

## Procedure

1. **Normalize the frame.** Fix the period, currency, segment, funnel definitions, and primary outcome. Record tracking or pricing changes that break comparability. Replace activity goals with measurable business outcomes.
2. **Run every layer below.** Quick depth records the main finding per layer; standard depth follows the full checklist. Structurally inapplicable metrics are N/A with a reason; unavailable evidence is a data gap.
3. **Complete each layer before continuing.** Write its finding with a cited quantity or data gap, one leading metric to monitor, and any specialist handoff. A healthy layer gets one evidence-backed line; missing data never means healthy.
4. **Score recommendations.** Record impact on the leading metric or primary outcome, effort in person-days, evidence E0–E3, and regulatory, brand, and technical risk (low/medium/high plus failure mode). Label estimates and unknowns under the quantity rules.
5. **Rank the constraints.** Sort supported recommendations by impact and effort, then evidence, risk, reversibility, and dependencies. Separate unknown-impact diagnostics; do not fabricate a numeric ranking for them.
6. **Write the output contract.** Recommend one next diagnostic or experiment that could change the decision. Offer specialist work without claiming it has run.

## Seven-layer checklist

| Layer | Checks | Leading metric to consider |
|---|---|---|
| Metrics baseline | Growth accounting; revenue quality and concentration; activation and funnel conversion; unit economics; outcome goals | Worst-trending input to the primary outcome |
| Measurement | Event coverage; duplicate/missing conversions; identity; attribution; campaign tags; consent; device differences | Conversion attribution coverage |
| Market and offer | Audience, trigger, alternative, promise, proof, pricing; competitor channel and search gaps | Share of relevant demand, if measurable |
| Acquisition | SEO access, relevance and authority; brand/non-brand split; content decay; paid volume, cost, quality, fatigue, landing-page fit | Non-brand clicks and acquisition cost by segment |
| Activation and UX | First value event; time to value; signup and pricing friction; mobile usability; critical flows | Visitor-to-activated conversion |
| Retention and lifecycle | Cohort decay; activation drop-off; revenue segments; voluntary/payment churn; lifecycle sequence gaps; deliverability | Cohort retention at a stated age |
| Revenue and execution | Gross margin; expansion/contraction; payback; owners, capacity, dependencies; experiment conclusions and throughput | Model-appropriate revenue quality metric |

Adapt baseline metrics to the business model: recurring revenue and logo/revenue retention for SaaS; order contribution and repeat purchase for commerce; buyer/seller repeat, liquidity, take rate and contribution per transaction for marketplaces. Do not treat marketplace transaction value as company revenue.

Split net revenue change into new, expansion, reactivation, contraction and churn where data allows. Separate logo retention from revenue retention. Compare acquisition cost per retained customer alongside initial conversion cost when cohorts permit; otherwise mark the missing channel/cohort evidence.

Before diagnosing a product problem from worsening retention, compare cohorts at the same age and cut by source, geography, device and revenue segment. Distinguish never-activated users from users who activated then dropped. Review lifecycle sequences rather than one isolated email.

For standard depth, walk a small set of critical end-to-end flows where read-only access permits. Record screenshots or supplied observations, severity, affected step, and consequence. If an account, transaction, message, or live change is required, stop at the approval boundary and use supplied walkthrough evidence instead.

Avoid cosmetic tests or a brand redesign presented as a proven acquisition lever. Recommend instrumentation for recurring user failures when absent, with implementation subject to approval. Verify current platform and search requirements before recommending technical changes.

## Output contract

1. **Verdict:** the likely binding constraint, confidence, and strongest evidence; leave the verdict provisional when data is missing.
2. **Seven-layer scorecard:** healthy, constrained, or unknown; evidence level, source/period, leading metric, and handoff for each layer.
3. **Top findings:** evidence → consequence → recommendation → checkbox next steps. Link each factual claim to a supplied export, report, screenshot, or dated public source. Never pad the finding count.
4. **Data gaps:** missing evidence that could reverse the verdict and the smallest next check. Do not request already supplied data.
5. **Action matrix:** recommendation, layer, impact, effort, evidence, risk, dependencies, proposed owner, leading metric, and priority (now/next/later/stop). Owners remain unassigned unless confirmed.
6. **90-day outline:** quick wins first, then larger work, with proposed owners, milestones and check-in dates. Label proposed timing; do not invent commitments. Use `growth-roadmap` for the full quarterly plan.
7. **Benchmark snapshot:** actual versus relevant median/top-quartile only where current, comparable sources exist. Otherwise state unknown and the missing comparison.
8. **Next diagnostic:** one named specialist route, the finding and evidence it receives, the expected output, and the approval requirement below.
9. **Approval boundary:** state explicitly that this is a read-only audit and specify the required approval before live action.

## Handoffs

Record the finding here, then offer the relevant existing specialist:

- planning and ownership → `growth-roadmap`;
- acquisition structure or weak fit across channels → `channel-fit-diagnostic`;
- paid account performance and acquisition-cost reconciliation → `paid-analysis-review`;
- measurement, tagging and attribution → `marketing-tagging-audits`;
- audience, alternatives and missing customer evidence → `customer-research`;
- product-driven distribution → `product-led-acquisition`;
- signup, first value and activation friction → `onboarding-activation`;
- retention architecture and lifecycle gaps → `retention-state`;
- engagement depth → `power-user-curve`;
- economics and payback grading → `saas-unit-economics-audit`;
- a defined experiment after diagnosis → `experiment-design`.

For specialist work without a matching installed skill, describe the expertise and evidence needed in plain language; do not invent a skill name. Every handoff must carry the approval requirement. Do not claim specialist execution without its output.

## Approval and delivery checks

This audit is read-only; drafts and analysis may proceed. Before any live edit, publication, spend change, tracking or lifecycle activation, deletion, or other irreversible action, obtain the authorized owner's explicit prior approval for that specific action. The audit, roadmap, owner assignment, and handoff are not permission to implement.

Before delivery, confirm that this requirement appears explicitly in the deliverable and every specialist handoff. Check every quantity's provenance and resolve each `[VERIFY]` marker with a dated source or remove the claim. Keep explicit data gaps. Never modify the skill or its references during an audit; report any needed correction for separate review.
