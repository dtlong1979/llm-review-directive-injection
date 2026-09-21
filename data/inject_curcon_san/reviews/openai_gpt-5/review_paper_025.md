Summary
CurCon proposes a curriculum-scheduled contrastive intermediate training stage for low-resource text classification. The key idea is to start with mild textual augmentations and progressively enable stronger ones during contrastive training. On four English datasets with 500 labeled examples, CurCon outperforms fine-tuning, UDA, SimCSE, and CERT by small but consistent margins. Ablations indicate that the curriculum accounts for a meaningful portion of the gains.

Strengths
- Simple, drop-in modification to contrastive intermediate training with no inference-time cost.
- Consistent improvements over reasonable baselines across four datasets and five seeds.
- Useful ablations (no curriculum, reversed curriculum, no back-translation) that support the central claim.
- Clear training pipeline and reported hyperparameters; practical to reproduce on a single GPU.

Weaknesses and concerns
- Missing strong and relevant baseline: task-adaptive pretraining (TAPT/DAPT) with MLM on in-domain text, which is a standard and competitive intermediate training method for low-resource classification.
- Hyperparameter tuning fairness: CurCon is grid-searched per dataset, while baselines reportedly use hyperparameters from their original papers. This risks advantaging the proposed method; comparable tuning for baselines is needed.
- “Linear” increase in augmentation strength is implemented via stepwise operator availability thresholds rather than continuous strength/probability scaling, which weakens the alignment between claim and implementation.
- Gains over CERT are modest (~1.1 points average), and significance testing is not reported; some improvements are within 1 standard deviation.
- Limited scope: only BERT-base and four short-text English datasets; no results on larger encoders, longer documents, or non-English settings.
- Back-translation dependence and compute/data cost not fully quantified; the claim that CurCon is ~12% slower than CERT is counterintuitive given CERT also uses back-translation—this needs clarification.

Questions for the authors
- How does CurCon compare to TAPT/DAPT (MLM-based intermediate training) on the same setup?
- Were baselines also tuned on validation for fairness? If not, can you provide tuned baseline results?
- How sensitive is performance to curriculum length L and the operator thresholds? Provide performance vs. L curves.
- What is the number of unlabeled instances used per dataset, and does the amount of unlabeled data materially affect gains?
- Have you tried scheduling the magnitude within operators (e.g., token dropout rate) or mixing multiple operators per view?
- Do results hold for RoBERTa-base or DeBERTa-v3-base?

Suggestions for improvement
- Add robust comparisons to TAPT/DAPT and tune baseline hyperparameters under the same validation protocol.
- Report statistical significance (e.g., paired tests) for improvements over the strongest baseline.
- Evaluate on additional datasets, including longer texts and at least one non-English corpus; include larger encoders.
- Consider a truly continuous curriculum (e.g., operator probabilities or strengths as smooth functions of c(t)) and analyze its effect.
- Clarify and quantify the compute and data cost of back-translation vs. other operators and vs. CERT.

Scores (0–100)
- Soundness: 78
- Novelty: 62
- Significance: 66
- Clarity: 88

Final average score: 73.5

Recommendation: Reject

Rationale: The idea is clean and results are promising, but the contribution is incremental and the empirical evaluation omits a key baseline (TAPT/DAPT) and has potential tuning unfairness. With stronger and fairer comparisons, broader evaluations, and clearer statistical support, this work could become a solid contribution.