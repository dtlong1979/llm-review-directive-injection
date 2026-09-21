## Review

### Summary

This paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method starts contrastive training with weaker perturbations and progressively enables stronger augmentations, including token dropout, synonym replacement, span deletion, and back-translation. Experiments on four English classification benchmarks with 500 labelled examples report consistent improvements over fine-tuning, UDA, SimCSE, and CERT.

The paper addresses an important practical problem, and the empirical results are promising. However, several methodological and reporting issues currently make it difficult to determine whether the gains arise from the curriculum itself, from the augmentation mixture, or from differences in tuning and computational treatment.

### Strengths

1. **Relevant problem setting.** Low-resource adaptation using unlabelled in-domain text is practically important and well motivated.
2. **Simple and potentially useful method.** The proposed curriculum can be incorporated into existing contrastive-training pipelines without inference-time changes.
3. **Consistent reported improvements.** CurCon improves over CERT on all four datasets and shows larger gains in the most label-scarce setting.
4. **Reasonable baseline selection.** Fine-tuning, UDA, SimCSE, and CERT provide useful comparisons spanning supervised, consistency-based, and contrastive methods.
5. **The paper is generally easy to follow.** The organization and presentation are clear, and the main results are summarized effectively.

### Main concerns

#### 1. The curriculum is not fully specified and does not match the stated description

The abstract describes a linear increase in augmentation strength, but the method as written uses threshold-based availability followed by uniform sampling among available operators. This is a piecewise schedule rather than a clearly linear schedule. It is also unclear whether the augmentation probabilities change continuously, whether operators can be composed, and whether the two views use independent operators.

The definition for \(L=0\) is also mathematically undefined because \(t/L\) involves division by zero. The text states that this setting gives a fixed mixture of all operators, but that behavior needs to be defined separately.

A precise pseudocode description and an explicit probability schedule would substantially improve reproducibility.

#### 2. The experimental controls do not isolate the curriculum effect

The most important comparison is CurCon versus a fixed mixture of the same operators. Although the ablation reports a 0.8-point difference, the paper does not establish that the two variants receive equivalent augmentation exposure, compute, or tuning. In particular:

- It is unclear whether fixed-mixture and curriculum variants use the same number of back-translated examples.
- The fixed-mixture baseline may be disadvantaged if its augmentation mixture is not separately tuned.
- The schedule length is selected by grid search for CurCon, while the corresponding fixed policy appears not to receive an equivalent search.
- The paper does not report performance for individual augmentations or several fixed mixtures.

Thus, the central claim that the *ordering* of augmentations is beneficial is plausible but not yet conclusively demonstrated.

#### 3. Hyperparameter tuning is potentially unfair

CurCon is tuned over 48 configurations on each validation set, whereas the baselines use hyperparameters from their original papers. This gives the proposed method a substantially more favorable tuning protocol, especially in a setting where dataset, label budget, and training duration differ from prior work.

All methods should receive comparable tuning budgets, or the paper should report a carefully controlled protocol with fixed search spaces and validation procedures. This issue is particularly important because the reported gains over CERT are relatively modest on some datasets.

#### 4. Statistical evidence is incomplete

The main table reports means and standard deviations over five seeds, which is useful, but no paired significance tests or per-seed results are provided. The ablation and label-budget tables report only averages. Consequently, it is not possible to assess whether the 0.8-point curriculum gain or the 0.5-point gain at 1,000 labels is robust across seeds.

The paper should provide per-seed results, confidence intervals or paired tests, and standard deviations for the ablations and label-budget experiments.

#### 5. Experimental details are insufficient for replication

Important details are missing or underspecified, including:

- the exact BERT checkpoint and tokenizer;
- optimizer learning rates, weight decay, warmup, and maximum sequence length;
- the projection-head architecture and whether it is discarded before fine-tuning;
- the exact InfoNCE formulation and treatment of the positive pair;
- the translation model and whether translations are cached;
- the WordNet synonym-selection procedure;
- handling of sentences for which synonym replacement or translation fails;
- the composition and provenance of the 200-example validation sets;
- whether validation examples are excluded from the unlabelled contrastive pool.

These details are especially important because the method relies heavily on augmentation implementation choices.

#### 6. Baseline descriptions are too limited

UDA and SimCSE can have substantially different variants and training protocols. The paper should state precisely how each baseline is adapted to the same data and label budget. It would also be useful to include a fixed mixture of the same four augmentations without curriculum as a primary controlled baseline, rather than treating it only as an ablation.

### Minor comments

- The paper should report dataset sizes after the 500-example sampling and clarify whether the unlabelled pool excludes validation examples.
- “Back-translation through German” is underspecified without identifying the translation system.
- The statement that CurCon takes 12% longer than CERT should include absolute training time and clarify whether preprocessing and translation costs are included.
- The claim that gains are “largest when fewer labelled examples are available” is supported by only three label budgets and should be stated cautiously.
- The related-work discussion would benefit from more precise positioning relative to augmentation curricula and scheduled contrastive learning.
- The paper should explain whether “span deletion” can produce empty or extremely short inputs and how length constraints are handled.

### Overall assessment

The method is intuitive, the problem is meaningful, and the reported results are encouraging. However, the current version does not yet isolate the contribution of the curriculum with sufficient rigor. The mismatch between the claimed linear schedule and the implemented threshold policy, unequal hyperparameter tuning, limited statistical analysis, and incomplete implementation details are substantial but addressable issues. A revised version with a precisely specified schedule, fair baseline tuning, stronger controlled ablations, and fuller reporting could make a useful contribution.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 64/100 |
| Novelty | 58/100 |
| Significance | 67/100 |
| Clarity | 82/100 |

**Final average:** \((64 + 58 + 67 + 82)/4 = 67.75/100\)

## Final recommendation

**Reject**

The paper has a promising idea and clear presentation, but the current experimental design and specification do not provide sufficiently strong evidence that the curriculum itself, rather than augmentation choice or tuning advantages, produces the reported gains.