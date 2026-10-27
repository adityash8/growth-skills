# Sources and provenance

The skills in this repository synthesize established growth concepts and generalized operating lessons into agent-ready procedures, output contracts, and guardrails. The influences below identify frameworks and documentation families, rather than claiming that a platform endorses these procedures.

Framework-level influences:

- **Product-channel fit and the Four Fits:** Brian Balfour and Reforge. Used in `channel-fit-diagnostic` to test whether product attributes, market, model, and channel can coexist.
- **Natural product-led acquisition and value-accrual retention:** Julian Shapiro's Startup Handbook. Used in `product-led-acquisition` and `retention-state`.
- **Power User Curve / activity histograms:** a16z writing on L7 and L30 engagement distributions. Used in `power-user-curve`.
- **SaaS unit economics:** David Skok's SaaS Metrics 2.0 and related public writing. Used in `saas-unit-economics-audit`.
- **Lean experiment design and painted-door tests:** established lean product-development practice. Used in `channel-fit-diagnostic` and `growth-roadmap`.
- **Constraint-first growth planning:** synthesized from growth-model, funnel, and experimentation practice. Used in `growth-strategist`, `growth-audit`, and `growth-roadmap`.
- **Viral loop measurement and design:** Andrew Chen's public writing on viral loops and cohort-based product growth. Used at framework level in `viral-loop`.
- **Customer decision research:** jobs-to-be-done interview practice and continuous product-discovery methods. Used in `customer-research` without reproducing proprietary exercises.
- **Controlled experimentation:** standard randomized-experiment and causal-inference practice. Used in `experiment-design`.
- **Reliable recurring operations:** idempotency, durable state, bounded authority, and fail-closed automation practice. Used in `marketing-loops`.
- **Offer and activation design:** synthesized from product marketing, risk-reversal, conversion, and activation practice. Used in `offer-design` and `onboarding-activation`.
- **Governed advertising operations:** least privilege, staged changes, independent state readback, rollback, and bounded approval practice. Used in `paid-media-creative-operations` and `conversational-ads-optimization`.
- **Measurement provenance and consent testing:** event lineage, browser/server deduplication, controlled consent scenarios, and source-to-destination reconciliation. Used in `marketing-tagging-audits`; consult current GTM, GA4, Meta, and Stape documentation for the actual implementation.
- **Paid-channel evidence review:** matched populations and observation windows, financial reconciliation, attribution limits, and controlled comparison. Used in `paid-analysis-review`, with current platform, PostHog, or Mixpanel documentation as appropriate.
- **Conversational advertising diagnosis:** delivery-first troubleshooting, destination verification, attribution reconciliation, and bounded creative tests. Used in `conversational-ads-optimization`; verify current OpenAI Ads or ChatGPT Ads access, features, and API contracts before applying platform-specific steps.
- **Evidence-led reporting:** metric dictionaries, claim-to-source traceability, cohort maturity, billing reconciliation, falsification checks, and rendered-document QA. Used in `evidence-led-growth-audit`.

## Attribution policy

- Source names identify intellectual influences; they do not imply affiliation or endorsement.
- Third-party frameworks, publications, names, and trademarks remain the property of their owners.
- Examples are generic and rewritten. Long quotations and proprietary extracts are intentionally excluded.
- Benchmarks must be dated, segmented, and re-verified before use. This repository does not treat a historical benchmark as a universal target.
- Verify platform behavior, consent requirements, API schemas, and field mappings against current primary documentation when using a skill. A procedural reference is not a promise that a feature is available.

If you believe attribution is missing or material is too close to a source, open an issue with the exact file and passage. Maintainers will review and either add attribution, rewrite, or remove the material.
