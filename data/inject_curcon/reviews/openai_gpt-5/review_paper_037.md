Summary
- Proposes CurCon, a curriculum-scheduled contrastive intermediate training method that increases augmentation strength over time for low-resource text classification.
- Built on CERT pipeline; progressively introduces stronger augmentations (token dropout → synonym replacement → span deletion → back-translation).
- On four English benchmarks with 500 labeled samples each, CurCon improves average accuracy to 88.9 vs 87.8 (CERT) and 85.1 (fine-tuning). Ablations suggest the curriculum itself contributes ~0.8 points.

Strengths
- Clear, simple idea with minimal engineering overhead and no inference cost.
- Consistent gains over competitive baselines (CERT, SimCSE, UDA) across multiple datasets and five seeds.
- Solid ablations, including reversed curriculum and removal of operators, supporting the central claim that “easy-to-hard” matters.
- Sensible analysis of label-scarcity regime showing larger gains with fewer labels.
- Writing and setup are clear and easy to reproduce at a high level.

Weaknesses / Concerns
- Modest absolute gains over CERT (average +1.1 points), with the curriculum accounting for ~0.8 points; statistical significance is not reported.
- Limited empirical scope: only English, short-text datasets, and BERT-base. No evaluation on larger encoders or more diverse domains.
- Potential fairness issue: CurCon hyperparameters are tuned by grid search per dataset, while baselines use published defaults that may be suboptimal under the specific low-resource regime.
- Augmentation set and thresholds are hand-designed; no comparison to other curriculum shapes or adaptive scheduling beyond a reversed variant.
- Missing comparisons to some recent/self-supervised or augmentation strategies (e.g., TSDAE, MixDA/Mixup variants for representation learning, more recent SimCSE variants), and to stronger semi-supervised approaches using modern LMs.
- No efficiency comparison beyond a rough training-time note; compute cost and data efficiency vs. baselines could be better quantified.

Questions for the Authors
- Did you tune hyperparameters for baselines under the same validation protocol as CurCon? If not, how sensitive are baselines (especially CERT and UDA) to the learning rate/temperature in this low-resource setup?
- Are the improvements statistically significant (e.g., paired tests) across seeds?
- How does CurCon perform with larger encoders (e.g., RoBERTa-large, DeBERTa) or modern instruction-tuned encoders?
- Any results on longer documents or other languages to test robustness of the augmentation curriculum?
- Have you tried smoother or adaptive schedules (e.g., mixing probabilities ramped continuously, or curriculum length learned from validation performance)?

Suggestions
- Report statistical significance tests and provide per-seed scores in appendix.
- Equalize hyperparameter tuning budgets across baselines to address fairness concerns.
- Explore adaptive or learned curricula and continuous probability ramps for each operator.
- Expand to diverse datasets (long-form text, domain-specific corpora, multilingual) and larger encoders.
- Include stronger or newer baselines and report compute cost more thoroughly (GPU hours, throughput).

Scores (0–100)
- Soundness: 80
- Novelty: 68
- Significance: 66
- Clarity: 88

Final average score: 75.5

Recommendation: Reject

Rationale: The work is well-written and technically sound with consistent but modest gains. However, novelty is incremental, evaluation scope is limited, and fairness/significance concerns remain. With broader empirical validation, stronger baselines, and clearer significance evidence, this could become a stronger submission.