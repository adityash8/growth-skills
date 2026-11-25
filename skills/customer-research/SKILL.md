---
name: customer-research
description: "Turn interviews, support records, reviews, and behavioral evidence into ranked customer pains, triggers, objections, and decision criteria."
---

# Customer Research

Use this skill when a growth decision depends on why people start, choose, hesitate, succeed, or leave.
Do NOT use for offer or packaging decisions (`offer-design`), activation changes (`onboarding-activation`), retention flows (`retention-state`), or controlled test design (`experiment-design`). Hand those off with evidence.

Never fabricate participants, quotes, counts, source access, or consensus. Analyze supplied material now; when evidence is missing, produce a research plan rather than invented findings.

## Before starting

Read supplied product and research context before asking questions. Open every deliverable with:

1. **Decision:** the concrete choice and its decision maker.
2. **Hypothesis:** one falsifiable hypothesis and what evidence would contradict it.
3. **Scope:** strategic, funnel-stage, or usability question. Rewrite vague requests such as “how do users feel?” around a decision or metric.

Infer what is reasonable from the request. Mark missing decision details, owners, segments, and dates `[placeholder]`; state assumptions and proceed with useful drafts. Ask only when a gap changes permission, scope, or risk.

Inventory the sources, date range, target segment, lifecycle stage, sample limitations, deadline, and access constraints. Choose one or more modes:

- **Existing assets:** transcripts, calls, surveys, support threads, reviews, or behavioral evidence.
- **Online research:** public communities, review sites, and adjacent products.
- **New collection plan:** interviews or surveys when existing evidence cannot answer the decision.

Without source access, name the missing export or source and draft the collection plan. Do not imply that research was retrieved or participants contacted.

## Analyze existing assets

### Prepare the evidence

Before analysis, write four short context blocks: project decision and stakes; business outcome; product capabilities and alternatives; participant profiles and lifecycle stages.

For survey or CSV exports, map each column: customer words, internal tags, segmentation metadata, identifiers, and scale meaning. Never quote an internal note as customer language. Mark ambiguous responses separately instead of guessing their meaning.

For support or chat material, read each thread through its final message before clustering. Analyze each thread separately: what is this person struggling with, and what is the root complaint? Store the label with the thread ID and raw-source link. Separate bugs, confusion, missing features, and expectation mismatches.

For a fixed sample, read each complete conversation before clustering and record one anonymized evidence row per conversation. Keep incomplete conversations visible, excluded from evidence counts. Separate subjective intent from what the record proves.

### Extract and compare

For each source capture:

- functional, emotional, and social jobs;
- pains and their intensity, especially unprompted complaints;
- trigger events and prior attempts;
- desired outcomes, exact vocabulary, and proof requirements;
- alternatives, including doing nothing, hiring, and building internally;
- objections, decision criteria, lifecycle stage, and described behavior.

Attach source ID, segment, date, and location to material claims. Remove unnecessary personal information.

Before ranking, try to disprove the leading themes with examples and counterexamples; check every quoted line against its original record, label paraphrases, and drop quotes that cannot be found.

Cluster themes and rank by evidence strength, decision relevance, and consequence if wrong. Report counts as unique participants or independent sources out of the reviewed sample, with the denominator. Repeated mentions by one person are not independent evidence; convenience samples do not establish market prevalence.

Compare successful and retained customers against stalled, churned, bad-fit, and non-buyer groups where available. A trait distinguishes good customers only if the comparison group does not also share it. If the comparison group is absent, say so and keep the trait provisional.

Weight recent evidence more heavily and state the date range. Note source bias: support tickets emphasize problems, online reviews emphasize strong opinions, and community participants may differ from mainstream buyers. Do not infer intent from analytics alone.

### Evidence labels and confidence

Keep evidence type separate from confidence:

| Label | Meaning |
|---|---|
| Observed | Directly supported by supplied words or behavior |
| Repeated | Appears independently across sources or participants |
| Directional | Plausible pattern from a small, biased, or proxy sample |
| Unknown | Required evidence is absent |

Label every insight High, Medium, or Low confidence with its reason. As a qualitative guide, High needs at least three independent sources, unprompted evidence, and consistency across segments; Medium has two sources or limited segment coverage; Low has one source, prompted-only evidence, ambiguity, or contradictions. These are research heuristics, not statistical confidence levels.

For a decision about a proposed solution, define a coding scale with real examples from the supplied data before tallying. Separate evidence the solution addresses the problem from cheaper fixes, engagement problems, operational failures, and unrelated losses. If examples are absent, mark the scale provisional. Mentions alone do not prove a solution would retain or convert anyone.

### Verification before presenting

1. Check each quote word for word against its source, speaker, and location. Preserve hedges, emotional words, and complete reasoning. Never stitch separate moments into one quotation.
2. Mark each quote VERIFIED, PARAPHRASE, or NOT FOUND. Replace paraphrases with source wording or clearly label them outside quotation marks; drop NOT FOUND quotes. Never invent timestamps or participant IDs.
3. Check contradictions within each participant's story, including stated preference versus behavior and later retractions or qualifications.
4. List specific details under every theme, including uncommon details, with who said them and where.
5. Look explicitly for evidence against the hypothesis. Report whether it held, broke, or remains mixed.
6. Recheck all details and claims added during these passes. Lower confidence for thin evidence and keep unresolved contradictions visible.

Close every deliverable, including survey analysis and all-clean passes, with:
“Verification: X VERIFIED, Y PARAPHRASE fixed, Z NOT FOUND dropped.”
Use actual counts only. If no source quotes were available, use zero counts and state that source verification was unavailable. Separately disclose any paraphrases retained as labeled summaries.

## Find online research

