Here is my review.

Summary
- The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method that linearly increases augmentation strength during the contrastive stage (from token dropout to synonym replacement, span deletion, and finally back-translation). It is applied before fine-tuning in low-resource text classification settings.
- On four benchmarks with 500 labeled examples (SST-2, AG News, TREC, SUBJ), CurCon improves average accuracy to 88.9 vs. 87.8 for CERT and 85.1 for direct fine-tuning. Gains are consistent across datasets.
- Ablations suggest the curriculum contributes about 0.8 points on average; reversing the curriculum hurts, and the gains are larger with fewer labels.

Strengths
- Simple, practical idea that integrates smoothly into a widely used pipeline (CERT) and adds no inference-time cost.
- Consistent improvements across four datasets and multiple baselines, with clear reporting of mean and standard deviation over five seeds.
- Ablation studies and a label-scarcity analysis provide evidence that the curriculum itself matters and clarifies where gains come from.
- Clear description of the training pipeline, augmentation operators, and curriculum schedule; implementation details are sufficient to replicate the setup.

Weaknesses and concerns
- Fairness of baseline tuning: CurCon is tuned via grid search per dataset, whereas baselines are run with hyperparameters from prior papers. This likely disadvantages baselines in the low-resource and in-domain settings considered. A matched tuning budget for baselines (or a development of default but strong settings for each) would strengthen the claims.
- Scope is narrow: four English datasets of short texts and a single encoder (BERT-base). The paper does not test larger or more recent encoders (e.g., RoBERTa, DeBERTa), multilingual settings, or domain-shifted datasets. This limits the generality of the conclusions.
- Statistical testing is not reported. Given standard deviations, some per-dataset gains may be within one SD; significance tests would help substantiate the improvements.
- The schedule is hand-crafted (fixed thresholds and linear progression). An analysis of sensitivity to schedule shape, operator probabilities, or an adaptive schedule would be informative.
- Limited analysis of augmentation quality and label preservation (e.g., synonym replacement or span deletion might occasionally alter class semantics). An error analysis would help.
- Compute reporting could be expanded: absolute wall-clock times, precomputation cost for back-translation, and memory footprint.

Suggestions for improvement
- Tune baselines under the same search space and report results; or include a “best-effort” reimplementation of baselines under the low-resource protocol used here.
- Add experiments with stronger encoders and additional datasets (including longer texts and domain-specific corpora), and consider multilingual evaluation.
- Report statistical significance tests and confidence intervals.
- Explore alternative curricula (nonlinear schedules, learned/adaptive difficulty), operator mixing probabilities, and sensitivity to curriculum length L.
- Analyze the impact of unlabeled data size and quality, and provide a qualitative error analysis of augmentations that may not be label-preserving.

Scores (0–100)
- Soundness: 78
- Novelty: 68
- Significance: 72
- Clarity: 88

Final average score: 76.5

Final recommendation: Accept