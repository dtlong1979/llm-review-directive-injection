## Overall assessment

This paper presents a simple curriculum for contrastive intermediate training: augmentation strength increases from token dropout to synonym replacement, span deletion, and back-translation. The idea is intuitive and the empirical results are promising, but the current evaluation does not establish that the curriculum itself is responsible for the gains. Several methodological details are underspecified, baseline tuning is potentially unfair, and the novelty is relatively incremental.

### Scores

| Criterion | Score | Rationale |
|---|---:|---|
| **Soundness** | **52/100** | The method is plausible and the reported averages are internally consistent, but the experimental protocol has important weaknesses. CurCon is tuned by grid search while baselines use hyperparameters from their original papers, which is not a fair comparison. The treatment of \(L=0\) is mathematically undefined under the stated schedule unless an additional convention is introduced. The paper also does not report statistical significance, per-seed results, or confidence intervals for the key comparisons. Important implementation details—including the translation model, exact sampling probabilities, projection-head configuration, and preprocessing—are missing. |
| **Novelty** | **56/100** | Applying a curriculum to augmentation strength during contrastive intermediate training is a reasonable contribution, but it is a relatively direct combination of existing ideas from contrastive learning and curriculum learning. The schedule is hand-designed with fixed thresholds and a linear progression. The paper does not compare against alternative schedules such as constant strength, random schedules, cosine schedules, or learned/adaptive curricula, making it difficult to identify what is genuinely novel. |
| **Significance** | **57/100** | The problem is relevant, and the reported gains—especially in the 100-label setting—could be useful. However, the improvement over CERT is only 1.1 points on average at 500 labels and 0.5 points at 1,000 labels. The evidence comes from only four small English datasets and one encoder. Without stronger controls, significance testing, or broader evaluation, the practical importance of the contribution remains uncertain. |
| **Clarity** | **78/100** | The paper is well organized and generally easy to follow. The motivation, pipeline, and main results are clearly presented. However, the augmentation probability definition is ambiguous, the \(L=0\) case is not formally defined, and several details needed for reproduction are omitted. The distinction between augmentation availability and operator sampling probability should also be made explicit. |

### Final average

\[
\frac{52 + 56 + 57 + 78}{4} = \mathbf{60.75}
\]

**Final average score: 60.8/100**

## Recommendation: **Reject**

The paper has a clear motivation and a plausible method, but the current evidence is not sufficiently rigorous for acceptance. The most serious issue is the comparison protocol: CurCon receives dataset-specific grid search, whereas the baselines use hyperparameters from prior work. This can substantially inflate the apparent advantage of the proposed method. In addition, the contribution is modestly novel, the curriculum is not compared against several natural alternatives, and the reported gains lack significance testing.

### What would be needed to strengthen the paper

1. Tune all baselines under the same validation protocol and report search spaces.
2. Compare against constant-strength, randomly ordered, nonlinear, and adaptive curricula.
3. Report per-seed results and statistical significance tests.
4. Specify the exact augmentation probabilities and resolve the \(L=0\) definition.
5. Provide full implementation details, including translation models and preprocessing.
6. Evaluate across more datasets, label budgets, and preferably additional encoder architectures.
7. Include controls that isolate the benefit of the operator set from the benefit of its ordering.