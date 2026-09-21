## Review

### Soundness: 58/100
The overall method is plausible and the experimental design is directionally appropriate, but several details weaken confidence in the conclusions:

- The curriculum policy is underspecified. It is unclear how the probability of each available augmentation depends on \(c(t)\), especially before all operators become available.
- CurCon is tuned over 48 configurations per dataset, while baselines use hyperparameters from their original papers. This creates an uneven comparison and may inflate CurCon’s advantage.
- No statistical significance tests or paired seed-level comparisons are reported, despite relatively small gains over CERT.
- The ablation does not isolate whether gains come from the curriculum itself, the particular augmentation mixture, or unequal exposure to augmentations over training.
- The claim that the curriculum adds only 12% runtime is difficult to assess without details about preprocessing, back-translation generation, and the exact CERT implementation.
- The use of the “remaining training sentences” and a separate validation set needs clearer clarification to rule out overlap or validation leakage.
- The experiments are limited to four relatively small English benchmarks and one encoder, so robustness is not established.

The reported trends are coherent, but the evidence is not yet sufficiently controlled to support strong causal claims about the curriculum.

### Novelty: 57/100
Scheduling augmentation difficulty during contrastive intermediate training is a reasonable and potentially useful idea. However, the contribution appears incremental:

- Curriculum learning and augmentation scheduling are established concepts.
- The method mainly combines known text augmentations with a manually designed linear schedule.
- The paper does not clearly distinguish CurCon from prior work on augmentation-magnitude schedules, adaptive contrastive learning, or curriculum-based consistency training.
- The proposed schedule is hand-designed, with threshold-based operator activation, rather than offering a substantially new learning objective or adaptive mechanism.

The application to low-resource text classification is relevant, but the conceptual novelty is moderate rather than high.

### Significance: 54/100
The reported average improvement over CERT is 1.1 points, and the gains are larger in the 100-label setting. If reliable, this could be practically useful. Nevertheless:

- The absolute gains are modest.
- The evaluation covers only four datasets, all in English and mostly short-text classification.
- There is no comparison with stronger modern parameter-efficient, prompt-based, or semi-supervised baselines.
- The computational cost and dependence on WordNet and machine translation reduce practical universality.
- The paper does not establish whether the method transfers to domains where back-translation or synonym resources are less reliable.

Thus, the work may be useful as an incremental method, but its broad scientific or practical impact is currently limited.

### Clarity: 78/100
The paper is generally well organized and easy to follow. The motivation, pipeline, and main results are clearly presented. However, several important implementation details are ambiguous:

- The exact augmentation sampling probabilities are not specified.
- The definition of a “curriculum length” and the behavior at \(L=0\) are not fully formalized.
- Dataset splits, validation construction, and unlabeled-data usage need more detail.
- Baseline training and tuning procedures are not described symmetrically.
- The paper should report confidence intervals or per-seed results and clarify whether all methods use identical unlabeled data and compute budgets.

### Final average

\[
\frac{58 + 57 + 54 + 78}{4} = 61.75
\]

**Final score: 61.8/100**

### Recommendation: Reject

The paper presents a plausible and clearly motivated incremental method, but the current evidence is insufficient for acceptance. A revised version should provide a fully specified curriculum policy, tune all baselines comparably, include stronger and more recent baselines, perform more informative ablations and significance testing, and broaden the evaluation.