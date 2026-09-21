# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary
The paper proposes CurCon, which schedules augmentation strength (token dropout → synonym replacement → span deletion → back-translation) during contrastive intermediate training via a linear curriculum controlled by a single hyperparameter L. The method is evaluated against fine-tuning, UDA, SimCSE, and CERT on four text classification benchmarks with 500 labelled examples, showing consistent improvements, with ablations on curriculum design and label budget.

## Strengths
- Clear, simple idea with a well-motivated connection to curriculum learning literature applied to an underexplored axis (augmentation policy in contrastive intermediate training rather than example ordering).
- Reasonable experimental scope: multiple baselines, multiple datasets, seed averaging, ablations, and a labelled-data-scale analysis.
- The reversed-curriculum ablation is a nice sanity check that isolates the effect of ordering rather than just exposure to varied augmentations.
- Cost analysis is honestly reported (12% overhead).

## Weaknesses (Soundness)
- No statistical significance testing despite reporting standard deviations; differences between CurCon and CERT (e.g., 0.6 on AG News) are within one standard deviation, making claims of consistent superiority weak.
- Single encoder (BERT-base), single language, and relatively short-text datasets—generalizability is unverified, and this is only mentioned in limitations rather than explored.
- Grid search of 48 configurations for CurCon vs. baselines using "hyperparameters reported in original papers" introduces a confound: CurCon may benefit from more extensive tuning, not from the method itself.
- No description of how many seeds/runs were used for the ablation table (variance not reported), making the 0.8-point curriculum contribution hard to trust.
- Back-translation is described as "pre-computed" in the cost section but used dynamically within the curriculum schedule (available only after c(t)>0.75)—the interaction between pre-computation and per-step gating is not clearly explained.

## Novelty
The core contribution—applying curriculum scheduling to augmentation *strength* in contrastive intermediate training—is a reasonably novel combination, though each component (curriculum learning, contrastive intermediate training, the specific augmentation operators) is drawn directly from prior work (CERT, UDA-style augmentations, vision curriculum-augmentation papers). The novelty is incremental/combinatorial rather than conceptual.

## Significance
The improvements are real but modest (1.1 points over CERT on average, within one std on some datasets). The paper is useful as an empirical contribution to a practical low-resource setting, but the effect sizes and single-architecture scope limit broader significance.

## Clarity
The paper is well-organized and easy to follow, with clear method description, explicit schedule formula, and clean tables. Minor gaps: the interaction between back-translation pre-computation and the curriculum schedule, and lack of detail on how ablation variance was computed.

---

### Scores (0–100)

| Criterion | Score |
|---|---|
| Soundness | 58 |
| Novelty | 50 |
| Significance | 55 |
| Clarity | 78 |

**Average: 60.25**

## Recommendation: **Reject** (borderline)

The paper presents a clean, well-motivated idea with solid execution, but the modest and statistically uncertain gains, confound between tuning budgets across methods, and limited scope (one encoder, one language) leave the empirical claims insufficiently robust for acceptance at this stage. A revision with significance testing, matched hyperparameter search budgets across baselines, and broader architecture/language coverage would substantially strengthen the submission.