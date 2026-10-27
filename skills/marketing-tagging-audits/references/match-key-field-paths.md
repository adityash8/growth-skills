# Match-key field paths

Use when a web tag sends to server GTM and destination diagnostics suggest missing identity, weak matching, or unequal browser/server coverage.

## Trace the consumer's actual path

```text
data layer or browser cookie
-> transport request
-> server client event model
-> vendor template lookup
-> outgoing platform payload
-> destination receipt
```

A field can be present in the request and absent from the vendor payload because the consumer reads a different path.

## Verify installed behavior

Read the imported template version and compare it with current official documentation or upstream source before relying on a mapping. Record which source and version support each claim. Upstream support does not prove the live template includes it.

For Stape Data Tag and Data Client, inspect current source or docs for:

- whether common cookies are nested or flattened;
- how user-data rows enter the server event model;
- which fields are synthesized from request headers;
- whether consent signals and cookie-storage controls are supported and consumed.

For LinkedIn, verify the click-identity paths the installed server template reads. For OpenAI Ads, verify the currently supported click/browser identity fields and their lookup order. Do not assume a common-cookie option reaches every destination. Add explicit mappings only when the installed consumer requires them.

## Pitfall: identity arrives after initialization

An All Pages tag cannot carry identity that becomes available only during signup or checkout. Inspect event-time user data on those events, then confirm the outgoing payload. A supported field in the template is insufficient if the producer never sends it.

## Route and destination matrix

When the same server client accepts browser and backend requests, build an event x request-path x destination matrix:

- evaluate actual trigger predicates and pause states;
- confirm each destination has an enabled producer;
- inspect browser and backend routes independently;
- test approved hostnames against their allowlists and stream mappings;
- trace hostname exceptions to the exact tags that reference them.

A route title is not a request-path predicate. A GA4 exception does not automatically block independent pixels or transport tags.

## Pitfall: runtime inheritance looks like missing mapping

A built-in Google Ads server tag may consume transaction identity from the event model without an explicit export parameter. A destination template may consume matching IDs from cookies or common fields. Verify incoming and outgoing payloads before reporting a missing field or adding a duplicate mapping.

## Webhook identity

A generated client ID on a cookie-free backend request does not prove browser continuity. Require a traced link to the browser's actual client/session identity before claiming attribution continuity. Check IP and user-agent fallbacks so server identity is not mistaken for the visitor.

A browser lifecycle identifier is not automatically shared with a payment webhook. Use the platform's documented event or transaction identity contract and prove runtime equality for intended deduplicated pairs.

## Consent and acceptance

Check web consent gating, forwarding, and server consumption separately. A field named consent does not establish enforcement.

Acceptance requires:

- policy-correct behavior for denied and granted consent in the intended region;
- one eligible event per intended route and action;
- matching event semantics and deduplication identity where pairing is used;
- expected identity at the exact path consumed by the installed template;
- user data refreshed when it becomes available;
- destination receipt and deduplication diagnostics after the documented delay.

Keep configuration risk, observed requests, and platform acceptance as distinct evidence levels.
