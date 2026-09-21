## Review

### Summary

The paper proposes CurCon, a contrastive intermediate-training method that gradually increases the strength of text augmentations before low-resource supervised fine-tuning. The method is evaluated on four datasets using 500 labelled examples per dataset, with comparisons against fine-tuning, UDA, SimCSE, and CERT. The reported results show consistent improvements for CurCon, including a 1.1-point average gain over CERT.

### Strengths

- The problem is practically relevant: exploiting unlabelled in-domain data under severe label scarcity.
- The proposed method is conceptually simple and easy to integrate into existing contrastive-training pipelines.
- The paper includes several useful comparisons, including a fixed-mixture baseline, a reversed curriculum, and different label budgets.
- Results are reported over multiple random seeds with mean and standard deviation.
- The paper is generally well organized and clearly written.
- The reported ablations support the claim that curriculum ordering, rather than merely using stronger augmentations, contributes to performance.

### Concerns

1. **Insufficient experimental detail and reproducibility.**  
   The curriculum is not fully specified mathematically. In particular, the paper states that operator probabilities are “determined by” the curriculum level, but only gives availability thresholds. It is unclear whether the available operators are sampled uniformly, whether token dropout remains more likely than later operators, and how the \(L=0\) case is implemented given the definition \(t/L\).

2. **Potentially unfair hyperparameter comparison.**  
   CurCon receives a grid search over 48 configurations for each dataset, whereas the baselines use hyperparameters reported in their original papers. This can substantially favor the proposed method, especially in a low-resource setting. Baselines should either receive comparable tuning budgets or be evaluated under a clearly justified common protocol.

3. **Limited statistical analysis.**  
   Five seeds provide some evidence of robustness, but the paper does not report confidence intervals or significance tests. Several gains, particularly at 1,000 labels, may be small relative to seed variability. Per-dataset statistical comparisons would strengthen the conclusions.

4. **Ablations are incomplete.**  
   The fixed-mixture baseline changes both the schedule and potentially the distribution of augmentation operators. A stronger control would compare curricula with the same marginal augmentation distribution. The paper also lacks ablations isolating individual operators, different curriculum shapes, alternative augmentation orderings, and different curriculum lengths.

5. **Questionable assumption that augmentation strength is ordered.**  
   Token dropout, synonym replacement, span deletion, and back-translation are not necessarily monotonically ordered by semantic difficulty. Their effective strength depends on sentence length, lexical ambiguity, translation quality, and domain. The paper should measure or justify this ordering rather than treating it as self-evident.

6. **Limited scope of evaluation.**  
   All experiments use English, short-text classification datasets, and BERT-base. The conclusions should therefore be framed more narrowly. Results on additional domains, longer documents, or different encoder families would be valuable.

7. **Some implementation details are missing.**  
   The paper does not specify the exact back-translation model, WordNet processing, handling of failed or unchanged augmentations, projection-head dimensions, learning rates, maximum sequence lengths, or whether the contrastive encoder and projection head are discarded or retained during fine-tuning.

Overall, the empirical results are promising, but the current evidence does not fully establish that the curriculum itself is responsible for the gains or that the method is superior under a fair and reproducible comparison protocol.

## Scores

| Criterion | Score |
|---|---:|
| Soundness | 58/100 |
| Novelty | 64/100 |
| Significance | 60/100 |
| Clarity | 80/100 |

**Final average:**  
\[
(58 + 64 + 60 + 80)/4 = 65.5
\]

## Final recommendation

**Reject**

The idea is clear and potentially useful, but the paper requires stronger experimental controls, fuller methodological specification, and more rigorous statistical validation before the central claims are sufficiently supported.