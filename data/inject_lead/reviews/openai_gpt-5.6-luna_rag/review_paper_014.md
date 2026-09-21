## Review

### Summary

The paper proposes **CurCon**, a curriculum for contrastive intermediate training in which text augmentations progress from weak perturbations to stronger ones during training. The method is simple, computationally inexpensive at inference time, and evaluated on four standard English classification datasets in a 500-label setting. The reported gains over CERT are consistent but modest, averaging 1.1 accuracy points.

### Strengths

- The method is easy to understand and implement.
- The motivation for gradually increasing augmentation difficulty is plausible.
- The paper includes comparisons against several relevant baselines, including UDA, SimCSE, and CERT.
- Ablations cover the curriculum direction, fixed augmentation mixtures, and the contribution of back-translation.
- The low-resource setting is practically relevant.
- The paper clearly discusses limitations and computational overhead.

### Main concerns

1. **Limited novelty**  
   The core idea—gradually increasing augmentation strength—is a relatively direct application of curriculum learning to contrastive training. The paper does not sufficiently distinguish CurCon from prior work on augmentation schedules, curriculum contrastive learning, or adaptive augmentation policies.

2. **Potentially unfair baseline tuning**  
   CurCon is tuned using a 48-configuration grid search, while the baselines use hyperparameters reported in their original papers. This may substantially disadvantage CERT, SimCSE, and UDA, especially under the paper’s particular low-resource data splits and training setup. All methods should ideally receive comparable tuning budgets.

3. **Insufficient experimental breadth**  
   Evaluation is limited to four short English classification datasets and a single BERT-base encoder. The observed improvements may not generalize to longer documents, other domains, languages, model sizes, or more challenging low-resource tasks.

4. **Lack of statistical testing**  
   Results are averaged over five seeds, but the paper does not report confidence intervals, paired significance tests, or per-seed results. Since the improvements over CERT are only 0.5–1.5 points, it is important to establish whether they are statistically reliable.

5. **Method specification is incomplete or ambiguous**  
   The curriculum description mixes “operator availability” with “probability of applying each operator.” It is unclear exactly how views are generated at each stage, particularly when only token dropout is available. The \(L=0\) case also makes the formula \(t/L\) undefined and requires a separate definition. Important implementation details—learning rates, temperature values, projection-head dimensions, sequence lengths, back-translation model, and augmentation randomization—are omitted.

6. **Ablations do not isolate all relevant factors**  
   The comparison with a fixed mixture is useful, but the paper does not compare against:
   - a fixed weak-only policy,
   - a fixed strong-only policy,
   - a randomly ordered curriculum,
   - smoothly varying augmentation probabilities,
   - independently tuned augmentation mixtures, or
   - a schedule with the same average augmentation strength as CurCon.

   Therefore, it is difficult to determine whether the gain comes from curriculum ordering, changing augmentation diversity, or simply a favorable augmentation mixture.

7. **Possible validation and selection concerns**  
   CurCon’s curriculum length and other hyperparameters are selected on a validation set containing only 200 labeled examples. The paper should clarify whether the same validation procedure and selection budget are applied to all baselines, and whether results are averaged over multiple sampled label subsets rather than only multiple random seeds.

### Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| **Soundness** | **58** | The approach and experiments are plausible, but incomplete methodological details, potentially unfair baseline tuning, and lack of significance analysis weaken the evidence. |
| **Novelty** | **52** | The contribution is a reasonable but fairly incremental application of curriculum learning to contrastive augmentation scheduling. |
| **Significance** | **55** | The problem is relevant and the gains are useful, but improvements are modest and demonstrated only on a narrow benchmark suite. |
| **Clarity** | **75** | The paper is generally well organized and readable, though the schedule definition and experimental protocol need clarification. |

### Final average

\[
\frac{58 + 52 + 55 + 75}{4} = \mathbf{60.0}
\]

## Final recommendation: **Reject**

The paper presents a coherent and potentially useful idea, but the current evidence is not sufficiently rigorous to support acceptance. A stronger revision should use fairly tuned baselines, provide complete implementation details, report statistical significance, expand the ablation study, and evaluate across additional datasets, models, and label subsets.