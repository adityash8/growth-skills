# Reddit weekly read-only reconciliation

Use for a weekly Reddit Ads review that combines a historical baseline, platform reporting, downstream confirmation, pacing, and creative recommendations.

## Scope and source order

1. Read the agreed methodology, decision-maker overrides, and exact named baseline.
2. Confirm the current reporting period, account timezone, output destination, and mutation boundary.
3. Pull live sources only when permitted. If the user requests assembly from an existing run, use that run's artifacts and mark missing values unavailable.
4. Review related pending decisions by exact ad identifier before producing new pause recommendations. Shared creative names do not identify cloned ads.

Return drafts in the requested surface. A review request does not authorize publication or campaign changes.

## Frozen baseline and backfill

When an owner names a historical report as the comparison baseline, preserve it. Record later platform backfill separately rather than silently replacing its numbers. Recover detailed rows only from the same run unless another source is explicitly accepted.

If no frozen baseline was specified, apply the documented refresh policy consistently and retain the retrieval timestamps.

## Report mechanics

- Verify the current reporting API or installed CLI, units, date semantics, reporting lag, and pagination against current documentation and help.
- Use completed local dates and preserve exact inclusive/exclusive boundaries.
- Inspect nested metric rows rather than trusting a summary that may omit daily spend.
- Carry required request filters and bodies through every page. Verify row completeness and avoid summing aggregate totals together with their breakdowns.
- Split click-attributed and view-through purchases. Cost per click-attributed purchase is undefined when that count is zero.

## Downstream confirmation

1. Verify the analytics project, timezone, canonical event, deduplication key, test filters, and property population.
2. Prove the outcome event is live with a bounded all-channel count.
3. Count strict event-time channel attribution separately from current and initial profile sources or historical click IDs.
4. An old Reddit click ID does not establish current Reddit attribution when the event explicitly identifies another source.
5. Split by campaign or ad group only when stable identifiers survive or a verified mapping exists. Do not allocate unattributed outcomes by spend share.
6. Report platform and downstream numbers with their definitions. Compute a gap or capture rate only for a matched outcome and established coverage.

## Pacing

Use the cap actually in force during each part of the period. A daily cap multiplied by the number of days is valid only when that cap and eligibility held throughout. Otherwise reconstruct the schedule or label the denominator approximate.

Separate intended targets, period-live caps, current caps, partial launches, and later changes. Apply the owner's pacing threshold literally; do not invent a universal underdelivery rule.

## Action and inventory checks

- Count new ads from creation history in the local window.
- Count pauses from verified transitions. A current paused status and modification time alone do not prove when or why the pause occurred.
- Compare budgets on existing entities separately from initial budgets on newly created entities.
- Hydrate campaign, ad-group, and ad effective status before calling an ad active.
- Distinguish all-active inventory from ads observed delivering in the report.
- Preserve per-entity impressions, spend, and CTR when summarizing cloned creatives in a matrix.
- Apply the exact approved pause rule, including impression, spend, outcome, and maturity gates. Below-gate rows are watch items.

## Decision and output

A scale recommendation needs the agreed downstream-quality evidence; view-through-inclusive platform CPA alone is insufficient. Frequency alone need not imply fatigue without the methodology's paired evidence. Keep prior approved pauses and pending decisions visible rather than relabeling them as new actions.

Return a short decision block with overall condition, campaign evidence, actions, and next step. Put frozen-baseline caveats, matched reconciliations, pacing, active inventory, and entity-level decision evidence in an appendix. Do not publish or execute recommendations unless separately authorized.
