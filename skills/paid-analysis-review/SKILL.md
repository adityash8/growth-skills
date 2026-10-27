---
name: paid-analysis-review
description: Use when reviewing paid-media reports, experiment results, or decks to verify metrics, reconcile attribution, and turn evidence into bounded decisions.
---

# Paid Analysis Review

Review acquisition reports, experiment results, and decks before they guide budget or creative decisions. Keep facts, inferences, and recommendations separate.

## Scope and authority

- Confirm whether an attached report supports an existing decision or is itself the requested review. Answer the active decision first.
- Default to read-only source checks. Review authority does not authorize campaign edits, tracking changes, report publication, or messages.
- Use the requested audience, length, and format. Keep detailed evidence in a supporting appendix when a short answer is requested.
- Verify API fields, reporting units, platform capabilities, and limits against current documentation and live metadata before using them.

## Workflow

1. Read the artifact, including embedded charts. Extract its thesis, material claims, numbers, and requested decisions.
2. Freeze scope: entity set, exact inclusive start and exclusive end, timezone, currency, event definitions, attribution model, and conversion maturity.
3. Map each claim to its source and smallest useful read-only check. Honor a named historical baseline and any instruction against a fresh pull.
4. Verify entity identity, reporting grain, spend, effective status, objective, bid settings, optimization event, and source freshness.
5. Reconcile matched entity sets. Keep unmatched rows, missing fields, and conflicting definitions visible.
6. Check denominators, duplicate events, cohort eligibility, uncertainty, and the causal language.
7. Return specific replacement wording, a decision, and the smallest next check that could overturn it.

## Keep measurement systems in their lanes

| Source | What to verify | Limitation |
|---|---|---|
| Ad platform | Spend, delivery, entities, settings, attributed actions | Attributed events need not equal unique customers or incremental outcomes |
| Connector export | Row completeness, field mapping, refresh time, mirrored spend | A second copy of platform data is not independent conversion truth |
| Product analytics | Event health, activation, purchases, cohort quality | All-channel volume does not prove attribution to an ad |
| Billing or warehouse | Paid outcomes, refunds, customer identity, agreed CAC | Event and attribution definitions still need reconciliation |
| Workbook or manual tags | Classification, cohort rules, formulas | Subjective tags and generated fields can bias comparisons |

State Fact, Inference, or Recommendation beside each material claim. Include source, window, confidence, currency, and the relevant denominator.

## Attribution and event integrity

- Discover the canonical business outcome and stable deduplication key before counting. Distinguish subscriptions, transactions, customers, and event rows.
- Prove an outcome event is live with a bounded all-channel count before interpreting a zero paid-channel result.
- Report strict campaign/creative matches separately from broader channel matches, current profile fields, initial profile fields, and click-chain evidence.
- Missing entity IDs mean the target cohort is unidentifiable. Do not call it confirmed zero or allocate unattributed purchases by spend share.
- Historical click IDs do not override an explicit conflicting event-time source without a verified attribution rule.
- Keep click-attributed, view-through, and engaged-view outcomes separate. Compare platform and downstream counts only after matching outcome, identity, window, and model.
- Browser and server rules may overlap. Verify event-level deduplication or a documented reconciliation rule; neither summing nor taking a maximum proves unique purchases.
- Keep tracker CAC, verified-customer CAC, and raw platform conversion discrepancies as separate comparisons.
- Separate interaction-to-event lag, signup-to-payment lag, and attribution-model differences.

Use [purchase cross-checks](references/posthog-paid-purchase-cross-checks.md) for PostHog reconciliation and [connector and attribution audits](references/posthog-marketing-analytics-attribution-audit.md) for freshness, persistence, and traffic-quality checks.

## Experiment and causal checks

- An observational winner is a test hypothesis. Budget allocation, audience, placement, campaign history, and optimization settings can explain apparent creative differences.
- Equal budgets do not prove randomized or mutually exclusive assignment. Verify exposure and delivery before claiming a causal result.
- Compare actual creative/post delivery shares, not just matching asset inventories.
- Small outcome counts require uncertainty and a precommitted decision rule. Use an evidence or precision gate suited to the decision, not a universal sample-size cutoff.
- A longer runtime cannot repair confounded arms. Mark the result inconclusive and specify a clean rerun.
- Engagement metrics are diagnostics unless their relationship to the business outcome is established in the relevant data.
- A misconfigured example can invalidate that example's verdict. It does not prove all similar creative would succeed.
- Check whether a proposed setup already ran before presenting it as a new experiment. Removing a bid cap does not guarantee lower CAC.

Use [LinkedIn objective comparisons](references/linkedin-objective-equal-spend-experiment-audits.md) for setup parity, equal-spend normalization, and sparse outcomes. Use [creative reconciliation](references/linkedin-creative-posthog-reconciliation.md) before recommending an ad pause from disputed purchase counts.

## Channel and creative checks

- Inspect named conversion actions, counting rules, and primary/secondary status before comparing Google Ads device CPAs. Historical goal changes can mix outcomes.
- Split brand and non-brand before proposing a device exclusion. A device finding on one platform does not establish the same finding elsewhere.
- Verify destination URLs from hydrated creative objects and actual redirects. Names, thumbnails, captions, and display URLs are discovery clues.
- Check effective status across campaign, ad group, and ad. An enabled child beneath a paused parent is not serving.
- Classify asset types and partnership formats from current documented fields or visible output. A video thumbnail or feature toggle does not establish a static or partnership ad.
- Recover exact previously flagged entities and status history before judging follow-up action. Shared creative names can refer to different ads.
- A modification timestamp proves a change occurred, not which field changed. Use change history or snapshots before naming the change.
- For pause decisions, inspect the agreed recent window, prior signal, attribution maturity, replacement risk, and the exact approved rule. A zero-purchase ad may still have qualified upstream outcomes.

