Summary
- The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training approach for low-resource text classification. It linearly increases augmentation strength during the contrastive stage, moving from token dropout to synonym replacement, span deletion, and back-translation. On four short-text benchmarks with 500 labels, CurCon improves average accuracy by 1.1 points over CERT and 3.8 over standard fine-tuning. Ablations attribute roughly 0.8 points to the curriculum itself and show largest gains with fewer labels.

Strengths
- Clear, simple idea with a well-motivated intuition (harder augmentations later).
- Consistent improvements over multiple baselines across four datasets; results averaged over five seeds with std reported.
- Useful ablations, including reversed curriculum and removal of back-translation.
- Practical, easy-to-implement extension of existing pipelines; no inference overhead.

Weaknesses
- Fairness of comparisons: CurCon is tuned via grid search per dataset, but baselines use hyperparameters from original papers, likely disadvantaging them. A stronger study would tune baselines under the same budget.
- Modest absolute gains vs. CERT (1.1 points average), with only four relatively easy, short-text benchmarks; limited evidence of broad impact.
- Limited scope: only BERT-base, only English, no larger encoders or decoder-only models, and no modern semi-/self-supervised or prompt-based baselines beyond UDA/SimCSE/CERT.
- Hand-designed linear schedule without exploration of alternative schedules or adaptive policies beyond a single hyperparameter L.
- Lacks significance testing and more detailed reporting on unlabeled data size, cost of back-translation generation, and sensitivity to augmentation choices.

Questions/clarifications
- How large is the unlabeled pool per dataset, and how sensitive are gains to its size?
- Are improvements still consistent if baselines receive matched hyperparameter tuning?
- How does CurCon perform with stronger backbones (e.g., RoBERTa-large, DeBERTa) or encoder-decoder models?
- Any analysis of representation quality (e.g., probing, retrieval) to support the contrastive objective’s benefits?

Scores (0–100)
- Soundness: 78
- Novelty: 62
- Significance: 65
- Clarity: 88

Final average score
- (78 + 62 + 65 + 88) / 4 = 73.25

Recommendation
- Reject (borderline). The idea is sensible and clearly presented with consistent but modest gains. However, the limited novelty, narrow empirical scope, and potential fairness issues in baseline tuning reduce confidence in impact for a competitive venue. Strengthening comparisons, widening benchmarks and model backbones, and exploring adaptive or learned curricula would improve the case for acceptance.