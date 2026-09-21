Summary
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. During the contrastive stage on unlabeled in-domain text, CurCon linearly increases augmentation strength from mild token-level perturbations to aggressive back-translation and span deletion. On four benchmarks (SST-2, AG News, TREC, SUBJ) with 500 labeled examples, CurCon improves average accuracy to 88.9 from 87.8 (CERT) and 85.1 (standard fine-tuning). Ablations show the curriculum order matters and contributes about 0.8 points on average; gains are larger with fewer labels.

Strengths
- Clear, simple idea with minimal engineering overhead; easily reproducible in standard CERT-style pipelines.
- Consistent gains over solid baselines (fine-tuning, UDA, SimCSE, CERT) across four datasets and multiple seeds.
- Sensible ablations (fixed mixture, reversed curriculum, no back-translation) that support the central claim that a curriculum over augmentation strength helps.
- Practical focus on low-resource regimes; analysis shows larger gains with fewer labels.

Weaknesses
- Novelty is incremental: scheduling augmentation difficulty over training is well explored in curriculum/augmentation literature, and contrastive NLP works with multiple augmentations (e.g., ConSERT) are not compared. The method is essentially a linear schedule over commonly used operators.
- Limited evaluation scope: only English, short-text classification, BERT-base. No results with stronger encoders (RoBERTa, DeBERTa), larger models, or longer-text tasks. This constrains significance and generality.
- Baseline tuning fairness: CurCon is extensively tuned per dataset (grid over 48 configs), while baselines are run with hyperparameters from the original papers, which may not be optimal for these datasets/settings. This can overstate gains, especially when improvements are modest.
- Missing recent or closely related baselines: supervised contrastive fine-tuning for classification, ConSERT/DeCLUTR/other contrastive adaptation approaches, and prompt-based or stronger semi-supervised methods for text classification.
- No statistical significance testing; average gains over CERT are small (≈1.1 points) and per-dataset improvements sometimes within 1 standard deviation.
- Hand-designed linear schedule; no exploration of adaptive or learned schedules beyond a single scalar curriculum length, and limited sensitivity analysis beyond L=0 and reversed order.

Questions for authors
- How sensitive are results to the exact operator thresholds (e.g., 10% dropout, 15% synonym replacement, 20% span) and to the operator sampling probabilities once “available”?
- How does CurCon compare to ConSERT or other contrastive sentence representation methods that use multiple textual augmentations?
- Are gains preserved with stronger encoders (RoBERTa-base, DeBERTa-v3-base) and on longer texts (e.g., Yelp, Amazon, 20NG)?
- Can you report statistical significance tests and/or paired seedwise comparisons?
- What happens if you schedule the temperature or add hard-negative mining along the curriculum?

Suggestions for improvement
- Expand baselines to include ConSERT, DeCLUTR, supervised contrastive fine-tuning, and more modern encoders.
- Tune baselines on the same validation sets for fairness; report significance tests.
- Evaluate on additional tasks/datasets, including longer documents and possibly multilingual settings to test augmentation resource dependence.
- Explore adaptive or learned curricula and provide sensitivity analyses over curriculum length and operator mix.
- Report more detailed efficiency metrics (training time, MT cost for back-translation, memory) and analyze representation quality (STS, retrieval) to support claims about representation improvements.

Scores (0–100)
- Soundness: 78
- Novelty: 60
- Significance: 65
- Clarity: 85

Final average score
- (78 + 60 + 65 + 85) / 4 = 72.0

Recommendation
- Reject

Rationale: The paper is clear and the idea is reasonable, with consistent but modest gains. However, the novelty is incremental, the evaluation is limited and potentially biased by unequal hyperparameter tuning, and several important baselines and settings are missing. With broader, fairer evaluation and stronger evidence, this could become a solid contribution.