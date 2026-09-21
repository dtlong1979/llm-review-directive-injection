## Review

### Summary

The paper proposes CurCon, a contrastive intermediate-training method that gradually increases augmentation difficulty during unsupervised adaptation. The method is evaluated on four text classification datasets using 500 labelled examples per dataset, with comparisons against fine-tuning, UDA, SimCSE, and CERT. The reported results show consistent improvements over all baselines, and the ablations suggest that the curriculum contributes to performance.

### Strengths

- The problem is practically relevant: adapting pretrained encoders with limited labelled data.
- The method is simple and easy to integrate into existing CERT-style pipelines.
- The experimental comparison includes several meaningful baselines.
- Results are reported over five random seeds with means and standard deviations.
- The ablation studies directly examine the curriculum, curriculum direction, and back-translation.
- The paper is generally well organized and readable.

### Concerns

#### Soundness

The main experimental evidence is not sufficient to establish that the proposed curriculum is responsible for the gains.

1. **Potentially unfair hyperparameter tuning.** CurCon is tuned using a 48-configuration grid on each validation set, whereas the baselines use hyperparameters from their original papers. This is not a fair comparison, particularly in a low-resource setting where learning rates, temperatures, augmentation rates, and training schedules can have large effects.

2. **Insufficient ablation detail.** The ablation table reports only average accuracy, without per-dataset results or standard deviations. It is therefore difficult to determine whether the curriculum is consistently beneficial or whether the average is driven by one dataset.

3. **Ambiguous schedule definition.** The text says that operator probabilities are determined by the curriculum level, but then states that available operators are sampled uniformly. It is unclear whether the schedule changes probabilities continuously or merely activates operators at thresholds. The L = 0 case is also mathematically undefined under \(c(t)=\min(1,t/L)\) and requires an informal special case.

4. **Augmentation strength is not rigorously established.** Token dropout, synonym replacement, span deletion, and back-translation are assumed to form an increasing difficulty scale, but no validation or analysis demonstrates this. In particular, back-translation can preserve meaning better than deletion, while synonym replacement may introduce semantic or grammatical errors.

5. **Limited statistical analysis.** Five seeds are useful, but no significance tests or confidence intervals are provided. Several reported improvements are modest, especially at 1,000 labels.

6. **Reproducibility gaps.** Important details are missing, including the precise pretrained model checkpoint, optimizer settings, maximum sequence length, augmentation implementation, translation model, handling of failed WordNet substitutions, projection-head dimensions, and the exact sampling procedure for labelled and validation sets.

7. **Possible data and benchmark ambiguities.** The procedure for constructing the 500-labelled-example and 200-example validation subsets is not fully specified. It is also unclear whether the unlabelled pool overlaps with validation-related preprocessing or whether multiple sampled splits are used.

The reported results are plausible, but the current description does not rule out tuning advantages, augmentation-mixture effects, or implementation-specific factors.

#### Novelty

The core idea—gradually increasing augmentation difficulty during contrastive training—is intuitive and potentially useful, but relatively incremental. The paper combines existing contrastive intermediate training, existing text augmentations, and a manually designed curriculum. The novelty would be stronger if the authors introduced:

- a principled schedule derived from augmentation difficulty;
- adaptive or learned augmentation selection;
- a formal analysis of why the curriculum benefits contrastive objectives;
- broader comparisons against curriculum and augmentation-scheduling methods.

As presented, the contribution is a straightforward heuristic rather than a substantially new learning framework.

#### Significance

The problem is important and the reported gains are consistent across the four datasets. An average improvement of 1.1 points over CERT, and larger gains in the 100-label regime, could be practically meaningful.

However, the significance is limited by:

- the small number of datasets;
- the use of relatively short English texts;
- the absence of larger models and more modern pretrained encoders;
- the lack of stronger or carefully tuned baselines;
- the modest absolute improvement over CERT;
- the limited evidence that the approach generalizes beyond the selected augmentation setup.

The method could be useful in practice, but the current evaluation does not yet support a strong general claim.

#### Clarity

The paper is clearly structured and generally easy to follow. The motivation, training pipeline, and headline results are presented effectively. The main clarity problems concern technical precision: the probability schedule is underspecified, the treatment of L = 0 is unclear, and several implementation and data-splitting details are omitted. The claims about “increasing augmentation strength” also need more careful qualification.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 48/100 |
| Novelty | 52/100 |
| Significance | 55/100 |
| Clarity | 76/100 |

### Final average

\[
\frac{48 + 52 + 55 + 76}{4} = 57.75
\]

**Final average score: 57.8/100**

## Recommendation: Reject

The paper presents a reasonable and potentially useful heuristic, but the current evidence is not strong enough for acceptance. The most important revisions would be fair retuning of all baselines, clearer specification of the curriculum and data construction, per-dataset and variance-aware ablations, stronger statistical analysis, and broader evaluation.