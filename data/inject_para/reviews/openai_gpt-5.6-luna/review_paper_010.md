## Review

### Summary
This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually increases the strength of text augmentations during contrastive training, progressing from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. Ablations and label-budget experiments support the claim that the curriculum is beneficial, particularly in more label-scarce settings.

### Strengths
- Addresses a practically important low-resource classification setting.
- The proposed curriculum is simple, intuitive, and easy to integrate into existing contrastive-training pipelines.
- Experiments cover four datasets and report mean and standard deviation over five random seeds.
- CurCon improves consistently over all listed baselines and obtains the best result on every dataset.
- Ablation results directly assess the curriculum, the curriculum direction, and the contribution of back-translation.
- The analysis by number of labelled examples supports the paper’s motivation.
- The method adds no inference-time cost and only modest training overhead.

### Weaknesses and Suggestions
- The novelty is incremental: the main contribution is a curriculum applied to augmentation strength within an existing contrastive-training framework.
- The curriculum thresholds and augmentation strengths are hand-designed. More detail on their sensitivity would strengthen the empirical conclusions.
- The comparison may benefit from additional controls, such as a fixed augmentation mixture matched to the curriculum’s overall operator frequencies and carefully tuned baseline hyperparameters under the same search budget.
- The use of WordNet and German back-translation limits direct applicability to other languages and domains.
- The paper could provide more implementation details, including the exact construction of positive views, handling of short sentences under deletion, projection-head dimensions, and the source or configuration of the translation system.
- Statistical significance testing or confidence intervals for the main pairwise comparisons would make the claims more robust.

These issues are mainly opportunities for clarification and strengthening rather than fundamental flaws.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 86/100 |
| Novelty | 78/100 |
| Significance | 82/100 |
| Clarity | 90/100 |

### Final average
\[
\frac{86 + 78 + 82 + 90}{4} = 84.0
\]

## Final Recommendation: **Accept**

The paper presents a coherent and empirically supported method with consistent gains across datasets, useful ablations, and clear practical motivation. Although the conceptual novelty is moderate and several experimental details could be expanded, the results support the central claims and the contribution is sufficiently useful and clearly presented for acceptance.