## Review

### Soundness: 58/100
The paper presents a plausible experimental design and reports results across four standard datasets with multiple seeds. The ablations are directionally consistent with the proposed curriculum hypothesis.

However, several methodological details weaken confidence in the conclusions:

- CurCon is tuned using a 48-configuration grid search on each validation set, while baselines use hyperparameters from their original papers. This creates an unfair comparison, particularly in a low-resource setting.
- The curriculum is not actually linear in augmentation strength. Operators become available at discrete thresholds and are then sampled uniformly, causing abrupt changes in the augmentation distribution.
- The definition \(c(t)=\min(1,t/L)\) is undefined for \(L=0\), despite the paper claiming that \(L=0\) represents the fixed-mixture baseline.
- The experimental protocol does not sufficiently specify preprocessing, exact data splits, back-translation models, WordNet handling, sequence truncation, or whether unlabelled data processing is identical across methods.
- No statistical significance tests or paired seed-level comparisons are reported.
- The cost analysis is underspecified and difficult to verify, especially given that back-translations are precomputed for CurCon but the corresponding treatment for CERT is not clearly described.

The central results are plausible, but the comparison and reproducibility issues make the strength of the evidence uncertain.

### Novelty: 62/100
Scheduling augmentation difficulty during contrastive learning is a reasonable and potentially useful idea. Applying a curriculum specifically to intermediate contrastive training for low-resource classification provides a coherent contribution.

Nevertheless, the conceptual novelty is moderate rather than substantial. The method combines well-known augmentation operators, contrastive intermediate training, and a hand-designed easy-to-hard schedule. The paper should more carefully distinguish its contribution from prior work on augmentation schedules, curriculum learning, and adaptive contrastive learning. The claimed gap may also be overstated without a broader literature comparison.

### Significance: 64/100
The problem is practically important, and improvements in low-resource classification could be valuable. The reported gains over CERT are meaningful at 100 and 500 labels, and the approach requires no inference-time changes.

The significance is limited by the narrow evaluation: only four short English classification datasets, one encoder size, and one fixed label-sampling protocol. The results also do not establish whether the gains generalize to domain-specific, multilingual, longer-document, or more difficult tasks. Since the method incurs additional preprocessing and training cost, the paper should include stronger efficiency and accuracy trade-off analyses.

### Clarity: 78/100
The paper is generally well organized and easy to follow. The motivation, training pipeline, augmentation operators, and main findings are clearly presented.

Clarity and reproducibility would improve with:

- a precise mathematical specification of the augmentation sampling probabilities;
- clarification of how views are generated when multiple operators are available;
- a valid definition of the \(L=0\) baseline;
- exact details of dataset splitting, preprocessing, and translation systems;
- per-dataset ablation results and seed-level variance;
- a clearer distinction between validation-based tuning and fixed baseline settings.

## Final score

\[
\frac{58 + 62 + 64 + 78}{4} = 65.5
\]

**Average score: 65.5/100**

## Recommendation: Reject

The idea is sensible and the presentation is reasonably clear, but the current evidence is not sufficiently rigorous for acceptance. The unequal hyperparameter tuning, underspecified implementation details, and limited evaluation make it difficult to determine whether the gains arise from the curriculum itself rather than from tuning or augmentation differences. A revised version with matched baseline tuning, stronger statistical analysis, clearer schedule definitions, and broader experiments could become a solid contribution.