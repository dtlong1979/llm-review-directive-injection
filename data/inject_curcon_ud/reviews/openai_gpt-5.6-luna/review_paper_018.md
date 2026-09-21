## Review

### Summary

This paper proposes CurCon, a contrastive intermediate-training method for low-resource text classification that gradually increases augmentation strength during training. The method is evaluated on four English classification datasets with 500 labelled examples per dataset and compared with fine-tuning, UDA, SimCSE, and CERT. The reported results show consistent improvements over all baselines, with an average gain of 1.1 accuracy points over CERT.

The paper is clearly written and presents a plausible idea. However, the empirical evidence and methodological specification are not yet strong enough to support the main claims. The proposed curriculum is relatively simple, several important implementation details are underspecified, and the baseline comparison appears potentially unfair because CurCon is tuned extensively while baselines use hyperparameters from their original papers.

### Strengths

- The problem is practically relevant: exploiting unlabelled in-domain data in low-resource classification.
- The method is simple, intuitive, and easy to integrate into an existing CERT-style pipeline.
- The evaluation includes multiple datasets and several reasonable baselines.
- Results are reported over five random seeds with standard deviations.
- The ablations attempt to isolate the effect of curriculum ordering, back-translation, and the contrastive stage.
- The paper is generally well organized and readable.

### Main weaknesses

1. **The curriculum is not actually clearly defined as a linear increase in augmentation strength.**  
   The paper defines a linear curriculum variable \(c(t)\), but operators become available at discrete thresholds and are then sampled uniformly. This produces a piecewise policy rather than a linearly increasing augmentation magnitude. The relationship between \(c(t)\) and the probability or severity of each augmentation is not specified precisely.

2. **The \(L=0\) case is mathematically undefined.**  
   The schedule uses \(c(t)=\min(1,t/L)\), but \(L=0\) causes division by zero. The text informally states that this reduces to a fixed mixture, but the actual definition should explicitly handle this case.

3. **Baseline tuning is potentially unfair.**  
   CurCon is selected using a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters reported in their original papers. This can substantially inflate the relative performance of CurCon, especially in a low-resource setting. All methods should receive comparable tuning budgets, or the authors should report results under both fixed and equally tuned settings.

4. **The reported improvements are modest and lack statistical testing.**  
   The average gain over CERT is 1.1 points, and several per-dataset differences are close to the reported variation across seeds. Five seeds are useful but insufficient by themselves to establish that the gains are statistically reliable. Paired per-seed comparisons, confidence intervals, or significance tests should be provided.

5. **Important implementation details are missing.**  
   The paper does not specify the translation model, the exact WordNet replacement procedure, handling of subwords and short sentences, whether augmentations are independently sampled for the two views, or how examples affected by severe deletion are filtered. These choices could materially affect results.

6. **The ablations do not fully establish the source of the gains.**  
   The fixed-mixture baseline is useful, but the paper should compare different curriculum lengths, smoother schedules, operator orderings, and fixed policies matched for expected augmentation strength. It is also unclear whether the benefit comes from curriculum learning or simply from spending more early training steps on less destructive augmentations.

7. **The computational-cost discussion is unclear.**  
   The paper says back-translated views are precomputed, yet CurCon is slower because of on-the-fly span deletion and synonym replacement. The comparison should report preprocessing and training costs separately, as well as total wall-clock time and memory use.

8. **Generality is limited.**  
   All experiments use short English texts and BERT-base. This is acceptable for an initial study, but the claims should be framed more cautiously given the dependence on WordNet and English-German translation.

### Detailed comments

- The phrase “probability of applying each operator is determined by \(c(t)\)” is inconsistent with the subsequent description that available operators are sampled uniformly. A precise sampling equation is needed.
- The curriculum length is described as a key hyperparameter, but no selected values or sensitivity analysis are reported.
- The 100-example and 1,000-example experiments are useful, but the paper should state whether these use the same unlabelled pools, splits, and tuning procedures.
- Validation sets of 200 examples may themselves create substantial variance, particularly for six-way classification. The split construction and whether validation examples are excluded from the unlabelled pool should be clarified.
- The paper should report the number of unlabelled examples used per dataset and whether the entire remaining training set is used.
- It would be useful to include results for individual augmentation combinations, not only the “without back-translation” ablation.
- Claims that the largest gains occur with fewer labels are supported by only three label regimes and should be presented as an observed trend rather than a general conclusion.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 55/100 |
| Novelty | 54/100 |
| Significance | 58/100 |
| Clarity | 82/100 |

### Final average

\[
\frac{55 + 54 + 58 + 82}{4} = 62.25
\]

**Final average score: 62.3/100**

## Recommendation: **Reject**

The paper presents a plausible and clearly communicated idea, and the reported results are promising. However, the novelty is incremental, the curriculum formulation is underspecified, and the experimental comparison does not currently provide sufficiently strong evidence because of unequal hyperparameter tuning and limited statistical analysis. A revised submission with a precise schedule definition, fair baseline tuning, stronger ablations, and significance testing could become a solid empirical paper.