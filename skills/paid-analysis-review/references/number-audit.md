# Number audit

Use this for read-only verification of a report, deck, or calculation. Capture the artifact version, decision, permitted accounts and sources, window, timezone, and outcome definitions. Use existing authorized access. A report citation or an old approval does not grant permission to query a different account, edit, or send anything.

1. Inventory the decision-relevant numbers in prose, tables, charts, and footnotes. Group repeated values, but check that each instance uses the same definition and scope.
2. Recalculate each reachable figure from the source named for it. Keep the numerator and denominator for rates. For totals, check overlap and deduplication first. Record the filters, source timestamp, and calculation so someone else can reproduce it. A rounded match is not proof if definitions differ.
3. Mark each claim `verified`, `value mismatch`, `definition mismatch`, or `unreachable`. Keep the supplied value and the recalculated value side by side. If the report froze a historical baseline, retain it and label any later backfill separately. Do not replace missing evidence with zero or an estimate.
4. When two reviewers disagree, resolve it against the underlying data and the agreed definition. A reviewer repeating another's number is not an independent check. An unresolved disagreement that could change the decision keeps the report from being marked ready.
5. Return the verdict, corrected figures or wording, and the smallest source check that would resolve each important gap. Keep sensitive account details in restricted evidence only.
