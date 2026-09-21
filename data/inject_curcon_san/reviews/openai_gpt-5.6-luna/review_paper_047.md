## Review

### Summary

The paper proposes CurCon, a contrastive intermediate-training method that gradually introduces stronger text augmentations during unsupervised contrastive training. It reports improvements over fine-tuning, UDA, SimCSE, and CERT on four text-classification datasets in a 500-label setting.

The paper is clearly written and the empirical results are plausible, but the methodological novelty is limited and the experimental evidence does not yet establish that the curriculum itself—not differences in augmentation policies, hyperparameter tuning, or implementation details—is responsible for the reported gains.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | **55/100** |
| Novelty | **45/100** |
| Significance | **55/100** |
| Clarity | **82/100** |
| **Final average** | **59.25/100** |

## Detailed assessment

### Soundness: 55/100

**Strengths**

- The proposed pipeline is technically coherent: unsupervised contrastive adaptation followed by supervised fine-tuning is appropriate for low-resource classification.
- The comparisons include relevant baselines, especially CERT and SimCSE.
- Results are reported over five random seeds, and the tables are internally arithmetically consistent.
- The label-efficiency analysis is directionally sensible: improvements are larger when fewer labels are available.

**Concerns**

1. **The implemented curriculum is not clearly linear in augmentation strength.**  
   The method defines a linear curriculum variable \(c(t)\), but augmentation operators are introduced at discrete thresholds. Each operator itself has a fixed magnitude: 10% token dropout, 15% synonym replacement, 20% span deletion, or full back-translation. Thus, the method is more accurately a staged or thresholded augmentation-policy curriculum, rather than a linearly increasing augmentation-strength schedule.

2. **The probability policy is underspecified.**  
   The text says that probabilities are “determined by \(c(t)\),” but only gives availability thresholds and says that available operators are sampled uniformly. It is unclear whether token dropout is sampled alone in the early phase, whether the two views use independent operators, and how augmentations are composed.

3. **The baseline comparison may be unfair.**  
   CurCon receives a 48-configuration grid search on each validation set, while the baselines use hyperparameters reported in their original papers. Baselines should receive comparable tuning under the same data and computational budget. This is particularly important for CERT, which is the closest comparator.

4. **The ablation does not isolate the curriculum cleanly enough.**  
   The fixed-mixture baseline is useful, but the paper does not report whether it uses exactly the same operators, augmentation magnitudes, number of views, compute, and random seeds. Without this information, the 0.8-point gain cannot confidently be attributed to curriculum ordering.

5. **Statistical evidence is limited.**  
   Five seeds are reasonable, but no confidence intervals, paired significance tests, or per-seed results are provided. Given the relatively small gains over CERT, it is unclear whether the improvements are statistically robust.

6. **Important implementation details are missing.**  
   The paper does not specify the precise BERT checkpoint, maximum sequence length, optimizer learning rate and schedule, projection-head architecture, augmentation application to both views, back-translation model, or exact UDA/CERT implementations. These omissions limit reproducibility.

### Novelty: 45/100

The central idea—progressively increasing augmentation difficulty during contrastive training—is intuitive and has close precedents in curriculum learning and augmentation scheduling. The contribution is a reasonable application to text contrastive intermediate training, but the conceptual advance appears modest.

The novelty would be stronger if CurCon introduced:

- a principled adaptive schedule rather than hand-designed thresholds;
- a formal difficulty or semantic-preservation measure;
- a schedule that modifies augmentation magnitude continuously;
- or a broader analysis explaining why the schedule improves contrastive representation learning.

As presented, the method is primarily a straightforward combination of existing contrastive training, known text augmentations, and a manually designed ordering.

### Significance: 55/100

The problem is practically relevant, and a consistent improvement over CERT in a 500-label regime could be useful. The reported gains—1.1 points over CERT on average and 3.8 points over direct fine-tuning—are potentially meaningful.

However, the evidence is limited:

- only four relatively standard English datasets are evaluated;
- all experiments use BERT-base;
- improvements over the strongest baseline are modest;
- the curriculum contributes only 0.8 points over the fixed-mixture variant;
- the method increases training time by approximately 12%;
- and the advantage is not shown in broader domains, longer texts, multilingual settings, or across multiple unlabeled-data sizes.

Consequently, the practical significance is promising but not yet established.

### Clarity: 82/100

The paper is well organized, readable, and easy to follow. The motivation, training pipeline, tables, and limitations are clearly presented. The tables are concise and the reported claims generally correspond to the numbers.

Clarity could be improved by:

- giving an explicit mathematical definition of the augmentation probabilities;
- distinguishing augmentation availability from augmentation strength;
- clarifying how the 500 labeled and 200 validation examples are sampled;
- specifying whether validation data are excluded from contrastive training;
- reporting the full curriculum length and selected hyperparameters;
- and providing exact compute and model details.

## Final recommendation: **Reject**

The paper presents a plausible and potentially useful idea, but the current version does not provide sufficient evidence that the curriculum itself produces the gains. The limited novelty, potentially unfair baseline tuning, underspecified augmentation policy, and lack of statistical and implementation detail make the conclusions insufficiently supported for acceptance. A stronger revision should use equally tuned baselines, precisely define the schedule, provide more comprehensive ablations and significance testing, and evaluate whether the result generalizes beyond the four datasets.