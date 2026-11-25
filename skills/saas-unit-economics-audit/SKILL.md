---
name: saas-unit-economics-audit
description: "Audit SaaS unit economics by segment using gross-margin LTV, CAC, payback, retention, and sensitivity analysis."
---

# SaaS Unit Economics Audit

Answer per segment: can customer profit repay acquisition cost, how fast, and should the business accelerate, fix, or stop investment?

Do NOT use for channel selection (`channel-fit-diagnostic`), engagement-depth analysis (`power-user-curve`), or retention product design (`retention-state`). This skill grades economics and prepares recommendations; it does not execute changes.

## Inputs and missing-data fallback

Use a consistent currency, time unit, customer definition, and cohort window. Ask once for missing data, then produce the useful partial audit from supplied exports without claiming tool access or invented measurements.

| Input | Minimum needed | If missing |
|---|---|---|
| Revenue | Monthly revenue, new recurring revenue, expansion, contraction and churn, ideally two quarters or more | Use available history; label immature cohorts |
| Acquisition spend | Ads, salaries, tools, agency and allocated sales costs by acquisition cohort/channel | Flag marketing-only CAC as understated; show allocation method |
| Margin | Gross margin and its cost definition | A 75% classic-SaaS or 40% AI margin may be a clearly marked scenario, never a measured margin |
| Churn | Monthly logo churn and net revenue churn separately | Derive only from reconciled opening counts/revenue, losses and expansion; otherwise unavailable |
| Customers | Opening/ending paying logos, new customers per month, cohort counts | Mark sample size and ceiling utilization unavailable where needed |
| Variable costs | Service costs, payment fees, support, shipping, incentives, refunds and discounts where relevant | For transactional models, show [Degraded: GM proxy] if contribution margin is unavailable |
| Segments | Channel, customer type/size, pricing plan; app versus web billing where relevant | Use [Degraded: blended-only]; segmentation is the first action |
| Motion and cash | Contract size, sales cycle, billing timing, implementation cost, capital tolerance | Give a provisional verdict and identify the missing decision constraint |
| Attribution | Attributed versus incremental customers, brand versus nonbrand spend | Label [Attributed CAC]; it cannot alone support Accelerate |

Missing inputs remain unavailable. A sensitivity assumption is a scenario, not a recovered input; do not invent a numeric LTV from hypothetical churn and present it as an observed result.

## Procedure

### 1. Reconcile definitions and segment first

Split economics by channel, customer type and plan where data allows. Explain small samples and allocations. Do not let a profitable blend hide a weak segment.

- Separate app-billed and web-billed subscriptions. Deduct app-store fees once: either from revenue before margin, or within cost of revenue, according to the reported margin definition.
- Exclude brand-search spend AND its attributed customers from nonbrand paid CAC, including plan-level allocations. Show brand separately as context.
- Prefer experimentally supported incremental CAC when available. Preserve the distinction from platform-attributed CAC.
- Include AI inference and service costs in margin. Free-tier or promotional inference costs booked as acquisition spend belong in CAC instead; count each cost once.
- Reconcile paying customers versus users, activity definitions, cohort membership, refresh timing and retention windows before comparing analytics and billing exports.

### 2. Compute economics per segment and cohort

State formulas, units, period and input references next to results.

| Metric | Calculation and limits |
|---|---|
| CAC | Fully loaded acquisition costs / new paying customers; align spend with the cohort and sales-cycle delay |
| Gross margin | (Revenue minus cost of revenue) / revenue |
| Monthly gross profit per customer | Monthly ARPA × gross margin |
| Simple LTV | Monthly ARPA × gross margin / monthly logo churn, only for stable positive churn with adequate cohort history |
| LTV:CAC | Gross-profit LTV / CAC |
| Simple CAC payback | CAC / monthly gross profit per customer; report months |
| Cohort payback | First elapsed month cumulative cohort gross profit covers cohort acquisition cost; include sales/onboarding delays |
| Contribution-margin payback | CAC / steady-state monthly contribution margin per customer |
| Logo ceiling | New logos per month / monthly logo churn; current logos / ceiling gives utilization |
| Revenue ceiling | New MRR per month / positive monthly net revenue churn, under constant-addition assumptions |

