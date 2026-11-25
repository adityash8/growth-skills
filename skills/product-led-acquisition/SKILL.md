---
name: product-led-acquisition
description: "Design product mechanics that expose value to non-users and create natural invitations, collaboration, or shareable outputs."
---

# Product-Led Acquisition

Design product use so existing users naturally expose value to new users through invitations, collaboration, shared artifacts, user-generated content, or word of mouth.

Do NOT use for incentivized referral-program design, launch campaigns, or sales-assisted funnel design. Use `retention-state` for retention architecture and `channel-fit-diagnostic` for channel comparison.

## Modes

- **Diagnostic:** identify which acquisition mechanism the product can support.
- **Loop audit:** find the weakest link in an existing acquisition loop.
- **Idea comparison:** compare products by their ability to transfer valuable goods or support important conversations. Run the fit checks for each idea first.

## Inputs and missing evidence

Use supplied product context, documentation, exports, and observations. Do useful draft work without demanding information already supplied. Label unknown facts as unknown; do not invent usage, retention, or analytics access.

| Input | If missing |
|---|---|
| Core value event and time to value | State what is unknown and assess only supported facts. |
| Activation and habit retention by cohort | Mark the first fit check unproven and stop at that check. |
| Actions visible to non-users, recipient types, permissions | List candidate surfaces as unverified. |
| Entry source: shared-in, public artifact, or cold signup | Propose source measurement; do not assume equivalent activation. |
| Invite, view, edit, and creator pricing | Mark unknown and verify before recommending a pricing change. |
| Exposure, signup, activation, repeat-sharing, and cost data | Give an instrumentation plan; leave unsupported calculations unavailable. |

Label substantive numbers as supplied/measured, calculated with inputs, or estimates with assumptions. Examples are not product targets. A missing denominator or incompatible cohort makes a calculation unavailable, not zero.

## Step 0 — Fit checks before recommendations

**Print BOTH fit-check results before any mechanism preference, ranking, recommendation, or opening verdict.** For each, show pass, fail, or unproven, with evidence. If the first check stops work, still print the second as unproven when it cannot be assessed.

| Check | Result and next action |
|---|---|
| Activation and habit retention proven? Users reach value and return through normal use. | Fail or unproven: stop the build plan. Give an evidence checklist and hand off activation to `onboarding-activation` or habit retention to `retention-state`. |
| One-to-many use at the core? Valuable transfers or conversations naturally involve other people. | Fail or unproven: stop invitation, billboarding, and content-loop build recommendations. If retention passes, discuss only supported word-of-mouth opportunities and route channel choice to `channel-fit-diagnostic`. |

If a check stops work, provide missing evidence and the appropriate handoff instead of a ranked build plan. Do not invent a sharing feature to make an unsuitable product appear suitable.

When both checks pass, answer with evidence:

| Product fact | Eligible mechanism |
|---|---|
| Transfers valuable goods, deliverables, approvals, or signatures | Natural invitation: receive something owed |
| Hosts conversations both parties care about | Natural invitation: join a conversation |
| Normal use is visible through links, exports, messages, or public artifacts | Billboarding: visible product attribution |
| Users create content others want to find or share | User-generated content loop |

Rank only supported mechanisms. If all four are absent, state the honest ceiling, suggest at most an evidence-supported word-of-mouth opportunity, and hand off to `channel-fit-diagnostic`.

## Step 1 — Map the loop

Map value → exposure → recipient motivation → conversion → activation → repeat exposure.

Identify the sender, natural recipient, exact surface, recipient action, and reason to act. If the recipient never produces another exposure, describe a one-time acquisition path rather than a repeating loop.

Optimize both conversion and elapsed time from exposure to signup. Do not maximize invitations while recipient activation falls.

## Step 2 — Choose the mechanism

### Natural invitations

The recipient gets something useful or joins a relevant conversation. Maximize use of that valuable action and its frequency, rather than adding generic invite prompts.

For document, workspace, or builder products, distinguish:

- **Team sharing:** a user creates an artifact, shares it with collaborators, and some recipients create and share their own.
- **Public publishing:** a user deliberately publishes an artifact or template; visitors discover its value and create their own.

Keep private sharing separate from public publishing. The sharer supplies the first explanation: provide useful templates, context, and defaults.

Audit charges at the invite, view, or edit step. Prefer removing recipient friction where economics permit; draft pricing proposals for approval rather than changing prices. A personal-use path into team use is viable only if actual usage supports it; measure personal-to-workspace conversion.

Cash incentives are a separate referral-program task. A reward does not repair a weak value proposition or justify unsolicited invitations.

