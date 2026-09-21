Here is a concise review of the paper.

Summary
- Proposes CurCon, a curriculum-scheduled contrastive intermediate training method that progressively increases augmentation strength during contrastive pre-training on in-domain unlabeled data, then fine-tunes on limited labeled data.
- Demonstrates consistent gains over fine-tuning, UDA, SimCSE, and CERT on four English text classification benchmarks with 500 labeled examples, plus ablations and analysis across label budgets.

Strengths
- Simple, general idea that is easy to implement and adds no inference cost.
- Consistent improvements over strong baselines, including CERT, with statistically stable results across five seeds.
- Clear ablations isolating the contribution of the curriculum (vs fixed mixture and reversed schedule) and of back-translation.
- Sensible analysis showing gains are larger when labeled data are scarcer.
- Clear exposition with concrete implementation details and limitations.

Weaknesses / Concerns
- Fairness of comparisons: CurCon hyperparameters are tuned via grid search per dataset, while baselines use hyperparameters from their papers; this could bias results in CurCon’s favor. Comparable tuning for baselines would strengthen claims.
- Evaluation scope is limited to English, short-text datasets and BERT-base. No results with stronger encoders (e.g., RoBERTa, DeBERTa) or longer/formal domains; this limits external validity.
- Reported average improvement over CERT is modest (~+1.1 points), though consistent; it would help to include significance testing across seeds.
- The augmentation set is somewhat conventional (dropout, synonyms, span deletion, back-translation) and the curriculum is linear and hand-crafted; more adaptive or learned curricula could be compared or discussed more deeply.
- Compute and cost fairness vs CERT could use more clarity (both rely on back-translation; differences from on-the-fly ops should be precisely quantified and matched if possible).

Suggestions
- Tune baselines on the same validation splits (or include sensitivity analyses) to address potential hyperparameter bias.
- Add experiments with a stronger encoder and at least one non-English or long-text/domain-specific dataset.
- Include statistical significance tests and per-dataset effect sizes.
- Explore alternative or adaptive curricula (e.g., difficulty estimated via representation alignment or model confidence), or at least report sensitivity to curriculum length L.

Scores (0–100)
- Soundness: 80
- Novelty: 72
- Significance: 75
- Clarity: 90

Final average score: 79.3

Recommendation: Accept