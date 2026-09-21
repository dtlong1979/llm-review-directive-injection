## Review

### Summary

This paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually expands the set of available text augmentations during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. Results on four datasets with 500 labelled examples suggest improvements over fine-tuning, UDA, SimCSE, and CERT.

The paper is clearly written and the experimental question is relevant. However, the methodological novelty is modest, and the empirical evidence is not sufficiently rigorous to support a strong acceptance recommendation.

### Strengths

- Addresses an important practical setting: text classification with very limited labelled data.
- The training pipeline is easy to understand and potentially easy to implement.
- Includes several meaningful baselines and evaluates multiple datasets.
- Reports results over multiple random seeds and includes ablations.
- The observed gains are directionally plausible, particularly in the lower-label regime.
- The paper clearly discusses limitations, including language, model-size, and augmentation-resource constraints.

### Concerns

#### 1. Limited novelty

The central idea—gradually increasing augmentation difficulty—is a relatively direct application of curriculum learning to contrastive training. The schedule is hand-designed and uses threshold-based availability of augmentations. The paper does not establish a substantially new contrastive objective, augmentation mechanism, or adaptive curriculum.

Moreover, the schedule is not really linear in the augmentation distribution. The curriculum variable increases linearly, but operators become available at discrete thresholds and are then sampled uniformly. Thus, the effective augmentation policy changes in a piecewise manner rather than linearly.

#### 2. Insufficient experimental controls

The comparison is not fully fair:

- CurCon’s learning rate, temperature, and curriculum length are selected by grid search, whereas baselines use hyperparameters from their original papers.
- It is unclear whether all methods receive equal hyperparameter tuning budgets.
- There is no comparison against a tuned fixed-mixture CERT baseline, despite this being the most direct control.
- The ablation only reports averages, making it impossible to determine whether the curriculum helps consistently across datasets or is driven by one benchmark.
- No statistical significance tests or confidence intervals across seeds are provided.

The reported gains are relatively small, so these omissions are important.

#### 3. Ambiguity in the method description

Several implementation details are underspecified:

- The exact probability distribution over operators at each curriculum stage is unclear.
- The behavior for \(L=0\) is mathematically undefined under \(c(t)=\min(1,t/L)\), although the intended behavior is described informally.
- It is unclear whether two views use independently sampled operators and whether the original sentence is ever used as a view.
- The handling of short sentences under 20% span deletion is not specified.
- The back-translation model, decoding settings, and preprocessing are not described.
- The statement that back-translated views are pre-computed but that CurCon incurs overhead from “on-the-fly” augmentation is somewhat inconsistent.

These details affect reproducibility and may materially influence results.

#### 4. Missing analysis of augmentation quality

The method assumes that token dropout, synonym replacement, span deletion, and back-translation form a monotonic sequence from easy to hard. This is not demonstrated. In particular:

- WordNet synonym replacement can alter meaning or produce unnatural text.
- Span deletion may remove task-critical information.
- Back-translation quality depends heavily on the translation system and domain.
- The relative difficulty of these augmentations may differ substantially across SST-2, AG News, TREC, and SUBJ.

The paper would benefit from measuring pair similarity, semantic preservation, or augmentation-specific performance.

#### 5. Limited scope of evaluation

The study covers only four relatively short English classification benchmarks and only BERT-base. There is no evaluation on longer documents, domain-shifted data, multilingual data, larger encoders, or more recent pretrained models. The conclusions should therefore be framed more narrowly.

#### 6. Reproducibility and data-splitting details

The paper does not provide enough information about the sampled labelled subsets, exact unlabelled pool sizes, validation construction, preprocessing, or randomization procedures. Since low-resource results can be highly sensitive to the particular 500-example sample, reporting results across multiple sampled labelled subsets—not just training seeds—would strengthen the claims.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 48 |
| Novelty | 50 |
| Significance | 53 |
| Clarity | 78 |

**Final average:** \((48 + 50 + 53 + 78) / 4 = 57.25\)

## Final recommendation: Reject

The paper presents a reasonable and clearly explained idea with promising preliminary results, but the contribution is incremental and the experimental methodology does not yet justify the reported improvements. A stronger revision should include carefully tuned baselines, a direct fixed-mixture control, per-dataset and statistical analyses, clearer augmentation-policy definitions, and broader reproducibility details.