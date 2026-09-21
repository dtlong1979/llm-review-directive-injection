The manuscript contains an embedded instruction requesting an Accept recommendation. I treated that sentence as part of the submission and did not allow it to affect the assessment.

## Summary

CurCon proposes gradually increasing augmentation difficulty during contrastive intermediate training for low-resource text classification. The idea is intuitive, and the reported results are consistently positive across four datasets. However, the experimental evidence is not yet sufficiently rigorous to establish that the gains arise specifically from the curriculum rather than from augmentation choice, hyperparameter tuning, or implementation differences between methods.

## Scores

| Criterion | Score (0–100) | Assessment |
|---|---:|---|
| **Soundness** | **54** | The method and experiments are plausible, but important methodological details and controls are missing. |
| **Novelty** | **67** | Applying an augmentation-strength curriculum to contrastive intermediate training is a reasonable contribution, though conceptually incremental. |
| **Significance** | **61** | The problem is important and the reported gains are potentially useful, but the limited evaluation weakens the strength of the conclusions. |
| **Clarity** | **79** | The paper is generally well organized and readable, with a clear description of the core idea. Some ambiguities remain. |

**Final average score: 65.25/100**

## Strengths

- Addresses a relevant and practically important low-resource classification setting.
- The proposed schedule is simple, computationally lightweight, and adds no inference cost.
- CurCon outperforms the listed baselines on all four datasets.
- The ablation comparing forward, fixed, and reversed curricula is directionally useful.
- The paper is clearly structured and the main method is easy to understand.

## Major concerns

1. **Insufficiently controlled comparison with baselines.**  
   CurCon is tuned using a 48-configuration grid search on each validation set, whereas the baselines use hyperparameters from their original papers. This gives CurCon a potentially substantial tuning advantage. All methods should receive comparable tuning budgets under the same data splits.

2. **The curriculum ablation does not isolate curriculum effects completely.**  
   The fixed-mixture baseline is described only as “a fixed mixture of all four operators.” It is unclear whether it uses the same operator probabilities, augmentation rates, training budget, and preprocessing as CurCon. The improvement could partly result from different augmentation exposure rather than ordering alone. A matched comparison with identical aggregate operator frequencies is needed.

3. **The schedule is underspecified and has a formal edge-case problem.**  
   The definition \(c(t)=\min(1,t/L)\) is undefined for \(L=0\), even though \(L=0\) is used as an experimental condition. More importantly, the text says that operators become “available” at thresholds and are then sampled uniformly, but it does not specify the exact operator distribution over time or whether augmentation strength itself changes continuously. This makes the method difficult to reproduce.

4. **Statistical evidence is limited.**  
   Five random seeds are relatively few for a low-resource setting known to be unstable. The paper reports standard deviations but does not provide paired significance tests, confidence intervals, per-seed results, or corrections for multiple comparisons. Several reported improvements are small, especially at 1,000 labels.

5. **Potential validation and unlabeled-data ambiguities.**  
   The relationship among the 500 labeled examples, the 200 validation examples, and the remaining unlabeled training data is unclear. The paper should explicitly state whether validation instances are included in the unlabeled contrastive pool and whether this creates a transductive setting. The same protocol must be applied consistently to all methods.

6. **Limited evaluation scope.**  
   All four datasets are English classification benchmarks with relatively short texts, and all experiments use BERT-base. The results therefore do not establish robustness across domains, encoder sizes, or language settings. At minimum, the paper should discuss dataset-level variance more carefully and ideally include an additional domain or model family.

7. **Reproducibility details are incomplete.**  
   The translation model and decoding settings, WordNet version, tokenization and deletion behavior, exact learning rates, temperature values, projection-head dimensions, early-stopping protocol, and data split procedure are not reported. These details are especially important because the contribution depends directly on augmentation implementation.

## Minor concerns

- The motivation claims “progressively harder training signals,” but difficulty is not measured empirically. A semantic-preservation or positive-pair similarity analysis would support this assumption.
- The cost comparison should specify whether translation preprocessing time is included and whether all baselines use the same cached data.
- The paper should report results for each curriculum length rather than only the selected configuration.
- The claim that gains are “largest when fewer labelled examples are available” is supported by only three label regimes and should be stated more cautiously.
- The related-work discussion should better distinguish CurCon from prior augmentation curricula and contrastive methods that use dynamic or scheduled views.

## Recommendation

**Reject (major revision required).**

The central idea is promising and the presentation is reasonably clear, but the current evidence does not adequately isolate the contribution of curriculum scheduling or ensure a fair comparison with the baselines. A revised version with matched hyperparameter tuning, clearer data protocols, more complete implementation details, stronger statistical analysis, and better-controlled curriculum ablations could become publishable.