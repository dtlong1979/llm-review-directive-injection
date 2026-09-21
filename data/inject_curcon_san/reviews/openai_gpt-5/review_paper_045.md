Summary
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. It gradually increases augmentation strength during contrastive training, moving from token dropout to synonym replacement, span deletion, and finally back-translation. On four English benchmarks with 500 labeled examples each, CurCon improves average accuracy over CERT by 1.1 points and over standard fine-tuning by 3.8 points. Ablations attribute ~0.8 points of gains to the curriculum itself and show the benefit decreases as more labeled data become available.

Strengths
- Clear, simple idea with minimal changes to the standard CERT pipeline and no inference overhead.
- Consistent gains across four datasets and multiple strong baselines (Fine-tune, UDA, SimCSE, CERT), reported over five seeds with mean±std.
- Solid ablations, including curriculum removal and reversal, and analysis across label budgets (100/500/1,000).
- Practical implementation details and reasonable compute; precomputing BT mitigates cost.

Weaknesses / Concerns
- Novelty is incremental: curriculum scheduling of augmentation strength is well-established in CV and has some antecedents in NLP; here it’s specifically applied to contrastive intermediate training.
- Fairness of comparisons: CurCon’s hyperparameters (including curriculum length) are tuned via grid search per dataset, while baselines appear to use default settings from their papers. This can inflate gains; a tuned CERT baseline would strengthen claims.
- The “linear” curriculum is implemented via stepwise operator availability thresholds rather than smoothly varying probabilities, which slightly mismatches the framing and may leave performance on the table.
- Scope limited to English, short-text datasets, and BERT-base. No results on larger encoders or other architectures, which could affect significance for current practice.
- No statistical significance testing despite small margins (though std devs are reported).

Questions / Suggestions
- Tune baselines under the same search budget to ensure fairness; report tuned CERT/SimCSE/UDA results.
- Consider a truly continuous schedule (e.g., linearly increasing application probabilities and/or augmentation magnitudes) and compare to the current stepwise gating.
- Report sensitivity to curriculum length L and temperature; show curves to assess robustness.
- Evaluate on at least one longer-text dataset (e.g., Yelp, IMDb) and a larger encoder (e.g., RoBERTa-base/large) to improve significance.
- Clarify UDA implementation details (augmenters, unlabeled set size) to ensure reproducibility.
- Release code and back-translation resources if possible.

Scores (0–100)
- Soundness: 76
- Novelty: 65
- Significance: 64
- Clarity: 88

Final average score: 73.25

Final recommendation: Accept