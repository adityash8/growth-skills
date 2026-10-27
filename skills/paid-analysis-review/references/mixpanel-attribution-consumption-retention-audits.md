# Mixpanel acquisition and consumption retention audits

Use when a campaign, creator, landing page, or first-purchase product cohort will influence paid budget. Keep the procedure read-only unless the owner separately authorizes saved reports or tracking changes.

## Split the question

- **Acquisition retention:** attribution existed before or at the first qualifying conversion.
- **Consumption retention:** the first basket contained a particular product, creator, or category.

A product in the first basket does not prove it acquired the customer. Report the two reads separately.

## Read-only sequence

1. Freeze one as-of time, timezone, initial-event window, and repeat horizon. For each horizon, exclude initial events too recent to mature. If instrumentation began after the required cutoff, report that checkpoint unavailable.
2. Count total events and unique people for every candidate event over the actual window. Inspect naming/casing variants and client/server duplicates.
3. Measure property fill rates and inspect representative values before defining cohorts. Use event-row denominators for event properties and unique-person denominators for profile properties. Label current profile state as such.
4. Verify current API filter syntax, data types, and report limits against current documentation. Chunk large inventories while retaining each chunk's denominator.
5. Prefer immutable conversion-event attribution, then verified immutable first-touch profiles. If using a near-first-order event as a proxy, prove sequence, cohort size, conversion fraction, and lag to the canonical first-order event.
6. Define a repeat outcome explicitly as a second-or-later order. Verify the population and meaning of any first-order flag; missing flags must not become repeats.
7. For cumulative returned-by-checkpoint rates, use a bounded initial-to-repeat funnel. A retention report's returned-in-interval curve can answer a different question.
8. For list-of-object basket cohorts, inspect current supported quantifiers. A target cohort usually needs any matching item; its exact complement requires every item not to match, with null/empty baskets handled explicitly.
9. Verify target plus control covers the eligible population without overlap. If multiple products can coexist in one basket, creator/product cohorts may overlap even when each target's complement is valid.
10. For paid baselines assembled from separate slices, make the slices disjoint or deduplicate people before summing. Inspect delimiter boundaries in serialized attribution strings.

## Query reliability

- A missing metric in a response is unavailable until a control query establishes why. It is not automatically zero.
- Match returned labels and fields rather than spreadsheet-style position or metric letters.
- Calculate each fill rate from a consistent numerator and denominator. Late-arriving events can move totals between calls.
- Inspect serialized attribution values before choosing a campaign rule. A keyword can occur in a landing path or content field without identifying acquisition.
- A query link supports reproducibility. It does not authorize saving a cohort, dashboard, or report.

## General pitfalls

- **Pitfall:** empty first-touch profiles can coexist with useful event-time attribution. Prove a candidate event's timing and coverage, then label it as a proxy.
- **Pitfall:** mutable profiles can rewrite the apparent source of a historical cohort. Do not treat current UTMs as immutable first touch.
- **Pitfall:** a first purchase counted as a return inflates repeat rates. Test the repeat flag against known event sequences.
- **Pitfall:** a fixed minimum cohort size is not a universal validity rule. Set the required precision or evidence threshold before interpreting budget differences.

## Report contract

Return acquisition and consumption verdicts separately: possible, partial, or blocked. For each checkpoint include cohort size, repeat-person count, rate, matched baseline, point difference, and uncertainty. Attach exact windows, maturity cutoffs, event definitions, filters, population rates, and reproducible query details where available.

Disclose identity stitching, attribution loss, overlapping baskets, late instrumentation, missing properties, and unequal maturity. Neither scorecard proves causality.
