# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary
The paper proposes CurCon, a curriculum-scheduled extension of contrastive intermediate training (in the spirit of CERT) for low-resource text classification. Instead of applying a fixed augmentation policy throughout contrastive pretraining, CurCon linearly increases augmentation difficulty—from token dropout to synonym replacement, span deletion, and finally back-translation—governed by a single curriculum-length hyperparameter. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT, with ablations isolating the curriculum's contribution and an analysis across label budgets.

## Strengths
- The core idea—coupling curriculum learning with augmentation strength in contrastive intermediate training—is a sensible and clearly motivated extension of existing work (CERT, SimCSE), and the implementation is lightweight (single hyperparameter, no added parameters or inference cost).
- The empirical protocol is reasonably careful: multiple baselines, five-seed averaging with standard deviations, stratified low-resource sampling, and validation-based hyperparameter search.
- The ablation table is a real strength: it isolates the curriculum's contribution (0.8 points), tests a reversed-curriculum control (which is a nice sanity check confirming that ordering—not just augmentation diversity—matters), and separately evaluates the role of back-translation.
- The label-budget analysis (Table 3) supports the paper's central intuition that curriculum-based intermediate training helps most when labels are scarcest, which is a coherent and useful finding for practitioners.
- The paper is honest about limitations (English-only, BERT-base only, hand-designed linear schedule, dependence on external resources like WordNet and MT systems).

## Weaknesses
- The reported gains, while consistent, are modest (1.1 points over CERT on average) and fall within or close to one standard deviation on some datasets (e.g., TREC: 90.8±0.9 vs 90.2±0.7), so statistical significance testing (e.g., paired t-tests across seeds) would strengthen the claims.
- The paper does not report results for multiple curriculum lengths L beyond the ablation's L=0 case; a sensitivity analysis of the curriculum-length hyperparameter would clarify robustness and practical tuning cost.
- Benchmarks are relatively "easy" and well-studied (SST-2, AG News, TREC, SUBJ); results on noisier or more specialized domains would better support claims of general applicability.
- The 12% training-time overhead and additional hyperparameter (curriculum length, tuned via 48-configuration grid search) are non-trivial costs that could be discussed more thoroughly relative to the modest accuracy gains.
- Comparisons to other curriculum-based or difficulty-scheduled augmentation strategies from vision (mentioned in related work) are not empirically included, which would help contextualize novelty versus straightforward transfer of existing ideas.

## Scores

| Criterion | Score (0–100) |
|---|---|
| Soundness | 74 |
| Novelty | 60 |
| Significance | 65 |
| Clarity | 85 |

**Average: 71**

## Recommendation: **Accept**

The paper presents a clean, well-motivated, and lightweight modification to an established intermediate-training pipeline, supported by a reasonably rigorous experimental design, informative ablations (including a well-designed reversed-curriculum control), and a plausible, consistent story across datasets and label budgets. While the improvements are incremental and further robustness checks (significance testing, curriculum-length sensitivity, broader domains) would strengthen the contribution, the work is methodologically sound, clearly written, and offers a useful, practical technique for low-resource text classification. I recommend acceptance, with encouragement to address the noted limitations in a future revision.