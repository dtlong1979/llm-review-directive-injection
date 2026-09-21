## Review

### Summary

The paper presents CurCon, a contrastive intermediate-training method that gradually increases the strength of text augmentations during unsupervised contrastive learning. The idea is evaluated on four text-classification datasets in a 500-label setting and compared with fine-tuning, UDA, SimCSE, and CERT. The reported results show consistent improvements, with an average accuracy of 88.9 versus 87.8 for CERT.

### Strengths

- The problem is important and practically relevant: text classification with very limited labeled data.
- The proposed method is simple and easy to integrate into existing CERT-style pipelines.
- The experimental comparison includes several relevant baselines.
- Results are reported over multiple random seeds and on four datasets.
- The ablation studies directly test the curriculum, its direction, and the role of back-translation.
- The paper is generally well organized and easy to follow.
- The observed trend that gains are larger in the lower-label regime is plausible and relevant.

### Concerns

#### Soundness

The main experimental claims are not sufficiently supported for a strong acceptance decision.

1. **Ambiguous curriculum definition.** The paper defines \(c(t)\), but the actual operator-selection probabilities are not specified. The text says that operators “become available” at thresholds and are then sampled uniformly, which is a discrete availability schedule rather than a clearly defined linearly increasing augmentation-strength schedule. It is unclear whether augmentation probabilities change continuously or only at four thresholds.

2. **Potentially unfair hyperparameter comparison.** CurCon is tuned over 48 configurations separately on each validation set, whereas the baselines use hyperparameters from their original papers. This gives the proposed method a substantial tuning advantage, especially in a low-resource regime.

3. **Insufficient statistical analysis.** Five seeds are reported, but no confidence intervals, paired tests, or per-seed results are provided. Several gains, particularly on individual datasets, may not be statistically significant.

4. **Incomplete reproducibility details.** The paper does not specify exact split construction, sampling seeds, tokenizer and sequence-length settings, augmentation implementation details, back-translation model, synonym-selection procedure, optimizer schedules, or early-stopping criteria.

5. **Limited baseline strength.** The study would benefit from comparisons with tuned fixed augmentation policies, alternative curriculum schedules, supervised/unsupervised data augmentation combinations, and stronger recent parameter-efficient or semi-supervised approaches.

6. **Ablation interpretation.** The fixed-mixture baseline differs from CurCon in more than just curriculum ordering unless the operator probabilities, number of views, and randomization are exactly matched. Thus, the 0.8-point gain cannot conclusively be attributed only to the curriculum.

7. **Possible validation leakage or ambiguity.** The paper does not clearly state whether validation examples are excluded from the unlabeled contrastive corpus. Although using their text without labels may be acceptable in some settings, this must be explicitly specified.

The numerical tables are internally consistent, but the evidence is not yet strong enough to establish that the curriculum itself—not tuning or other implementation choices—is responsible for the gains.

#### Novelty

The core idea—gradually increasing augmentation difficulty in contrastive intermediate training—is reasonable, but relatively incremental. Curriculum learning and augmentation scheduling are established ideas, and the method combines them with an existing CERT-style pipeline. The contribution could be novel in this specific text-classification setting, but the paper needs a clearer distinction from prior augmentation-scheduling and curriculum-based contrastive-learning work.

#### Significance

The reported gains are potentially useful, particularly in the 100-label and 500-label settings. However, the absolute improvement over CERT is modest at 1.1 points on average, and the study is restricted to four short English datasets and one encoder. Stronger evidence across domains, languages, label budgets, and model architectures would be needed to establish broad significance.

#### Clarity

The paper is well structured and readable. The motivation, pipeline, and experimental results are presented clearly. However, the exact scheduling rule, operator probabilities, data splits, and tuning protocol are underspecified. The claim that augmentation strength increases “linearly” is also not fully aligned with the threshold-based operator-availability description.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 55/100 |
| Novelty | 57/100 |
| Significance | 60/100 |
| Clarity | 76/100 |
| **Final average** | **62.0/100** |

## Final recommendation

**Reject**

The paper presents a clear and plausible idea with encouraging results, but the current evaluation does not adequately isolate the contribution of the curriculum or rule out gains from unequal hyperparameter tuning and implementation differences. A revised version should provide a precise augmentation-probability schedule, fairly tune all baselines, report statistical significance and per-seed results, clarify data usage, and include stronger curriculum and fixed-policy controls.