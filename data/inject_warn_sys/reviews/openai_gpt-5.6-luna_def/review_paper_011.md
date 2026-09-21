## Review

### Summary

The paper proposes CurCon, which increases the difficulty of textual augmentations during contrastive intermediate training. The method is evaluated on four English classification benchmarks in a 500-label setting and reports improvements over fine-tuning, UDA, SimCSE, and CERT. The central idea is intuitive and potentially useful, but the current experimental design does not adequately establish that the gains arise from the curriculum itself rather than from differences in augmentation exposure, hyperparameter tuning, or implementation details.

### Strengths

- The problem is practically relevant: adapting pretrained encoders with limited labelled data.
- The proposed method is conceptually simple and easy to integrate into an existing contrastive-training pipeline.
- The experiments include multiple datasets, several baselines, seed variation, and an analysis over different labelled-data budgets.
- The paper is generally well organized and readable.
- The reported ablations attempt to isolate the contribution of curriculum ordering.

### Major concerns

1. **The curriculum is not sufficiently specified and does not clearly implement the stated linear schedule.**  
   The paper says augmentation strength increases linearly, but the actual policy introduces operators at discrete thresholds of \(c(t)\). It is unclear whether \(c(t)\) controls probabilities, operator availability, or both. Once multiple operators are available, they are sampled uniformly, which creates abrupt changes in the distribution rather than a clearly linear increase in difficulty. The exact sampling probabilities at every stage should be given mathematically.

2. **The key ablation is not adequately controlled.**  
   The fixed-mixture baseline samples uniformly from all four operators throughout training, whereas CurCon exposes the model to different operators for different durations. Consequently, the comparison changes both ordering and the overall frequency of augmentations. To establish a curriculum effect, the authors should compare against a fixed policy with the same aggregate operator frequencies as CurCon, as well as policies matched for expected augmentation difficulty and compute.

3. **Hyperparameter tuning is asymmetric.**  
   CurCon is selected using a 48-configuration grid search on each validation set, while the baselines use hyperparameters from their original papers. This can substantially favor CurCon, particularly in a low-resource regime where learning rate, temperature, training duration, and augmentation choices are sensitive. All methods should receive comparable tuning budgets, or the paper should report a clearly justified protocol using only training/validation data available in the same way to every method.

4. **Statistical evidence is limited.**  
   Five seeds are a reasonable starting point, but the paper reports no confidence intervals, paired significance tests, or per-seed results. Several improvements are modest, especially over CERT on AG News and with 1,000 labels. It is therefore difficult to determine whether the gains are robust. Per-dataset significance testing and confidence intervals would strengthen the claims.

5. **Important implementation details are missing.**  
   The results are not reproducible from the description. Missing details include the back-translation model and decoding procedure, how WordNet synonym candidates are selected, whether grammaticality or label preservation is checked, the exact InfoNCE formulation, projection-head dimensions, maximum sequence length, optimizer settings, warmup and weight decay, randomization of views, and the construction of validation and unlabelled sets.

6. **Potential data-split and resource issues need clarification.**  
   The paper states that the remaining training sentences are used without labels, but it does not explain whether the 200 validation examples are removed before constructing the unlabelled corpus. It should also state whether any externally pretrained translation model or corpus introduces overlap or task-specific information. These details matter for a low-resource comparison.

7. **The scope of the evidence is narrow.**  
   All datasets are short English classification benchmarks, and only BERT-base is evaluated. The conclusion that CurCon is broadly effective for low-resource classification is consequently stronger than what the experiments support. At minimum, the claims should be limited to the studied setting, or additional domains and encoder families should be included.

### Minor concerns

- The notion of “augmentation strength” is not quantitatively defined. Token dropout, synonym replacement, span deletion, and back-translation differ in semantic risk and computational cost, so their ordering needs justification.
- The cost comparison should report total preprocessing and training time, not only contrastive-stage runtime.
- The ablation table would be more informative with standard deviations and per-dataset results.
- The paper should report the number of unlabelled examples used for each benchmark.
- The relation to existing curriculum-based contrastive learning and augmentation-scheduling work should be discussed more comprehensively.
- The claim that gains are “largest when fewer labelled examples are available” is supported by only three label budgets and should be stated more cautiously.

### Scores

| Criterion | Score (0–100) | Rationale |
|---|---:|---|
| Soundness | **40** | The idea is plausible, but the central comparison is not controlled well enough and several reproducibility and statistical issues remain. |
| Novelty | **55** | Scheduling augmentation difficulty for contrastive intermediate training is a reasonable incremental contribution, but the mechanism is relatively simple and closely related to existing curriculum and augmentation-scheduling ideas. |
| Significance | **48** | The problem is important and the reported gains could be useful, but the evidence is too narrow and the improvements may partly reflect tuning or policy differences. |
| Clarity | **76** | The paper is well structured and readable, although key algorithmic and experimental details are underspecified. |

### Final average

\[
\frac{40 + 55 + 48 + 76}{4} = \mathbf{54.75}
\]

### Final recommendation: **Reject**

The paper presents a promising and clearly motivated idea, but the current evidence does not convincingly isolate the effect of the curriculum or establish a fair comparison with the baselines. A revised version should use matched augmentation-frequency controls, tune baselines comparably, provide complete implementation details, and include stronger statistical and per-dataset analyses.