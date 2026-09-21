Review summary

Strengths
- Simple, well-motivated idea: gradually increasing augmentation strength during contrastive intermediate training fits curriculum learning intuitions and is easy to implement.
- Consistent gains across four benchmarks and five seeds; improvements over strong baselines (CERT, SimCSE, UDA), with largest benefits in the lowest-label regime.
- Solid ablations (fixed mixture, reversed curriculum, removal of back-translation) that isolate the effect of the schedule and augmentation choices.
- Clear training pipeline and reproducible details; limitations are candidly discussed.

Weaknesses and concerns
- Fairness of comparisons: CurCon is tuned via a per-dataset grid search while baselines use hyperparameters “from original papers.” This can inflate CurCon’s advantage. Baselines should also be tuned on the same validation splits or, at minimum, a sensitivity check should be provided.
- Magnitude of gains is modest (≈+1.1 average over CERT at 500 labels) and may fall within practical variance for some settings; statistical significance tests would strengthen claims.
- Evaluation scope is narrow: English-only, short-text datasets and BERT-base only. It is unclear whether gains transfer to larger encoders, encoder-decoder/decoder-only LMs, longer documents, or other tasks.
- The curriculum design is hand-crafted and linear; limited exploration of schedule shapes or operator weights beyond on/off thresholds.
- Compute/accounting: precomputing back-translations offloads a substantial cost that is not measured; a fair wall-clock or FLOPs comparison (including MT cost) would be informative.

Suggested improvements
- Re-tune baselines on the same validation sets and report results; include sensitivity analyses for CurCon’s curriculum length and temperature.
- Extend to at least one larger encoder and one longer-text dataset; add a cross-domain setting to test generality.
- Provide significance testing and/or confidence intervals for main improvements.
- Explore alternative or learned curricula (e.g., linear vs cosine, adaptive by loss).

Scores (0–100)
- Soundness: 80
- Novelty: 68
- Significance: 72
- Clarity: 88

Final average score: 77.0

Recommendation: Accept

Rationale: Despite modest gains and some fairness concerns in hyperparameter tuning, the method is simple, well-supported by ablations, consistently improves over strong baselines in low-resource regimes, and is likely to be useful to practitioners. The paper is clearly written and makes a focused, incremental but meaningful contribution.