Contribution margin subtracts every variable cost to serve, including discounts, incentives, payment fees, support and shipping. Keep acquisition spend out of the denominator. For a one-time first-period shortfall, use `(CAC + shortfall) / steady-state monthly contribution margin`, where shortfall is steady-state contribution margin minus first-period contribution margin. Do not also include that same shortfall in CAC.

Use contribution-margin payback for transactional, marketplace and direct-to-consumer subscriptions. Marketplace CAC must include acquisition costs on both sides; if those costs are missing, do not invent them.

Use quarterly cohort views alongside monthly ones. If using prior-quarter spend as a lag proxy, state why that lag fits the sales cycle. Divide by attributable monthly new recurring gross profit to obtain months; do not silently mix quarters and months. State the definition and annualization if reporting an annual CAC recovery ratio.

Simple LTV is unsafe with near-zero or negative churn, material expansion, changing retention, immature cohorts or high concentration. Prefer observed cumulative cohort gross profit and an explicitly modeled forecast tail; lead with payback when mature LTV is unavailable. Nonpositive recurring margin means no finite payback under current assumptions. Zero churn does not prove infinite LTV or a meaningful finite ceiling.

### 3. Choose decision thresholds

Use the business's explicit thresholds and cash constraints first. Otherwise consult [dated benchmark context](references/benchmarks.md), match the motion and margin basis, and label any provisional threshold [Benchmark: source/year]. Never present an average as proof of viability.

Check source freshness before grading. If the reference date is older than twelve months, verify current comparable benchmarks before using them as decision thresholds. If verification is unavailable, retain the dated context, mark grading provisional, and ask the business to approve thresholds. Do not silently update bundled reference files.

### 4. Check retention from the business model upward

Give a finding for each of these six rows, with evidence or an explicit data gap:

1. **Acquisition capacity:** can the motion supply enough retained new customers for target growth?
2. **Expansion:** is there an expansion axis, or does the business need stronger upfront value capture? Separate expansion from logo survival.
3. **Influenceable levers:** which changes can the business control, versus customer closures or external demand?
4. **Stage and strategy:** do maturity, renewal evidence, cash reserves and an evidenced expansion plan support the proposed growth pace?
5. **Logo ceiling:** calculate per segment using its own adds and churn; show the current base as a percentage where known. State constant-addition and stable-churn assumptions.
6. **N beside NRR:** show opening/ending logo counts beside every net revenue retention figure. NRR uses the opening cohort, including churned customers at zero ending revenue; new customers are excluded.

Net revenue churn above 2% monthly is a dated structural-risk warning from the reference, requiring retention repair before additional growth investment. For products serving small businesses on a platform, closures can cause high logo churn while surviving accounts expand. Judge NRR and customer-count trends together; do not stop investment solely on logo churn.

### 5. Issue a verdict per segment

- **Accelerate:** passes the selected LTV:CAC and applicable payback thresholds, retention and cash checks, with credible acquisition measurement. Explain the cash trough before repayment.
- **Fix:** one or more constraints remain, but a named influenceable lever could plausibly close the gap. Missing material evidence means a provisional Fix/hold, never an unsupported Accelerate or Kill.
- **Kill:** multiple economics constraints fail with no plausible remedy, or churn makes the model unsustainable without a credible expansion plan. This is a recommendation to stop investment, not authorization to cancel customers or campaigns.

Before Kill on payback alone, test whether mature renewal evidence, multiyear contracts, proven expansion, available capital or an explicitly approved strategic objective justifies longer repayment. State the evidence and condition for Fix instead. Show ramping sales reps separately; any fully ramped comparison must exclude both their costs and bookings consistently, while retaining the fully loaded company view.

When extending payback tolerance or acquisition spend, calculate marginal payback for the extra customers, not just the blend. If the spend-to-customer effect is unmeasured, label the proposed effect as a scenario. Never optimize CAC alone; pair it with retained margin and payback.

### 6. Rank levers and show sensitivities

