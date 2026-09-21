Paper summary
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. It linearly increases augmentation strength during contrastive pre-adaptation of a BERT-base encoder, progressing from token dropout to synonym replacement, span deletion, and finally back-translation. On four English sentence-level benchmarks with 500 labeled examples each, CurCon improves average accuracy to 88.9, above CERT (87.8) and standard fine-tuning (85.1). Ablations suggest the curriculum accounts for ~0.8 points of the gain; benefits are larger with fewer labeled examples.

Strengths
- Clear, simple idea with minimal engineering overhead and no inference cost.
- Consistent improvements over strong baselines across four datasets and five seeds.
- Thorough ablation including reversed curriculum, removal of back-translation, and fixed-operator mixture.
- Sensible analysis of label-scarcity effects; gains largest with fewer labels.
- Clear write-up with concrete hyperparameters and training details; limitations acknowledged.

Weaknesses
- Novelty is modest: curriculum over augmentation strength in contrastive learning is known in other modalities; adapting it to intermediate contrastive training for text is incremental.
- Evaluation scope is limited: four English sentence-level datasets, one encoder (BERT-base). No results on longer texts, other architectures, or multilingual settings despite claims of generality.
- Potential fairness concerns in comparisons: CurCon uses per-dataset grid search over 48 configurations, while baselines are run with hyperparameters from their papers; this can disadvantage baselines in the low-resource, in-domain setting.
- Reported gains are relatively small (≈1.1 points over CERT on average) and may be sensitive to augmentation/operator choices and schedule details; no statistical significance tests reported beyond mean±sd.
- Lacks comparisons to more recent text augmentation curricula or adaptive policies (e.g., learned schedules, loss-based curricula), and to stronger contemporary baselines such as supervised contrastive objectives during fine-tuning or modern semi-supervised methods for text.

Questions and suggestions
- Tune baselines with comparable per-dataset validation sweeps to address fairness; report validation curves and selection criteria.
- Add significance testing (e.g., paired t-tests across seeds) to quantify reliability of small improvements.
- Evaluate on additional datasets (longer documents, domain-specific corpora), larger encoders (RoBERTa, DeBERTa), and possibly decoder-only LMs to demonstrate generality.
- Compare against alternative schedules (cosine, sigmoid, stage-wise) and adaptive schedules (e.g., based on loss/confidence or online performance).
- Include an operator-strength sensitivity study (percentages for token dropout/span deletion; different BT pivots) and cost breakdowns, including translation compute if not precomputed.
- Consider comparing to supervised contrastive fine-tuning and modern semi-supervised consistency methods tuned for today’s encoders; also consider prompt-based baselines as additional context for low-resource setups.
- Clarify the amount of unlabeled data used and ensure no leakage; discuss domain shift scenarios (unlabeled not fully in-domain).

Scores (0–100)
- Soundness: 73
- Novelty: 57
- Significance: 64
- Clarity: 87

Final average score: 70.25

Recommendation: Reject

Rationale: The method is clean and empirically beneficial, but the contribution is incremental with modest gains, limited evaluation breadth, and some fairness concerns in hyperparameter tuning. Strengthening comparisons, broadening experiments, and exploring/adopting adaptive curricula would make a stronger case for acceptance.