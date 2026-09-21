Paper summary
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training approach for low-resource text classification. It progressively increases augmentation strength during the contrastive stage, moving from token dropout to synonym replacement, span deletion, and finally back-translation. On four benchmarks with 500 labeled examples, CurCon outperforms fine-tuning, UDA, SimCSE, and CERT, with an average accuracy of 88.9 versus 87.8 for CERT. Ablations suggest the curriculum contributes roughly 0.8 points on average, and gains are larger with fewer labels.

Strengths
- Clear, simple idea: scheduling augmentation strength during contrastive intermediate training.
- Solid empirical protocol: four datasets, five seeds, standard deviations, 100/500/1,000 label regimes, and ablations (fixed mixture, reversed curriculum, removal of back-translation).
- Consistent improvements over strong baselines; improvements are largest where they matter most (lowest-label setting).
- Reasonable cost analysis and pragmatic implementation choices (precomputing back-translation).
- Clear presentation and well-scoped limitations.

Weaknesses and concerns
- Modest average gains over the strongest baseline (1.1 points at 500 labels; 0.5 points at 1,000 labels). Statistical significance tests are not reported.
- Potential fairness concern: CurCon is tuned via grid search per dataset, while baselines use hyperparameters from original papers; stronger, equally tuned baselines could narrow the gap.
- Curriculum design is hand-crafted and somewhat coarse (operator availability thresholds and uniform sampling among available operators). Alternative schedules (e.g., smoothly varying probabilities or strength within operators) are not explored.
- Limited scope: only English, short-text datasets, and BERT-base. No results on larger encoders, domain-shifted data, or multilingual settings.
- Limited analysis of which augmentation combinations drive gains beyond the ablation removing back-translation; per-operator contributions and schedule length sensitivity could be more granular.

Suggestions for improvement
- Tune baselines with the same search protocol and report significance tests.
- Explore smoother probability schedules or intensity scaling within operators (e.g., span proportion, synonym rate) and adaptive curricula.
- Provide sensitivity to curriculum length L and temperature/batch size.
- Extend to larger/pretrained encoders and additional domains/languages to assess generality.
- Add analyses on representation quality (e.g., sentence embedding benchmarks) to test transferability beyond the target tasks.

Reproducibility
- Good level of detail on datasets, sampling, schedule, and training setup. Releasing code and augmentation resources would close the loop.

Scores (0–100)
- Soundness: 82
- Novelty: 70
- Significance: 78
- Clarity: 90

Final average score
80.0

Final recommendation
Accept