---
name: power-user-curve
description: "Build L7 or L30 core-action histograms to measure engagement depth, identify power users, and compare cohort movement."
---

# Power User Curve

Use this skill when average engagement ratios hide whether a product has a deeply engaged segment or whether engagement is improving across cohorts.

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

1. **Define the core action.** Choose the event that represents value delivered, not login, app open, or page view unless viewing is the product's value.
2. **Fix the denominator.** For each cohort and window, define eligible users and whether the curve includes all activated users or only active users. Keep it consistent.
3. **Count distinct active days.** For every eligible user, count days with at least one core action in the chosen window.
4. **Build the histogram.** X-axis is active days; Y-axis is percent of the cohort. Include cohort size and missing-data rate.
5. **Classify the shape.** Look for:
   - strong left concentration: mostly one-time or occasional value;
   - right-side concentration: broadly frequent value;
   - two-ended or “smile” shape: casual users plus a power-user segment;
   - workweek pattern: high weekday frequency with expected weekend drop.
6. **Compare cohorts.** Overlay at least three comparable cohorts. Movement toward higher-frequency buckets may indicate improving engagement; check releases, audience mix, and data changes before assigning cause.
7. **Profile the tails.** Compare high-frequency and one-day users by source, segment, first-session behavior, plan, and retained outcome.
8. **Connect to the model.** Decide whether frequency matters for value and revenue. A left-heavy curve is not automatically bad for high-value episodic products.

## Output contract

1. **Core-action definition and window rationale.**
2. **Histogram table or chart specification with cohort sizes.**
3. **Shape classification and uncertainty.**
4. **Cohort movement:** improving, flat, degrading, or incomparable.
5. **Power-user profile and casual-user contrast.**
6. **Business implication:** activation, retention, monetization, or audience quality.
7. **Next queries:** three to five analyses that can change the decision.

## Guardrails

- Do not use opens or logins when a value event exists.
- Do not compare curves with different denominators or windows.
- Exclude bots, staff, QA, and migrated activity.
- Band sparse tails instead of over-reading noise.
- Do not compare unrelated product categories as if frequency were universal quality.
- Do not infer a product change caused movement without controlling for cohort mix and instrumentation changes.
