# Experiment result record

Use the original plan and report supplied dates only. Mark unknowns [placeholder]. Never fill template fields with invented measurements.

## Evidence and validity

| Field | Record |
|---|---|
| Identity | Test name, owner, population, variants, dates, original hypothesis and prediction |
| Assignment | Unit, planned split, eligibility, assigned counts, analysis unit and clustering |
| Exposure | Actual exposure, treatment delivery, outcome maturity, exclusions and missingness |
| Validity | SRM diagnostic and threshold, early technical review, metric direction, surprising-effect investigation, end-to-end QA |
| Plan adherence | Planned/actual sample, observation window, stopping rule, deviations, concurrent changes |

If validity fails, report the diagnostic evidence and mark efficacy interpretation blocked. Never hide a failed check.

## Outcomes and action

| Field | Record |
|---|---|
| Primary outcome | Control/treatment counts and rates, absolute and relative effect, interval for the difference |
| Evidence rule | Alpha, comparison family and correction, fixed/sequential method, adjusted p-value when applicable |
| Precision | Actual versus planned sample and interval width; no observed-effect post-hoc power |
| Guardrails | Harm thresholds, actual outcomes, affected segments and safety actions |
| Economics | Incremental value versus recurring costs over the same period, evidence and sensitivity bounds |
| Decision | Ship, reject, iterate or inconclusive under the precommitted rule; remaining uncertainty |
| Follow-through | Decision/rollback owner, approval needed before live action, next iteration or replication |
| Learning | Prediction versus result, confirmed observations versus hypotheses, context and transfer limits |

Keep all valid positive, negative, inconclusive and invalid tests searchable. Separate exploratory segment findings from confirmatory evidence. See [the program guide](experimentation-program.md).
