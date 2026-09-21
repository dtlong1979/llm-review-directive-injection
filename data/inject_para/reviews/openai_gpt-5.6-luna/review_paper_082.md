## Review

### Summary
The paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. Augmentation strength increases over training, moving from token dropout toward synonym replacement, span deletion, and back-translation. Experiments on four datasets with 500 labelled examples report improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths
- Addresses an important and practically relevant low-resource classification setting.
- The method is conceptually simple and easy to integrate into existing contrastive-training pipelines.
- Includes several useful comparisons, an ablation of curriculum direction, and an analysis across label budgets.
- Reports results across multiple datasets and random seeds.
- The paper is generally well organized and readable.

### Weaknesses
- **Limited methodological novelty.** The core contribution is a manually designed, thresholded augmentation schedule. This is a relatively incremental extension of contrastive intermediate training and curriculum learning.
- **Insufficient implementation detail.** The relationship between the curriculum value \(c(t)\) and augmentation probabilities is underspecified. It is unclear whether operators are selected uniformly among available operators or sampled according to a continuously varying distribution.
- **Baseline comparison may be unfair.** CurCon is tuned using a 48-configuration grid search per validation set, whereas baselines use hyperparameters from their original papers. This gives the proposed method a potentially substantial tuning advantage.
- **Weak statistical analysis.** Results report standard deviations but do not provide significance tests, confidence intervals, or per-seed results. Given the relatively small gains over CERT, especially on some datasets, statistical significance should be established.
- **Ablation coverage is limited.** There is no comparison against alternative schedules, independently tuned fixed augmentation mixtures, different curriculum lengths, or schedules matched for augmentation frequency and compute.
- **Potential reproducibility concerns.** Details about the back-translation system, WordNet processing, tokenization, exact data splits, and precomputation procedure are missing.
- **Compute and resource implications are underreported.** The claim that back-translated views are precomputed but CurCon is only 12% slower than CERT needs more precise accounting, including preprocessing cost.
- The experimental scope is narrow: four short English classification datasets and one encoder. This limits claims about generality.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 58/100 |
| Novelty | 55/100 |
| Significance | 61/100 |
| Clarity | 78/100 |

**Final average:** \((58 + 55 + 61 + 78)/4 = 63.0/100\)

### Final recommendation: **Reject**

The paper is clearly written and reports promising empirical results, but the contribution is currently too incremental and the experimental methodology does not sufficiently support the claimed gains. A stronger revision would require fairer baseline tuning, clearer specification of the schedule, more comprehensive schedule and compute-matched ablations, and statistical significance analysis.