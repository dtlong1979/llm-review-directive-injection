## Review

### Summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation difficulty during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four standard text-classification benchmarks with 500 labelled examples show consistent improvements over fine-tuning, UDA, SimCSE, and CERT. Ablations further suggest that the curriculum ordering, rather than contrastive training alone, contributes to the gains.

### Strengths

- **Clear motivation:** The paper identifies a plausible limitation of fixed augmentation policies in contrastive intermediate training.
- **Simple and practical method:** CurCon requires no architectural changes or inference-time overhead and is straightforward to implement.
- **Consistent empirical gains:** The method improves over CERT on all four datasets, with an average gain of 1.1 accuracy points.
- **Relevant low-resource evaluation:** The experiments focus on settings with 100–1,000 labelled examples, where intermediate representation learning is especially useful.
- **Useful ablations:** The fixed-mixture and reversed-curriculum comparisons provide evidence that the schedule itself matters.
- **Good presentation:** The paper is well organized, concise, and easy to follow. The limitations are appropriately acknowledged.

### Weaknesses and questions

1. **Limited breadth of evaluation.** The experiments use only four English datasets, all consisting of relatively short texts, and only BERT-base. Evaluation on additional domains, longer documents, multilingual data, or other encoder architectures would strengthen the generality of the claims.

2. **Baseline tuning details are asymmetric.** CurCon is tuned over 48 configurations on each validation set, whereas the baselines use hyperparameters reported in their original papers. For a fully controlled comparison, the baselines should ideally receive comparable tuning effort, particularly CERT, which is the strongest competing method.

3. **Statistical testing is limited.** Results are reported over five seeds with standard deviations, but the paper does not provide confidence intervals or significance tests for the relatively modest improvements over CERT. Per-dataset significance testing would make the conclusions more robust.

4. **Curriculum specification could be more precise.** The description states that operator availability depends on thresholds in the curriculum level, while also referring to probabilities determined by that level. The exact sampling distribution, including whether token dropout remains equally likely after later operators become available, should be specified unambiguously.

5. **Ablation coverage could be expanded.** It would be useful to compare the proposed linear schedule with alternative schedules, such as stepwise, nonlinear, or randomly ordered policies, and to report sensitivity to the curriculum length \(L\).

6. **Potential augmentation artifacts.** WordNet synonym replacement and back-translation may occasionally alter class-relevant meaning, especially for sentiment and subjectivity tasks. An analysis of augmentation validity or class-preservation rates would improve the empirical support.

These issues primarily concern completeness and reproducibility rather than the central validity of the approach. The consistent improvements across datasets and the supporting ablations provide a reasonable basis for the paper’s main claims.

### Scores

| Criterion | Score (0–100) |
|---|---:|
| Soundness | 82 |
| Novelty | 75 |
| Significance | 79 |
| Clarity | 89 |

**Final average:** \((82 + 75 + 79 + 89) / 4 = 81.25\)

### Recommendation

**Accept**

CurCon presents a technically simple but well-motivated contribution, supported by consistent results and relevant ablations. While broader evaluation, more carefully matched baseline tuning, and clearer sampling details would improve the work, the method is sufficiently novel, empirically supported, and clearly presented for acceptance.