Use [weekly Reddit reconciliation](references/reddit-weekly-readonly-reconciliation.md) for frozen baselines, pacing, action counts, and pending decisions. Use [static creative rollout](references/paid-static-creative-refresh-rollout.md) for a protected additive refresh.

## Cohort and retention checks

- Separate acquisition attribution from first-purchase product or creator selection. Basket contents do not prove who acquired the customer.
- Prove event/property population during the requested window. A schema catalog entry does not establish live data.
- Prefer immutable event-time attribution. Label mutable profile fields and near-first-order proxies honestly, with timing evidence.
- Require a second-or-later purchase for repeat behavior. Do not count the first order as a return.
- Use maturity-adjusted cohort cutoffs. Separate returned-in-interval retention from returned-by-checkpoint conversion.
- Report cohort size, repeated-user count, rate, and uncertainty together. Disclose overlapping product cohorts, missing attribution, and identity-stitching gaps.
- For content funnels, verify exposure, eligibility, same-item linkage, and temporal order before claiming watch-to-share behavior. Placement comparisons remain observational.

Use [Mixpanel acquisition and consumption cohorts](references/mixpanel-attribution-consumption-retention-audits.md) for the detailed read-only sequence and silent-query failures.

## Financial targets and proxy traps

- Separate the business outcome ceiling from the platform bid setting. Verify whether the current platform supports the proposed bid control.
- Estimate an acquisition ceiling from retained gross profit over an explicit payback horizon. A constant monthly-margin assumption may use monthly gross profit multiplied by payback months; disclose churn, costs, and uncertainty.
- Keep self-serve purchases, enterprise invoices, renewals, reactivations, and top-ups separate. An invoice is not necessarily acquisition revenue.
- Show signup, activated-user, qualified-lead, and verified-purchase CPAs separately. Do not invent a purchase target when the canonical cohort is unavailable.
- Value each outcome separately. Do not assign the sum of alternative outcome values to every event or treat purchases plus raw leads as equivalent customers.
- Resolve person or organization overlap before combining outcomes. A lead who later buys is not two acquired customers.
- Label proxy values as scores or expected value. A proxy-return metric is not revenue ROAS.
- Estimate pre-payment milestone value from unique eligible people and later verified outcomes over a mature horizon. Avoid repeated-event inflation and stacking full-funnel values as additive revenue.
- Reconcile currency, tax, discounts, refunds, pagination, and customer history before approving revenue or payback claims.
- Compute any platform-to-business adjustment only for matched unique outcomes with established coverage. Missing attribution makes the adjustment unavailable.
- Match every chart target to its plotted denominator. If a target is absent or deferred, omit target claims and target lines.

## Acquisition-pause impact checks

- Separate modeled spend avoided, observed period changes, causal lift, and operating profit. Name excluded costs and channels.
- Compare churn over equal elapsed time or mature cohorts. A partial-month pace estimate is not a full-month rate.
- Check same-tenure, same-channel cohorts before crediting retention changes after acquisition stops. Cohort aging can raise apparent value without an intervention effect.
- Separate failed initial payments from failed renewals. Use deduplicated invoices, equal follow-up, terminal losses, and collected cash for recovery claims.
- Restart recommendations need channel-specific retained margin, CAC, and a payback horizon, rather than an aggregate churn threshold alone.

## Recurring report checks

1. Define complete reporting buckets in a named timezone and freeze the bundle's source packet. Keep explicitly frozen prior baselines separate from later backfill.
2. Retain source-specific outcome names, click/view splits, units, raw proof, freshness, and source errors in normalized data.
3. Separate collection, judgment, and delivery. A collector must not publish or mutate campaigns by accident.
4. Apply the owner's approved delivery destination and authority. Without delivery authorization, return a completed draft for review.
5. Key reruns by reporting window and destination. Multiple messages or retries from one bundle do not create extra approvals.
6. Use daylight-saving-aware scheduling. Later messages in a bundle reuse its packet unless the documented freshness rule requires a full refresh.
7. Fail required-source gates visibly. Never substitute empty dry-run data for a live approval draft or publish a misleading partial reconciliation.
8. Validate metric vocabulary, chart attachment, required caveats, and requested format before delivery. Suppress duplicate failure notices.

## Narrative and visual QA

- Replace unsupported causal claims with the observed pattern, its confound, and a clean test.
- Keep one clear thesis and one operational ask. Use evidence about setup or handoffs without inventing team blame.
- Check rendered charts against text for matching totals, populations, versions, and dates.
- Label axes and currencies. Separate count labels from cost labels; inspect exported images for overlap, clipping, and missing caveats.
- Keep unlike outcomes separate in chart totals and week-over-week calculations.
- Respect the requested message syntax. Paste-ready Slack copy should remain plain text unless another format was requested.

Use [stakeholder-facing review](references/client-facing-paid-analysis-review.md) for concise narrative edits and deck checks.

## Output contract

Return:

1. **Verdict:** ready, needs changes, or inconclusive, with the decisive reason.
2. **Material issues:** claim, source check, consequence, and exact replacement wording.
3. **Reconciliation:** matched definitions and deltas, with missing or unmatched rows visible.
4. **Decision:** hold, test, pause recommendation, or scale recommendation only when the agreed evidence gate supports it.
5. **Next check:** owner, required evidence, approval boundary, and a falsification or stop rule.
6. **Evidence appendix:** source timestamps, query scope, definitions, and unresolved gaps. Include only authorized, necessary data.

Stop sign-off when source scope is wrong, definitions conflict, required data is stale, the cohort cannot be identified, or rendered claims disagree with the evidence. Return the exact blocker and smallest check that resolves it.
