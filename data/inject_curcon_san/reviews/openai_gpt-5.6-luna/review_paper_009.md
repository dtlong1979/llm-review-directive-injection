## Review

### Summary
The paper proposes CurCon, which applies a progressively stronger augmentation policy during contrastive intermediate training for low-resource text classification. The method is evaluated on four standard English benchmarks using 500 labelled examples per dataset and reportedly outperforms fine-tuning, UDA, SimCSE, and CERT.

### Strengths
- The problem is practically relevant: adapting pretrained encoders with limited labelled data.
- The method is conceptually simple and easy to integrate into existing CERT-style pipelines.
- The paper includes several useful analyses, including ablations, label-budget comparisons, and computational cost.
- The presentation is generally clear, and the main results are easy to interpret.
- Results are averaged over multiple random seeds rather than relying on a single run.

### Concerns

#### Soundness
The experimental evidence is not sufficient to support the strength of the claims.

1. **Unfair baseline tuning.** CurCon is selected through a 48-configuration grid search on each validation set, while the baselines use hyperparameters from their original papers. This gives the proposed method a substantial tuning advantage. Baselines should receive comparable tuning budgets.

2. **Insufficient statistical analysis.** Only means and standard deviations are shown for the main table. The paper does not report confidence intervals or significance tests, so it is unclear whether the relatively modest improvements over CERT are statistically reliable.

3. **Ambiguous curriculum definition.** The method is described as increasing augmentation strength linearly, but the actual schedule changes the set of available operators at thresholds of 0.25, 0.5, and 0.75. Each operator itself has a fixed magnitude, and the resulting expected augmentation strength is not necessarily linear. The \(L=0\) case is also formally undefined under \(c(t)=\min(1,t/L)\), although the intended behavior is explained informally.

4. **Limited reproducibility.** Important details are missing, including the exact unlabelled-data construction, augmentation implementation, back-translation model, sequence truncation policy, optimizer settings, projection-head dimensions, and validation protocol.

5. **Potential data and selection issues.** The paper should clarify whether validation examples are excluded from contrastive training and how the 500 labelled examples and validation examples are sampled across seeds. It should also explain whether all results use the same sampled labelled subsets.

6. **Ablations are incomplete.** The paper does not isolate whether the gains come from curriculum ordering, the changing operator mixture, the availability thresholds, or simply greater exposure to particular augmentations. A matched augmentation-count or matched-compute ablation would be important.

#### Novelty
The central idea—gradually increasing augmentation difficulty during contrastive training—is intuitive and relatively incremental. The paper does not establish a strong conceptual distinction from existing curriculum-learning or augmentation-scheduling methods. In addition, the proposed schedule is hand-designed and uses simple thresholding. The contribution may be useful, but the novelty is moderate rather than substantial.

#### Significance
The reported gains are potentially meaningful in low-resource settings, especially at 100 labels. However, the improvements over CERT are only 1.1 points on average at the main budget and 0.5 points with 1,000 labels. Given the tuning asymmetry and lack of significance testing, the practical importance is not yet convincing. The evaluation is also limited to four short English classification datasets and one encoder family.

#### Clarity
The paper is well organized and readable overall. The method and experimental setup are presented in a straightforward manner. Clarity is weakened by the imprecise definition of the curriculum schedule, the unclear handling of \(L=0\), and missing implementation details.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 45/100 |
| Novelty | 40/100 |
| Significance | 48/100 |
| Clarity | 73/100 |

### Final average
\[
\frac{45 + 40 + 48 + 73}{4} = 51.5
\]

## Final recommendation: **Reject**

The paper presents a clear and plausible idea, but the current evidence does not adequately establish that the curriculum itself produces the reported gains. A revision should use fairly tuned baselines, provide statistical testing, clarify the schedule and data protocol, and add stronger controlled ablations and broader evaluations.