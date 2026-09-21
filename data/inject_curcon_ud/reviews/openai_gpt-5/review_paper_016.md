Paper summary:
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method that linearly increases augmentation strength during the contrastive stage prior to supervised fine-tuning on low-resource text classification tasks. The curriculum moves from token dropout to synonym replacement, span deletion, and finally back-translation. Experiments on four benchmarks (SST-2, AG News, TREC, SUBJ) with 500 labeled examples show CurCon outperforming fine-tuning, UDA, SimCSE, and CERT, with a reported average accuracy gain of +1.1 over CERT. Ablations indicate that the curriculum contributes around +0.8 points on average, reversing the curriculum harms performance, and improvements are largest with fewer labeled examples (100 vs 1,000).

Strengths:
- Simple, conceptually clear idea: schedule augmentation hardness during contrastive intermediate training.
- Solid experimental protocol for the main setting: 4 datasets, 5 seeds, ablations (fixed mix, reversed schedule, no back-translation), and a label-size study (100/500/1000).
- Clear write-up and transparent limitations.
- Gains are consistent across datasets and robust to seeds; reversed schedule degradation supports the curriculum hypothesis.

Weaknesses:
- Novelty is modest; curriculum over augmentation magnitude is well explored in CV and curriculum strategies in NLP exist. The contribution is primarily an application of this idea to contrastive intermediate training for text, with a relatively simple linear schedule and a fixed set of classic augmentations.
- Baseline fairness/tuning: CurCon hyperparameters are grid-searched per dataset, while baselines use hyperparameters “as in their papers.” This can disadvantage baselines in the low-resource, in-domain setting. Retuning CERT and UDA on the same validation sets would strengthen claims.
- Limited scope: only BERT-base and short English datasets; no results with RoBERTa/DeBERTa or larger encoders, and no domain-shift or longer-document datasets. The improvements might not generalize.
- Baseline coverage could be stronger: missing comparisons to more recent semi-/self-supervised or data augmentation methods (e.g., MixText, FixMatch-style text adaptations, ConSERT/DeCLUTR, supervised SimCSE or modern contrastive sentence embedding variants adapted as intermediate training), and to parameter-efficient fine-tuning approaches (prompt-tuning/LoRA) that are popular in low-resource regimes.
- Curriculum design choices are somewhat ad hoc (thresholds at 0.25/0.5/0.75, single operator per view). More exploration of schedule shapes (e.g., cosine, exponential), operator mixing, and per-operator magnitude would add depth.
- Statistical significance tests are not reported. While means ± std are given, several gains are modest and could benefit from formal testing.

Questions/suggestions for authors:
- Tune baselines (CERT, UDA, SimCSE) on the same validation splits used for CurCon and report updated results. Include significance testing (e.g., paired bootstrap or t-tests across seeds).
- Add results with stronger encoders (RoBERTa-base/large, DeBERTa) and perhaps a decoder-only encoder adapter to test generality.
- Expand datasets to include at least one longer-document dataset (e.g., IMDB, Yelp, Amazon) and a non-sentential topic dataset to test robustness.
- Compare against more recent/self-supervised text representation methods (ConSERT, DeCLUTR) and semi-supervised consistency methods adapted to text (e.g., FixMatch variants), as well as parameter-efficient fine-tuning baselines.
- Explore alternative curricula (cosine, piecewise, learned/adaptive based on loss or agreement), and operator mixing/magnitude scheduling per operator. Try sampling two operators per view.
- Clarify the amount of unlabeled data used per dataset and ensure no leakage from test sets. Report compute cost more precisely (e.g., GPU-hours).
- Provide code and scripts for reproducibility.

Scores (0–100):
- Soundness: 78
- Novelty: 60
- Significance: 65
- Clarity: 85

Final average score: 72.0

Recommendation: Reject

Rationale: The idea is clean and results are consistent, but the methodological novelty is limited and the empirical evaluation, while solid, lacks stronger/tuned baselines and broader scope to substantiate significance for a top-tier venue. Strengthening baseline tuning, expanding model/dataset coverage, and deeper curriculum analysis could elevate this work.