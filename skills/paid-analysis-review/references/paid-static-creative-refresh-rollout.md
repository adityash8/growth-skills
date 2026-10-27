# Controlled static creative refresh

Use when refreshing paid image assets while protecting performance and preserving a usable comparison.

## Release sequence

Inventory current delivery, freeze the baseline, identify protected controls, build the asset-to-audience matrix, approve the exact launch rows, add variants, verify delivery, then evaluate mature downstream outcomes.

## Guardrails

- Add variants beside protected controls unless replacement is explicitly authorized. Verify that shared budgets will not starve the controls.
- Hold audience, objective, bid, budget, destination, and attribution settings stable during the creative comparison. If another change is required, record it and restart or qualify the baseline.
- Use complete account-timezone days and a decision-appropriate historical window. Freeze campaign, ad-group, and ad-level performance before upload.
- Give each variant a stable name and tracking slug that links it to the hypothesis, audience, and asset.
- Set an early operational check and a later outcome-maturity check. Choose their timing from review latency, volume, and conversion lag rather than a universal duration.
- Treat CTR, CPC, and CPM as diagnostics. Keep platform credit separate from qualified leads, activation, purchases, and retained value.
- Define rollback before launch. If new variants break URLs, tracking, quality, or control delivery, stop the new variants within the approved boundary.

## Exact approval manifest

For each proposed ad, record the source asset, filename, MIME type, dimensions, size, target entity, exact ad name, final copy, CTA, destination, tracking template, protected control, proposed budget exposure, and rollback action.

Verify source access, current platform asset requirements, existing entity state, baseline, and downstream event health before presenting the manifest. Bound the first wave by available budget and the evidence needed for a decision. A concept list is not an executable approval packet.

Do not upload, publish, or alter ads unless the exact scope is authorized. Read back created objects and test final destinations after an authorized launch.

## Platform checks

Verify capabilities and field semantics against current documentation and the live account.

- **OpenAI Ads or ChatGPT Ads:** confirm supported asset, targeting, bidding, and measurement controls. Map the asset to intent and audience; distinguish curiosity clicks from activated or qualified users.
- **Reddit Ads:** separate click and view-through outcomes, monitor downstream quality, and avoid combining a refresh with a targeting rebuild.
- **LinkedIn Ads:** distinguish sponsored-person, page, and retargeting formats where relevant. Compare audience temperature and post delivery. Resolve browser/server conversion overlap before interpreting purchase totals.

No channel is the default first lane merely because it was convenient in another account. Choose the smallest valid lane with enough decision-relevant volume and bounded downside.

## Output contract

Provide a channel sequence, exact launch manifest, protected controls, measurement plan, early warning conditions, outcome gate, rollback authority, and named owner. Mark missing assets, unverified tracking, or unsupported controls as blockers.
