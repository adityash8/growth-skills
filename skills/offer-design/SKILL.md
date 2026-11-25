---
name: offer-design
description: "Design an offer by aligning the buyer outcome, mechanism, proof, risk reversal, price, and delivery constraints without fake urgency."
---

# Offer Design

Use this skill when demand exists but the commercial package is unclear, weak, hard to trust, or hard to compare. Design the exchange: outcome, scope, mechanism, proof, risk, price, terms, and delivery.

Do NOT use for buyer discovery (`customer-research`), SaaS economics (`saas-unit-economics-audit`), or experiment design (`experiment-design`). Price-level, tier and value-metric decisions need a pricing specialist; sales pages, launch plans, email sequences and buyer conversations need their respective specialists.

## Drafts and approval

Produce reviewable offer drafts immediately. Explicitly state that the user must approve the concrete scope, price/payment, guarantee and delivery terms before any live publication, billing or contract change. Require separate explicit approval for destructive actions such as deleting customer records. Preparing an offer does not authorize live execution; never claim it occurred.

## Inputs and missing data

Read any supplied product and marketing context before asking questions. Use what is already available:

- target segment, buying trigger, objections and research evidence;
- current offer, alternative and switching cost;
- desired outcome, mechanism and time horizon;
- capabilities, capacity, delivery owners and support limits;
- proof assets, price, costs, gross margin and refund history.

If information is missing, draft the supported portions now. Mark unknowns and provisional assumptions; ask only for missing evidence that changes the decision. Do not invent customer research, proof, capacity, margin, refund rates or conversion lift. With no research, identify the proposed segment as a hypothesis and provide a concrete `customer-research` handoff.

## Diagnose the offer

1. Identify the business type and state the current offer in plain language: name, scope, price/payment, guarantee and deadline.
2. Diagnose four value levers: desired outcome, perceived likelihood of success, time to first value, and buyer effort or sacrifice. Any rating is a judgment, not a measured fact.
3. Audit the components below. Find the weakest supported component and recommend one primary change. Do not rebuild everything by default.
4. Check delivery capacity, margin, support cost, refund exposure and operational ownership before adding promises or extras.
5. Draft the changed component and explain the mechanism it should improve. Expected lift stays unknown unless evidence supports an estimate; label any estimate and its assumptions. Do not treat historical results as a guarantee.
6. Create two or three variants, each changing one major variable from the current offer. Send the comparison to `experiment-design` with a decision, metric and constraints to test.

## Offer components

| Component | Required decision |
|-----------|-------------------|
| Core deliverable | Who receives what, by when, with what exclusions and buyer responsibilities? |
| Bonuses | Which evidenced objection does each optional extra resolve, at what delivery cost? |
| Guarantee | What qualifies, what remedy applies, when can it be claimed, and can the seller honor it? |
| Scarcity or urgency | Is there a real capacity, inventory or calendar limit the seller will enforce? If none, omit it. |
| Name | Does a plain outcome or method name describe what is actually delivered? |
| Price and payment | What is charged, when, for what commitment, under which cancellation and renewal terms? |

Bonuses support a complete core; they must not patch an incomplete service or add unbounded support. Quote a monetary bonus value only with a verifiable comparable or standalone price. Do not inflate a total value to manufacture a discount.

For partner-funded annual bundles, verify audience fit, public list prices, partner commitments, eligibility, code availability, activation, cancellation and renewal conditions. Distinguish the seller's subscription refund from partner access and renewal charges. Do not imply every buyer can use every benefit.

Guarantees may use a trial, first-milestone exit, conditional refund, service credit or bounded extension. State eligibility, time window, buyer obligations, remedy and limits. Avoid open-ended work and promises dependent on market conditions or buyer execution. If costs or refund history are unavailable, label exposure unknown and request the inputs before approval.

Use only real scarcity. Never invent deadlines, stock counts, resetting countdowns, visitor counts or expiring bonuses. A real limit needs an owner and an enforcement plan.

## Match the business model

