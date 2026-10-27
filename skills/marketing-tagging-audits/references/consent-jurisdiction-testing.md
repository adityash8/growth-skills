# Consent testing across regions

Use when consent behavior must be checked across marketing, app, blog, or help-center surfaces.

## Establish the acceptance policy

Record the intended region, CMP mode, approved purposes, and expected behavior for each state. Verify current platform documentation and the organization's approved consent policy. Technical observations alone do not establish legal compliance.

Source presence, runtime behavior, and region configuration are separate proof layers:

1. **Source:** CMP, defaults, and analytics code are loaded in the intended order.
2. **Runtime:** requests, storage, and data-layer changes match the acceptance policy.
3. **Region:** the CMP uses the jurisdiction mode required by the test.

## Pitfall: the runner uses a different region

A result from a different jurisdiction mode cannot close a region-specific test. Use an approved regional proxy or documented CMP test mode, record which was used, and repeat the runtime checks. Do not label the product passed or failed before confirming the environment.

## Test matrix

Use fresh profiles for independent cases and preserve one profile for persistence tests. Start network capture before navigation and inspect storage as well as requests.

| Case | Check |
|------|-------|
| Fresh visit before choice | Defaults and pre-consent behavior match the approved policy |
| Explicit denial | Prohibited purposes do not collect identifiers or emit blocked events |
| Denial followed by reload | The intended denial persists across the documented scope |
| Mid-session grant | Eligible tags start once without duplicate page views or conversions |
| Persisted acceptance | Intended tags fire once without requiring another update event |
| Withdrawal | Future collection stops or changes as required by the policy |
| SPA navigation | Eligible route events occur once and remain consent-aware |

Check browser requests, server receipt, cookies, local storage, session storage, and consent signals. For approved cookieless behavior, inspect the actual payload and applicable settings instead of assuming every pre-consent request is a defect.

## Source checks support the runtime test

Inspect CMP coverage, consent defaults before tag execution, and platform-specific consent settings. Code in a bundle does not prove pre-consent firing. Code absent from initial HTML may arrive through loaded chunks.

## Reporting

For each surface record region, CMP mode, initial state, action, expected result, observed request/storage behavior, destination proof, and verdict. If region or server evidence is missing, leave that acceptance item open and name the exact test needed.
