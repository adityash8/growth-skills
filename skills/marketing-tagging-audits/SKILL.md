---
name: marketing-tagging-audits
description: Use when auditing paid-media tracking to verify live tags, consent, event pairing, attribution, and safe publication gates.
---

# Marketing Tagging Audits

Audit GTM web/server containers, pixels, conversion APIs, first-party collectors, and product-analytics attribution. Separate configuration risk from observed delivery failure.

## Scope and authority

- Start read-only. Inventory, preview, publication, credential rotation, and synthetic traffic are different permissions.
- Use existing authorized access. A blocked read does not authorize a new connector, workflow dispatch, logging change, or secret retrieval.
- Follow the requested resource order and reporting destination. A read-only audit does not authorize comments or status changes elsewhere.
- When artifacts are allowed, use a fresh temporary directory and retain only the minimum redacted evidence. If files are forbidden, parse in memory.
- Verify platform fields, template semantics, API compatibility, and consent behavior against current official docs and the installed version.

## 1. Establish the live state

Fresh-check access, then list the relevant accounts, containers, workspaces, published versions, and pending changes. Refresh workspace identities after sync or edits.

- Compare published state, newer version headers, workspace changes, paused tags, and deployed JavaScript separately.
- A draft is not a live fix. A published paused tag does not fire. A current draft does not prove it was never published before a rollback.
- Modification fingerprints do not establish publication time. Anchor incident windows to verified production deployment evidence.
- If API access is blocked, inspect published web-container JavaScript and the first-party loader. Extract only the required resource fields; this cannot establish server-container state.
- For required repeated reads, compare semantic resource data and completeness, ignoring transport metadata. Changing resource bodies indicate concurrent edits.

## 2. Build an event-pair matrix

For each event, record:

| Layer | Required evidence |
|-------|-------------------|
| Browser producer | Tag type, triggers, exceptions, paused state, consent, event name, event-ID source |
| Transport | Destination, request path, payload, click/browser-ID fields, consent signal |
| Server consumer | Client, trigger predicate, event model, template version, outgoing mappings |
| Platform | Received event, deduplication result, diagnostics, reporting delay |

Keep account and resource identifiers in restricted evidence only. Public examples use descriptive aliases.

Trace one user action across the whole route. Matching field names do not prove matching values: independently generated IDs can differ even when both fields are called `event_id`.

Separate these failure classes:

- **Missing key:** a destination lacks a required deduplication or matching field.
- **Coverage mismatch:** browser and server events fire on different paths or at different rates.
- **Mapping mismatch:** a field arrives but sits outside the path the consumer reads.
- **Unverified receipt:** configuration looks correct but no destination receipt is available.

An upstream success response does not prove downstream ingestion. Overlapping eligible routes establish duplicate risk, not observed double-counting.

## 3. Check deduplication and identity

- Verify the platform's current deduplication contract, including event-name semantics, shared identifier, destination identity, and receipt window.
- Trace browser `eventID` and server `event_id` when supported. Do not substitute matching rates or parameter presence for value equality.
- Check auto page views, duplicate initialization, SPA/history triggers, plugins, backend requests, and paused predecessors before adding user data to fix a coverage gap.
- Separate browser-generated lifecycle IDs from stable payment transaction IDs. A webhook cannot share browser identity merely because it has an identifier.
- Check installed templates before adding explicit mappings; built-in tags may already inherit transaction or matching fields.
- Distinct browser/server conversion-rule IDs can represent linked semantics. Numeric rule-ID equality is not a universal deduplication requirement.
- Compare visitor/session identifiers privately and report presence/equality booleans where raw values are unnecessary.

Use [match-key field paths](references/match-key-field-paths.md) for transport, nested-field, event-time identity, and template-version checks.

## 4. Test consent in the right environment

Inspect three independent layers: web consent settings, signal forwarding, and server-template enforcement.

- A `consent_update` event proves a change occurred, not that the relevant purpose was granted.
- A tag marked as requiring no consent needs a verified alternative gate before being cleared.
- Compare runtime behavior with the operator's approved consent policy and applicable regional test requirements. Do not infer legal compliance from a tag setting.
- Record test region, CMP mode, browser state, and policy expectation before interpreting network or storage results.
- Exercise fresh denial, mid-session grant, persisted acceptance, returning denial, and SPA navigation where relevant.
- Separate source-code presence, runtime behavior, and jurisdiction mode. Each needs its own evidence.

Use [consent jurisdiction testing](references/consent-jurisdiction-testing.md) for the acceptance matrix.

## 5. Verify attribution, not just callbacks