Rank the top three levers by modeled impact on payback or LTV:CAC. Candidates include activation/retention repair, expansion, price or annual-plan design, conversion, and reallocation toward segments with supported economics. State an owner and first action.

Vary CAC, margin, churn, expansion and price only as explicitly labeled scenarios. Show which assumption changes the verdict, including conversion loss or cash exposure where relevant. Do not invent an impact when the necessary inputs are absent: mark it unavailable and name the missing evidence.

## Output contract

Return one deliverable, framed around the recipient's decision:

1. **First-line verdict:** name every segment and its Accelerate / Fix / Kill recommendation; mark provisional decisions and any blended-only limitation on this line.
2. **Input evidence ledger:** immediately after the verdict, list `segment | input | value | unit and period | source/status`. Cover every raw quantity used anywhere, including formula-only operands, costs, churn, fees, customer counts, opening/ending cohort revenue and sensitivity baselines. Use [Supplied: source/window] for supplied inputs, [Assumption: basis] for assumptions, and unavailable for missing quantities. Do not label missing or inferred inputs supplied.
3. **Segment metrics table:** retain columns `segment | ARPA | GM% | CAC | LTV | LTV:CAC | payback months | CM payback months | threshold/motion | net revenue churn | logo ceiling (% reached) | verdict`. Use n/a for inapplicable CM payback; unavailable with reason for missing metrics. When a segment base is unknown, still give its calculable ceiling and state utilization unavailable; add a blended context row if its utilization is known.
4. **Cohort view:** cumulative gross profit versus acquisition cost and observed repayment timing, or the exact data gap.
5. **Retention block:** all six rows above, including N beside NRR.
6. **Top-three levers table:** `lever | segment | modeled effect | owner | first action`; explicitly mark unquantifiable effects.
7. **Sensitivity table and cash-risk note:** scenario assumptions, verdict reversals, collection timing and capital exposure.
8. **Assumptions and data gaps:** up to five prioritized bullets, followed by the approval statement and concrete handoffs.

Map every derived result to [Calculated: ledger inputs/formula], every threshold to [Benchmark: source/year] or the supplied business policy, and every proposed target or modeled effect to [Scenario: changed assumptions]. Retain assumed-input flags in results. Before delivery, check every numeric operand, metric cell, retention finding and lever claim against its ledger entry or explicit calculation, benchmark or scenario mapping. A generic evidence key does not establish raw-input provenance.

## Approval and handoffs

Explicitly state in every deliverable: human approval is required before any live budget or price change, billing change, campaign/customer cancellation, or external send. Drafts and modeled recommendations may proceed immediately; a verdict never authorizes execution. Confirm segment definitions and cost loading before finalizing the verdict.

End every deliverable with the receiving skill and the specific data or question it receives. Include applicable routes, and do not claim another skill ran without its output:

| Deferred work | Route and packet |
|---|---|
| Attribution reconciliation | `paid-analysis-review`: nonbrand spend, attributed customers, billing outcomes and CAC definition discrepancies |
| Incrementality study | `experiment-design`: segment, baseline outcomes, spend, incremental-CAC question and decision threshold |
| Channel selection | `channel-fit-diagnostic`: segment economics, cash limits and channel-choice question |
| Price, package or annual-plan design | `offer-design`: segment margin, conversion/retention constraints and candidate terms |
| Retention product design | `retention-state`: cancellation causes, accumulated product value and portability constraints |
| Engagement depth | `power-user-curve`: paying cohorts, usage definitions and churn question |
| Quarterly implementation priorities | `growth-roadmap`: ranked levers, owners, evidence gaps and decision conditions |

Forecast construction, marketplace cost accounting and fresh benchmark research require the appropriate finance or research specialist; provide cohort revenue, cost, churn gaps and the exact question without inventing an installed sibling skill.

## Adaptation note

This public edition preserves the input ledger, explicit live-action approval and concrete handoff requirements retained in the source skill's bounded evaluation. Historical source scores were 45%/50% baseline and 100%/95% final, with generator and scorer the same model; self-evaluation is directional evidence. Public wording and public-skill route substitutions are editorial adaptations, not a newly scored evaluation.
