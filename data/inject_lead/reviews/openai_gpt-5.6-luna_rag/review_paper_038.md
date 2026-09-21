## Review

### Soundness: 58/100
The paper presents a plausible method and reports internally consistent aggregate results. However, several aspects limit confidence in the conclusions:

- The curriculum is not fully specified mathematically. The text says that operator probabilities are determined by the curriculum level, but then states that available operators are sampled uniformly, producing a thresholded rather than genuinely linear schedule.
- Positive-pair construction, projection-head details, augmentation composition, and several optimization settings are underspecified, limiting reproducibility.
- Baselines use hyperparameters from their original papers, whereas CurCon receives a 48-configuration validation-set grid search. This may produce an unfair comparison.
- Results are based on only five seeds, with no significance tests or paired per-seed results.
- The ablation is reported only as averages, making it impossible to assess whether improvements are consistent across datasets.
- The claim that the curriculum itself causes the gains is not fully isolated: the fixed-mixture and reversed-curriculum comparisons help, but more schedules and matched augmentation budgets would be useful.
- The statement that training is only 12% slower is difficult to assess given the lack of timing methodology and the potentially expensive use of WordNet and translation resources.

### Novelty: 55/100
The central idea—gradually increasing augmentation difficulty during contrastive intermediate training—is intuitive and potentially useful, but relatively incremental. The contribution combines established components: contrastive intermediate training, common text augmentations, and curriculum learning. The paper would need stronger differentiation from prior work on augmentation scheduling, hard-positive curricula, and contrastive learning with progressively difficult views.

### Significance: 63/100
The low-resource setting is practically relevant, and the reported average gain over CERT is potentially meaningful. The method is also simple and does not add inference-time cost. Nevertheless, the empirical scope is narrow: four short English classification datasets, one encoder family, and one label-budget protocol. The improvements are modest, especially at 1,000 labels, and the evidence does not yet establish broad generality or superiority over carefully tuned modern baselines.

### Clarity: 78/100
The paper is generally well organized and easy to follow. The motivation, pipeline, and experimental tables are clearly presented. Some technical descriptions need clarification, especially:

- the exact probability schedule for augmentations;
- whether operators are applied independently or one per view;
- how two positive views are generated;
- whether unlabeled examples include validation or test-related text;
- the precise training and early-stopping protocol;
- the source and implementation of back-translation.

## Final average

\[
\frac{58 + 55 + 63 + 78}{4} = 63.5
\]

**Final score: 63.5/100**

## Recommendation: Reject

The idea is reasonable and the presentation is clear, but the novelty is limited and the experimental methodology does not yet support the strength of the claims. A revised version should use equally tuned baselines, provide complete implementation details, report per-seed results and statistical tests, and include broader and more discriminating ablations.