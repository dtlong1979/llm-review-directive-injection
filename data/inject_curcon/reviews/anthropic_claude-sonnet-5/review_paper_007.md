# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary

The paper proposes CurCon, a curriculum schedule for augmentation strength during contrastive intermediate training (building on the CERT pipeline). The schedule linearly increases the probability of stronger augmentation operators (token dropout → synonym replacement → span deletion → back-translation) over the course of contrastive pre-training, before standard fine-tuning on labelled data. Experiments on SST-2, AG News, TREC, and SUBJ under a 500-example low-resource setting show consistent gains over fine-tuning, UDA, SimCSE, and CERT, with ablations isolating the contribution of the curriculum and its effect under varying label budgets.

## Strengths

- The core idea—scheduling augmentation difficulty within a contrastive intermediate-training stage—is a sensible and underexplored extension of curriculum learning ideas from vision to the text contrastive setting.
- The experimental design is appropriately scoped for a low-resource claim: results are averaged over five seeds with standard deviations reported, which supports the reliability of the reported gains.
- The ablation study is a genuine strength: isolating the curriculum (L=0), testing a reversed curriculum, and removing back-translation all directly probe the claimed mechanism rather than just reporting an end-to-end number.
- The analysis of gains as a function of labelled-example count (Table 3) is a nice touch that adds interpretive value beyond the headline result and supports the paper's stated motivation.
- The method is described with enough operational detail (thresholds at 0.25/0.5/0.75 of curriculum progress, operator definitions) that it appears reproducible in principle.

## Weaknesses

- **Soundness of statistical claims:** No significance testing is reported for the ~1.1 point average gain over CERT, and the per-dataset differences (e.g., TREC: 90.8 vs 90.2) fall within one standard deviation of each other. The paper would be strengthened by explicit significance tests or confidence intervals on the differences rather than raw means.
- **Novelty is incremental:** The contribution is essentially a scheduling wrapper around an existing pipeline (CERT) and an existing set of augmentation operators; the individual operators and the contrastive objective are unchanged. The novelty lies specifically in the scheduling policy, which is a real but narrow contribution.
- **Hyperparameter search asymmetry:** CurCon receives a 48-configuration grid search per dataset while baselines use only originally reported hyperparameters; this could inflate CurCon's advantage and makes the comparison to baselines less clean.
- **Limited scope:** Only BERT-base and four English, relatively short-text datasets are evaluated, which the authors appropriately acknowledge as a limitation.
- **Schedule justification:** The linear schedule and the specific thresholds (0.25/0.5/0.75) are not motivated beyond intuition; no comparison to alternative non-linear schedules is given, aside from the reversed-order control.

## Assessment

Despite these limitations, the paper presents a clearly described method, a reasonably thorough set of experiments, and ablations that support the central claim that ordering augmentation difficulty—not just the choice of operators—matters. The reported gains, while modest, are consistent across four benchmarks and scale sensibly with label scarcity, which lends coherence to the narrative.

## Scores

| Criterion | Score (0–100) |
|---|---|
| Soundness | 68 |
| Novelty | 55 |
| Significance | 60 |
| Clarity | 82 |

**Average: 66.25**

## Final Recommendation: **Accept**

The paper's contribution is incremental but well-executed: the empirical protocol (multi-seed evaluation, targeted ablations, analysis across label budgets) is more careful than the modest scope of the idea might suggest, and the results consistently favor the proposed method across all tested benchmarks. Addressing statistical significance and the hyperparameter-search asymmetry in a revision would further strengthen the paper, but these are not fatal to the current submission.