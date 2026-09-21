Summary
CurCon introduces a curriculum for augmentation strength during contrastive intermediate training on unlabeled in-domain text, progressively moving from mild token-level perturbations to strong operations like back-translation. Evaluated on four sentence-level classification tasks under low-resource settings (500 labels), CurCon outperforms fine-tuning, UDA, SimCSE, and CERT by 1.1 points on average over CERT. Ablations suggest the curriculum itself contributes ~0.8 points, with additional studies across label budgets.

Strengths
- Clear, simple idea with minimal changes to standard CERT-style pipelines; no inference overhead.
- Consistent improvements over strong baselines across four datasets and five seeds.
- Sensible ablations, including fixed mixture, reversed schedule, removal of back-translation, and label-budget analysis.
- Practical detail on operators and schedule; implementation specifics are stated.

Weaknesses and Concerns
- Novelty is incremental: curriculum over augmentation strength for contrastive learning has precedent in vision; applying it to NLP intermediate training is a targeted but modest extension.
- Fairness/tuning: CurCon is tuned via grid search per dataset, while baselines use hyperparameters from their papers; re-tuning baselines on the same validation splits would strengthen claims.
- Scope: only four English, sentence-level datasets and a single encoder (BERT-base). No results on larger or more recent backbones (e.g., RoBERTa/DeBERTa) or longer documents; no multilingual tests despite dependence on translation.
- Operator choices rely on external resources (WordNet, MT), which may vary in quality across domains/languages; robustness to resource variability not studied.
- Limited analysis of schedule sensitivity (e.g., different L, non-linear schedules, or adaptive policies).

Questions/Requests for the authors
- Report sensitivity to curriculum length L and temperature; how robust are gains without per-dataset tuning?
- Re-tune CERT and UDA on the same validation splits to confirm the margin holds under comparable tuning effort.
- Provide results on at least one stronger encoder (e.g., RoBERTa-base) and a longer-text benchmark to test generality.
- Clarify the size of unlabeled corpora used per dataset and whether any data leakage could occur during back-translation preprocessing.
- Release code and augmentation configs for reproducibility.

Scores (0–100)
- Soundness: 82
- Novelty: 68
- Significance: 72
- Clarity: 90

Final average score: 78.0

Recommendation: Accept