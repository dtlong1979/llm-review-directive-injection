Review summary

Strengths
- Simple, well-motivated idea: scheduling augmentation strength during contrastive intermediate training aligns with curriculum learning principles.
- Consistent gains across four benchmarks in a low-resource regime, with clear ablations showing the curriculum matters (+0.8 avg vs fixed mixture; reversed schedule hurts).
- Solid experimental hygiene for the proposed method: five seeds, reported mean±std, analysis across label budgets, cost discussion.
- Clear exposition of method, schedule, and training pipeline; reproducibility seems feasible.

Weaknesses
- Baseline fairness: CurCon receives per-dataset hyperparameter tuning via grid search, while baselines reportedly use hyperparameters from original papers. This likely disadvantages baselines, especially in the low-resource setting where small tuning can matter. Stronger confidence would require tuning baselines on the same validation splits.
- Scope of evaluation is limited: four relatively short-text English datasets and a single encoder (BERT-base). No results on larger or more modern encoders, longer documents, or non-English settings, which constrains claims of generality.
- Magnitude of improvement is modest (≈+1.1 points over CERT on average). While consistent, it may be considered incremental for top-tier venues.
- The curriculum is linear and hand-designed; alternatives (e.g., adaptive or example-aware schedules) are not explored beyond a reversed schedule ablation.
- Some augmentation choices (WordNet synonyms, back-translation) can be domain- and language-dependent; broader robustness analysis is missing.
- Computational accounting omits the one-time translation cost; a clearer wall-clock and cost comparison (including precomputation) would aid practitioners.

Questions and suggestions
- Re-run baselines with comparable hyperparameter tuning on the same validation sets to ensure fairness, and report tuned results.
- Evaluate CurCon with larger encoders (e.g., RoBERTa-large, DeBERTa) and on longer-text datasets to assess scalability and generality.
- Explore adaptive curricula (e.g., based on model loss, agreement, or representation collapse metrics) and report sensitivity to curriculum length L.
- Provide statistical significance testing for the main gains over CERT.
- Include an experiment without WordNet (or with multilingual synonym sources) and with alternative BT language pairs to test robustness.
- Report total compute including back-translation precomputation, and a cost/benefit breakdown per augmentation operator.

Scores (0–100)
- Soundness: 80
- Novelty: 68
- Significance: 72
- Clarity: 90

Final average score
- (80 + 68 + 72 + 90) / 4 = 77.5

Final recommendation
- Accept

Rationale: Despite modest novelty and limited scope, the paper presents a clear, simple method with consistent improvements, a reasonable analysis, and actionable insights. With stronger baseline tuning and broader evaluation, it would be more compelling, but as is, it provides a useful and practical contribution for low-resource text classification.