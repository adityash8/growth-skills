---
name: conversational-ads-optimization
description: Use when diagnosing conversational ad delivery, attribution, activation, landing-page fit, and cohort economics before changing campaigns or scaling spend.
---

# Conversational Ads Optimization

Diagnose OpenAI Ads, ChatGPT Ads, or another conversational ad surface from delivery through downstream value. Treat platform support and API behavior as account-specific facts to verify against current documentation and live reads.

## Operating posture

Work through delivery, tracking, activation, intent and landing fit, cohort economics, then budget. Cheap clicks or signups alone do not prove a channel can scale.

Use read-only access for diagnosis. Campaign, targeting, creative, conversion, upload, and spend changes require explicit authority for the named scope. Existing authorization does not need duplicate confirmation.

## Workflow

### 1. Set the decision contract

Capture the business goal, decision horizon, account timezone, currency, attribution model, conversion definition, acceptable acquisition cost, guardrails, and reporting delay. Ask for missing thresholds rather than inventing benchmarks.

Resolve the intended account through its configured credential route. Keep secrets and account identifiers out of public artifacts.

### 2. Verify live delivery state

Read account, campaigns, groups, ads, status, objective, bidding, budget, context hints or equivalent targeting, destination, copy, review state, and pacing. Record timestamp and pagination coverage.

For destination QA, walk active campaigns to active groups to active ads. Extract actual live destinations, follow redirects, check the final page and query parameters, and summarize failures by group. Old plans do not prove which URLs are serving.

### 3. Pull platform and downstream evidence separately

Collect spend, impressions, clicks, CTR, CPC, and CPM by day and the grain needed for the decision. Verify units and currency from the source.

Read product analytics or transaction records separately for attributed sessions, signups, activation, qualified leads, checkout, subscriptions, invoices, or purchases. Define the event and counting unit for each.

Keep unavailable conversions as `null`, not zero. Do not silently replace a failed live source with historical data. Isolate source failures so one broken connector does not hide the rest of the evidence.

### 4. Reconcile clicks, sessions, and outcomes

Compare matching windows and grains. Show click-to-session match, session-to-signup, signup-to-activation, cost per qualified outcome, and cost per customer where supported.

If match is weak, inspect redirects, UTM survival, consent, browser behavior, load errors, identity stitching, and event capture before recommending scale.

Do not sum campaign, group, and ad totals together. Do not mix unique users, sessions, event occurrences, and orders.

### 5. Compare matured cohorts

Compare paid conversational cohorts with relevant organic or paid cohorts using the same attribution rules, event definition, observation age, and eligibility criteria. Preserve unknown attribution as its own bucket.

Organic conversational referrals are a comparison, not a control group. Better organic activation suggests a matching or landing hypothesis; it does not establish that paid delivery will produce the same users.

### 6. Inspect intent, creative, and landing fit

Treat the optimization unit as:

```text
conversation intent -> hint cluster -> creative -> landing action -> qualified outcome
```

Write complete descriptions of the audience, job, and topic. Check whether the live system preserves each hint as intended. Pitfall: delimiter parsing can split one sentence into fragments, so inspect a fresh read after changes.

Match the destination's first viewport, proof, CTA, and first product action to that intent. A generic page is a testable mismatch hypothesis, not automatic proof of failure.

Read [the conversational ads playbook](references/conversational-ads-playbook.md) when drafting hints, tracking, creative, landing tests, or scale criteria.

### 7. Test scale readiness

Define gates from the operator's economics and data quality:

- acceptable click-to-session reconciliation and attribution coverage;
- qualified activation or purchase evidence rather than signup volume alone;
- acquisition cost within the approved target;
- sufficient matured exposure for the decision;
- reliable tracking and no unresolved policy or destination failures.

Set budget increments, observation period, maximum loss, and stop rules in advance. Scale only the supported intent/creative/landing combination. No universal percentage or cadence substitutes for account evidence.

### 8. Separate recommendation from execution

A recommendation names exact scope, evidence, expected effect, confidence, alternative explanation, metric, guardrails, check date, and falsification condition.

For an approved asset refresh, use [paid media creative operations](../paid-media-creative-operations/SKILL.md). Map every copy row and asset, count operations, verify destinations, preserve controls, and read back created objects.

For clones, create the parent paused unless activation is explicitly authorized. Keep an experimental campaign distinguishable in tracking without changing unrelated creative or targeting. Check total spend exposure before activation.

## API and reporting pitfalls

Verify current schemas, versions, supported aggregation levels, and account capabilities before using an endpoint.

- A local wrapper can lag the platform schema. Check both and test one read before a backfill or batch.
- Validate pagination limits, array serialization, time-range fields, timestamp alignment, and metric prefixes. Do not reuse a historical query shape blindly.
- Requested fields may return nested or flattened. Inspect raw, redacted responses and test one complete period before aggregating history. Stop on ambiguous shapes.
- Segmentation can repeat campaign totals across segment rows. Verify the grain and reconcile to independent totals before summing.
- Missing country or device conversion support does not justify reporting true segment CPA. Label any joined downstream estimate and expose unattributed outcomes.
- After a location exclusion, split pre-change and post-change dates. Check the latest complete day separately from residual delivery in a rolling window.
- Resolve conversion-event definitions from current account settings. A similar name or old export does not prove the event identifier, type, or attribution window.
- If an HTTP client is blocked, use a supported authenticated route. Do not expose credentials or weaken access controls.
- For a URL-only edit, use the documented update method, preserve other creative fields, and rerun destination QA. Check review state again after the edit.

## Tracking contract

Use the existing analytics taxonomy. A generic shape is:

```text
utm_source=<platform_slug>
utm_medium=<paid_medium>
utm_campaign=<campaign_slug>
utm_content=<group_slug>__<creative_slug>
utm_term=<intent_theme_slug>
```

Preserve first-touch attribution into downstream events where permitted and relevant. Verify click identifiers and platform macros against current documentation. Group-only attribution cannot support creative-level conclusions.

## Recurring agents

For scheduled or self-improving operation, read [shared ads learning loop](references/shared-ads-learning-loop.md). Learning may improve ranking and wording. It must never widen write permission.

Start with live reads and evidence packets. Prove source access, state persistence, gate behavior, and a real scheduled run separately from offline tests. Do not automate an unresolved channel hypothesis.

## Output contract

Return:

1. decision and confidence;
2. observed facts with source, window, grain, timezone, currency, and attribution definition;
3. delivery-to-value funnel with unknowns and reconciliation gaps;
4. hypotheses, recommendations, and one falsification check;
5. approved action or blocker, independent readback, and next review date.

When an external delivery format is explicitly requested, complete the authorized sequence and verify persistence. Do not infer permission to send messages from an analysis request.
