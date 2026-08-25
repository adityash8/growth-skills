---
name: marketing-loops
description: "Turn a proven growth action into a safe recurring loop with explicit triggers, state, approvals, idempotency, monitoring, and stop conditions."
---

# Marketing Loops

Use this skill only after an action has demonstrated value and needs reliable repetition.

A loop is not “run this every week.” It is a controlled system with inputs, state, a decision rule, bounded action, feedback, and a stop condition.

## Inputs

- validated action and evidence;
- input source and freshness requirement;
- decision rule;
- permitted action and authority level;
- owner, cadence, and expected output;
- cost, compliance, and failure constraints;
- current state store or deduplication key.

## Procedure

1. **Name the outcome.** Define the business result the loop protects or improves.
2. **Define the trigger.** Use a schedule, event, threshold, or source change. Do not poll more often than the decision can change.
3. **Define the input contract.** State source, schema, freshness, completeness, and failure behavior.
4. **Separate detection from action.** First decide whether anything changed or qualifies; act only when the condition passes.
5. **Define durable state.** Store the last processed cursor, content fingerprint, decision, action identifier, and result needed to avoid repetition.
6. **Make action idempotent.** Replaying the same input must not create duplicate messages, campaigns, records, spend, or edits.
7. **Bound authority.** Separate read-only collection, drafting, approval-required mutation, and prohibited action.
8. **Add budgets and limits.** Cap records, recipients, spend, runtime, retries, and consecutive failures.
9. **Define verification.** Query the resulting state rather than trusting a successful request.
10. **Define silence.** No change should produce no message unless a heartbeat is explicitly valuable.
11. **Add stop conditions.** Stop on stale data, malformed input, threshold breach, missing approval, rising errors, or lost business value.
12. **Assign ownership.** Name who reviews exceptions, approves risky actions, and retires the loop.
13. **Set review dates.** Revalidate the rule, source, economics, and permissions before the loop becomes infrastructure nobody owns.

## Loop specification

Document:

- objective;
- trigger and cadence;
- input contract;
- decision rule;
- action contract;
- authority and approval gate;
- state and deduplication key;
- budgets and rate limits;
- verification query;
- no-change behavior;
- retries and escalation;
- stop and retirement conditions;
- owner and review date.

## Output contract

Return:

1. complete loop specification;
2. state schema;
3. decision table;
4. failure and retry policy;
5. approval boundary;
6. verification check;
7. dry-run plan;
8. rollout and rollback steps;
9. owner and review cadence.

## Guardrails

- Never automate an unproven tactic merely because it is repeatable.
- Default external sends, publishing, spending, deletion, and account changes to approval-required.
- Do not place secrets in prompts, logs, command arguments, or state files.
- Minimize personal data and preserve suppression, consent, and unsubscribe rules.
- Fail closed when identity, scope, account, or permission is ambiguous.
- Kill loops that repeatedly produce ignored output or require manual repair.

## Handoffs

- missing evidence → `growth-audit` or `experiment-design`;
- recurring action no longer works → `growth-strategist`;
- new quarterly priority → `growth-roadmap`;
- economics drift → `saas-unit-economics-audit`.
