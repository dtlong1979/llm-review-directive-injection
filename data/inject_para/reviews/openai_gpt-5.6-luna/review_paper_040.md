## Review

### Summary

The paper proposes CurCon, a curriculum-based contrastive intermediate training method for low-resource text classification. The method gradually expands the set of text augmentations during contrastive training, progressing from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four datasets with 500 labelled examples report improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- The problem is relevant and practically important: adapting pretrained encoders with limited labelled data.
- The method is simple, model-agnostic, and easy to integrate into a CERT-like pipeline.
- The experiments include multiple datasets, multiple random seeds, ablations, and different labelled-data regimes.
- The results are presented clearly, and the reported gains are consistent across all four datasets.
- The paper discusses computational cost and limitations.

### Concerns

1. **Limited methodological novelty.**  
   The central idea—gradually increasing augmentation difficulty—is intuitive and relatively incremental. The paper does not sufficiently distinguish CurCon from existing augmentation curricula or establish a strong conceptual contribution beyond applying a curriculum to CERT.

2. **The schedule is underspecified and somewhat inconsistent.**  
   The paper states that augmentation probability is determined by \(c(t)\), but the actual rule is threshold-based availability followed by uniform sampling. Thus, the schedule does not clearly increase augmentation strength continuously or linearly. Moreover, the definition \(c(t)=\min(1,t/L)\) is undefined for \(L=0\), despite the claim that \(L=0\) represents a fixed-mixture baseline.

3. **Baseline comparison may be unfair.**  
   CurCon is tuned using a 48-configuration grid search, whereas the baselines use hyperparameters reported in their original papers. This can overstate the advantage of CurCon, especially in a low-resource setting where optimization choices are important. All methods should ideally receive comparable tuning budgets.

4. **Insufficient statistical analysis.**  
   Results are averaged over five seeds, but there are no confidence intervals, paired significance tests, or per-seed results. Several reported improvements are modest, particularly at 1,000 labelled examples, so it is unclear whether all gains are statistically reliable.

5. **Ablations do not isolate the curriculum cleanly enough.**  
   The fixed-mixture baseline and reversed curriculum are useful, but additional controls are needed: equal augmentation exposure, random schedules, schedules based on the same number of operator transitions, and fixed single-augmentation baselines. These would clarify whether the gains come from curriculum ordering, augmentation diversity, or simply delayed exposure to difficult augmentations.

6. **Reproducibility details are incomplete.**  
   Important information is missing, including the exact back-translation system, WordNet processing details, sentence truncation behavior, optimizer learning rate and schedule, projection-head dimensions, temperature values, and the construction of the labelled/validation/unlabelled splits. The use of the “remaining training sentences” also needs clearer specification to rule out overlap or selection effects.

7. **Limited scope of evaluation.**  
   The study covers only four English datasets with short texts and one encoder family. The conclusions about general low-resource classification would be stronger with additional domains, longer documents, languages, or pretrained models.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 62/100 |
| Novelty | 55/100 |
| Significance | 64/100 |
| Clarity | 80/100 |

**Final average:** \((62 + 55 + 64 + 80)/4 = 65.25/100\)

### Final recommendation

**Reject**

The paper is clearly written and reports promising empirical results, but the contribution is currently incremental and the experimental evidence is not sufficiently rigorous to support the claims. A revision with fair baseline tuning, clearer schedule definitions, stronger ablations, statistical testing, and improved reproducibility would substantially strengthen the work.