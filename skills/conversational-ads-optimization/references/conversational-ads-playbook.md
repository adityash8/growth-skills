# Conversational ads playbook

Use when designing a test for a conversational ad surface. Verify objectives, eligibility, geographies, conversion tracking, bidding, limits, and reporting against current documentation and live account capabilities.

## Test the intent chain

Map each proposed group to a buyer job, intent theme, creative promise, destination, first action, and business outcome. Treat funnel position as a hypothesis rather than assuming that all conversational traffic has the same intent.

Do not scale from CTR, CPC, or raw signups alone.

## Setup checklist

1. Define a meaningful success event, counting unit, target cost, and observation horizon.
2. Confirm current platform objectives, supported events, policies, and account eligibility.
3. Verify event capture using a permitted test event. Check browser or server receipt, downstream analytics, deduplication, and attribution persistence.
4. Compare platform-reported conversions with product or transaction truth. Keep the sources separate.
5. Group by intent and the approved budget or regional boundary.
6. Match each group to an appropriate page or deep link.
7. Define scale and stop criteria before exposing traffic.

Pitfall: a campaign can deliver while downstream event capture is broken. Passing campaign QA does not prove conversion tracking.

## Hint formula

Use a complete description:

```text
audience + job or problem + solution or topic being evaluated
```

Generic examples:

- `small business operators comparing scheduling tools to reduce missed appointments`
- `support managers seeking a faster way to route repeated billing questions`

Avoid bare brand names, dangling sentence fragments, and keyword dumps. Check delimiter handling. After an authorized change, inspect a fresh live read to prove the intended strings persisted.

## Creative and landing rules

Write copy that continues the user's question. Make one useful promise and support it with approved evidence. Avoid fabricated proof, urgency, prices, and customer results.

For each intent theme, check:

- headline answers the active question;
- proof supports that answer;
- CTA advances the relevant job;
- the first product action is available and works;
- redirects preserve tracking.

Comparison, problem-solving, action, and proof-led variants are hypotheses to test. They are not guaranteed winners.

## Conversion objective

Choose the event closest to business value that is observable, reliable, eligible for optimization, and frequent enough for a useful decision. Verify current bidding support per account.

If signup is a proxy, track signup-to-activation and downstream quality. A cheaper proxy can conceal a worse customer acquisition cost.

## Scale contract

Write the operator's thresholds for tracking coverage, qualified conversion, acquisition cost, sample maturity, and maximum loss. Choose one bounded increment and a review window appropriate to conversion delay.

A failed tracking check blocks a scale decision. Sparse or immature cohorts remain inconclusive. Record the smallest next test that could change the decision.

## Common pitfalls

- counting repeated event occurrences as customers;
- comparing fresh paid cohorts with mature organic cohorts;
- hiding unattributed outcomes;
- changing targeting, bidding, creative, and destination simultaneously;
- judging performance inside unmeasured reporting lag;
- claiming segment CPA when conversions are unavailable at that grain;
- treating a successful create response as proof of approved delivery;
- building a recurring optimizer before reliable channel evidence exists.
