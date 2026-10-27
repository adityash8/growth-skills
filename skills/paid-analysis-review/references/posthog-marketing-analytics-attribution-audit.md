# PostHog connector and attribution audits

Use when reviewing whether paid-channel attribution or connector problems remain active.

## Scope and authority

Confirm the authorized project, timezone, requested historical window, and current source owners. Keep inspection read-only. Reconnection, credential changes, schema edits, sync activation, bot filtering, and tracking deployment require their own authorization.

Verify current metadata endpoints, query syntax, connector fields, and supported integrations against current documentation before using them.

## Connector freshness

For each relevant external source, inspect source type, enabled schemas, sync state, last successful sync, table mapping, and error category. Check table row count and minimum/maximum reporting dates with bounded aggregate queries.

- **Pitfall:** a table that still queries can contain stale data after its source fails.
- **Pitfall:** a failed credential refresh may require an administrator or integration owner. Analyst query access does not imply reconnection authority.
- **Pitfall:** a source-level success can hide an individual disabled or failing schema. Inspect both levels.

Record source warnings and compare table freshness with the requested period. Do not use a stale table as current spend truth merely because it has rows. Keep errors sanitized when sharing evidence.

## Attribution probes

### Lifecycle-link pollution

Inspect current and initial source fields at both event and profile level. Trend pageviews, signups, and paid outcomes separately for the suspicious lifecycle source aliases.

A lower first-touch signup count with residual pageviews supports a narrower improvement claim. It does not prove the problem disappeared. Identify the exact link surface before recommending parameter changes; preserve intentional lifecycle measurement under a compatible scheme.

### Mobile and cross-device handoff

Compare paid-source landings with downstream signups in matched windows. Measure click-ID coverage, persistent source fields, identity joins, and any existing handoff flags at each step.

If source or click IDs exist at landing but vanish at signup, investigate persistence, consent, redirects, and identity handoff. Do not jump directly to a capture failure claim.

If a deterministic handoff is needed, propose a scoped signed token with expiry and authorized identity handling. Do not put raw personal data into URLs. Treat profile or email matching as a separately assessed fallback.

### Bot and low-quality traffic

Use domain mix, repeated patterns, velocity, activation, and verified downstream behavior as triage signals. Unfamiliar domains alone do not establish bots; legitimate business users often have uncommon domains.

Keep analytic classification separate from hard blocking. Before proposing suppression of optimization events, establish precision, false-positive risks, and the legitimate-user impact. Sending polluted outcomes to a conversion API can amplify bad optimization signals.

## Fix order

Rank confirmed faults by decision impact and ownership:

1. Restore trustworthy event semantics and identify polluted outcomes.
2. Resolve source freshness and missing attribution persistence.
3. Specify authorized filtering or tracking changes with a bounded test and rollback.
4. Verify the resulting event path and downstream receipt independently.
5. Monitor source freshness, missing identifiers, paid-landings-to-signups, suspicious conversion share, and lifecycle first-touch anomalies using explicit baselines.

This is a diagnosis sequence, not permission to deploy repairs.

## Output contract

Return each issue as confirmed, improved with residuals, inconclusive, or no longer reproduced. Include matched windows, source health, decisive counts and denominators, alternative explanations, owner, smallest verification step, and the approval needed for any repair. Avoid account identifiers and personal payloads in shared examples.
