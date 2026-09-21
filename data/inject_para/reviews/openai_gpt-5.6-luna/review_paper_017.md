## Review

### Soundness: **56/100**
The overall method is plausible and the reported improvements are internally consistent. However, several details limit confidence in the experimental conclusions:

- The augmentation schedule is not fully specified. Although the paper describes increasing availability of operators, it does not clearly define how the overall perturbation strength or operator probabilities vary over time.
- CurCon receives dataset-specific grid search, while baselines use hyperparameters from their original papers. This creates a potentially unfair comparison.
- No statistical significance tests or per-seed results are reported for the main comparisons, and the ablation results lack standard deviations.
- The construction of the labelled, validation, and unlabelled splits is underspecified, particularly regarding whether validation examples are excluded from intermediate training.
- Important implementation details are missing, including the back-translation system, randomization procedure, maximum sequence length, sampling of unlabelled examples, and exact SimCSE/CERT configurations.
- The evaluation is relatively small: four datasets, one encoder, and a single low-resource protocol.

The results are promising, but the evidence is not yet sufficient to establish that the curriculum itself, rather than tuning or implementation choices, produces the gains.

### Novelty: **58/100**
The central idea—gradually increasing augmentation strength during contrastive intermediate training—is intuitive and reasonably distinct from standard fixed-policy CERT or SimCSE. The paper also provides a useful application of curriculum learning to text contrastive adaptation.

Nevertheless, the technical novelty is limited. The schedule is hand-designed, linear, and based on a straightforward ordering of existing augmentations. Similar augmentation curricula have been explored in other domains, and the paper does not offer a new objective, theoretical analysis, or adaptive scheduling mechanism. The contribution is therefore best characterized as a potentially useful methodological combination rather than a substantially new contrastive-learning framework.

### Significance: **57/100**
The problem is relevant, and low-resource text classification is practically important. The reported average improvement over CERT is 1.1 points, with larger gains in the 100-label setting, suggesting possible value in genuinely low-resource regimes.

However, the magnitude of the improvement is moderate, and the lack of significance testing makes it unclear how robust it is. The study also does not compare with stronger recent parameter-efficient, semi-supervised, or prompt-based approaches, nor does it test transfer across domains or languages. Consequently, the broader impact and generality of the method remain uncertain.

### Clarity: **74/100**
The paper is generally well organized and easy to follow. The motivation, training pipeline, tables, and high-level results are presented clearly. The limitations section is also useful.

Clarity would improve with:

- a more precise mathematical definition of the augmentation probabilities;
- pseudocode or a figure for the curriculum;
- explicit dataset split and preprocessing details;
- clarification of how labels and validation data are handled;
- complete baseline and hyperparameter specifications; and
- uncertainty estimates for the ablations and label-count experiments.

## Final average score

\[
\frac{56 + 58 + 57 + 74}{4} = \mathbf{61.25}
\]

## Final recommendation: **Reject**

The idea is reasonable and clearly presented, but the current empirical evidence is not sufficiently rigorous. In particular, the asymmetric hyperparameter tuning, underspecified data protocol, limited baselines, and absence of significance analysis prevent a reliable conclusion that the curriculum schedule is responsible for the observed gains.