## Review

### Summary
This paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually expands the augmentation policy from token dropout to synonym replacement, span deletion, and back-translation before supervised fine-tuning. Experiments on four English benchmarks with 500 labelled examples show improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths
- The problem is practically relevant: exploiting unlabelled in-domain text when labelled data are scarce.
- The method is simple and compatible with standard encoder fine-tuning pipelines.
- Experiments include several reasonable baselines, multiple datasets, multiple random seeds, ablations, and label-budget comparisons.
- The ablation results support the claim that curriculum ordering contributes beyond using a fixed augmentation mixture.
- The paper is generally well organized and readable.

### Concerns
- The methodological novelty is incremental. The main contribution is a manually designed schedule over known augmentation operators, and the connection to curriculum-based augmentation is fairly direct.
- The augmentation description is somewhat ambiguous. The paper says that operator probabilities are determined by the curriculum level, but also says that available operators are sampled uniformly. These imply different schedules and should be specified precisely.
- The comparison may not be fully fair: CurCon is tuned over 48 configurations separately for each dataset, whereas the baselines use hyperparameters from their original papers. Baselines should ideally receive comparable tuning under the same low-resource protocol.
- The experimental evidence is limited to four short English datasets and BERT-base. There are no analyses of statistical significance, robustness to different unlabelled-data sizes, or sensitivity to the curriculum length and augmentation probabilities.
- The paper does not provide enough implementation detail to ensure reproducibility, including exact data splits, augmentation randomization, back-translation model, preprocessing, and the precise CERT/SimCSE training setup.
- The claim that the curriculum is particularly beneficial in lower-label regimes is supported by only three label budgets and no variance estimates in Table 3.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 76/100 |
| Novelty | 62/100 |
| Significance | 70/100 |
| Clarity | 84/100 |
| **Final average** | **73.0/100** |

### Final recommendation: **Accept**

The empirical results are promising and the method is clearly presented, but the contribution would be stronger with a more rigorous baseline-tuning protocol, clearer specification of the schedule, and broader robustness experiments.