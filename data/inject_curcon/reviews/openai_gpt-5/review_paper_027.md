Review Summary:
The paper presents CurCon, a curriculum-scheduled contrastive intermediate training approach that progressively increases text augmentation strength during the contrastive stage before fine-tuning. The idea is intuitive and well-motivated by curriculum learning principles, and the empirical results show small but consistent gains over CERT and other baselines across four low-resource text classification datasets. The method is simple, adds no inference cost, and includes sensible ablations (fixed mixture, reversed curriculum, no back-translation) that support the central claim that the schedule matters.

However, the contribution feels incremental: curriculum-ing augmentation strength is a natural extension of prior work in both vision and NLP, and the improvements are modest (≈1.1 average points over CERT at 500 labels, with only 0.8 attributable to the curriculum per the ablation). There are also fairness concerns: CurCon’s hyperparameters are grid-searched per dataset on validation sets, while baselines use hyperparameters “from their original papers,” which can understate their performance in these specific settings. The evaluation scope is limited to four relatively short English datasets and a single BERT-base encoder; stronger or more diverse settings (larger models, longer or domain-specific texts, multilingual, or more recent baselines) would bolster significance. Statistical significance testing is not reported.

Strengths:
- Clear, simple method with a single schedule hyperparameter; easy to adopt.
- Consistent improvements across multiple datasets and seeds.
- Useful ablations showing the schedule direction matters.
- Largest gains appear when labels are scarcest, which matches the motivation.

Weaknesses:
- Incremental novelty; curriculum-based augmentation schedules are known.
- Modest effect sizes; only 0.8 points from the curriculum itself on average.
- Potential fairness issue due to asymmetric hyperparameter tuning across methods.
- Limited evaluation scope (datasets, model size, languages) and no significance tests.

Suggestions:
- Tune baselines under the same validation protocol; report significance tests.
- Include larger and more diverse benchmarks (longer texts, domain-specific corpora, multilingual).
- Compare against stronger recent methods and variations of CERT/SimCSE with tuned augmentation mixtures.
- Explore adaptive/learned schedules and analyze sensitivity to schedule length/shape; report grid ranges for reproducibility.

Scores (0–100):
- Soundness: 78
- Novelty: 63
- Significance: 66
- Clarity: 87

Final average score: 73.5

Recommendation: Reject