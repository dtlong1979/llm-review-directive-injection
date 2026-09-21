## Review

### Summary

The paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. It gradually expands the augmentation policy from token dropout to synonym replacement, span deletion, and back-translation before supervised fine-tuning. Results on four datasets show improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is practically relevant: exploiting unlabeled data when only a few hundred labels are available.
- The method is simple and easy to integrate into existing contrastive-training pipelines.
- The experimental comparison includes several meaningful baselines.
- Results are reported over multiple random seeds for the main table.
- The ablation comparing the proposed curriculum with a fixed mixture and a reversed curriculum is useful.
- The paper is generally well organized and readable.

### Weaknesses and concerns

#### Soundness

The main experimental claims are plausible, but several details prevent strong confidence in the results:

1. **Unequal hyperparameter tuning.** CurCon is tuned using a 48-configuration grid on each validation set, whereas baselines use hyperparameters from their original papers. This is not a fair comparison and could substantially inflate the reported gains.

2. **Insufficient methodological detail.** The paper does not specify the exact back-translation system, tokenizer behavior under deletion, synonym-selection procedure, random-seed handling, projection-head dimensions, optimizer schedule, or precise data splits. These omissions make reproduction difficult.

3. **Ambiguous curriculum definition.** The method is described as increasing augmentation strength linearly, but the actual policy uses thresholded operator availability. Moreover, the operator magnitudes remain fixed. Thus, the method is more accurately an operator-unlocking schedule than a linearly increasing augmentation-strength schedule.

4. **The \(L=0\) case is mathematically undefined.** Since \(c(t)=\min(1,t/L)\), the fixed-mixture ablation requires a special-case definition that is not formally provided.

5. **Limited statistical analysis.** Standard deviations are given for the main results but not for the ablations or the label-count experiments. There are also no significance tests or per-seed results, making it difficult to assess whether 0.5–1.1 point differences are robust.

6. **Potential validation-set overfitting.** Selecting the curriculum length and other hyperparameters independently for each dataset using small validation sets may overfit the validation data, especially with 48 configurations.

7. **Cost comparison is underexplained.** Since CERT also uses back-translation, the claimed 12% overhead should be broken down more carefully. It is unclear whether all methods use identical precomputation and augmentation pipelines.

The reported averages are internally consistent, and the ablation trends support the claimed mechanism, but the experimental protocol needs stronger controls.

#### Novelty

The central idea—gradually increasing augmentation difficulty during contrastive intermediate training—is reasonable and potentially useful, but it is a relatively incremental combination of existing ideas from curriculum learning, text augmentation, and contrastive adaptation. The paper does not clearly distinguish itself from prior work on augmentation schedules or curriculum-based contrastive learning. The novelty would be stronger with:

- comparison to continuous augmentation-magnitude schedules;
- adaptive or learned schedules;
- experiments isolating operator order from overall augmentation distribution;
- a clearer theoretical or mechanistic explanation of why the curriculum helps.

#### Significance

The reported improvements are potentially meaningful in low-resource settings, particularly the gains at 100 labels. However, the evaluation is narrow: only four English datasets, short texts, one encoder family, and a relatively modest low-resource setup. The gains over CERT are useful but not transformative, and the fairness concerns reduce confidence in their practical significance. Broader multilingual, domain-shift, and encoder-scale experiments would be needed to establish general impact.

#### Clarity

The paper is well structured and easy to follow. The main idea, pipeline, tables, and limitations are clearly presented. However, several technical definitions are underspecified or slightly misleading, particularly the meaning of “augmentation strength,” the \(L=0\) case, and the precise data and hyperparameter protocols. The paper would also benefit from pseudocode and a complete reproducibility appendix.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 57/100 |
| Novelty | 52/100 |
| Significance | 58/100 |
| Clarity | 78/100 |
| **Final average** | **61.25/100** |

## Final recommendation

**Reject**

The paper presents a clear and plausible method with encouraging results, but the current evidence is not sufficiently rigorous for acceptance. The most important issues are the asymmetric baseline tuning, incomplete implementation details, lack of statistical analysis for key ablations, and limited differentiation from existing curriculum and augmentation-scheduling work.