### Billboarding

Audit normal exposure surfaces: physical use, shared links, exported artifacts, branded communications, identity markers, and useful outputs inside shared workspaces.

For forms, signatures, events, or similar artifacts, inspect the recipient completion page. Explain the product and offer a create-your-own action after the recipient finishes their original task.

When creators need white-label output, propose small branding changes with explicit permission and opt-out rules. Measure branded-artifact click-to-signup conversion per release step; track opt-out requests as a trust measure, not a separate acquisition change.

### User-generated content

Identify why creators already want an audience or why their answers help others. Assess public profiles, browse/search discovery, sharing, and visitor-to-creator conversion.

Public discovery requires permission to publish. Do not expose private content or promise search or AI-answer visibility without evidence.

### Word of mouth

Find a remarkable pain reduction, delight moment, or shared identity. Use customer comments to identify the core benefit people describe to others. A tell-your-friends button alone is not a strategy.

For early products, direct support by builders can reveal recurring problems and create delight. Specify the problem to solve and how that learning improves the product.

Do not assume satisfaction scores imply referrals. Compare observed advocacy and conversion across satisfaction bands when compatible data exists.

## Step 3 — Measurement and honest ceiling

For each proposed change, name its viral input metric and event location: shares per active user, recipient views, invite-to-signup conversion, recipient activation, repeat sharing, and exposure-to-signup time.

Separate shared-in, publicly discovered, and cold signup cohorts before judging activation or retention. Define cohort, denominator, and observation window. Use `viral-loop` for detailed viral coefficient and cycle-time modelling.

Estimate the ceiling from eligible actions × exposures per action × recipient response × activation for a defined period. State assumptions, overlapping recipients, and the limiting factor; do not present potential reach as guaranteed acquisition.

For word of mouth, propose a how-did-you-hear-about-us question on a sample of new users and compare answers with referrer and unattributed direct traffic. Respect consent and identify attribution uncertainty.

### Free usage with per-use model costs

Treat free credits and event giveaways as acquisition spend in the comparison. Before recommending a cut, calculate monthly free-usage model cost divided by monthly activations from free users, using matching cohorts and periods. Print separately:

`Cost per activated user (free usage): $X vs paid CAC $Y`

If either input is missing, mark it unavailable and name the missing evidence. Explain that activated-user cost and paying-customer acquisition cost have different denominators. Use `saas-unit-economics-audit` to assess economics before recommending changes.

## Output contract

1. **Both fit-check results first**, then a viable, buildable, or structurally weak verdict. If stopped, give evidence checklist and handoff instead of a ranked plan.
2. **Loop map and ranked eligible mechanisms**, grounded in actual usage; name the primary mechanism and why.
3. **Three to seven buildable product changes** when both checks pass. For each, specify what changes, its location, what the non-user sees, its input metric, and where to measure it.
4. **Measurement plan:** event chain, cohort cuts, time-to-conversion, assumptions, and decision rule. Use `experiment-design` for detailed experiments and `growth-roadmap` for sequencing.
5. **Removal proposals:** forced sharing, incentive mechanics that replace core value, or share-edge pricing friction. These are proposals requiring approval.
6. **Honest ceiling and trust risks:** limiting factor, privacy, spam, fraud, and permission requirements.
7. **Free-usage cost comparison** when per-use model costs apply, before any recommendation to cut free usage.

## Approval and trust

Prepare drafts immediately, but explicitly require human approval before any live product or analytics edit, rollout, publication, pricing or free-credit change, invitation sending, or deletion. A request to prepare changes is not permission to execute them. Never claim execution without evidence.

- Do not force sharing before value is delivered.
- Do not scrape contacts, preselect consent, or send unsolicited invitations.
- Keep private artifacts private unless publication is explicitly approved.
- Let recipients understand value before registration where privacy permits; preserve context through signup.
- Do not claim a sibling skill ran without its output.

## Method and validation history

Framework: natural invitations, billboarding, user-generated content, and word of mouth; distinguish acquisition from self-serve sales conversion.

The source skill reports a frozen four-input, five-check evaluation: baseline 70% / 75%, final 100% / 100%. Kept changes: explicit human approval before live changes; both fit-check results before any opening recommendation or ranked build plan. Generator and scorer were the same model, so this is directional self-evaluation evidence.

This public adaptation preserves those instructions. It was edited for portability and checked structurally; no new behavioral evaluation was run. Harder future checks include overlapping cohorts, creator versus recipient retention, activation versus payer costs, permission to publish privately shared content, and ranked-plan requests with unknown retention.
