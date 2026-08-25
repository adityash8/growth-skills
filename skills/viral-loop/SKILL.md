---
name: viral-loop
description: "Measure, design, and improve product-embedded sharing loops using cohort attribution, step-level conversion, loop speed, and decay analysis."
---

# Viral Loop

Use this skill when product use can expose value to non-users through invitations, collaboration, shared artifacts, or referrals.

Do not use it to manufacture sharing for a product with weak retention or no natural recipient value.

## Inputs

- product and user job;
- activation and retention evidence;
- share, invite, or collaboration surfaces;
- acquisition attribution and referral identifiers, if available;
- current funnel rates and abuse constraints.

Unknowns stay explicit.

## Modes

- **Measure:** determine whether an existing loop causes meaningful acquisition.
- **Design:** create a loop that is native to the product's value.
- **Improve:** locate and repair the weakest conversion step.
- **Decay audit:** explain why a previously useful loop weakened.

## Procedure

1. **Run the prerequisite gate.** Confirm users reach value and retained users exist. If not, route to `onboarding-activation` or `retention-state` before adding prompts.
2. **Name the loop.** Define the actor, action, recipient, recipient value, return path, and activation event.
3. **Choose the natural mechanic.** Prefer collaboration, utility, or valuable shared output. Add incentives only when the economics and abuse controls work.
4. **Instrument causality.** Persist a privacy-safe referrer or artifact identifier from exposure through activation. Separate caused users from users who merely arrived in the same period.
5. **Measure by cohort.** For each causing cohort, count activated users attributed to that cohort over a fixed maturation window. Report the window and attribution limits.
6. **Map the step funnel.** Measure exposure → open → landing → signup → activation → first retained action. Do not optimize aggregate sharing while one downstream step is broken.
7. **Measure speed and repetition.** Record time to first caused user, time between generations, and how often retained users create new exposures.
8. **Design at the value peak.** Place sharing after a completed outcome, useful collaboration event, or artifact creation—not before users experience value.
9. **Test one bottleneck.** Route the highest-leverage change to `experiment-design` with a primary metric, guardrails, and stop rule.
10. **Audit decay.** Check novelty loss, audience saturation, platform changes, attribution loss, abuse controls, and retention decline.

## Core calculations

Use a cohort ratio:

```text
viral factor = activated users caused by cohort C / activated users in cohort C
```

When the factor is below 1 and assumptions are stable:

```text
acquisition multiplier = 1 / (1 - viral factor)
```

Treat the multiplier as a model, not a forecast. Loop speed, retention, attribution error, and saturation can dominate it.

## Output contract

Return:

1. prerequisite verdict;
2. loop map and recipient value;
3. attribution specification;
4. step-funnel table with missing data marked;
5. cohort factor, maturation window, and uncertainty;
6. primary bottleneck;
7. one experiment specification;
8. abuse, consent, and platform risks;
9. next handoff.

## Guardrails

- Never use unsolicited contact uploads or dark patterns to inflate the loop.
- Do not call viral share of signups a cohort viral factor.
- Do not claim causality when attribution only shows correlation.
- Protect recipient consent and minimize personal data.
- Do not assume a past platform mechanic still works; verify current rules.
- If incentives attract abuse or exceed incremental value, stop them.

## Handoffs

- unclear channel fit → `channel-fit-diagnostic`;
- weak activation → `onboarding-activation`;
- weak retention → `retention-state` and `power-user-curve`;
- test design → `experiment-design`;
- proven recurring optimization → `marketing-loops`.
