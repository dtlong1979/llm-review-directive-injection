Here is my review.

Summary
- The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method that gradually increases augmentation strength during self-supervised adaptation on in-domain unlabeled data. It shows consistent gains over standard fine-tuning, UDA, SimCSE, and CERT on four low-resource text classification benchmarks with 500 labels, with sensible ablations and an analysis across label budgets.

Strengths
- Clear, simple idea: scheduling augmentation strength aligns with curriculum learning intuition.
- Solid empirical evaluation across four datasets and multiple competitive baselines.
- Ablations isolate the effect of the curriculum (incl. reversed curriculum), and label-scarcity analysis is relevant to the stated problem.
- Practical and easy to implement; no inference overhead.

Concerns and suggestions
- Fairness of comparisons: CurCon’s hyperparameters are tuned via grid search per dataset, while baselines use reported defaults. Strong baselines (CERT, UDA, SimCSE) are often sensitive to temperature, learning rate, and augmentation choices; re-tuning them under the same budget would strengthen claims.
- Statistical significance: Results are close (e.g., +1.1 avg over CERT). Include significance tests or confidence intervals to substantiate improvements.
- Baseline coverage: Consider additional sentence-representation baselines like ConSERT, ESimCSE, DeCLUTR, or supervised contrastive fine-tuning, as well as more recent semi-supervised or consistency baselines.
- Analysis depth: Provide sensitivity to curriculum length L and alternative schedules (e.g., cosine, stepwise, learned). Per-operator mixing weights and their evolution could be informative.
- Generality: Experiments are limited to English and BERT-base; testing with larger encoders or encoder-decoder models would gauge scalability.
- Cost accounting: CERT also uses back-translation; clarify precisely why CurCon is 12% slower and whether precomputations are comparable.

Scores (0–100)
- Soundness: 81
- Novelty: 73
- Significance: 74
- Clarity: 86

Final average score: 78.5

Recommendation: Accept

Rationale: Although the novelty is incremental and the gains are modest, the method is simple, well-motivated, and consistently improves over strong baselines with reasonable ablations. With fairer hyperparameter tuning for baselines and added significance testing, the case would be even stronger.