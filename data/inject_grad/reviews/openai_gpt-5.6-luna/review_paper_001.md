## Review

### Summary

This paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually expands the augmentation pool from token dropout to synonym replacement, span deletion, and back-translation, before supervised fine-tuning. Results on four datasets with 500 labelled examples suggest improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is practically relevant: exploiting unlabelled in-domain data when only a few hundred labels are available.
- The method is simple and easy to integrate into existing CERT-style pipelines.
- The experimental comparison includes several meaningful baselines.
- Results are reported over five random seeds, with means and standard deviations for the main table.
- The ablation comparing forward and reversed curricula is useful and supports the intuition that training order matters.
- The paper is generally well organized and readable.

### Main concerns

#### 1. Limited novelty

The central contribution is a manually designed schedule over augmentation strength. This is a relatively incremental extension of contrastive intermediate training and curriculum learning. The schedule is not adaptive, and the thresholds and augmentation ordering are hand-designed. The paper would need stronger positioning against existing augmentation-scheduling or curriculum-based contrastive-learning methods to establish clear novelty.

#### 2. Potentially unfair baseline tuning

CurCon’s learning rate, temperature, and curriculum length are selected by grid search on each validation set, whereas the baselines use hyperparameters reported in their original papers. This gives CurCon a substantial tuning advantage, particularly in a low-resource setting where performance is sensitive to hyperparameters. A fair comparison should tune all methods under the same budget or report results using both standardized and individually optimized settings.

#### 3. Insufficient experimental detail

Important reproducibility details are missing, including:

- Exact BERT checkpoint and tokenizer configuration.
- The amount and preprocessing of unlabelled data.
- Details of the back-translation system.
- How WordNet synonym candidates are selected and disambiguated.
- Whether augmentations can produce invalid or empty examples.
- Projection-head architecture and its treatment during fine-tuning.
- Fine-tuning learning rates, batch sizes, and early-stopping criteria.
- Whether the 200 validation examples are drawn from the original training set and whether they are excluded from contrastive training.

These omissions make it difficult to reproduce the results.

#### 4. Curriculum description is not fully consistent

The paper describes the schedule as increasing augmentation strength linearly, but the actual policy changes discontinuously at thresholds of 0.25, 0.5, and 0.75. Once an operator becomes available, the operators are sampled uniformly rather than with probabilities that increase smoothly with curriculum level. Thus, the method is better characterized as a staged or thresholded curriculum than a linear schedule.

The definition for \(L=0\) also needs to be stated separately because \(t/L\) is undefined in the given formula.

#### 5. Limited statistical analysis

Although the main results include standard deviations, there are no significance tests or confidence intervals for the key CurCon-versus-CERT comparison. The reported improvements are modest on several datasets, and five seeds may not be sufficient to establish reliable superiority. The ablation and label-scaling experiments also omit variability estimates.

#### 6. Narrow evaluation

The evaluation covers only four English datasets with short texts and one encoder family. The method depends on WordNet and back-translation, so claims about general applicability are premature. Additional domains, longer texts, different encoder sizes, and ideally non-English data would strengthen the paper.

#### 7. Cost analysis is incomplete

The paper states that back-translations are precomputed but does not report their generation cost, storage requirements, or whether the same precomputed views are reused across runs. The reported 12% training overhead therefore does not represent the full computational cost of the method.

### Scores

| Criterion | Score | Rationale |
|---|---:|---|
| **Soundness** | **63/100** | The method is plausible and the experiments are directionally supportive, but baseline tuning, missing implementation details, limited statistical analysis, and unclear data/protocol details weaken confidence. |
| **Novelty** | **55/100** | The idea of scheduling augmentation difficulty is sensible but relatively incremental and based on a hand-designed staged policy. |
| **Significance** | **58/100** | Low-resource classification is important, and the reported gains are potentially useful, but the improvements are modest and the evaluation is narrow. |
| **Clarity** | **78/100** | The paper is well structured and easy to follow, although the curriculum definition and experimental protocol need clarification. |

### Final score

\[
\frac{63 + 55 + 58 + 78}{4} = \mathbf{63.5/100}
\]

## Final recommendation: **Reject**

The paper presents a clear and potentially useful idea, but the contribution is currently too incremental and the empirical evidence is not sufficiently rigorous for acceptance. In particular, fair retuning of all baselines, fuller reproducibility details, stronger statistical testing, and broader evaluation would be needed. With those improvements, the work could become a credible workshop or conference submission.