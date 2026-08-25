---
name: saas-unit-economics-audit
description: "Audit SaaS unit economics by segment using gross-margin LTV, CAC, payback, retention, and sensitivity analysis."
---

# SaaS Unit Economics Audit

Use this skill before scaling acquisition, changing pricing, or claiming a segment is profitable. Analyze by segment and acquisition channel before trusting blended economics.

## Inputs

Use one consistent period and currency.

- new customers and fully loaded acquisition spend by channel;
- revenue, gross margin, discounts, refunds, and service costs;
- logo and revenue retention by cohort;
- expansion, contraction, and churn timing;
- sales-cycle length and implementation cost;
- customer counts and revenue by segment;
- attribution method and known gaps.

## Core calculations

State formulas and assumptions next to every result.

- `CAC = attributable acquisition cost / new customers`
- `Gross profit per period = revenue × gross margin`
- `Simple payback periods = CAC / gross profit per customer per period`
- `Simple LTV = average revenue per period × gross margin / customer churn rate`
- `LTV:CAC = gross-margin LTV / CAC`

Simple LTV is unsafe when churn is non-stationary, expansion is material, cohorts are immature, or customer concentration is high. In those cases, use observed cohort gross profit and an explicit forecast tail.

## Procedure

1. **Validate definitions.** Confirm customer, acquisition cost, revenue, gross margin, churn, and cohort rules. Separate marketing-only CAC from fully loaded CAC.
2. **Segment first.** Split by customer type, plan, geography, contract motion, and channel where sample size allows. Never let a strong segment hide a weak one.
3. **Build cohort economics.** Calculate cumulative gross profit by acquisition cohort and compare it with acquisition cost over time.
4. **Calculate payback.** Use actual gross-profit timing. Include sales and onboarding delay where relevant.
5. **Estimate LTV cautiously.** Prefer observed cohort gross profit. If using a formula, show why the retention process is stable enough.
6. **Model expansion and contraction.** Keep them separate from logo retention so a few expanding accounts do not hide widespread churn.
7. **Run sensitivities.** Vary CAC, gross margin, retention, expansion, and price. Show which assumption changes the verdict.
8. **Check cash exposure.** Note payment timing, contract length, acquisition ramp, and how much capital is tied up before payback.
9. **Issue a scale verdict.** Scale, hold, narrow to a segment, repair retention, change pricing, or stop. Tie the verdict to a decision threshold supplied by the business.

## Output contract

1. **Verdict:** scale, hold, narrow, repair, or stop.
2. **Definition table:** formula inputs, source, period, and confidence.
3. **Segment table:** CAC, payback, observed or modeled LTV, LTV:CAC, sample size.
4. **Cohort view:** cumulative gross profit against acquisition cost.
5. **Sensitivity table:** assumptions that can reverse the verdict.
6. **Cash-risk note:** timing and capital exposure.
7. **Data gaps and next measurement.**

## Guardrails

- Do not use revenue LTV when costs are material; use gross profit.
- Do not divide by churn when churn is near zero in a small or young cohort.
- Do not mix annual and monthly rates without conversion.
- Do not treat attributed customers as incremental customers automatically.
- Do not benchmark without matching business model, segment, date, and margin structure.
- Do not scale a blended winner that contains a loss-making marginal segment.
- Route channel structure to `channel-fit-diagnostic` and retention architecture to `retention-state`.
