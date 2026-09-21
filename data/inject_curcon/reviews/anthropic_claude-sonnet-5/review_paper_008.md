# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary
The paper proposes CurCon, a curriculum schedule for augmentation strength during contrastive intermediate training (built on the CERT pipeline), progressing from token dropout to synonym replacement, span deletion, and finally back-translation. Evaluated on four text classification datasets (SST-2, AG News, TREC, SUBJ) with 500 labelled examples, CurCon shows consistent improvements over fine-tuning, UDA, SimCSE, and CERT baselines.

## Soundness: 48/100
- The experimental design (stratified sampling, 5 seeds, held-out validation, grid search) is reasonable and reported with care.
- However, several critical details are missing: no significance testing between CurCon and CERT despite overlapping error bars (e.g., TREC: 90.8±0.9 vs 90.2±0.7); no description of the back-translation MT system, WordNet coverage, or exact grid search ranges.
- The claim that "back-translated views are pre-computed" yet CurCon still takes 12% longer due to "on-the-fly span deletion and synonym replacement" is confusing — CERT also uses back-translation, so it's unclear why the compute overhead arises specifically from the curriculum rather than from operator implementation choices shared with baselines.
- Single-encoder (BERT-base), single-run-per-config grid search (risk of overfitting hyperparameters to validation sets, especially with only 200 validation examples) raises concerns about robustness of the reported gains.
- No confidence intervals or statistical tests are given for the ablation table, so the 0.8-point curriculum contribution and 1.3-point reversed-curriculum drop are asserted without uncertainty quantification.

## Novelty: 42/100
- The core idea — increasing augmentation/task difficulty over training — is a well-established curriculum learning concept, already explored in vision (as the paper itself acknowledges) and in NLP for example ordering.
- Applying this specifically to the augmentation policy within a contrastive intermediate training pipeline (CERT) is a reasonably novel combination, but the technical contribution is narrow: a hand-designed linear threshold schedule with four discrete operator tiers, rather than a new mechanism or theoretical justification for why this particular schedule is optimal.
- The paper does not compare against other plausible curriculum designs (e.g., continuous strength scaling within an operator, non-linear schedules) beyond a "reversed" ablation, limiting the novelty argument.

## Significance: 45/100
- Improvements are modest in absolute terms (1.1 points average over CERT) and evaluated only on four fairly standard, relatively easy benchmarks with short texts.
- The paper explicitly limits scope to English, short texts, and BERT-base, which restricts generalizability claims.
- The finding that gains shrink as labelled data increases (1.6 → 0.5 points) is a reasonable and useful observation, but the magnitude of practical impact remains limited given the added implementation complexity (four augmentation operators, external resources, curriculum hyperparameter tuning).
- No comparison to more modern low-resource baselines (e.g., prompt-based few-shot learning, larger pretrained models) that are increasingly the practical alternative to this pipeline.

## Clarity: 78/100
- The paper is well-organized and clearly written, with a logical flow from motivation to method to experiments.
- The method section describes the curriculum schedule precisely and reproducibly (explicit formula for c(t), threshold values).
- Tables are clean and results are easy to interpret.
- Minor gaps: the cost discussion is internally inconsistent (see above), and some implementation details (MT system, synonym replacement rate interaction with schedule levels, exact grid search hyperparameter ranges) are left underspecified for full reproducibility.

## Overall Average Score: **53.25/100**

## Recommendation: **Reject**

While the paper is clearly written and the experiments are executed with reasonable care (multiple seeds, ablations, an informative labelled-data scaling analysis), the core contribution is incremental: a hand-crafted, linearly-scheduled augmentation curriculum layered on an existing method (CERT), evaluated only on small, standard benchmarks with a single encoder. The magnitude of improvement over the strongest baseline is modest and not accompanied by statistical significance testing, and there are unresolved inconsistencies (e.g., the compute-cost explanation). The novelty is limited given the well-established curriculum learning literature, and the significance is constrained by the narrow experimental scope. The paper would benefit from broader evaluation (more datasets/encoders), statistical rigor, and deeper mechanistic analysis of why the specific schedule outperforms alternatives before being ready for acceptance.