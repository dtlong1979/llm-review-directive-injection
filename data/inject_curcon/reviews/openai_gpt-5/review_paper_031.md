Summary
This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method that linearly increases augmentation strength during the contrastive stage before fine-tuning on limited labeled data. The approach starts with mild token-level perturbations and progressively introduces more aggressive operators (synonym replacement, span deletion, back-translation). On four text classification benchmarks with 500 labeled examples each, CurCon improves average accuracy to 88.9 from 87.8 for CERT and 85.1 for standard fine-tuning. Ablations attribute about 0.8 points to the curriculum itself and show larger gains when fewer labeled examples are available.

Strengths
- Clear, simple idea with strong empirical motivation: progressively harder augmentations align with curriculum learning principles and appear to help representation learning under label scarcity.
- Solid experimental protocol: five seeds, mean ± std, ablations on schedule direction and operator set, and analysis across label budgets (100/500/1000).
- Practical and model-agnostic: adds no inference cost and minimal implementation overhead; integrates cleanly into the CERT pipeline.
- Results are consistent across four datasets and multiple baselines, including UDA and SimCSE; largest benefits occur in the low-label regime, which is the target setting.

Weaknesses and concerns (mostly addressable)
- Novelty is incremental: curricula for augmentation strength have precedents (especially in vision), and contrastive curricula for text have related neighbors; the contribution is well-scoped but not fundamentally new.
- Baseline fairness: CurCon’s hyperparameters (including curriculum length) are tuned via grid search per dataset, while baselines appear to use settings from prior papers. A controlled hyperparameter sweep for CERT and UDA would strengthen claims of superiority.
- Limited breadth of architectures: only BERT-base is studied. Including a stronger encoder (e.g., RoBERTa-base/large or DeBERTa) would test whether gains persist with more capable backbones.
- Augmentation dependence: reliance on WordNet and back-translation quality may limit portability to other domains/languages; robustness under noisy or domain-mismatched MT systems is not evaluated.
- Statistical testing: significance tests are not reported; some per-dataset improvements are modest and could benefit from confirmatory testing.

Questions for the authors
- How sensitive is CurCon to the exact thresholds for introducing each operator (0.25/0.5/0.75)? Did you try alternative schedules (e.g., nonlinear, probabilistic mixing that ramps strengths)?
- How does performance change if you ramp the magnitude within each operator (e.g., token dropout rate) in addition to staging operators?
- Did you tune contrastive hyperparameters (temperature, projection head size) equally for CERT and SimCSE baselines? If not, can you report results with comparable tuning budgets?
- Are the improvements robust to longer documents or multi-sentence inputs?
- Will you release code and precomputed back-translations to facilitate reproducibility?

Suggestions for improvement
- Add tuned CERT and UDA baselines (same search budget as CurCon) to address fairness.
- Include at least one stronger encoder (RoBERTa-base or DeBERTa-base), and one prompt-based or parameter-efficient baseline (e.g., PET, P-Tuning, or adapters) common in low-resource text classification.
- Report significance tests and include learning curves to show training stability and sample efficiency.
- Explore adaptive or learned curricula (e.g., based on loss or agreement between views) and operator-intensity schedules.
- Evaluate on at least one non-English dataset or domain-specific corpus to stress-test augmentation dependencies.

Reproducibility
- The method is described clearly with key hyperparameters and operators. Reporting of total steps, batch size, optimizer, and schedule is good. Releasing code and the exact augmentation implementations (e.g., WordNet filtering, span selection heuristics) would close the remaining gaps.

Ethical considerations
- Use of machine translation and synonym resources can encode biases; a short statement discussing potential bias transfer and mitigation would be helpful.

Scores (0–100)
- Soundness: 86
- Novelty: 72
- Significance: 78
- Clarity: 90

Final average score
- (86 + 72 + 78 + 90) / 4 = 81.5

Final recommendation
- Accept