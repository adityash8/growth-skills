# PostHog paid purchase cross-checks

Use when reconciling paid-platform purchase credit against product analytics.

## Core workflow

1. Confirm the authorized organization, project, timezone, identity model, and reporting window through project metadata. Avoid exposing private project identifiers in public artifacts.
2. Discover the canonical purchase event and stable deduplication key from current schema, event samples, and the business definition. Do not substitute a similarly named historical event.
3. Prove event flow with a bounded all-channel count and measure missing deduplication keys.
4. Run strict entity-level matching against verified campaign/ad-group/creative fields, then a separate broader channel-attribution read.
5. Keep event-time, current-profile, and initial-profile attribution distinct. Initial profile fields are not automatically immutable first touch.
6. Break out entities only when stable identifiers or verified mappings survive. Missing identifiers mean attribution unavailable, not zero customers.
7. Compare platform click-only and click-plus-view totals separately, with matching outcome definitions and known overlap.
8. State attribution coverage beside every downstream count. Sparse visible attribution is not complete purchase truth.

## Query shape

Adapt these logical steps to the current HogQL schema and supported query API. Verify syntax against current documentation; field names below describe roles, not a preconfigured account.

```text
eligible_outcomes = canonical paid events
  within [start, end) in the agreed timezone
  excluding documented test traffic

key_health = rows with a usable stable outcome key / eligible rows
all_outcomes = distinct stable keys among eligible outcomes
strict_target_outcomes = distinct stable keys whose verified entity field
  exactly matches the requested target under the declared attribution rule
channel_visible_outcomes = distinct stable keys with the declared channel source
```

Use parameterized values where supported. Parse controlled identifier tokens rather than arbitrary substring searches. Handle empty keys before deduplication; otherwise missing values can become a false single purchase or disappear silently.

If attribution must bridge signup and purchase, form a strict signup cohort and join locally when the supported remote query cannot reliably express the sequence. Require purchase after the qualifying signup and use the agreed maturity horizon. Keep the raw cohort and outcome counts for verification.

## Reconciliation traps

- **Pitfall:** an all-channel purchase total establishes event health, not channel attribution.
- **Pitfall:** historical click IDs can coexist with a later explicit source from another channel. Declare the attribution model rather than letting an old ID override it silently.
- **Pitfall:** a campaign identifier embedded in an unrelated URL can pass a broad string search. Inspect field semantics and exact matches.
- **Pitfall:** platform purchase events, unique buyers, and subscriptions are different units. Do not use event counts as audience-seed counts.
- **Pitfall:** direct purchases and signup-cohort purchases answer different attribution questions. Report both without adding overlapping outcomes.

## Output contract

Return canonical event and key, exact dates/timezone, all-channel health, strict target count, broader channel count, unique buyers where defined, missing-key and identifier coverage, platform click/view figures, matched-definition deltas, and one evidence-bounded decision.

Use visible or attributed when coverage is incomplete. Use target breakout unavailable when the required identifiers do not survive. Do not allocate unattributed purchases by platform spend share.
