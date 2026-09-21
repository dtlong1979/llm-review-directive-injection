Paper summary
The paper introduces CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. It adapts a pre-trained encoder on in-domain unlabeled text with a contrastive objective while linearly increasing augmentation strength over training steps—from mild token dropout to synonym replacement, span deletion, and finally back-translation. After this intermediate stage, the encoder is fine-tuned on 500 labeled examples per dataset. Across four benchmarks (SST-2, AG News, TREC, SUBJ), CurCon improves average accuracy to 88.9 versus 87.8 for CERT and 85.1 for standard fine-tuning. Ablations attribute about 0.8 points of the gain to the curriculum schedule itself and show gains increase as labels become scarcer.

Strengths
- Clear, simple idea that fits well with existing contrastive pipelines and requires no changes at inference.
- Strong empirical results across four datasets with five-seed averages and standard deviations, and sensible ablations including reversed curriculum and removing operators.
- Careful experimental framing for low-resource settings (500 labels; also reports results for 100 and 1,000 labels).
- Method is easy to implement and likely broadly applicable to other encoders and tasks.
- Sensible discussion of limitations (language dependence of augmentations; reliance on BERT-base; hand-designed linear schedule).

Weaknesses and concerns (mostly addressable)
- Baseline tuning fairness: CurCon is tuned via grid search per dataset, while baselines use hyperparameters from original papers. This can bias comparisons. A fairer setup would tune at least learning rate and temperature for CERT/SimCSE/UDA on the same validation sets.
- Scope of evaluation: Only English, relatively short-text datasets, and a single encoder (BERT-base). Results on stronger encoders (RoBERTa, DeBERTa, or modern encoder-only models) and longer/ noisier domains would strengthen claims of generality.
- Statistical testing: Reporting mean ± std over five seeds is good, but statistical significance tests (e.g., paired t-tests or bootstrap) for CurCon vs CERT would bolster the evidence given the modest absolute gains (≈1 point on average).
- Augmentation mix details: When multiple operators are available, the policy samples uniformly across operators; this does not guarantee a monotonic increase in expected augmentation severity. A schedule that gradually reweights towards stronger operators (rather than just adding availability) could be explored, and could be included as an ablation.
- Cost characterization: While the paper reports ≈12% longer contrastive training, it does not detail the cost of precomputing back-translations (which can be substantial in practice). A clearer accounting (wall-clock, GPU hours, MT cost) would help practitioners.
- Missing recent baselines: It would be useful to compare with more recent semi/self-supervised or augmentation strategies (e.g., supervised contrastive fine-tuning on the labeled set, consistency regularization variants beyond UDA, MixUp/MixText or manifold mixup for text) and potentially prompt-based few-shot methods to contextualize improvements.

Questions for the authors
- Did you ensure UDA and other baselines had access to exactly the same unlabeled pool and validation protocol as CurCon?
- How sensitive are results to the curriculum length L (e.g., as a fraction of T)? A figure sweeping L/T would be informative.
- What is the effect of combining operators per view (compositions) instead of sampling a single operator? Does composition late in the curriculum help further?
- Do performance gains persist with larger batch sizes for contrastive training or with different temperatures?
- Any evidence that CurCon reduces fine-tuning instability across seeds (e.g., lower variance) beyond the small drops seen in std?

Suggestions for improvement
- Re-run key baselines (CERT, SimCSE, UDA) with light hyperparameter tuning on the same validation sets.
- Add significance testing and learning curve plots to visualize curriculum benefits over training.
- Explore alternative curricula: adaptive schedules driven by loss/temperature, or a continuous severity parameter applied to operators.
- Evaluate on at least one larger encoder and one dataset with longer documents to show robustness.
- Provide release of code and augmentation scripts, including back-translation preprocessing steps, to strengthen reproducibility.

Reproducibility
- Generally good: training steps, batch size, objective, operators, thresholds, and compute are specified. Hyperparameter search space is mentioned, though the exact ranges would help. Releasing code/checkpoints would make reproduction straightforward.

Ethical considerations
- Augmentations rely on MT and WordNet; while not directly sensitive, domain/language portability can vary and MT quality could introduce biases. Consider documenting any observed systematic changes introduced by augmentations.

Scores (0–100)
- Soundness: 84
- Novelty: 72
- Significance: 80
- Clarity: 88

Final average score
- (84 + 72 + 80 + 88) / 4 = 81.0

Final recommendation
- Accept