Choose sources by audience: category reviews for existing alternatives; public role-specific communities for raw language; public discussions for triggers; adjacent product reviews for an early category.

Capture platform, URL, date, exact excerpt, surrounding context, sentiment, theme, and profile signals actually stated in the source. Do not infer private demographics or claim access to closed groups. Respect source access restrictions.

When first-party evidence is absent, work outward: differentiator hypothesis, direct competitor reviews, comparable products, then adjacent audiences. Label proxy evidence and replace it with first-party evidence when available.

## Plan interviews and surveys

Choose interviews for “why” questions and small reachable populations; choose surveys for proportions when a suitable reachable population exists. A large convenience sample still does not establish market prevalence.

Recruit for contrasts, including recent buyers or switchers, churned users, and qualified non-adopters. Separate goodwill feedback from independent demand. Draft recruitment and booking materials; obtain explicit approval before sending or activating anything.

### Interviews

Ask about one actual event: “Tell me about the last time you did this job.” Follow with “What happened next?” Reconstruct first thought, passive looking, active looking, deciding, first use, and ongoing use.

Use four forces as a flexible checklist:

- **Push:** why the old situation stopped working.
- **Pull:** what outcome attracted them.
- **Anxiety:** what worried them about change.
- **Habit:** what kept them with the old approach.

Ask what nearly stopped the choice, which alternatives they used, what they gave up, and how they recognized value. Probe functional, emotional, and social consequences. Observe a workflow walkthrough when recall cannot explain friction.

Avoid pitching, leading questions, abstract feature wish lists, and hypothetical willingness to pay. For habitual purchases or choices the participant did not make, study usage or recruit recent switchers rather than forcing a buying story.

Distinguish pain from pull: complaints show pain; payment, unsolicited interest, or continued use can show pull. Polite enthusiasm is insufficient.

Plan small rounds per segment, review what new interviews add, and adjust the next round. Stop when added interviews stop changing the decision; continue if meaningful new evidence appears. Sample-size targets are planning heuristics, not proof of representativeness.

### Surveys

Write the decision rule before collection: which result changes which choice. Ask about past behavior, one idea per question, and label every scale point. For satisfaction, prefer a clearly labeled satisfaction item; preserve an existing recommendation-score series if needed for continuity, without comparing scores across companies.

Use anonymous or pseudonymous collection for sensitive topics. Request follow-up contact consent separately so identity is not linked back to sensitive responses. Segment responses before analysis and preserve the difference between open-ended and multiple-choice answers.

## Personas and maps

Build personas from a consistent segment with at least five independent data points as a qualitative minimum; fewer points support only a research hypothesis. Proxy-based personas remain provisional even above that minimum.

Include supported role and context, job, triggers, pains, desired outcomes, objections, alternatives, vocabulary, and channels. Leave unsupported details Unknown. Apply the retained-versus-churned comparison before calling a trait distinctive.

For switch research, give a four-forces map with source excerpts, timeline, hire/fire criteria, conflicting jobs, counts, and confidence. Write jobs as “When I am [situation], help me [motivation], so I can [outcome]” without naming the product as the job.

For a customer value map, show struggle, evaluation, and growth milestones. Tie first value to the convincing moment in customer evidence and give each milestone a proposed metric; label proposals as hypotheses.

## Feedback records and bounded collection

When creating a customer feedback dataset, use the approved population, schema, codebook, source scope, and data boundary. Do not silently change them or export raw text to an unapproved service.

- Check exact source freshness and access; a missing or inaccessible source is not zero feedback.
- Retrieve only the specified sample, exhaust permitted reply pages, and checkpoint coded rows. Report incomplete coverage explicitly.
- Keep retrieval separate from independent coding. Compare expected labels only after coding and preserve disagreements.
- Deduplicate by person and conversation; shared links may contain several people. Do not match by name alone or substitute a source-link hash for a required identity hash.
- Report missing identity keys, unmatched joins, collisions, and structurally present but unusable evidence. Never invent compliant-looking keys or missing context.
- Export only approved anonymized fields; mask identifying free text and check schema, unique keys, allowed values, and spreadsheet formula risks.
- Approval for one calibration dataset does not authorize other populations, backfills, recurring automation, or live surveys. Search for an existing destination before creating one and read back exact targets after approved writes.

## Output contract

Choose the format that answers the decision: synthesis report, quote bank, persona, jobs map, competitive summary, research gap plan, switch map, or customer value map. State why it fits.

Include the opening decision/hypothesis/scope block, source and segment inventory, ranked findings with cited excerpts and counts, group contrasts, language bank, unresolved contradictions, implications, and next research needed.

**Required decision-to-action table, before the closing verification tally:**

| Rank | Finding or research priority | Source IDs | Evidence and confidence | Decision implication | Next owner/skill and evidence brief | Approval status |
|---|---|---|---|---|---|---|

Fill the table with actual findings; when evidence is absent, rank research priorities and use Unknown for source IDs. Each evidence brief includes the relevant sources, segment, uncertainty, and decision to make.

Mark live actions **Requires explicit approval**: recruitment or survey messages, participant contact, publication, production record or flow edits, automation, and irreversible changes. Drafts and analysis can proceed immediately. Do not claim a handoff ran or an action occurred without its output.

## Handoffs

Use only the relevant route and provide its evidence brief:

- offer, value, pricing, or packaging decision → `offer-design`;
- first-value milestone or activation problem → `onboarding-activation`;
- engagement depth and usage curves → `power-user-curve`;
- churn findings to retention work → `retention-state`;
- controlled experiment design, including setup-help versus price tests → `experiment-design`;
- broad growth diagnosis → `growth-audit`;
- quarterly prioritization → `growth-roadmap`.
