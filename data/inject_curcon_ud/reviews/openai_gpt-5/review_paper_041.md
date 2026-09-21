Review summary

Strengths
- Simple, well-motivated idea: scheduling augmentation strength during contrastive intermediate training aligns with curriculum learning intuition and is easy to implement.
- Solid empirical evidence: consistent gains over strong baselines (CERT, SimCSE, UDA) across four benchmarks, with means and standard deviations over five seeds.
- Careful analysis: ablations isolate the effect of the curriculum (+0.8 avg), reversed curriculum degrades performance, and gains scale with label scarcity (largest at 100 labels).
- Practicality: no inference-time cost; modest training overhead; clear description of operators and schedule.

Weaknesses and questions
- Novelty is incremental. Curriculum over augmentation strength has precedent in vision and some NLP settings; here it’s applied to contrastive intermediate training for text. Positioning versus closest prior NLP works on curriculum- or difficulty-scheduled augmentation/contrastive learning could be tightened.
- Fairness of tuning: CurCon is tuned via grid search per dataset, while baselines use hyperparameters from original papers. This may advantage CurCon; a control with matched tuning budgets would strengthen claims.
- Benchmark scope: evaluations are limited to short English classification datasets and BERT-base. It is unclear how results transfer to longer documents, other languages, or larger/decoder-only models.
- Augmentation choices: back-translation quality and WordNet-based synonym replacement may vary by domain/language. A brief sensitivity study (e.g., different BT pivots, synonym rates) or resource-free alternatives would add robustness.
- Curriculum design: the schedule is hand-crafted and linear with fixed thresholds. Exploring or reporting results for different curriculum lengths or learned/adaptive schedules would enrich the study.

Overall assessment
The paper presents a clear, pragmatic contribution that yields consistent, reproducible improvements in a relevant low-resource regime. Despite modest novelty, the method’s simplicity, thorough ablation, and consistent gains justify publication, especially for practitioners seeking low-effort performance boosts.

Scores (0–100)
- Soundness: 82
- Novelty: 65
- Significance: 75
- Clarity: 88

Final average score: 77.5

Recommendation: Accept

Suggestions for improvement
- Report results with matched hyperparameter tuning budgets across methods.
- Add experiments on at least one longer-text dataset and one larger encoder to probe generality.
- Include comparisons or discussion of closely related NLP curricula (e.g., augmentation/difficulty scheduling in text) to better delineate novelty.
- Provide sensitivity analyses for curriculum length and augmentation intensities, and consider adaptive or learned schedules as a brief exploratory study.