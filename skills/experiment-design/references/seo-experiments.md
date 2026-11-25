# SEO experiments: page and cluster designs

Use for template or page changes affecting organic discovery. Randomization is usually by page or related-page cluster, not visitor: crawlers and users should receive a coherent page. Visitor split tests answer on-site conversion questions and do not by themselves estimate SEO lift.

## Design and preconditions

1. Specify the change, eligible pages, outcome (for example organic clicks), business guardrails and mechanism. Record indexing, canonicalization and rendering constraints before launch.
2. Match or stratify pages using pretreatment topic/template and traffic where useful, then randomize pages or clusters into treatment/control if feasible. Freeze eligibility before assignment. Related pages competing for the same queries may need cluster assignment; account for spillovers and site-wide changes.
3. Estimate precision from page-level variance, cluster count, autocorrelation and seasonality. Daily events and repeated impressions are not independent randomized units. Do not use the binary-user sample-size table as an SEO power calculator.
4. Predefine crawl/index lag, representative observation window, comparison family and stopping criteria. Check treatment rendering, crawlability, canonical tags and stable logging for both arms; do not split solely on post-change traffic.

## Readout

Analyze at the assignment unit with appropriate clustering and pre-period adjustment. Compare concurrent treatment/control outcomes, report uncertainty and inspect query/page composition. Record algorithm updates, crawl/index delays, holidays and concurrent content changes. Zero traffic from a not-yet-indexed page is a validity diagnostic, not an immediate treatment verdict.

## When randomization is unavailable

Use matched-page controls, difference-in-differences or interrupted time series as observational designs. Explain parallel-trends, stable measurement and no-concurrent-confounding assumptions, inspect pretreatment fit and run sensitivity checks. A before/after chart alone is not causal evidence; search updates and demand changes can move both outcomes and denominators. Few pages or interacting clusters can make a result inconclusive even with large impression counts.

## Decision and handoff

Report assignment, exposure/index status, actual outcome window, effect and interval, guardrails and remaining uncertainty. Ship, iterate, park or monitor according to the precommitted decision rule; non-significance is not equivalence. Keep page/template implementation with the site owner and experiment validity here. Use `test-templates.md` for the decision record, adapting unit and analysis fields explicitly.
