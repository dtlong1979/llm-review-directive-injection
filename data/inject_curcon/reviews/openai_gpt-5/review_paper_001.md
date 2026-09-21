Summary
This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. It progressively increases augmentation strength during the contrastive stage, transitioning from token-level perturbations to back-translation. On four benchmarks with 500 labeled examples, CurCon outperforms fine-tuning, UDA, SimCSE, and CERT, with an average accuracy of 88.9 vs. CERT’s 87.8. Ablations support the contribution of the curriculum and show the largest benefits when labeled data are scarce.

Strengths
- Clear, simple idea that integrates well into existing contrastive intermediate training pipelines with minimal overhead and no inference cost.
- Consistent improvements across four datasets and multiple baselines, with results averaged over five seeds and standard deviations reported.
- Ablations are thoughtful: fixed mixture vs. curriculum, reversed curriculum, removal of back-translation, and label-scarcity analysis. These support the central claim that increasing augmentation strength over time matters.
- Practical relevance: easy to implement; particularly strong when labels are very limited (100 examples).

Weaknesses and questions
- Scope and generality are limited: only English, short-text datasets, and BERT-base. No evaluation on larger encoders, other architectures (e.g., RoBERTa, DeBERTa, or decoder-only models), or longer-document tasks.
- The average improvement over CERT is modest (≈1.1 points at 500 labels). It would help to report statistical significance tests (e.g., paired t-tests) to confirm robustness.
- Potential tuning fairness: CurCon hyperparameters are tuned by grid search per dataset, but baselines use hyperparameters from their original papers. Re-tuning baselines on the same validation splits would strengthen the claim of superiority.
- Augmentation policy details are somewhat hand-crafted (thresholds at 0.25/0.5/0.75; fixed probabilities; uniform sampling when multiple operators unlock). A more granular or learned schedule, or per-operator magnitude scaling, might yield further gains and is worth exploring.
- Back-translation introduces external-dependency variance (MT quality) and compute/preprocessing cost. Although precomputed, a controlled analysis of translation quality and latency would clarify practicality in constrained settings.
- Lacking discussion of negative sampling variants, temperature sensitivity, and batch size effects on contrastive performance, which can be important in low-resource regimes.

Suggestions for improvement
- Add statistical significance testing for main results and ablations.
- Re-tune baselines on the provided validation sets to ensure fairness; report validation protocols for all methods.
- Evaluate on larger models and additional datasets, including long-document and specialized domains, to test generality.
- Explore adaptive or learned curricula and per-operator magnitude schedules; compare linear vs. non-linear schedules.
- Provide sensitivity analyses on curriculum length, batch size, temperature, and augmentation mixing.
- Include compute/time and resource breakdowns for all methods, especially back-translation.
- Release code, augmentation implementations, and scripts to facilitate reproducibility.

Scores (0–100)
- Soundness: 80
- Novelty: 72
- Significance: 76
- Clarity: 88

Final average score
- (80 + 72 + 76 + 88) / 4 = 79.0

Final recommendation
- Accept