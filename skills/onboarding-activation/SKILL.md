---
name: onboarding-activation
description: "Design onboarding around a measurable activation event, shorten time to value, remove friction, and recover stalled users."
---

# Onboarding Activation

Use this skill when qualified users start but fail to reach meaningful first value, or when onboarding is organized around setup tasks rather than outcomes.

Start from first use, before or after signup. Preserve account-free products. Give users a real useful result before asking for an account or payment when the product permits it; a promise or simulated personal result does not count.

Do NOT use for employee onboarding, signup-form conversion, paid-access screen design, or email-only lifecycle sequences. Keep activation here; assign those product surfaces to their responsible owners as described in Handoffs.

## Execution boundary

Draft audits, flows, copy and test plans immediately. Explicitly state that live flow or payment changes, experiment enrollment, sending messages, and rollout require user approval before execution. A request to prepare work, tool access, or an experiment win is not permission to launch. Never claim execution without evidence.

## Inputs

- target segment and promised outcome;
- candidate activation event;
- signup-to-value funnel with timestamps;
- required setup, permissions, integrations, or data;
- successful and stalled user evidence;
- product, support, and lifecycle-message constraints.

Read any supplied product context before asking questions. Use available screenshots, exports and observations now; ask only for missing evidence needed to resolve a decision. When data is absent, draft a provisional flow and measurement plan rather than blocking useful work.

Label supplied observations, calculations with their inputs, and estimates or hypotheses distinctly. Keep missing activation rates, median time-to-value and retention relationships explicitly unknown. Do not invent baselines, lift, segment differences or causal evidence. Candidate activation events remain provisional until validated.

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
10. **Test the bottleneck.** Route one meaningful change at a time to `experiment-design`. Provide the proposed change, eligible cohort, provisional activation outcome, supplied evidence, missing data and guardrails. Do not imply that skill ran without its output.

## Flow details

- Keep the first session focused on one successful outcome, with a clear next action and no dead ends. Measure activation from first use; use signup as the denominator only when it is the relevant entry point.
- For a checklist, use a short sequence ordered by value, with an action, benefit, estimated effort and direct start action for each item. Show truthful progress and allow dismissal without blocking unrelated value.
- Empty states should explain the value, preview the useful state, and offer a primary action to create the first real item plus an optional import or template path. Label example data clearly.
- Prefer doing the task over a tour. Make guidance dismissible and avoid repeating it for returning users.
- Request mobile permissions when the feature needs them, after demonstrating value. Keep a useful path when optional permission is declined.
- Define stalled states using missing activation behavior and elapsed time. Coordinate in-product, email and human recovery around one resume action; stop reminders once activation occurs. Treat timing as a hypothesis unless supported by evidence.
- Draft welcome, checklist, empty-state, tooltip, milestone and recovery copy only for the surfaces in scope. Celebrate meaningful outcomes and make sharing optional.

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

For an audit, write each issue as Finding → Impact → Recommendation → Priority. For a flow design, include the activation goal, step sequence, relevant checklist and copy, recovery triggers and measurement plan within the contract above.

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
- registration friction → registration-flow owner, with required fields, observed drop-off and the first-value dependency;
- paid-access or upgrade decisions → payment-flow owner for purchase and decline behavior; use `offer-design` for price, trial and commercial terms, with the current offer, value milestone and constraints;
- full lifecycle email series → lifecycle-message owner, with user states, triggers, resume action and suppression rules;
- controlled test → `experiment-design`, with the concrete brief specified above;
- proven recovery process → `marketing-loops`.

Name the relevant skill or responsible owner explicitly and include the requested deliverable and unresolved dependencies. Never imply another skill or owner executed work without their output.
