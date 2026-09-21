Summary
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training approach for low-resource text classification. It progressively increases augmentation strength during the contrastive stage, moving from token-level perturbations to aggressive back-translation. Evaluated on SST-2, AG News, TREC, and SUBJ with 500 labeled examples each, CurCon improves average accuracy to 88.9, outperforming CERT (87.8), SimCSE (87.3), UDA (86.9), and standard fine-tuning (85.1). Ablations suggest the curriculum schedule contributes around 0.8 points of the average improvement, and gains are larger with fewer labels.

Strengths
- Clear, simple idea that integrates smoothly into the CERT pipeline with no inference overhead.
- Consistent improvements over strong baselines across four datasets and five random seeds; standard deviations are reported.
- Well-motivated curriculum design; ablations (fixed mixture, reversed curriculum, without back-translation) support the claim that curriculum direction and stronger augmentations matter.
- Sensible analysis of label-scarcity regime, showing larger gains with fewer labeled examples.
- Practical details provided (operators, schedule, training regimes), enabling reproduction in principle.

Weaknesses and Concerns
- Fairness of comparisons: CurCon uses grid search over 48 configs, while baselines use hyperparameters from original papers. Re-tuning baselines with the same budget could narrow gaps.
- Scope: Experiments are limited to English, short-text datasets and BERT-base. No evaluation on domain-specific or longer-text datasets, and no larger or decoder-only models.
- Novelty is incremental: curriculum scheduling of augmentation strength is established in vision; here it is an adaptation to text contrastive intermediate training rather than a fundamentally new algorithm.
- The “linear” schedule is implemented via stepwise operator availability and uniform sampling among available operators, which may not strictly correspond to a monotonic increase in augmentation magnitude at the instance level.
- Missing statistical significance testing beyond reporting mean ± std; some per-dataset improvements are close to 1 SD.
- Limited comparison set: no recent prompt-based/few-shot baselines (e.g., PET/LM-BFF) or stronger semi-supervised methods (e.g., FixMatch-style for text, pseudo-labeling with confidence thresholds), which could be competitive around 500 labels.

Suggestions for Improvement
- Re-run baselines with comparable hyperparameter tuning budgets and report compute to strengthen fairness of comparisons.
- Provide a sensitivity study of curriculum length L and operator sampling probabilities; consider a smoothly varying mixture (e.g., weights proportional to c(t)) or magnitude ramps within operators.
- Add significance tests (e.g., paired t-tests across seeds).
- Expand to larger encoders and at least one domain-shifted or long-text dataset; consider multilingual evaluations to test dependence on MT/WordNet quality.
- Compare against modern prompt-based/few-shot and semi-supervised baselines adapted to 100–1,000 label regimes.

Reproducibility
- Positive: Clear description of operators, schedule, training steps, batch sizes, optimizer, and seeds; uses standard datasets.
- Missing: Exact hyperparameter grids per dataset, code availability, details for MT system/back-translation implementation, and tokenization specifics for span deletion.

Ethical/Practical Considerations
- Back-translation and WordNet-based augmentation quality may vary across domains and languages; potential biases introduced by MT systems should be considered if extending beyond English.

Scores (0–100)
- Soundness: 84
- Novelty: 72
- Significance: 78
- Clarity: 88

Final average score: 80.5

Final recommendation: Accept