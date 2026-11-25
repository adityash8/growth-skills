---
name: power-user-curve
description: "Build L7 or L30 core-action histograms to measure engagement depth, identify power users, and compare cohort movement."
---

# Power User Curve

Use this skill when average engagement ratios hide whether a product has a deeply engaged segment or whether engagement is improving across cohorts.

Do NOT use for activation-flow design (`onboarding-activation`), accumulated-value design (`retention-state`), or unit-economics grading (`saas-unit-economics-audit`).

## Inputs

- one core action tied to user value or monetization;
- natural product cadence: daily, weekly, monthly, or episodic;
- user-level event data with timestamps;
- acquisition or activation cohort definition;
- internal, test, automated, and duplicate-user exclusions;
- monetization model and relevant segments.

## Window choice

- **L7:** count distinct active days from 1–7 for weekly-cycle or work products.
- **L30:** count distinct active days from 1–30 for products where monthly depth is meaningful.
- Use a longer or event-based window for naturally episodic products. Do not force daily frequency onto a product that delivers value less often.

## Procedure

1. **Define the core action.** Choose the event that represents value delivered, not login, app open, or page view unless viewing is the product's value. Confirm the definition in one line before querying. For social or multiplayer products, prefer completed reciprocal interactions over one-sided activity.
2. **Fix the denominator.** Use core-action actives in each cohort/window for the main curve: WAU for L7 or monthly actives for L30. Each series sums to 100%. If reporting all eligible or activated users instead, include a zero-day bucket and label that separate denominator. Keep denominators, timezone, observation length and cohort age comparable.
3. **Count distinct active days.** For every eligible user, count days with at least one core action in the chosen window.
4. **Build the histogram.** X-axis is active days; Y-axis is percent of the cohort. Include cohort size and missing-data rate.
5. **Classify the shape.** Look for:
   - strong left concentration: mostly one-time or occasional value;
   - right-side concentration: broadly frequent value;
   - two-ended or “smile” shape: casual users plus a power-user segment;
   - workweek pattern: high weekday frequency with expected weekend drop.
6. **Compare cohorts.** Overlay at least three comparable cohorts. Movement toward higher-frequency buckets may indicate improving engagement; check releases, audience mix, and data changes before assigning cause.
7. **Profile the tails.** Compare high-frequency and one-day users by source, segment, first-session behavior, plan, and retained outcome.
8. **Connect to the model.** Decide whether frequency matters for value and revenue. A left-heavy curve is not automatically bad for high-value episodic products. Answer: can infrequent use monetize, who are the high-frequency users and how are they acquired, and is the left mass missing first value or drawn from the wrong audience?
9. **Set an engagement target.** State a proposed target as a change in median active days for a named core cohort by a date. Look for friction and substitute behaviors before recommending new features. Choose the target from product evidence, not universal benchmarks.
10. **Check AI serving costs.** For AI products on flat plans, add cost-to-serve and revenue per active-days band. Estimate cost from inference cost per active day times active days when defensible; flag bands where per-user cost exceeds matched-period plan revenue. Mark missing cost or revenue data unknown and request it before proposing tier economics.

## Output contract

1. **One-line read, core-action definition and window rationale.** Include the headline share and count of weekly actives completing the core action on at least 5 of 7 days (L5/L7); for L30 use at least 20 of 30 days (L20+/L30). Report week-over-week growth of the weekly count when comparable prior data exists. State unavailable metrics and the missing data rather than inventing them.
2. **Histogram table or chart specification with cohort sizes.** Rows are distinct active-day buckets, columns are cohorts, cells are percentages. Include missing-data rate. Use bars for one snapshot or overlaid lines for cohort comparison. Band sparse L30 cohorts as 1 / 2–3 / 4–7 / 8–14 / 15–30. Use L7-specific bands for weekly curves. AI flat-plan products also need cost and revenue per band.
3. **Shape classification and uncertainty.** Put the shape label on its own line: smile, left-leaning, right-leaning, or workweek smile. Explain frequency-dependent monetization exposure and the activation interpretation.
4. **Cohort movement:** improving, flat, degrading, or incomparable. Include the core cohort's median active-day change against its target and dated release or acquisition hypotheses. A suspected cause remains a hypothesis.
5. **Power-user profile and casual-user contrast.**
6. **Business implication:** activation, retention, monetization, or audience quality.
7. **Next queries:** three to five analyses that can change the decision. Always include core-action failure rate: unsuccessful attempts divided by all attempts, using an explicit success event and completion window. Missing attempt/success data means the rate is unavailable; provide the query or instrumentation specification. Treat shared power-user behaviors as hypotheses, not promised retention lifts.

## Guardrails

- **Approval before live changes.** Produce analysis, drafts and implementation specifications now; explicitly require the user's approval before any live product or instrumentation edit, publication, fee/tier change, automated rollout, or other irreversible action. Never claim execution without evidence.
- If only opens/logins exist, label the output `[Degraded: visit-based]` and make core-action instrumentation the first recommendation. Draft the specification; live instrumentation changes require approval.
- Label supplied observations, calculations and assumptions; leave unsupported metrics unknown. With fewer than three comparable cohorts, provide the available snapshot and mark the shift-right conclusion insufficient or incomparable.

- Do not use opens or logins when a value event exists.
- Do not compare curves with different denominators or windows.
- Exclude bots, staff, QA, and migrated activity.
- Band sparse tails instead of over-reading noise.
- Do not compare unrelated product categories as if frequency were universal quality.
- Do not infer a product change caused movement without controlling for cohort mix and instrumentation changes.

## Handoffs

- Activation gap or onboarding friction → `onboarding-activation`.
- Accumulated-value or structural retention design → `retention-state`.
- Wrong acquisition audience → `channel-fit-diagnostic`.
- User motivations or substitute behaviors → `customer-research`.
- Cost, payback or LTV analysis → `saas-unit-economics-audit`.
- Test a proposed change or causal hypothesis → `experiment-design`.
- AI tier design → prepare a pricing brief for the product/pricing owner; no tier changes without approval.

## Interpretation notes

- A smile has casual users at the left and a high-frequency hump at the right; a workweek smile can peak around five days and dip at six or seven.
- A histogram smile is different from a retention curve that dips and rises. Name the chart explicitly.
- Compare acquisition channel, market, plan and team/function to explain tails. For network effects, compare density within markets instead of blending them.
- Small cohorts can produce noisy tails; band them and disclose uncertainty. Counts show segment growth, while percentages show distribution movement.
- Do not force power-user behaviors onto casual users merely because they correlate with retention.
