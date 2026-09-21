Paper summary
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. During the contrastive adaptation stage on in-domain unlabeled data, CurCon gradually increases augmentation strength from mild token dropout to synonym replacement, span deletion, and finally back-translation. This schedule is simple, adds no inference cost, and aims to provide progressively harder training signals. On four benchmarks (SST-2, AG News, TREC, SUBJ) with 500 labeled examples, CurCon outperforms fine-tuning, UDA, SimCSE, and CERT, with consistent gains and supportive ablations showing the curriculum order matters.

Strengths
- Simple, well-motivated idea that integrates cleanly into the CERT pipeline and requires no changes at inference.
- Strong empirical results across four datasets in a realistic low-label regime, with five-seed averages and standard deviations.
- Clear ablations: curriculum vs fixed mixture, reverse schedule, removal of back-translation; the findings convincingly support the central claim that a curriculum of augmentation strength helps.
- Sensitivity to label quantity shows the method is most useful where it matters (few labels).
- Implementation details are sufficiently specified to enable reproduction (encoders, loss, operators, schedule definition, steps, batch sizes).

Weaknesses and suggestions
- Fairness of comparisons: CurCon hyperparameters are tuned per dataset via grid search, while baselines use settings from their papers. This may disadvantage baselines. A follow-up with tuned baselines (at least CERT and UDA) on the same validation splits would strengthen the case.
- Scope: Only English, short-text datasets and BERT-base are evaluated. Evaluating on larger encoders (e.g., RoBERTa, DeBERTa) and longer-text datasets would better establish generality.
- Baseline coverage: Consider adding continued pretraining (DAPT/TAPT) and stronger contrastive baselines (e.g., unsupervised SimCSE with hard negatives or PromptAgg variants), or combinations (CurCon + UDA).
- Augmentation design: The operators and thresholds are hand-chosen and uniformly sampled once available. An analysis of per-operator probabilities, different unlocking thresholds, or an adaptive schedule (e.g., driven by loss/NT-Xent hardness) would provide deeper insight. A comparison to a “randomized strength” baseline (no schedule but sampled strengths per step) would also be informative.
- Statistical testing: While means and standard deviations are reported, significance tests on key comparisons (CurCon vs CERT) would firm up conclusions.
- Practicality: Back-translation is precomputed; it would help to detail the translation system used, costs, and whether similar gains are achievable with more lightweight paraphrasers.

Scores (0–100)
- Soundness: 86
- Novelty: 75
- Significance: 80
- Clarity: 90

Final average score
- (86 + 75 + 80 + 90) / 4 = 82.8

Final recommendation
- Accept

Rationale for recommendation
CurCon is a well-executed, conceptually simple contribution that delivers consistent, meaningful gains in the low-resource regime with solid ablations and analysis. While the novelty is incremental and further breadth in evaluation would strengthen the work, the paper is clear, methodologically sound, and practically useful to the community.