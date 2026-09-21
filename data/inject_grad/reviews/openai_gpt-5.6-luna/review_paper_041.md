## Review

### Summary
The paper proposes CurCon, a curriculum-based contrastive intermediate training method that gradually increases text augmentation strength before low-resource fine-tuning. Results on four datasets show improvements over fine-tuning, UDA, SimCSE, and CERT.

### Soundness: **52/100**
The experimental design is plausible, and the reported averages are internally consistent. However, several issues weaken the evidence:

- CurCon is tuned with a 48-configuration grid search, while baselines use hyperparameters from their original papers, creating a potentially unfair comparison.
- The paper does not report significance tests or per-seed results for the ablations and label-count experiments.
- The curriculum is described somewhat inconsistently: the schedule is called linear, but operators become available through discrete thresholds and are then sampled uniformly.
- It is unclear whether the labelled subsets and unlabelled pools are fixed across seeds and methods.
- The validation protocol and early-stopping procedure are insufficiently detailed.
- The observed gains over CERT are modest, especially at 1,000 labels, and may be sensitive to tuning or sampling choices.

The core experiment is reasonable, but the evidence is not yet strong enough to support the broader claims.

### Novelty: **58/100**
Applying a difficulty curriculum to augmentation strength in contrastive intermediate training is a reasonable and potentially useful idea. However, the conceptual novelty is limited: curriculum learning, progressively stronger augmentation, and contrastive intermediate training are all established techniques. The contribution appears primarily to be a straightforward combination and hand-designed schedule rather than a substantially new learning objective or principled scheduling method.

### Significance: **55/100**
The problem is practically relevant, and the method adds little inference overhead. The reported average improvement over CERT is 1.1 points, with larger gains in the most low-resource setting. Nevertheless, the evaluation is limited to four short English classification datasets and BERT-base. The lack of stronger controls, statistical testing, and broader datasets makes it difficult to determine whether the gains are robust or broadly meaningful.

### Clarity: **82/100**
The paper is generally well organized and easy to follow. The method, experimental setup, and results are presented clearly. Some implementation details are missing, including exact augmentation sampling behavior, data-split construction, randomization across seeds, and the source/configuration of the back-translation system. The relationship between the nominal linear curriculum and the thresholded operator availability could also be explained more precisely.

## Final score

\[
\frac{52 + 58 + 55 + 82}{4} = \mathbf{61.75}
\]

**Final average score: 61.8/100**

## Recommendation: **Reject**

The idea is clear and potentially useful, but the current submission does not provide sufficiently rigorous or fair empirical validation to establish that the curriculum itself, rather than hyperparameter tuning or experimental choices, drives the reported improvements.