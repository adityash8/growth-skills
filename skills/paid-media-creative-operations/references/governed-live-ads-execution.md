# Governed live ads execution

Use for campaign clones and other multi-object writes. Verify platform-specific fields and methods against current documentation before execution.

## Authority

An explicit instruction to execute a stated mutation supplies authority for that scope. Do not replace it with another approval request. Preserve live preflight, bounded writes, policy checks, and independent verification.

Scope changes, increased caps, activation, and unrelated account changes need their own authority. A dry-run flag or delegated task is not an approval system.

## Run sequence

1. Read the request and live account. Resolve source and target objects, objective, conversion event, budget, countries, child inventory, statuses, and tracking.
2. Separate deliverable objects from paused or policy-excluded objects. Preserve hard exclusions. Record deliberate differences from a source campaign.
3. Check rollout mode, write enablement, kill switch, account status, policy, operation cap, daily allowance, and target existence.
4. Count campaigns, groups, ads, uploads, and activation operations before writing.
5. Keep normal caps intact. Use an exception only when explicitly authorized, validated, bounded, and confined to the approved run. Reject invalid values before an API call.
6. Bind approval to account, exact payload digest, actor, expiry, and scope. Use an idempotency key where supported.
7. Create the parent paused unless immediate activation is explicitly authorized. Add and verify children before activation. An active clone can increase spend immediately.
8. Re-read settings, children, conversion event, budget, countries, tracking, and states. Recheck gates between batch items.
9. Record verified results, partial results, blockers, and recovery actions. Read back any authorized external record update before calling it persisted.

## Build create bodies from the create schema

Do not send a read response straight to a create endpoint.

- Include only documented, writable fields.
- Remove read-only, computed, unknown, and unsupported null fields.
- Check location representation, objective availability, and budget shape for the actual account.
- Remove response-only creative identifiers, image URLs, timestamps, and review fields unless the create schema explicitly requires them.
- Do not add convenience fields that the endpoint does not support.

Pitfall: a validation error may come from a response-only field or unsupported shape. Read the redacted error detail and compare the payload with the current schema before retrying. Do not repeatedly replay the same failing request.

## Credential route

Use the configured account-specific credential through the intended launcher. Never print it in logs or work records.

Pitfall: assigning a shell variable while sourcing a configuration file does not automatically export it to a child process. Export only the required variables, then verify the exact launcher with a small account read. Tool discovery or a connection banner does not prove account access.

## Eventual consistency and resume

A create response can return an identifier before a list endpoint exposes the object.

- Poll the returned identifier with bounded retries and increasing delay.
- Treat delayed visibility as unresolved until verified, rather than immediately creating a duplicate.
- Before retrying a write, inspect the mutation record and fresh account state.
- Resume only missing objects; skip verified parents and children.
- If there is no supported external identifier, match conservatively using parent, exact name, creative asset, and destination. Stop on ambiguous matches.
- Stop on unknown active objects or scope drift.

## Final proof

Verify from fresh reads:

- parent identifier, name, objective, and intended state;
- conversion event name, type, attribution window, and availability;
- budget, currency, and exact location inclusion/exclusion;
- expected group and ad counts;
- excluded objects absent or inactive;
- destinations and tracking values;
- kill switch, gate outcomes, and executed-operation counts;
- the chosen work record and any authorized completion state.

Separate created, approved, active, and serving. A successful create proves only creation until the remaining states are checked.

If execution stops partway, report what exists, what remains paused, what did not run, and the safe resume or rollback path. Do not mark the whole batch complete.
