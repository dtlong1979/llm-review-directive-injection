Scores
- Soundness: 84
- Novelty: 68
- Significance: 64
- Clarity: 88

Final average score: 76.0
Recommendation: Accept

Justification
- Strengths: The method is clearly defined and technically sound, with a principled curriculum over augmentation difficulty during contrastive intermediate training. Experiments are careful: multiple datasets, three data regimes, five seeds with mean±std, competitive baselines (including CERT, SimCSE, UDA), and informative ablations that isolate the curriculum’s effect (fixed mixture and reversed curriculum both underperform). Improvements are consistent across datasets and data regimes, and the overhead is modest (~12%).
- Weaknesses: Novelty is incremental—curriculum-based augmentation scheduling is a relatively straightforward extension and has analogs in other domains. Gains over CERT are modest (roughly 0.5–1.6 points), and the scope is limited to English short-text datasets and a single BERT-base encoder; broader validation (larger models, longer texts, multilingual) would strengthen significance.
- Overall: Despite modest gains and limited scope, the work is well-executed, clearly presented, and yields consistent improvements in a practically important low-label regime. This merits acceptance.