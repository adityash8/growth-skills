# LinkedIn objective tests and equal-spend audits

Use when comparing campaign objectives or delivery targets. Separate observed arm performance from any claim that the objective caused it.

## Read-only collection

1. Freeze completed account dates, timezone, currency, and outcome-maturity rules.
2. Read both campaign objects: status, serving state, budgets, bids, objectives, placements, expansion, targeting, schedules, parent groups, and history.
3. Fetch complete creative inventory and exact campaign membership. If a filtered endpoint fails, use a supported broader inventory and filter locally; verify pagination.
4. Pull campaign, creative, and conversion-rule reporting at the same dates. Resolve rule definitions and current status.
5. Map delivered creative identifiers to underlying post references. Verify reporting fields, units, and namespaces against current documentation.
6. Cross-check canonical downstream outcomes separately from platform-attributed actions.

## Setup gate

An objective-only claim requires material parity apart from the intended objective difference, along with a valid assignment design.

- Compare targeting semantically. Sort arrays only where order is irrelevant; preserve sequence where it has meaning.
- Name differing targeting paths and values rather than relying on a whole-object inequality.
- Compare delivered post references and spend shares. Matching inventory does not prove matching exposure under optimized delivery.
- A useful allocation diagnostic is total variation across the union of post references:

```text
TV = 0.5 * sum(abs(share_a(post) - share_b(post)))
```

Zero means identical shares. One means disjoint allocation. Set a decision-relevant tolerance before inspecting outcomes; no universal threshold establishes causality.

Campaign age, learning history, eligibility, and audience overlap can confound results even when current settings match. More runtime cannot fix those differences.

## Metric layers

- **CTR:** clicks divided by impressions. It is sensitive to delivery objectives and does not alone establish purchase quality.
- **Landing-page CVR:** use only a populated, verified landing-click denominator with consistent semantics in both arms.
- **Mixed actions:** resolve conversion rules to business events. A raw lead is not a qualified demo.
- **Purchases:** separate click-attributed, view-through, deduplicated paid outcomes, and unique customers.

Browser/server rules may overlap. Verify documented deduplication or event-level matching. If overlap is unknown, neither their sum nor their maximum proves a unique purchase count. Label uncertainty or report bounds rather than manufacture precision.

## Equal-spend normalization

For positive arm spend, a descriptive normalization is:

```text
shared_spend = min(spend_a, spend_b)
normalized_count_i = observed_count_i * shared_spend / spend_i
```

Report actual spend and counts beside normalized counts. Do not rescale rate metrics such as CTR, CPC, or CPA. This assumes proportional outcomes at a different spend level; proportional scaling does not replay delivery or establish a causal counterfactual.

## Sparse outcomes

Report raw outcome counts, spend exposure, a rate ratio, and uncertainty. Choose a statistical method appropriate to assignment, dependence, repeated customers, and event generation.

Under independent Poisson-count assumptions with positive counts, an approximate diagnostic is:

```text
rate_ratio = (outcomes_a / spend_a) / (outcomes_b / spend_b)
SE(log(rate_ratio)) = sqrt(1/outcomes_a + 1/outcomes_b)
interval = exp(log(rate_ratio) +/- chosen_z * SE)
```

Do not use this approximation for zero counts or imply that its assumptions always hold. Use a suitable exact method or report the zero count and uncertainty. Cost per outcome is undefined when outcomes are zero.

Multiplying a desired outcome count by an observed CPA estimates spend under a constant-rate assumption. It is not a power calculation or a promised forecast.

## Downstream attribution

Prove event health, canonical deduplication, strict channel source, and stable arm identifiers. Check source and click-ID persistence from signup through paid conversion.

When the channel is visible but arm identifiers are absent, report channel visibility and arm-level attribution unavailable. Do not allocate downstream purchases by spend share.

## Decision contract

Return two verdicts:

1. observed arm performance under the recorded setup;
2. whether assignment, parity, maturity, and evidence support objective causality.

Name the decisive blocker and one clean next move. A rerun may require fresh simultaneous arms, controlled post allocation, verified assignment, stable identifiers, and a precommitted business outcome with guardrails. Separate qualified leads from purchases even if both are monitored.
