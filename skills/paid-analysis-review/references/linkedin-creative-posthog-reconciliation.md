# LinkedIn creative to PostHog reconciliation

Use when a disputed creative-level purchase count affects a pause or hold recommendation.

## Scope and event health

1. Read the methodology, decision-maker changes, named prior baseline, and exact target entities.
2. Confirm the authorized PostHog project, timezone, identity behavior, test filters, and source freshness.
3. Discover actual signup and purchase events, stable customer/transaction keys, and attribution property population.
4. Count all-channel outcomes in the bounded window to establish instrumentation health.
5. Pull LinkedIn creative, parent-campaign, and conversion-specific reporting for matching dates. Verify current API fields and conversion namespaces against current documentation.

## Platform verification

- Creative spend and parent-campaign spend are different grains. Show both when a cited number is disputed.
- Resolve conversion rules to purchases instead of treating every generic conversion as a purchase.
- Verify browser/server deduplication. Without proven overlap, summing or taking a maximum does not yield unique purchases.
- Hydrate current serving/review state, campaign membership, underlying post reference, and modification history.
- A modification timestamp does not reveal which field changed. Recover a field-level diff or change history before naming a budget, targeting, copy, or tracking change.
- If the entity materially changed inside the window, qualify the period or split it at a verified change time. Mark it mixed if the change cannot be resolved.
- When cited spend disagrees with both creative and campaign reads, recover the original payload, retrieval time, pivot, fields, dates, and filters. Numeric closeness alone does not prove provenance.

## Attribution ladder

Report each layer separately:

1. exact event-time channel source;
2. current and initial profile channel source;
3. documented legacy aliases;
4. click-ID presence;
5. strict campaign/ad-group identifier matches;
6. strict creative identifier matches;
7. verified underlying post-reference matches.

Search confirmed fields first with exact matching or parsed controlled tokens. Broad string searches can discover dynamic fields but require manual inspection before attribution. Do not project full property payloads or personal data into a review artifact.

A click identifier establishes click-chain evidence only until a verified mapping resolves it to a target entity. Persist stable entity identifiers through signup and purchase for future entity-level reads.

## Signup cohorts

- Count raw signup events and unique people separately.
- Form a strict creative/campaign cohort from stable identifiers, then require the downstream purchase to follow the qualifying signup within the agreed horizon.
- Exclude pre-existing customers if the metric is customer acquisition. Handle multiple signups and repeated purchases explicitly.
- Run broader channel-visible cohorts as tracking diagnostics; do not allocate their outcomes to a target without a mapping.
- A missing click ID at purchase after its presence at signup indicates persistence loss. It does not identify a hidden creative.

## Verdict gates

- **Pause recommendation:** the exact approved spend/impression/outcome rule is met, the requested window and maturity are complete, target attribution is identifiable, entity state is interpretable, and recent/lifetime signals do not contradict the rule.
- **Hold recommendation:** verified target-level downstream activity or an unmet evidence gate calls for continued observation within the approved budget.
- **Inconclusive:** target IDs are absent, cohort formation fails, the entity changed ambiguously, source health is unresolved, or the requested period is incomplete.

An unidentifiable cohort is not confirmed zero. Zero purchases alone is not a universal pause rule.

## Output contract

Include scope and exact boundaries, event-health baseline, target-level event and unique-person counts, broader channel visibility, signup-to-purchase results, platform creative-versus-campaign figures, attribution limitations, verdict, and next check. State whether any writes occurred. Do not pause, post, or alter tracking without separate authority.
