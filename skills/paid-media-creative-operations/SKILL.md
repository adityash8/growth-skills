---
name: paid-media-creative-operations
description: Use when mapping approved ad copy and assets into live paid campaigns with protected controls, bounded changes, approval gates, and independent verification.
---

# Paid Media Creative Operations

Turn approved concepts into a verified creative refresh. Start after the concepts exist. Keep strategy, targeting, and budget changes within the user's stated scope.

## Operating rules

- Read live state before mapping assets or writing.
- Add creatives without editing proven controls unless that exact edit is authorized.
- Require authority for each live mutation. An explicit instruction to execute the stated change supplies that authority; do not ask for duplicate confirmation.
- Approval covers the named scope, not unrelated account changes or policy exceptions.
- Keep click-attributed and view-through outcomes separate.
- Stop when source assets, copy, target entities, attribution, or write capability cannot be verified.

## Workflow

### 1. Establish scope and authority

Read the request and available operating record. Capture platforms, target entities, approved mutation types, exclusions, rollback owner, and stop conditions.

Distinguish analysis, dry run, and live execution. A delegated research task does not authorize an account change. If execution is already authorized, complete preflight and proceed within that scope.

### 2. Ground every proposed ad

Use the approved copy sheet and asset store. Record:

- source row, persona, funnel stage, concept, and version;
- exact copy fields and approved claim evidence;
- exact asset filename and immutable file identifier;
- MIME type, dimensions, and placement.

Do not invent testimonials, statistics, CTAs, or missing variants. If a row names an asset family, record the deliberate file choice and its fit.

### 3. Snapshot live account state

Read campaigns, groups, ads, status, objective, format, budget, relevant expansion or offsite settings, active-ad counts, timezone, and currency. Record the timestamp and pagination coverage.

Old exports and task descriptions provide context. They do not prove current account state.

### 4. Protect controls

Use a fixed window of complete days in the account timezone. Identify controls by target entity, using the strongest available signal:

1. click-attributed purchases or qualified leads;
2. other defined downstream outcomes;
3. signup plus delivery evidence when downstream volume is sparse;
4. spend or CTR only as a labeled fallback.

Keep attribution windows, sample limits, and view-through totals visible. Do not call a view-through purchase direct proof of a creative's effect.

### 5. Prune only with evidence

If rotation is crowded, prepare a separate pause proposal before adding more ads. Each candidate needs current active status, a fixed window, sufficient exposure under a stated decision rule, no protected outcome, no control overlap, and a one-ad rollback.

Set a capacity target rather than pausing an arbitrary percentage. Leave the target unmet if evidence does not support enough pauses. A creative refresh does not automatically authorize pausing existing ads.

### 6. Build bounded waves

Choose a small set of distinct concepts per target. Sequence waves by the approved experiment and risk, rather than distributing every available asset everywhere.

State the upload count, create count, activation count, and active-ad count after the wave. Keep one clear hypothesis per asset/copy pairing.

### 7. Preserve attribution and destinations

Read the existing analytics taxonomy before building URLs. Preserve stable source, medium, and campaign values. Give each creative a distinct content value and retain supported audience or click-identifier parameters.

Fetch every actual destination with redirects followed. Check the final page, expected response, and preservation of the complete tracking query. An accessible URL can still be the wrong landing page.

### 8. Check specifications and collisions

Verify files exist, dimensions and MIME match current placement rules, copy meets current limits, target entities still exist, and deterministic ad names do not collide.

For a naming-only cleanup, rename the existing ad. Do not upload a replacement. Check name uniqueness within the target group and choose an unused version when another creative already owns the desired name. Verify ad identifier, status, creative, destination, and total inventory are unchanged after the rename.

### 9. Prove the complete write path

Read access does not prove upload or create permission. Check each required operation separately:

1. media upload or registration;
2. post or creative-object creation;
3. ad attachment or creation;
4. review-state and delivery verification.

If one step is unsupported, name it and prepare a manual handoff. Do not label a batch executable through a tool that cannot create its required resources.

### 10. Freeze the execution manifest

Include:

- live-state timestamp, metric window, timezone, and currency;
- target entities and settings;
- protected controls and evidence-backed pause candidates;
- every new ad with source-copy and asset proof;
- operation counts, URL checks, and specification checks;
- settings that must remain unchanged;
- rollback steps, exact approved scope, and remaining blockers.

Hash the final manifest. Recompute its digest after any change, and renew approval if the payload or scope changed.

### 11. Execute and verify

Use bounded batches and the existing approved write path. For clones or multi-object launches, read [governed live ads execution](references/governed-live-ads-execution.md).

After each write, independently fetch the affected entity. Record identifier, status, review state, destination, source mapping, and unchanged settings. A successful API response does not prove serving or approval.

Update the operator's chosen work record only when authorized, then read the update back. Verify delegated results independently before reporting completion.

## Platform-specific checks

Verify these against current documentation and the actual account before use:

- **LinkedIn:** if a broad inventory lookup fails, analytics can identify delivered creatives for the requested window. Hydrate them with account-scoped reads. Label this the delivered universe unless full inventory coverage is proven. Check media, sponsored-post, and creative permissions separately.
- **Reddit:** confirm report request method, pagination, allowed breakdowns, and money units. If pagination requires repeating the request body, preserve it. Aggregate only exact returned dates and keep click and view conversions separate. Never assume every account reports in the same currency.
- **Conversational ads:** resolve the configured account and credential route, validate the current create schema, and verify upload permission separately. If one HTTP client is blocked, use a supported authenticated route without weakening access controls. Bound retries and resume from verified live objects.

## Stop conditions

Stop before the next mutation if authority is missing, a target changed, source proof is incomplete, a protected control is affected, a URL fails QA, required permissions are absent, or live results differ from the manifest.

## Output contract

Return:

- **Result:** prepared manifest, verified write, partial completion, or blocker.
- **Evidence:** source mapping, counts, readback checks, timestamps, and artifact digest.
- **Decision:** what to continue, stop, or request next, with confidence and a falsification check.
- **Recovery:** rollback status and any missing proof.

Keep account identifiers in access-controlled operating records. Redact them and any confidential metrics from public examples.
