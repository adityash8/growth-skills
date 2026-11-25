# Low-sample and B2B testing

A small sample is a precision constraint, not permission to weaken inference. Use the client's baseline, meaningful effect and decision window; no universal visitor cutoff applies.

## 1. Define the unit before choosing a method

Randomization might be by user, account, geographic cluster or market/time block. Analysis must respect that unit and repeated observations: many sessions from a few accounts are not many independent accounts. Check spillovers, sales involvement, eligibility and delayed outcomes. Size using independent units and any cluster design effect, not raw event count.

## 2. Make the treatment decision-relevant

A coherent bundle can create a larger effect worth detecting. It estimates the bundle's effect, not the contribution of each tactic. A non-significant or underpowered bundle cannot kill an idea forever. Prespecify minimum worthwhile benefit and harm bounds; equivalence requires an appropriate design and interval within the chosen equivalence bounds, not p > 0.05.

## 3. Choose an alternative with honest limits

- Account-randomized A/B: randomize accounts, stratify on pretreatment size where justified, and use cluster-aware inference. Few accounts may leave wide intervals despite many users.
- Geo/market randomized split: randomize comparable clusters, measure contamination and account for cluster correlation. A handful of markets limits inference and generalizability.
- Switchback: randomize market/time blocks where interference prevents user assignment. Predefine washouts, carryover assumptions, seasonality controls and block-aware inference; correlated time points are not independent samples.
- Matched markets or difference-in-differences: when randomization is unavailable, label the design observational. Document parallel-trends assumptions, pretreatment fit, concurrent campaigns and sensitivity to controls. Matching cannot remove all unmeasured confounding.
- Interrupted time series or before/after: use multiple pretreatment periods and record external changes. Trend, seasonality and composition can explain a change; before/after alone is not causal proof.

## 4. Validate cheaper where appropriate

Interviews, usability checks, concierge delivery, prototypes and ethically disclosed smoke tests can test comprehension or demand. State which decision each supports; intent and click metrics may not establish revenue or retention lift. A reversible rollout needs guardrails and rollback rules even without a formal efficacy test.

## 5. Read the uncertainty

Report actual eligible/assigned/exposed counts, outcome maturity, effect interval and practical costs. Avoid observed-effect post-hoc power; discuss which decision-relevant effects the design could detect. An inconclusive result may justify more data, a better treatment or a reversible decision under uncertainty, not a permanent verdict on the idea.

## 6. Reduce variance without changing the question

Consider stratification or CUPED using pretreatment covariates, with a prespecified adjustment and validated implementation. Robust/capped metrics change the estimand; define them before observing treatment differences. Neither variance reduction nor Bayesian modeling creates missing independent information. Test assumptions and report sensitivity. Use `sample-size-guide.md` for the simple independent-binomial case; do not apply its equal-arm formula blindly to clusters or switchbacks.
