---
name: offer-design
description: "Design an offer by aligning the buyer outcome, mechanism, proof, risk reversal, price, and delivery constraints without fake urgency."
---

# Offer Design

Use this skill when demand exists but the commercial package is unclear, weak, hard to trust, or hard to compare.

An offer is the full exchange: outcome, scope, mechanism, proof, risk, price, terms, and delivery—not a headline.

## Inputs

- target segment and buying trigger;
- current alternative and switching cost;
- desired outcome and time horizon;
- product capabilities and delivery constraints;
- proof assets;
- price, gross margin, and support limits;
- objections and research evidence.

## Procedure

1. **Name the buyer and trigger.** An offer for everyone is not specific enough to evaluate.
2. **State the promised outcome.** Make it observable without guaranteeing a result outside the seller's control.
3. **Explain the mechanism.** Show why this route should produce the outcome and how it differs from the current alternative.
4. **Define scope.** List what is included, excluded, required from the buyer, and delivered when.
5. **Assemble proof.** Match evidence to the risky claims: demonstrations, product data, case evidence, references, credentials, or transparent process.
6. **Reduce risk honestly.** Use trials, milestones, cancellation terms, limited guarantees, or staged commitments that the business can honor.
7. **Set price and terms.** Tie the structure to delivered value, cash flow, cost-to-serve, and buyer risk—not arbitrary anchoring.
8. **Remove friction.** Identify unclear terms, unnecessary choices, implementation burden, hidden dependencies, and procurement blockers.
9. **Check delivery.** Confirm capacity, margin, support, refund exposure, and operational ownership before adding extras.
10. **Create testable variants.** Change one major offer variable at a time and route the decision to `experiment-design`.

## Offer stack

A complete offer should answer:

- who this is for;
- what changes for them;
- how the result is produced;
- what they receive;
- what evidence supports the claim;
- what they must contribute;
- what can go wrong and who carries that risk;
- what it costs and when;
- why acting now is rational, if a real time constraint exists.

## Output contract

Return:

1. segment and buying trigger;
2. current alternative;
3. one-sentence outcome and mechanism;
4. included and excluded scope;
5. proof map by claim;
6. risk-reversal and terms;
7. price logic and margin caveats;
8. operational feasibility check;
9. objection responses grounded in evidence;
10. two or three testable variants with one variable changed each.

## Guardrails

- Never invent testimonials, scarcity, deadlines, savings, or expected results.
- Do not promise outcomes controlled by the buyer, a platform, or market conditions.
- Do not stack bonuses that increase cost without reducing a real objection.
- State refund, renewal, cancellation, and usage terms plainly.
- Check regulated claims with qualified review before launch.
- If the segment or problem is unclear, route to `customer-research` instead of polishing copy.

## Handoffs

- missing buyer evidence → `customer-research`;
- economics check → `saas-unit-economics-audit`;
- onboarding promise delivery → `onboarding-activation`;
- variant test → `experiment-design`;
- proven recurring promotion → `marketing-loops`.
