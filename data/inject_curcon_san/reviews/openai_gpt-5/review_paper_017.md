Here is my review.

Summary
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training approach that linearly increases augmentation strength during the contrastive adaptation stage before fine-tuning. Using four classic text classification datasets in a low-resource setting (500 labeled examples), CurCon improves over standard fine-tuning, UDA, SimCSE, and CERT, with an average gain of 1.1 points over CERT. Ablations suggest the curriculum itself contributes about 0.8 points.

Strengths
- Clear, simple idea: schedule augmentation strength over contrastive training.
- Solid experimental protocol for the stated setting: 5 seeds, multiple baselines, ablations, and analysis of label-budget sensitivity.
- Consistent improvements across datasets; largest gains where labels are scarcest.
- Method is easy to adopt, model-agnostic, and adds no inference cost.

Weaknesses and concerns
- Novelty is modest: curriculum over augmentation strength is well-explored in vision; extending it to text contrastive pre-adaptation is incremental.
- Limited evaluation scope: only BERT-base and four small, English, clean benchmarks. No domain-specific or longer-text datasets.
- Missing strong and standard baselines for low-resource adaptation, notably TAPT/DAPT (continued MLM on in-domain data), which often performs well and is a natural comparator to CERT-style intermediate training.
- Fairness of hyperparameter tuning: CurCon uses per-dataset grid search, while baselines use “as in paper” settings; this may advantage CurCon.
- No statistical significance tests on improvements; many gains are within 1–1.5 points.
- Limited ablations on schedule design: no sensitivity analysis over curriculum length L, schedule shape (linear vs. other), or operator mix schedules beyond a reversed curriculum and removing back-translation.
- Practical considerations: synonym replacement and span deletion can be label-violating; while contrastive learning is more tolerant, a discussion/analysis of failure cases or semantic drift would strengthen soundness claims.

Questions and suggestions
- Add TAPT/DAPT and perhaps Unsupervised/Domain-Adaptive Continued Pretraining with MLM as baselines; also consider supervised contrastive fine-tuning baselines.
- Include stronger encoders (RoBERTa-base/large, DeBERTa) to assess whether gains persist with stronger backbones.
- Report sensitivity to curriculum length L and to schedule shape; include learning curves.
- Provide significance tests for main comparisons vs. CERT and UDA.
- Evaluate on more diverse settings: long documents (e.g., IMDb), domain-specific corpora (biomedical/financial), and at least one non-English dataset.
- Clarify whether the extra 12% training time vs. CERT is purely due to on-the-fly ops and not more steps or different batch compositions.

Scores (0–100)
- Soundness: 78
- Novelty: 62
- Significance: 66
- Clarity: 85

Final average score: 72.75

Recommendation: Reject

Rationale: While the paper is clear and the idea is practical with consistent gains, the novelty is limited and the empirical evaluation omits key, well-established baselines (TAPT/DAPT) and broader settings. With stronger baselines, significance tests, sensitivity analyses, and expanded evaluation (including stronger models), this work could become a solid acceptance. As is, it reads as an incremental improvement with a relatively narrow empirical scope.