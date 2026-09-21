## Summary

The paper proposes CurCon, which gradually increases the strength of text augmentations during contrastive intermediate training before low-resource classification fine-tuning. The idea is intuitive and potentially useful, and the reported results are consistently better than the selected baselines. However, the empirical evidence and methodological specification are not yet sufficient to support the paper’s claims.

## Strengths

- The problem is practically relevant: exploiting unlabeled in-domain text when only a small labeled set is available.
- The proposed curriculum is simple and incurs no inference-time parameter or architectural cost.
- Experiments cover four established classification benchmarks and several relevant baselines.
- Results are reported over five random seeds, and the paper includes ablations and label-budget analyses.
- The manuscript is generally well organized and readable.

## Major concerns

### 1. The curriculum is not actually linear as described

The abstract and introduction characterize the method as a linear increase in augmentation strength. However, the implementation uses thresholded availability:

- synonym replacement becomes available at \(c(t)>0.25\),
- span deletion at \(c(t)>0.5\),
- back-translation at \(c(t)>0.75\).

Within each interval, the augmentation policy is unchanged, and once all operators become available, the policy is fixed. Thus, this is a discrete staged curriculum rather than a linearly scheduled augmentation-strength curriculum. The relationship between \(c(t)\) and operator-selection probabilities is also unclear: the manuscript says that probabilities are determined by \(c(t)\), but then states that available operators are sampled uniformly.

The method should specify the exact probability distribution at every step and distinguish clearly between the proposed schedule and the stated linear interpretation.

### 2. The baseline comparison is potentially unfair

CurCon’s learning rate, temperature, and curriculum length are selected by a 48-configuration grid search for each dataset, while the baselines use hyperparameters reported in their original papers. This gives the proposed method substantially more opportunity for dataset-specific optimization. In low-resource settings, this difference can materially affect results.

All methods should receive comparable tuning budgets, or the paper should report results under both original and fairly tuned baseline configurations. The handling of validation data and whether hyperparameters are selected independently for every seed also needs clarification.

### 3. Statistical evidence is insufficient

Although five random seeds are reported, the paper gives no statistical significance tests, confidence intervals for the mean differences, or paired seed-level comparisons. The average improvement over CERT is only 1.1 points, and several per-dataset standard deviations overlap. The ablation table reports no variability at all, making it difficult to determine whether the curriculum effect is robust.

The paper should include seed-level results, confidence intervals or appropriate paired tests, and standard deviations for the ablations and label-budget experiments.

### 4. The ablations do not isolate the source of improvement adequately

The fixed-mixture and reversed-curriculum comparisons are useful, but the study lacks controls for:

- the same augmentation operators with a randomized ordering,
- alternative curriculum lengths,
- different schedules besides linear/thresholded scheduling,
- augmentation strength without curriculum,
- operator composition versus sampling a single operator,
- additional contrastive training steps or compute.

Because CurCon introduces both a particular operator mix and a particular schedule, the current ablations do not fully establish that the ordering itself is responsible for the gains.

### 5. Important experimental details are underspecified

The paper should clarify:

- which back-translation model and decoding procedure are used;
- how WordNet synonym replacement handles ambiguity, morphology, and unavailable synonyms;
- whether the labelled examples are also included in the unlabeled contrastive corpus;
- whether validation examples are excluded from contrastive training;
- whether augmentations are applied independently to each view;
- the precise InfoNCE formulation and projection-head dimensions;
- maximum sequence length and truncation policy;
- the exact split construction for the 500 labelled examples;
- whether the reported test results were selected after repeated validation-based experimentation.

These details are important for reproducibility and for evaluating possible data leakage or transductive effects.

### 6. Claims about generality are stronger than the evidence

The evaluation uses four short English classification datasets and only BERT-base. This is acknowledged in the limitations, but the paper nevertheless makes broad claims about low-resource text classification. The reported gains may depend strongly on dataset size, text length, English lexical resources, or the quality of the translation system.

## Minor concerns

- The cost comparison is difficult to interpret because CERT also uses back-translation, while CurCon is said to precompute back-translated views but still incurs a 12% overhead from other augmentations. More precise wall-clock and preprocessing costs would be useful.
- The manuscript should cite and distinguish more carefully from prior work on augmentation schedules and curriculum-based contrastive learning.
- Average accuracy alone can obscure class imbalance and dataset-specific effects, especially for the heterogeneous benchmark collection.
- The wording “probability of applying each operator” conflicts with “one is sampled uniformly” and should be revised.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 48/100 |
| Novelty | 61/100 |
| Significance | 57/100 |
| Clarity | 76/100 |

**Final average:** \((48 + 61 + 57 + 76)/4 = \mathbf{60.5/100}\)

## Recommendation

**Reject**

The core idea is plausible and the presentation is clear, but the current empirical comparison does not establish that the curriculum itself, rather than tuning choices or the augmentation mixture, produces the reported gains. A revised submission with fair baseline tuning, clearer method specification, stronger statistical analysis, and more comprehensive ablations could become a valuable contribution.