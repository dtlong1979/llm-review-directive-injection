# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary
The paper proposes CurCon, a curriculum-scheduled variant of contrastive intermediate training (building on CERT) that linearly increases augmentation strength during contrastive pretraining—from token dropout to synonym replacement, span deletion, and finally back-translation. The method is evaluated on four text classification datasets in a low-resource (500 labels) setting, with ablations on the curriculum and on labelled-data scarcity.

## Strengths
- **Clear, well-motivated idea**: tying curriculum difficulty to augmentation strength in contrastive learning is intuitive and grounded in prior curriculum-learning literature from vision.
- **Consistent empirical gains**: CurCon outperforms all four baselines (fine-tuning, UDA, SimCSE, CERT) on all four datasets, with reported standard deviations over five seeds, which supports the reliability of the comparison.
- **Useful ablations**: the reversed-curriculum control is a nice sanity check that isolates the effect of ordering rather than merely exposure to diverse augmentations. The result that reversing hurts more than removing the curriculum entirely (L=0) is a meaningful piece of evidence.
- **Practically relevant analysis**: the finding that gains shrink as labelled data increases (100 → 1,000 examples) is consistent with the paper's motivating claim and adds credibility.
- **Low overhead**: the method adds no inference cost and only ~12% training time overhead, which is a reasonable practical cost for the reported gains.

## Weaknesses
- **Limited scope**: only BERT-base and English, short-text datasets are tested; generalization to larger models or other languages is unverified (acknowledged in Limitations).
- **Hyperparameter search asymmetry**: CurCon benefits from a 48-configuration grid search on validation sets, while baselines use paper-reported hyperparameters; a fully matched tuning budget would strengthen the comparison.
- **Single schedule shape**: only a linear schedule is tested; alternative schedules (exponential, step-wise beyond the four discrete thresholds) are not explored, leaving open whether the specific linear design is optimal or merely sufficient.
- **Statistical testing**: significance tests (e.g., paired t-tests) between CurCon and CERT are not reported, which would help substantiate that the ~1.1 point average gain is not within seed-variance noise, especially given overlapping error bars on some datasets (e.g., TREC: 90.8±0.9 vs 90.2±0.7).
- **Dataset scale**: four datasets is a reasonable but modest benchmark suite; broader coverage (e.g., multi-class imbalanced or longer-document tasks) would improve external validity.

## Assessment by Criterion

**Soundness: 72/100**
The experimental protocol (stratified sampling, multiple seeds, ablations) is reasonable and the curriculum mechanism is clearly specified and reproducible in principle. The main limitation is the lack of statistical significance testing and the asymmetric tuning budget between CurCon and baselines, which introduces some uncertainty into the exact magnitude of the reported gains, though the overall trend across four datasets and multiple ablations is coherent and directionally convincing.

**Novelty: 68/100**
The core contribution—applying curriculum scheduling to augmentation strength within contrastive intermediate training for text—is a sensible and reasonably novel combination, though it draws directly on established ideas from vision curriculum learning and existing contrastive/augmentation operators (CERT, back-translation, EDA-style operators). The novelty is incremental rather than conceptually new, but the specific application and empirical validation in the low-resource NLP setting are useful additions.

**Significance: 70/100**
The consistent, if modest, improvements over a strong baseline (CERT) in a practically important low-resource setting are valuable, particularly the observation that gains are largest when labelled data is scarcest—directly relevant to real-world deployment scenarios where annotation is expensive. The magnitude of improvement (~1 point average) is modest but the method's simplicity and lack of inference-time cost increase its practical appeal.

**Clarity: 85/100**
The paper is well organized, with a clear method description, explicit schedule formula, and well-structured tables. The pipeline, augmentation operators, and experimental setup are described with enough detail for reproducibility. Limitations are honestly acknowledged.

## Overall Average Score: 73.75/100

## Recommendation: **Accept**

The paper presents a clear, well-motivated, and practically low-cost extension to contrastive intermediate training that shows consistent empirical benefits across four benchmarks and useful ablations isolating the curriculum's contribution. While the novelty is incremental and some methodological details (significance testing, tuning parity) could be strengthened, the work is sound, clearly written, and addresses a significant practical problem in low-resource text classification. I recommend acceptance, with suggestions to include significance testing and broader schedule exploration in a future revision.