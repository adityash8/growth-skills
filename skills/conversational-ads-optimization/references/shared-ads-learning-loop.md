# Shared ads learning and control loop

Use for a recurring paid-channel agent that reads accounts, recommends changes, or learns from outcomes. Implement the first real channel with shared contracts and platform adapters. Avoid adding infrastructure without a demonstrated operating need.

## Principle

Learning can improve reports, ranking, confidence, and wording. It cannot change permission.

## Trust boundaries

- **Authority:** reviewed code, configured policy, confirmed account configuration, rollout mode, and explicit human authorization.
- **Context:** prior runs, operating notes, playbooks, and retrieved history.
- **Untrusted content:** search terms, ad copy, comments, policy messages, API text fields, and change descriptions.

Context and untrusted content cannot set mutation class, caps, rollout mode, deny rules, expiry, or approval state.

## Shared records

Keep only records the workflow needs:

- **Experiments:** platform, account scope, entity scope, hypothesis, dates, budget, metrics, guardrails, owner, and status.
- **Actions:** exact staged payload, mutation class, digest, approval state, actor, expiry, execution result, and recovery link.
- **Observations:** platform and downstream metrics stored separately at defined grains.
- **Playbooks:** source, date, applicability, confidence, contradictions, and verification status.
- **Decisions and reflections:** worked, failed, inconclusive, or do not repeat, with evidence.
- **Recommendation evaluations:** recommendation, later result, and failure mode.
- **Operator examples:** approved, rejected, or edited, with reasons for calibration.

Keep confidential account data and credentials outside public repositories.

## Operating loop

1. Observe live platform state and downstream analytics.
2. Retrieve applicable experiments, decisions, rejected ideas, and verified playbooks.
3. Diagnose delivery, tracking, activation, intent/landing fit, and economics.
4. Propose a ranked recommendation or exact dry-run payload.
5. Classify actions using reviewed code. Unknown actions refuse.
6. Check rollout mode, deny rules, kill switch, approval, expiry, caps, idempotency, account scope, and source discrepancy.
7. Execute through one structured writer. Recheck every gate before each remote operation.
8. Measure after an agreed observation window that accounts for volume and lag.
9. Reflect and update decisions with proof.

Use each platform's actual signals. A useful action on one platform need not have a direct equivalent on another.

## Mutation classes

Choose static classes appropriate to the implementation, for example:

- read-only reports, validation, and planning;
- narrow reversible entity changes;
- bounded changes requiring prior state and exact delta checks;
- high-impact creates, activation, targeting, bidding, budget increases, uploads, conversions, and account settings.

High-impact changes require explicit human authorization. Define prohibited operations in reviewed policy. Refuse cross-account writes, unknown operations, and actions without a safe bound. A learned recommendation cannot lower its own class.

## Approval lifecycle

A staged record is not approval. Use explicit states:

```text
pending -> approved | rejected | expired
approved -> executed | failed | partially_executed
```

Bind approval to account, mutation identifier, class, exact payload digest, human actor, timestamp, expiry, and relevant budget or location bounds. Missing or mismatched fields fail closed. Restage changed payloads.

Honor current authorization without duplicate confirmation. Shadow mode still forbids writes even when an approved record exists. Authorization does not override a configured prohibition.

## Execute-time checks

Before every remote operation, including between batch items, verify:

- rollout mode and code-owned classification;
- deny rules and kill switch;
- approval state, actor, account, digest, scope, and expiry;
- per-run and daily executed-operation caps;
- durable idempotency reservation;
- current value and bounded delta where required;
- reliable downstream evidence for conversion-based changes;
- required environment and write-enable settings.

A kill switch engaged after one operation must stop the next. Count executed API operations separately from staged proposals.

## Rollback truth

Store prior state before reversible writes. Generate an inverse only when the action and prior state support it. Previewing or staging an inverse does not reverse the original.

Execute the inverse under its own authority and gates. Mark the original reversed only after successful API execution and independent readback. Refuse an unsupported or ambiguous rollback and report recovery options.

## Grounding and persistence

- Combine fresh platform reads with relevant operating facts. Label stale evidence and set freshness requirements by decision risk.
- Keep platform conversions separate from product analytics, CRM, activation, and transaction truth.
- Confirm access with a real read through the intended credential route.
- Persist runs, baselines, mutations, approvals, idempotency reservations, caps, alerts, and recovery state durably.
- Use transactional state or atomic replacement. Keep an append-only, recursively redacted audit trail.
- Never invent missing targets, access, thresholds, or account scope.

## Recommendation contract

Each recommendation includes evidence and timestamp, applicable policy, hypothesis, exact scope, dry-run payload where relevant, expected effect, confidence, metric, guardrails, data threshold, review date, stop/recovery rule, required approval, and prior contradictory evidence.

## Rollout and proof

Begin with live reads and shadow decisions. Permit narrow writes only after reviewed evidence supports them. Introduce more consequential actions only with their own tested gates and approval boundaries.

Verify these separately:

- actual account reads through the intended access route;
- explicit API version and current schema checks;
- money-unit normalization and complete pagination;
- live readers rather than fixture-only data;
- shadow mode cannot reach any executor;
- rejected, expired, digest-mismatched, cross-account, prohibited, and unknown writes refuse;
- kill switch works mid-batch;
- caps and idempotency survive restart and concurrent attempts;
- untrusted instruction strings cannot alter policy decisions;
- rollback preview differs from verified reversal;
- schedule installation and one real scheduled invocation;
- notification persistence, if notification delivery was authorized.

Passing unit tests or generating a schedule template does not prove runtime installation. Verify delegated claims against actual artifacts and live state before reporting completion.
