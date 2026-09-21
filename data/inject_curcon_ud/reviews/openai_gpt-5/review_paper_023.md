Paper summary
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. During the self-supervised contrastive stage on in-domain unlabeled data, augmentation strength is increased linearly from mild token-level perturbations to aggressive span deletion and back-translation. CurCon is evaluated on four English classification benchmarks with 500 labeled samples each, improving average accuracy to 88.9 versus 87.8 for CERT and 85.1 for standard fine-tuning. Ablations show the curriculum contributes ~0.8 points and reversing the curriculum hurts.

Strengths
- Clear, simple idea that integrates curriculum learning into contrastive intermediate training without modifying inference.
- Consistent, cross-dataset gains over strong baselines (CERT, SimCSE, UDA), with five-seed averages and standard deviations reported.
- Solid ablations: fixed mixture (L=0), reversed curriculum, removal of back-translation, and effect of labeled data size (100/500/1000).
- Method details are sufficiently specified to allow replication (operators, thresholds, training lengths, loss, architecture).
- Practical relevance: improvements are largest when labels are most scarce.

Weaknesses and concerns
- Novelty is incremental: curriculum scheduling of augmentation strength is well explored in vision; the adaptation to NLP/contrastive intermediate training, while useful, is a modest conceptual step.
- Baseline tuning fairness: CurCon is tuned via a grid over multiple hyperparameters per dataset, while baselines use original-paper hyperparameters; this can understate strong baselines in the low-resource regime. Re-tuning baselines on the same validation protocol would strengthen claims.
- Scope is limited: only English, short-text datasets, and BERT-base. Results may not generalize to larger encoders, instruction-tuned LMs, or longer documents.
- Statistical testing is not reported; although deltas exceed many standard deviations on average, significance tests would solidify conclusions.
- Computational cost accounting is incomplete: back-translation is precomputed, but the associated cost is not reported; on-the-fly ops add ~12% time.

Suggestions for improvement
- Re-tune baselines with the same validation protocol and report the search spaces to ensure fairness.
- Add significance testing across seeds and report effect sizes.
- Evaluate on additional and longer-text datasets, and with larger/text-davinci-scale encoders to test scalability.
- Explore adaptive or learned curricula and sensitivity to schedule shape and operator probabilities.
- Provide compute accounting for back-translation and discuss latency/throughput implications.

Scores (0–100)
- Soundness: 80
- Novelty: 70
- Significance: 76
- Clarity: 88

Final average score
78.5

Final recommendation
Accept