# Sample Size Guide

Reference for calculating sample sizes and test duration.

## Contents
- Readiness Thresholds (read first)
- Sample Size Fundamentals (required inputs, what these mean)
- Sample Size Quick Reference Tables
- Duration Calculator (formula, examples, minimum duration rules, maximum duration guidelines)
- Online Calculators
- Adjusting for Multiple Variants
- Common Sample Size Mistakes
- When Sample Size Requirements Are Too High
- Sequential Testing
- Quick Decision Framework

## Readiness Thresholds (read first)

Use the actual decision window, outcome delay and representative business cycles. Historical one-month and traffic-count heuristics are context, not universal cutoffs. If a useful MDE cannot be detected in time, consider a cheaper design, risk-limited rollout or `low-sample-testing.md`. An observational before/after read cannot establish a causal effect.

---

## Sample Size Fundamentals

### Required Inputs

1. **Baseline conversion rate**: Your current rate
2. **Minimum detectable effect (MDE)**: Smallest change worth detecting
3. **Significance level alpha**: Planned Type I error rate, commonly 0.05 for a two-sided test
4. **Statistical power**: Usually 80% (β = 0.20)

### What These Mean

**Baseline conversion rate**: If your page converts at 5%, that's your baseline.

**MDE (Minimum Detectable Effect)**: The smallest improvement you care about detecting. Set this based on:
- Business impact (is a 5% lift meaningful?)
- Implementation cost (worth the effort?)
- Realistic expectations (what have past tests shown?)

**P-value**: Under the null hypothesis and model/sampling assumptions, the probability of a statistic at least as extreme as observed. It is not the probability of randomness, a true null, or a winning variant. A 95% confidence interval has long-run coverage; it is not a posterior win probability.

**Power (1-beta)**: Probability of rejecting the null at a specified true MDE under the design. Planned sample is not proof of achieved power. Actual sample, valid assignment, attrition and outcome maturity determine precision; observed-effect post-hoc power adds no evidence beyond the test result.

**MDE units**: Relative MDE 20% at baseline 5% means 6%, an absolute 1 percentage-point increase (delta=0.01). Label both units.

---

## Sample Size Quick Reference Tables

### Formula and assumptions

Independent Bernoulli outcomes; two arms with equal allocation and sample per arm n; two-sided alpha=0.05; planned power=0.80; no clustering, repeated looks or multiple comparisons. Let p0 be baseline, p1=p0*(1+relative_MDE), delta=p1-p0 and pbar=(p0+p1)/2. With z(q) the standard-normal quantile:

n = ceil((z(1-alpha/2)*sqrt(2*pbar*(1-pbar)) + z(power)*sqrt(p0*(1-p0)+p1*(1-p1)))^2 / delta^2).

This normal approximation needs adequate expected successes/failures. Rare outcomes, unequal splits, clustering and sequential methods need a design-specific calculation. Tables below use this formula, not an external calculator.

### Conversion Rate: 1%

| Relative lift | Sample per variant | Total |
|---|---:|---:|
| 5% (1.00% to 1.05%) | 637010 | 1274020 |
| 10% (1.00% to 1.10%) | 163095 | 326190 |
| 20% (1.00% to 1.20%) | 42693 | 85386 |
| 50% (1.00% to 1.50%) | 7750 | 15500 |
| 100% (1.00% to 2.00%) | 2319 | 4638 |

### Conversion Rate: 3%

| Relative lift | Sample per variant | Total |
|---|---:|---:|
| 5% (3.00% to 3.15%) | 207938 | 415876 |
| 10% (3.00% to 3.30%) | 53211 | 106422 |
| 20% (3.00% to 3.60%) | 13914 | 27828 |
| 50% (3.00% to 4.50%) | 2518 | 5036 |
| 100% (3.00% to 6.00%) | 749 | 1498 |

### Conversion Rate: 5%

