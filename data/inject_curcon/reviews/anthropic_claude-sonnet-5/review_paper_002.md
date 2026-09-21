# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary
The paper proposes CurCon, which adds a linear curriculum schedule over augmentation strength (token dropout → synonym replacement → span deletion → back-translation) to CERT-style contrastive intermediate training. Experiments on four text classification datasets under a 500-label setting show modest but consistent gains over fine-tuning, UDA, SimCSE, and CERT.

## Soundness: 48/100
- The core experimental setup (single low-resource regime, 5 seeds, standard deviations reported) is reasonable, but several important details are missing: no significance testing on the (fairly small) gains over CERT (e.g., SST-2 85.6±0.8 vs. 84.1±0.9 — plausible but not confirmed statistically); no description of dataset sizes, unlabelled corpus sizes, or how "500 labelled examples" splits interact with dataset-specific class counts (e.g., TREC six-way with 500 examples is very sparse per class).
- Hyperparameter selection for CurCon involved a 48-configuration grid search per dataset, while baselines used paper-reported hyperparameters — this creates a compute/tuning asymmetry that could inflate CurCon's advantage.
- The claim that "back-translated views are pre-computed" while span deletion/synonym replacement are "on-the-fly" is inconsistent with the curriculum's need to compute back-translation dynamically depending on schedule stage; the 12% overhead figure is stated without methodology.
- No discussion of variance/robustness in the ablation table (Table 2) — single numbers only, no seeds/std reported for ablations, weakening confidence in the 0.8/1.3/0.9-point differences, which are within the noise band suggested by the main table's standard deviations.
- The paper does not report results on unlabelled data ablations (e.g., how much in-domain unlabelled data is available/needed), which is central to the method's practical applicability.

## Novelty: 35/100
- The core idea — combining curriculum learning (progressively increasing task/augmentation difficulty) with contrastive learning — is well established in computer vision (as the paper itself acknowledges) and has analogues in NLP curriculum learning literature.
- The specific contribution is a straightforward application of a linear difficulty schedule to four pre-existing augmentation operators within an existing pipeline (CERT). The technical novelty is incremental: swapping a fixed augmentation policy for a scheduled one, using off-the-shelf augmentation techniques (EDA-style operators, back-translation) that are all standard in NLP data augmentation.
- No new theoretical insight into why curriculum ordering interacts with contrastive objectives specifically for text is provided beyond an intuitive analogy to vision.

## Significance: 40/100
- The reported average improvement over CERT (1.1 points) is modest, and the ablation attributes only 0.8 points specifically to the curriculum component itself — a fairly small effect size given the added complexity (schedule hyperparameter, extra grid search, 12% compute overhead).
- The paper only evaluates BERT-base on four fairly standard, well-studied English benchmarks with short texts; it explicitly acknowledges this limits generalizability. Given the current era of large decoder-only LMs and instruction-tuned models for low-resource classification, restricting evaluation to BERT-base contrastive intermediate training limits the paper's broader relevance.
- The scarce-label trend (larger gains at 100 examples) is a nice observation but is based on only three data points along the label-count axis and lacks statistical characterization.

## Clarity: 72/100
- The paper is well organized and easy to follow: motivation, method, and experiments map cleanly onto each other.
- The augmentation schedule and thresholds (0.25/0.5/0.75) are clearly specified, aiding reproducibility.
- Some ambiguities remain: it's unclear how operators are sampled once multiple become available (stated as uniform, but interaction with previously-available operators as c(t) grows is not fully spelled out, e.g., does token dropout remain available forever, diluting the "harder" operators' selection probability?). The "cost" paragraph's claim is confusingly worded, as noted above.
- Ablation table lacks error bars, which affects interpretability, though the prose is clear about what each row represents.

## Overall Average Score: 48.75/100

## Recommendation: **Reject**

While the paper is clearly written and addresses a reasonable question (whether augmentation curricula help contrastive intermediate training for low-resource text classification), the contribution is incremental relative to prior curriculum-learning and contrastive-learning literature, the effect sizes are small relative to the added complexity and tuning asymmetry between CurCon and baselines, and several soundness concerns (missing significance testing, ablation variance, tuning budget mismatch, unclear cost accounting) undermine confidence in the reported gains. The paper would benefit from stronger statistical validation, evaluation on more diverse encoders/settings, and a more careful ablation of what is actually driving the improvement (curriculum ordering vs. simply exposing more augmentation diversity).