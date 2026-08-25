---
name: product-led-acquisition
description: "Design product mechanics that expose value to non-users and create natural invitations, collaboration, or shareable outputs."
---

# Product-Led Acquisition

Use this skill when product use could itself create discovery, invitations, collaboration, or public proof. This is acquisition architecture, not a generic referral-program checklist.

## Inputs

- primary value event and time to value;
- who receives value from the product today;
- artifacts, outcomes, or interactions created during normal use;
- moments when another person is required or naturally useful;
- visibility, privacy, permission, and abuse constraints;
- invite, share, recipient-view, signup, and activation data if available.

## Diagnostic

A useful loop needs four links:

1. **Value:** an existing user gets real value.
2. **Exposure:** a non-user sees evidence of that value.
3. **Motivation:** the non-user has a reason to engage.
4. **Conversion:** the recipient can reach value with low friction.

If one link is structurally weak, incentives will not repair the loop.

## Procedure

1. **Map value-producing actions.** Identify what users already create, complete, publish, send, or coordinate.
2. **Find natural recipients.** List people who benefit from seeing or joining that action. Exclude audiences that require spammy distribution.
3. **Choose a loop archetype.** Use one primary mechanic:
   - collaboration or handoff;
   - shareable output or result;
   - public artifact or embedded attribution;
   - marketplace supply-demand participation;
   - audience or community contribution;
   - two-sided referral where both parties gain real value.
4. **Remove recipient friction.** Let the non-user understand the value before registration where privacy permits. Preserve context across the signup boundary.
5. **Design the return path.** The new user must create another valuable exposure event; otherwise the mechanic is a one-time referral, not a loop.
6. **Instrument the chain.** Measure exposure rate, recipient engagement, signup conversion, activation, and repeat-loop creation by cohort.
7. **Estimate the honest ceiling.** Use eligible actions × exposure rate × recipient response × activation. State which factor caps growth.
8. **Test safely.** Start with one surface, one recipient type, and clear opt-out or permission rules.

## Output contract

1. **Loop verdict:** viable, buildable, or structurally weak.
2. **Loop map:** value → exposure → motivation → conversion → repeat.
3. **Primary mechanic:** the one to build first and why.
4. **Product changes:** three to five feature-level changes.
5. **Measurement plan:** event chain, cohort cuts, and decision rule.
6. **Honest ceiling:** assumptions and bottleneck.
7. **Abuse and trust risks:** spam, privacy, fraud, or incentive gaming.

## Guardrails

- Do not force sharing before value is delivered.
- Do not use dark patterns, contact scraping, or preselected consent.
- Do not confuse a coupon with a self-reinforcing product loop.
- Do not optimize invite sends while recipient activation falls.
- Respect private content and the recipient's context.
- Hand retention architecture to `retention-state` and channel comparison to `channel-fit-diagnostic`.