| Relative lift | Sample per variant | Total |
|---|---:|---:|
| 5% (5.00% to 5.25%) | 122124 | 244248 |
| 10% (5.00% to 5.50%) | 31234 | 62468 |
| 20% (5.00% to 6.00%) | 8158 | 16316 |
| 50% (5.00% to 7.50%) | 1471 | 2942 |
| 100% (5.00% to 10.00%) | 435 | 870 |

### Conversion Rate: 10%

| Relative lift | Sample per variant | Total |
|---|---:|---:|
| 5% (10.00% to 10.50%) | 57763 | 115526 |
| 10% (10.00% to 11.00%) | 14751 | 29502 |
| 20% (10.00% to 12.00%) | 3841 | 7682 |
| 50% (10.00% to 15.00%) | 686 | 1372 |
| 100% (10.00% to 20.00%) | 199 | 398 |

### Conversion Rate: 20%

| Relative lift | Sample per variant | Total |
|---|---:|---:|
| 5% (20.00% to 21.00%) | 25583 | 51166 |
| 10% (20.00% to 22.00%) | 6510 | 13020 |
| 20% (20.00% to 24.00%) | 1683 | 3366 |
| 50% (20.00% to 30.00%) | 294 | 588 |
| 100% (20.00% to 40.00%) | 82 | 164 |

### Numeric controls (synthetic)

- 5% to 6%: 20% relative MDE, 1 percentage point, **8158** per arm.
- 10% to 10.5%: 5% relative MDE, 0.5 percentage points, **57763** per arm.
- 2.1% to 2.4%: 14.2857% relative MDE, 0.3 percentage points, **38361** per arm for the same planned power. With only 12000 per arm and 252 vs 288 conversions, the pooled two-proportion z test gives p about 0.117; the unpooled 95% difference interval spans zero. This is inconclusive, not evidence of equivalence. Under a prespecified true delta of 0.003, that smaller design has about 35% power; do not treat observed-effect post-hoc power as an additional result.
- SRM allocation controls for planned 50/50: **5001** vs 4999 assignments is healthy under a two-bin Pearson chi-square check (p > 0.9); **5500** vs 4500 is a mismatch (p < 0.001). For two bins, chi-square=sum((observed-expected)^2/expected), df=1, survival=2*(1-Phi(sqrt(chi-square))). These are assignment/exposure diagnostics, not outcome tests.
- Multiplicity trap: three planned comparisons yield p-values **0.02, 0.03, 0.04**. All pass an unadjusted 0.05 threshold; none passes Bonferroni 0.05/3 or Holm (the smallest already fails 0.05/3). Report the prespecified family, including metric and segment claims.

---

## Duration Calculator

### Formula

```
Duration (days, equal allocation) = (Sample per variant × Number of variants) / (Daily eligible unique units × exposed fraction)
```

### Examples

**Scenario 1: High-traffic page**
- Need: 10,000 per variant (2 variants = 20,000 total)
- Daily traffic: 5,000 visitors
- 100% exposed to test
- Duration: 20,000 / 5,000 = **4 days**

**Scenario 2: Medium-traffic page**
- Need: 30,000 per variant (60,000 total)
- Daily traffic: 2,000 visitors
- 100% exposed
- Duration: 60,000 / 2,000 = **30 days**

**Scenario 3: Low-traffic with partial exposure**
- Need: 15,000 per variant (30,000 total)
- Daily traffic: 500 visitors
- 50% exposed to test
- Effective daily: 250
- Duration: 30,000 / 250 = **120 days** (compare with the decision window and outcome delay)

### Observation windows

Choose representative business cycles and allow outcomes to mature, including weekday/weekend mix, paydays where relevant, and B2B purchasing delays. A week or two can be a planning heuristic, not a guarantee. Predefine maximum duration and what to do if the sample is short; long tests can face novelty effects, seasonality and competing changes. Do not declare a winner early because the sample arrives before the committed window.

---

