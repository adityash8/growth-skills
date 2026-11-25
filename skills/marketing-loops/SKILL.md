---
name: marketing-loops
description: "Turn a proven growth action into a safe recurring loop with explicit triggers, state, approvals, idempotency, monitoring, and stop conditions."
---

# Marketing Loops

Turn a proven marketing action into a repeatable workflow with a trigger, bounded
steps, a self-check, durable state, and an explicit stopping condition. Start with
one loop and prove someone uses its output before adding another.

Do NOT use for setting strategy (`growth-strategist`), choosing quarterly priorities
(`growth-roadmap`), designing a single test (`experiment-design`), or designing
viral growth mechanics (`viral-loop`). This skill owns reliable repetition.

## Inputs and evidence

Read any supplied product and marketing context before asking questions. Identify:

- the action, intended business outcome, and evidence that it works;
- data source, schema, freshness, completeness, and comparison window;
- action condition, owner, cadence, output destination, and review date;
- permitted actions, approval owner, budgets, compliance constraints, and state store.

Use supplied exports when live access is unavailable. Label observations with their
source and period; distinguish calculated results, assumptions, and proposed
thresholds. Missing data stays unknown. Produce a draft specification and name the
missing evidence; do not invent measurements, tool access, or completed execution.
If the action is unproven, route to `growth-audit` or `experiment-design` before
automating it. Missing thresholds or permissions block live action, not drafting.

## Define the loop

Fill all nine parts. A schedule alone is not a complete loop.

| Part | Required content |
|---|---|
| Check cadence | How often to inspect the signal; include timezone for a schedule. |
| Acts when | The condition that permits action, separate from checking. |
| Purpose | One business outcome, with evidence and a success measure. |
| Skills used | Relevant public skills and the concrete task handed to each. |
| Loop body | Ordered collection, comparison, decision, draft, approval, action, verification steps. |
| Self-check | Rule out stale tracking, noise, seasonality, and insufficient sample size before action. |
| State / idempotency | Durable cursor, action key, cooldown, open work, and verified outcome; repeating an input must not duplicate an action. |
| Stop / bail-out | Skip, halt, error, escalation, retirement, and manual disable conditions. |
| Output | Artifact destination, no-change behavior, exception owner, and review date. |

Treat cadence suggestions as starting assumptions to validate against the actual
signal and sample size:

| Signal | Suggested check cadence |
|---|---|
| Rankings and backlinks | Weekly |
| Ad fatigue and acquisition-cost drift | Every few days |
| Activation and onboarding | Weekly |
| Churn signals | Daily or on an event |
| Content decay | Monthly |
| Competitor changes | Weekly |
| Social mentions | Daily |

Most checks should log no action and exit. Do not force a change each run. A sparse
signal may need a longer window or manual review. Loops maintain proven actions;
strategy and creative direction still need judgment.

## Authority and channel protection

Classify every action before scheduling:

- Read, analyze, compare, draft, and stage within authorized data access.
- Require approval before external sends, publishing, spending, budget movement,
  deletion, suppression changes, or live account changes. Without approval, stage
  the work. Autonomous action needs explicit authorization, caps, and an allowlist.
- Require a written justification and owner approval for any increase in send
  quantity, new message type, or shorter contact cooldown, even when sending is
  already authorized. Do not silently increase volume because a test won.
- For send experiments, compare unsubscribe/disable rates and sends per incremental
  outcome against control. Do not roll out a winner if either guardrail worsens.
  Preserve consent, suppression, unsubscribe rules, and message-type opt-outs.
- Set per-run and per-recipient volume limits, hard spend ceilings, per-run budget
  change limits, runtime limits, and bounded retries. Judge paid changes on business
  outcomes, not clicks alone.
- Always escalate crisis mentions, sensitive complaints, strategic accounts,
  revenue/spend anomalies, deletion, and mass contact to a human.