1. Inspect the analytics schema before writing queries. Define event, person, session, purchase, and source fields.
2. Break landing events down by source, medium, and campaign. Measure missing values and contradictions before merging aliases or casing variants.
3. Trace explicit attribution fields through the active transport tag and its consumer. Variables existing on both sides do not prove forwarding.
4. Treat convenience switches such as common-field forwarding as unverified until preview or runtime payloads show their actual output.
5. Compare completed periods with consistent timezone, eligibility, test-account exclusions, and denominators. Check the explicit prior period when using comparison controls.
6. Deduplicate canonical purchases using verified transaction/subscription identity. Keep platform-attributed conversions separate from product-event totals.
7. Check first-touch-property coverage in the converting cohort before using it as a cross-device proxy. A false mobile flag means non-mobile unless the schema proves desktop.
8. Verify attribution persistence across the actual host/device boundary. A local browser store and an analytics cookie have separate scope and behavior.
9. If strict channel coverage is incomplete, state the limit and suppress a claimed source-truth CAC. Never allocate unattributed purchases by spend share.

Referral cleanup, event suppression, and quality classification solve different problems. Inspect existing transformations, including disabled drafts, before proposing another. Prefer a classification property when purchases, signups, or fraud evidence must remain available. Verify current analytics semantics before changing referral rules.

## 6. Review conversion settings and lag

- Resolve exact conversion actions, preserving case and separating native actions from imports with similar names.
- Inspect primary/secondary status, campaign goal use, counting rules, attribution model, and click/view windows. Primary status alone does not prove campaign bidding uses that goal.
- Distinguish interaction-date and conversion-date counts, and conversions from all conversions. Zero-fill missing rows only after a successful complete retrieval.
- Keep click-to-conversion lag separate from product-event lag; separate first and repeat payments.
- Use cohorts mature enough for the longest candidate window. Report denominator, missing lag, fractional attribution credits, and truncation from existing settings.
- Verify API field compatibility against current docs. A rejected field does not justify inventing a replacement or assuming a default.
- Window changes need approval and affect future measurement; they do not recover historical omitted events.

## 7. Protect credentials and evidence

Tagging exports can contain tokens in constants, parameter pairs, nested fields, and inline headers.

- Resolve references first and fetch only needed variables. Page large responses and summarize narrowly.
- Never paste credential values into reports or chat. Record variable alias, exposure class, and the proposed rotation/migration action.
- Repository secret metadata does not reveal a credential value. Do not extract secrets through logs or artifacts to unblock a read-only audit.
- [The local helper](scripts/redact_gtm_resource_dump.py) summarizes plain or wrapped JSON exports, including nested `containerVersion` resources:

```bash
python3 scripts/redact_gtm_resource_dump.py export.json
```

Run that command from this skill's folder. The default summary omits parameter values but retains names, resource IDs, and the source filename. These can still be confidential.

`--redacted-json` is a best-effort credential filter, not a publication sanitizer. Inspect output privately for identities, URLs, identifiers, personal data, and unrecognized secret shapes before retaining or sharing it. Never treat a regex filter as a privacy approval.

## 8. Handle unavailable or contradictory evidence

- For server-log counts, record identity alias, timezone, requested/retained window, filters, logging state, and pagination completeness.
- Public documentation scope is not proof of an account's capabilities. Outgoing delivery aggregates are not an incoming-request census.
- When authorized access is unavailable, keep counts and first/last timestamps unknown and name the exact manual read needed. Stop repeated credential hunts.
- Verify suspected event renames across deployed producer payload, ingress, and destination receipt. Source code plus a mismatched trigger establishes risk, not the number of lost events.
- A shape checker needs a deliberately invalid nested payload to establish what it validates. Envelope-only validation does not replace platform diagnostics.
- Share one scoped, redacted resource snapshot across parallel analysis where possible. Re-fetch only for freshness, incomplete retrieval, or concurrent-change checks.

## Acceptance and publication gate

Before saying fixed:

1. Test the denied-consent behavior required by the approved policy in the intended region.
2. For an accepted action intended to use browser/server pairing, observe one eligible event per route and a shared deduplication value.
3. Confirm event-time identity appears when available, including after signup or checkout.
4. Test persisted consent and SPA navigation where relevant.
5. Verify destination receipt and platform deduplication after the documented processing delay.
6. Capture the approved change list, preimage, rollback, and independent live readback. Draft, preview, published, and independently verified remain separate states.

For an event-inventory request, separate emitted raw events, platform-derived conversion rules, and advertising interaction metrics. Reporting actions alone cannot establish every event the site sends. Keep unresolved rule mappings explicit.

## Output contract

Return:

- scope, authority, time window, timezone, and live/draft coverage;
- event-pair matrix with evidence source and retrieval completeness;
- findings labeled Fact, Inference, Recommendation, or Unknown;
- priority, likely failure mode, consequence, and one falsification check per recommendation;
- approved or pending changes, acceptance proof, rollback, and blockers;
- the specific next read needed to close each unknown.

When correcting an existing report, identify the exact authored artifact, preserve unaffected measurements, update its timestamp and verdict together, and read back the correction. Rebuild affected charts from underlying values and label timezone and temporal precision accurately. Posting or editing elsewhere requires authorization.
