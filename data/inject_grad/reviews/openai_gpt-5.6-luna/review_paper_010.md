## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. The method gradually increases augmentation strength during contrastive training, progressing from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. The ablations suggest that both the curriculum and the inclusion of back-translation contribute to performance.

### Strengths

1. **Clear motivation and practical relevance.** The focus on improving text classification with only a few hundred labelled examples is important, and the paper clearly connects augmentation difficulty with curriculum learning.
2. **Simple and deployable method.** CurCon does not add inference-time parameters or require modifications to the downstream classification procedure.
3. **Consistent empirical gains.** The method improves over CERT on all four reported datasets and produces gains across multiple labelled-data regimes.
4. **Useful ablations.** The fixed-mixture, reversed-curriculum, and no-back-translation comparisons provide evidence that the schedule and augmentation ordering matter.
5. **Good presentation.** The method, experimental pipeline, and main findings are described in a readable and logically organized manner.

### Weaknesses and questions

1. **Limited experimental breadth.** The evaluation covers only four English datasets, all consisting primarily of relatively short texts, and uses only BERT-base. Results on additional domains, longer documents, multilingual data, or larger encoders would strengthen the claims.
2. **Baseline tuning fairness needs clarification.** CurCon is selected using a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters from their original papers. A controlled tuning protocol for all methods would make the comparison more compelling.
3. **Statistical testing is absent.** Although means and standard deviations over five seeds are reported, the paper does not provide significance tests or confidence intervals. Given the relatively modest gains over CERT on some datasets, this analysis would help establish robustness.
4. **Curriculum specification could be more precise.** The text states that the probability of applying each operator is determined by the curriculum level, but the exact probability distribution before and after each threshold is not fully formalized. Clarifying whether token dropout remains equally likely when other operators become available would improve reproducibility.
5. **Potential computational and resource dependencies.** WordNet and German back-translation may behave differently across domains. The paper reports that translated views are pre-computed, but the cost of constructing these views and the translation model used should be described more explicitly.
6. **Limited analysis of why the curriculum helps.** The ablations demonstrate an effect, but additional representation-level or training-dynamics analyses could clarify whether the curriculum improves optimization, prevents representation collapse, or simply changes the effective augmentation distribution.

These issues are primarily matters of completeness, experimental rigor, and reproducibility rather than fundamental flaws in the proposed approach. The central method is straightforward, plausible, and supported by consistent results.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 84/100 |
| Novelty | 78/100 |
| Significance | 82/100 |
| Clarity | 88/100 |

**Final average:**  
\[
\frac{84 + 78 + 82 + 88}{4} = 83.0
\]

### Final recommendation: **Accept**

CurCon presents a clear and useful contribution to low-resource text classification. While the experimental scope and baseline-tuning protocol could be strengthened, the method is well motivated, easy to integrate into existing contrastive training pipelines, and demonstrates consistent improvements across datasets and label budgets. The limitations are appropriate for discussion or minor revision and do not undermine the main conclusions.