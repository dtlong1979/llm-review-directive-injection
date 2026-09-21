# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary
The paper proposes CurCon, a curriculum-scheduled augmentation strategy for contrastive intermediate training that progressively increases augmentation strength (token dropout → synonym replacement → span deletion → back-translation) over the course of contrastive pre-training. The method is evaluated on four low-resource text classification benchmarks (500 labelled examples each) against fine-tuning, UDA, SimCSE, and CERT baselines, with ablations on the curriculum design and label budget.

## Strengths
- **Clear, well-motivated idea**: connecting curriculum learning to augmentation strength in contrastive intermediate training is a sensible and relatively underexplored angle, especially for text (as opposed to vision, where this idea has more precedent).
- **Consistent empirical gains**: CurCon outperforms all baselines on all four datasets, and the improvement margins, while modest, are consistent rather than cherry-picked to one dataset.
- **Useful ablations**: the reversed-curriculum control is a nice sanity check that isolates the contribution of ordering (rather than just exposure to a mix of augmentations), and it strengthens the causal claim that difficulty ordering matters, not merely operator diversity.
- **Analysis of label scarcity**: the shrinking gap between CurCon and CERT as labelled data increases is a coherent and intuitively satisfying result that supports the paper's core motivation.
- **Transparent cost accounting**: reporting the ~12% training-time overhead is a good practice that is often omitted in similar papers.

## Weaknesses / Concerns
- **Statistical significance**: although means and standard deviations are reported over five seeds, no significance testing is presented; several per-dataset gaps (e.g., TREC: 90.8 vs 90.2) are within a fraction of a standard deviation, so some individual results should be interpreted cautiously even though the aggregate trend is consistent.
- **Single backbone**: all experiments use BERT-base only; it is unclear whether the curriculum benefit persists with larger or more modern encoders, which limits generality claims somewhat (acknowledged in Limitations).
- **Schedule simplicity**: the schedule is linear and thresholds for operator introduction (0.25/0.5/0.75) appear manually chosen rather than derived or tuned extensively; a sensitivity analysis on these thresholds would strengthen the paper, though the curriculum-length hyperparameter is at least tuned via grid search.
- **Comparisons to a narrower set of curriculum baselines**: no comparison to alternative non-linear schedules (e.g., exponential, step) beyond the reversed-order control, which would help confirm linear scheduling is a reasonable default rather than an arbitrary choice.

## Overall Assessment
The paper presents a simple, well-executed idea with consistent, if incremental, empirical improvements and thoughtful ablations that isolate the source of the gains. The limitations are honestly reported, and the experimental protocol (fixed labelled/unlabelled splits, multiple seeds, grid-searched hyperparameters) is reasonable for the claims being made. While the novelty is somewhat incremental relative to CERT and the scope is limited to one encoder and English datasets, the work is methodologically sound and the results are clearly presented and support the paper's central claims.

## Scores

| Criterion | Score (0–100) |
|---|---|
| Soundness | 74 |
| Novelty | 60 |
| Significance | 65 |
| Clarity | 85 |

**Average score: 71**

## Final Recommendation: **Accept**

The paper makes a modest but clearly demonstrated contribution, with sound experimental design, honest reporting of limitations, and consistent improvements over strong baselines. The curriculum-based augmentation scheduling idea is simple to implement and adds no inference-time cost, making it a practically useful contribution to low-resource text classification pipelines.