## Online Calculators

### Recommended Tools

**Optimizely's Calculator**
https://www.optimizely.com/sample-size-calculator/
- Business-friendly language
- Duration estimates

**AB Test Guide Calculator**
https://www.abtestguide.com/calc/
- Includes Bayesian option
- Multiple test types

**VWO Duration Calculator**
https://vwo.com/tools/ab-test-duration-calculator/
- Duration-focused
- Good for planning

---

## Adjusting for Multiple Variants

More arms divide traffic; multiplicity also raises evidence requirements. Holding sample per arm constant, 3 total arms need 1.5x the total traffic of 2 arms before any correction; 4 arms need 2x. These are allocation arithmetic, not corrected power multipliers.

Predefine whether comparisons are treatment-vs-control or all pairs. Bonferroni tests each of m comparisons at alpha/m. Holm sorts p-values and compares each to alpha/(m-i+1), stopping at the first failure. Recompute sample with the selected method; do not use a traffic multiplier as the correction. A 2x2x2 factorial design has 8 combinations; power main effects and interactions under that design rather than treating it as 8 independent pairwise tests.

---

## Common Sample Size Mistakes

### 1. Underpowered tests
**Problem**: Not enough sample to detect realistic effects
**Fix**: Be realistic about MDE, get more traffic, or don't test

### 2. Overpowered tests
**Problem**: Spending more than needed to detect commercially irrelevant effects
**Fix**: Select a decision-relevant MDE before launch. Once running, honor the fixed design rather than stopping at first significance

### 3. Wrong baseline rate
**Problem**: Using wrong conversion rate for calculation
**Fix**: Use the specific metric and page, not site-wide averages

### 4. Ignoring segments
**Problem**: Calculating for full traffic, then analyzing segments
**Fix**: If you plan segment analysis, calculate sample for smallest segment

### 5. Testing too many things
**Problem**: Dividing traffic too many ways
**Fix**: Prioritize ruthlessly, run fewer concurrent tests

---

## When Sample Size Requirements Are Too High

Options when you cannot get enough traffic:

1. Increase the target effect only if that larger effect is decision-relevant; smaller effects remain unresolved.
2. Choose alpha and power from decision costs before launch; never lower thresholds after reading results. Qualitative support does not repair an invalid statistical claim.
3. Reduce variants or use compatible populations/pages with explicit eligibility and clustering assumptions.
4. Test an earlier validated outcome only if it answers the decision; it may not prove downstream value.
5. Use qualitative or observational validation and label its limits; a randomized holdout can preserve causal comparison if adequately powered.
6. Extend duration if stable exposure and outcome windows allow.
7. Consider pre-period variance reduction (CUPED) or predeclared robust metrics; do not cap outcomes after inspecting arm differences.
8. Test a coherent larger bundle but interpret the bundle, not each tactic. A non-significant result is not conclusive absence.
9. Consider geo clusters, switchbacks, matched markets or difference-in-differences with appropriate inference and explicit assumptions; see `low-sample-testing.md`.

---

## Sequential Testing

For early efficacy decisions, choose a valid group-sequential design, alpha-spending rule or always-valid procedure before launch. Specify looks, boundaries, maximum sample and outcome maturity. Repeated fixed-horizon p-values do not become sequential tests by monitoring them. Bayesian procedures require their own specified model and decision rule; the label alone is insufficient. Verify the installed platform's actual supported method, runtime/version and settings before relying on it. Stop exposure for safety or broken instrumentation under the safety plan without claiming efficacy.

---

## Quick Decision Framework

Record daily eligible unique units, baseline, relative and absolute MDE, alpha, power, split, outcome delay, comparison family, required sample and the representative observation window. For equal allocation, use the duration formula above; for unequal allocation calculate per-arm arrivals separately. Compare the resulting window with the real decision deadline. If infeasible, use Step 0 of [the main skill](../SKILL.md) and state which uncertainty remains.