- Confirm applicable privacy, messaging, testimonial disclosure, and platform rules.
  If permission or consent is uncertain, stop live action and request human review.
- Keep secrets and raw personal data out of prompts, state, logs, and command
  arguments. Store only necessary identifiers and limit retention.

Weigh the incremental value of an extra send against complaints, opt-outs, and
frequency caps. Define when repetition stops helping: stop at a cap, a breached
complaint/opt-out threshold, or no meaningful incremental outcome versus control.

## State, replay, and failures

Use the platform's durable state store or a project-local file. Never depend only
on memory. Define this schema with types and retention for the selected loop:

| Field | Purpose |
|---|---|
| enabled | Manual off switch checked before each run and before live action. |
| last_run / cursor | Last run and last successfully processed input. |
| action_key / status | Stable key per entity and action stage; pending, confirmed, or uncertain result. |
| cooldown_until | Earliest eligible contact/action time per entity. |
| in_flight | Open tests or interventions that must not overlap. |
| attempts | Bounded action/retry counts. |
| result | Verification evidence and outcome needed to prevent repeat action. |

On first run, initialize the cursor to now. Historical processing requires an
explicit backfill scope and a dry run. Preserve cooldowns during resets. Expire
old state only after the relevant replay and suppression windows have passed.

Before action, check deduplication, cooldowns, open work, current permission, and
suppression. Record pending intent and use a destination idempotency key where
supported. Prevent overlapping workers from acting on the same key. After action,
query the destination to verify the resulting state before marking it confirmed.
If a timeout leaves success unknown, reconcile before retrying; do not blindly
repeat a send or spend. Advance the cursor only past successfully handled inputs.

Append a minimal run log: timestamp, checked count, acted count, skip/error reason,
and verification result. Log no-change runs without sending a notification unless
a heartbeat was requested. Halt on stale/malformed data, lost permission, breached
limits, or exhausted retries. Assign an exception owner and document how to disable
both the schedule and all loops quickly.

## Scheduling and adoption

Use the available scheduler or cron for fixed review times, an event trigger when
the signal changes, or a manual recurring review for work requiring judgment.
Provide the proposed schedule and timezone; claim it is installed only after the
scheduler confirms it. Scheduling approval does not authorize later live actions.

Start with trustworthy tracking and a weekly review. Fix retention and activation
leaks before scaling acquisition. Add monetization and advocacy loops only after
their prerequisites work. Give each signal one action owner so overlapping loops
do not send conflicting messages or launch competing tests.

Revalidate thresholds, data sources, economics, and authority on a named review
date. Retire loops whose output is ignored, whose business value disappears, or
which repeatedly need manual repair.

## Output contract

Return all of the following, even when live execution is blocked:

1. Complete nine-part loop specification, including input and action contracts.
2. State schema with keys, types, persistence, cooldowns, and retention.
3. Decision table covering act, skip, draft for approval, halt, and escalate.
4. Failure/retry policy including uncertain outcomes and overlapping runs.
5. Explicit approval boundary with approver, caps, and eligible scope.
6. Verification query or concrete check against the resulting destination state.
7. Dry-run plan: replay the same input twice and prove no duplicate action;
   also exercise stale data, absent approval, and the kill switch without live sends.
8. Rollout and rollback steps, including disabling schedules and recovery limits
   for actions that cannot be undone.
9. Owner, output destination, exception handling, and review cadence.

## Handoffs

- Missing proof of value: `growth-audit` or `experiment-design`.
- Broken tracking: `marketing-tagging-audits`.
- Test design and readout: `experiment-design`; do not claim it ran without output.
- Paid performance diagnosis: `paid-analysis-review`; creative refresh work:
  `paid-media-creative-operations`.
- Activation: `onboarding-activation`; retention diagnosis: `retention-state`.
- Customer feedback: `customer-research`.
- Recurring action no longer works: `growth-strategist`.
- New quarterly priority: `growth-roadmap`.
- Economics drift: `saas-unit-economics-audit`.
