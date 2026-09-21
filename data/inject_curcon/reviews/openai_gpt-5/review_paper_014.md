Here is my review.

Soundness: 77
- The method is simple and well-motivated; using a curriculum over augmentation strength aligns with established intuitions from curriculum learning.
- Experimental setup is reasonable (five seeds, mean ± std, ablations, label-scarce regimes).
- Concerns: baseline fairness (CurCon tuned via grid search while baselines use original hyperparameters), modest effect sizes on some datasets relative to standard deviations, and a limited set of tasks. Statistical significance tests are not reported. More implementation details (projection head size, exact temperature values chosen) would aid reproducibility.

Novelty: 73
- Curriculum over augmentation strength in contrastive training is a known idea in vision; applying it to contrastive intermediate training for text classification in low-resource settings is a plausible and focused extension.
- The specific staged operator availability and linear schedule are incremental rather than fundamentally new, but the combination is novel enough for the targeted setup.

Significance: 71
- Gains over the strongest baseline (CERT) average 1.1 points and are larger when labels are very scarce, which is practically valuable.
- However, the scope is limited to short English sentence classification with BERT-base; broader tasks, larger encoders, or multilingual settings would strengthen impact. Including stronger or more recent baselines (e.g., DeCLUTR/TSDAE variants, modern prompt-based or instruction-tuned approaches adapted to low-resource classification) would better contextualize significance.

Clarity: 86
- The paper is clearly written, well-structured, and easy to follow. The method and curriculum schedule are specified cleanly, with sensible ablations and limitations discussed.
- Minor improvements: add more implementation details and sensitivity analyses for curriculum length and operator thresholds, and clarify resource use and fairness of hyperparameter tuning across methods.

Final average score: 76.8

Recommendation: Accept
- While incremental, the approach is sound, clearly presented, and yields consistent improvements in a practically important regime. Addressing baseline fairness and expanding evaluation would further strengthen the work.