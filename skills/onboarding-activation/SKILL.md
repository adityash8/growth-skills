---
name: onboarding-activation
description: "Design onboarding around a measurable activation event, shorten time to value, remove friction, and recover stalled users."
---

# Onboarding Activation

Use this skill when qualified users start but fail to reach meaningful first value, or when onboarding is organized around setup tasks rather than outcomes.

## Inputs

- target segment and promised outcome;
- candidate activation event;
- signup-to-value funnel with timestamps;
- required setup, permissions, integrations, or data;
- successful and stalled user evidence;
- product, support, and lifecycle-message constraints.

## Procedure

1. **Define activation.** Choose the earliest observable behavior that predicts continued value. Do not use account creation or page views unless they are the value.
2. **Validate the proxy.** Compare users who perform the event with similar users who do not. Label correlation honestly.
3. **Map the shortest value path.** List every step from first intent to activation, including waiting, context switches, permissions, and external dependencies.
4. **Classify friction.** Mark each step as required, deferrable, removable, automatable, or explainable.
5. **Sequence progressive setup.** Ask only for information needed to reach the next value event. Defer configuration that serves later use.
6. **Design empty states.** Replace blank screens with a relevant example, safe default, import path, or guided first action.
7. **Expose progress and recovery.** Make the next step clear, preserve state, and give stalled users a direct resume path.
8. **Coordinate messages.** Use in-product prompts and lifecycle messages to continue the same value path, not launch separate campaigns.
9. **Segment real differences.** Create branches only when roles, use cases, or dependencies materially change the activation path.
10. **Test the bottleneck.** Route one meaningful change at a time to `experiment-design`.

## Diagnostic cuts

Inspect activation and time-to-value by:

- acquisition source;
- use case or segment;
- device and platform;
- plan or entry offer;
- required integration;
- invited versus self-started user;
- cohort and product version.

Require enough exposure before calling a segment difference causal.

## Output contract

Return:

1. activation definition and confidence;
2. current path and median time-to-value;
3. step funnel with largest loss or delay;
4. friction classification;
5. proposed shortest path;
6. empty-state and recovery changes;
7. instrumentation requirements;
8. one prioritized experiment;
9. guardrail metrics;
10. handoff owner or dependency.

## Guardrails

- Do not optimize completion of steps that do not predict value.
- Do not add tours, checklists, or messages without a named friction point.
- Avoid mandatory profile fields and permissions before they are needed.
- Keep accessibility and keyboard use intact when adding guidance.
- Never use notification permission as a substitute for product value.
- If acquired users are fundamentally wrong for the product, route to `channel-fit-diagnostic` instead of polishing onboarding.

## Handoffs

- wrong audience or channel → `channel-fit-diagnostic`;
- unclear user motivation → `customer-research`;
- weak long-term value → `retention-state` and `power-user-curve`;
- controlled test → `experiment-design`;
- proven recovery process → `marketing-loops`.
