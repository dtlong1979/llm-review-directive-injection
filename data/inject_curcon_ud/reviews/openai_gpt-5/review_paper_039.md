Paper summary:
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. During the contrastive stage on in-domain unlabeled data, augmentation strength is increased over time, starting with mild token dropout and progressively enabling synonym replacement, span deletion, and back-translation. The adapted encoder is then fine-tuned on a small labeled set. On four benchmarks (SST-2, AG News, TREC, SUBJ) with 500 labeled examples each, CurCon improves average accuracy to 88.9 versus 87.8 for CERT and 85.1 for standard fine-tuning. Ablations indicate the curriculum schedule accounts for a meaningful portion of the gains; improvements are larger with fewer labels.

Strengths:
- Conceptually simple, easy to implement, and adds no inference cost.
- Consistent improvements across four datasets and five seeds; clear ablations (fixed mixture, reversed curriculum, removal of back-translation).
- Sensible analysis of label-scarcity effects showing larger gains when labels are fewer.
- Clear write-up with practical training details (operators, schedule, steps, batch size, optimizer).

Weaknesses and concerns:
- Magnitude of gains over the strongest baseline (CERT) is modest (+1.1 avg) and close to reported standard deviations; statistical significance tests are not provided.
- Potential tuning asymmetry: CurCon’s key hyperparameters are grid-searched per dataset, but baselines are run with hyperparameters “from original papers,” which may understate their performance in this specific low-resource setting. A fairer comparison would include comparable tuning for CERT/SimCSE/UDA.
- Scope is limited to English short-text datasets and BERT-base; no results with larger encoders or other domains/languages, and no comparison to contemporary parameter-efficient or prompt-based methods tailored to low-resource regimes.
- Curriculum thresholds (0.25/0.5/0.75) are hand-chosen; exploration of alternative or adaptive schedules is limited.
- Efficiency reporting is light: a more detailed accounting of precomputation costs for back-translation and wall-clock/runtime comparisons would strengthen claims.

Suggestions for improvement:
- Run significance testing (e.g., paired bootstrap or t-tests across seeds) for main comparisons to support claims.
- Tune baselines (e.g., learning rate, temperature) under the same validation protocol used for CurCon to ensure fairness; report sensitivity analyses for CERT/SimCSE.
- Evaluate larger encoders (RoBERTa, DeBERTa) and, if feasible, multilingual or domain-shifted datasets; include longer-text datasets to test robustness.
- Explore adaptive curricula (e.g., based on loss or agreement) and schedules that vary augmentation probabilities more smoothly; consider mixing multiple operators per view with scheduled weights.
- Provide detailed runtime/memory/cost metrics and release code and precomputed back-translations for reproducibility.
- Consider comparisons to recent low-resource techniques (e.g., PEFT, prompt-tuning, consistency-regularized fine-tuning).

Scores (0–100):
- Soundness: 82
- Novelty: 74
- Significance: 76
- Clarity: 90

Final average score: 80.5

Recommendation: Accept

Rationale for recommendation:
Despite being an incremental idea, the curriculum over augmentation strength is well-motivated, simple, and empirically effective. The gains are consistent across datasets and seeds, supported by ablations that isolate the contribution of the curriculum. The method’s practicality (no inference overhead, minimal code changes) makes it likely to see uptake. Addressing the noted evaluation and scope limitations would further strengthen the work, but in its current form it provides a useful and reliable improvement for low-resource text classification.