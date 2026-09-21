## Review

### Summary
The paper proposes CurCon, a contrastive intermediate-training method that gradually increases text augmentation strength during training. It evaluates the method on four datasets with 500 labelled examples each and reports improvements over fine-tuning, UDA, SimCSE, and CERT.

### Soundness: **55/100**
The overall experimental design is plausible, but several issues weaken confidence in the conclusions:

- The curriculum is not fully specified. The paper defines availability thresholds for augmentations, but does not clearly state how operator probabilities vary with the curriculum level or how two views are sampled.
- CurCon is tuned through a 48-configuration grid search separately for each validation set, whereas the baselines use hyperparameters from their original papers. This creates a potentially substantial comparison advantage for CurCon.
- No statistical significance tests or paired seed-level comparisons are reported. The improvements over CERT are relatively modest, especially on some datasets.
- The construction of the labelled, validation, and unlabelled splits is underspecified. It is unclear whether the validation examples are removed from the unlabelled contrastive corpus and whether all methods use exactly the same data.
- The claim that back-translation is precomputed but that CurCon takes longer due to on-the-fly augmentation should be explained more carefully.
- Important implementation details are missing, including the precise CERT and SimCSE configurations, projection-head handling, maximum sequence length, augmentation failure rates, and the source/model used for back-translation.

The reported results are internally consistent, but the evidence is not yet sufficient to establish that the curriculum itself, rather than tuning or augmentation composition, produces the gains.

### Novelty: **58/100**
The idea of increasing augmentation difficulty during contrastive training is reasonable, but the conceptual contribution is fairly incremental. Curriculum learning and augmentation scheduling are established ideas, and the paper applies them to an existing CERT-style pipeline. The paper would be more novel if it provided:

- A principled schedule derived from representation difficulty or semantic similarity;
- Comparisons against fixed-strength schedules, random schedules, and smoothly weighted mixtures;
- An analysis separating the effect of the augmentation set from the effect of its ordering;
- A theoretical or empirical explanation of why the schedule benefits contrastive learning specifically.

The method is simple and potentially useful, but the current contribution is primarily an engineering combination of known components.

### Significance: **63/100**
The problem is important, and improvements in low-resource classification could be practically valuable. The reported average gain of 1.1 points over CERT and 3.8 points over direct fine-tuning is promising, particularly in the 100-label setting.

However, the significance is limited by:

- Evaluation on only four relatively small English benchmarks;
- Use of a single encoder family;
- Lack of comparison with stronger modern parameter-efficient, prompt-based, or semi-supervised methods;
- Unclear robustness across domains and augmentation resources;
- Potentially unfair hyperparameter treatment between CurCon and baselines.

The results suggest practical value, but broader evidence is needed to support a strong claim of general usefulness.

### Clarity: **78/100**
The paper is generally well organized and easy to follow. The motivation, pipeline, datasets, and main results are presented clearly. The tables are concise and the limitations section is appropriate.

Clarity is reduced by several ambiguities:

- The exact curriculum probability distribution is unclear.
- The definition of “curriculum length” and its relationship to the 20,000 training steps could be more explicit.
- The data split protocol is not sufficiently detailed.
- The baseline training and tuning procedures are not described symmetrically.
- The paper should distinguish more clearly between augmentation availability, augmentation probability, and augmentation strength.

### Final Score

\[
\frac{55 + 58 + 63 + 78}{4} = 63.5
\]

**Final average score: 63.5/100**

## Recommendation: **Reject**

The paper presents a sensible and potentially useful idea, but the current evaluation does not adequately isolate the contribution of the curriculum and leaves important reproducibility and fairness concerns unresolved. A stronger revision should use equally tuned baselines, provide complete split and augmentation details, include fixed-schedule and random-order controls, report statistical tests, and evaluate on a broader set of models and tasks.