- **Services and agency retainers:** define included work, exclusions, handoffs, milestones, review limits and delivery capacity. Prefer a scoped engagement over unlimited access.
- **Courses, coaching and information products:** match delivery to learning and implementation needs. Explain access duration, support limits, refund conditions and any real cohort deadline.
- **Self-serve SaaS:** tier structure, packaging and value metric usually matter more than bonuses. Prepare a pricing-specialist brief before selecting levels or tiers; send missing segment evidence separately to `customer-research`. Do useful offer work now without treating pricing advice as completed research.
- **High-ticket B2B after a demo:** reduce fear of making a mistake. Recommend one option, a conservative evidence-backed business case, a post-signature plan with owners and milestones, and bounded support held in reserve. Preserve genuine capacity limits; avoid deadline discounts for a hesitant buyer. Give the sales owner the objections and evidence needed to design a pilot or buyer conversation.
- **Pilots:** choose a bounded value demonstration when customer data is unnecessary, or a scoped paid integration pilot when data and implementation are required. Define success, duration, owners, fees and any contract credit; leave unsupported values provisional.

## Evidence and claims

- Match each risky claim to supplied demonstrations, product data, customer evidence, references or a transparent process.
- Label supplied observations, calculations with their inputs, assumptions, estimates and unknowns distinctly.
- Never invent testimonials, named customers, savings, expected results or research findings.
- Do not guarantee outcomes controlled by the buyer, a platform or market conditions.
- Use concrete, supported language instead of superlatives or unsupported value claims.
- Have qualified reviewers assess regulated claims before publication.

## Output contract

Return a reviewable brief containing:

1. Segment, buying trigger and current alternative, with evidence or hypothesis labels.
2. Current offer diagnosis and the single primary change recommended.
3. Offer name, one-sentence outcome and mechanism.
4. Included and excluded scope, delivery schedule, owners and buyer responsibilities.
5. Claim-to-proof map, identifying gaps explicitly.
6. Optional bonuses, the objection each resolves and delivery cost or unknowns.
7. Guarantee, eligibility, remedy, refund, cancellation, renewal and usage terms.
8. Real scarcity with evidence and enforcement, or an explicit statement that none is justified.
9. Price/payment proposal, supporting logic and margin/refund exposure caveats.
10. Operational feasibility, remaining decisions and evidence-grounded objection responses.
11. Two or three variants, with one variable changed each, and a test handoff.
12. Concrete handoffs and an explicit request for approval of commercial and delivery terms before live action.

Mark unsupported fields unknown or provisional rather than withholding the whole brief.

## Concrete handoffs

For every adjacent task, name the responsible skill or human specialist, the brief or evidence it receives, and the decision or deliverable it should return. Never claim a skill ran without its output. If unavailable, prepare the brief and state that execution is pending.

| Need | Owner | Send | Expected return |
|------|-------|------|-----------------|
| Missing buyer evidence | `customer-research` | Segment hypothesis, objections, existing evidence and gaps | Validated buyer/segment evidence and unresolved questions |
| SaaS economics | `saas-unit-economics-audit` | Proposed price/terms, costs, support and refund assumptions | Economics assessment and constraints; unknowns retained |
| Delivering onboarding promises | `onboarding-activation` | Outcome, first-value promise, buyer effort and delivery owners | Activation plan, milestones and dependencies |
| Comparing variants | `experiment-design` | Current offer, single-variable variants, hypothesis, metric and constraints | Test design and decision rule |
| Proven recurring promotion | `marketing-loops` | Tested offer, audience, results and delivery constraints | Repeatable promotion plan |
| Price levels, tiers, value metric | Pricing specialist | Buyer evidence, packaging options, costs and current terms | Supported price/packaging recommendation |
| Sales page, email or launch | Copy, email or launch specialist | Approved offer brief, proof and terms | Corresponding draft or launch plan |
| Hesitant B2B buyer or pilot | Sales owner | Buyer objections, proof, implementation risks and constraints | Buyer conversation or bounded pilot proposal |
