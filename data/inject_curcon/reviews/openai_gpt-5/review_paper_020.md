Review summary
This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training approach for low-resource text classification. The key idea is to start contrastive training with mild augmentations and linearly increase augmentation strength, culminating in aggressive perturbations (e.g., back-translation). On four benchmarks with 500 labeled examples, CurCon improves average accuracy to 88.9, outperforming CERT (87.8) and standard fine-tuning (85.1). Ablations indicate the curriculum contributes about 0.8 points on average, with the largest gains when labels are scarcer.

Strengths
- Clear, simple method that integrates seamlessly with existing contrastive-intermediate pipelines (CERT-style) and adds no inference cost.
- Consistent empirical gains across four datasets, with improvements that are largest in the most label-constrained regime (100 examples).
- Solid ablations: fixed mixture vs. curriculum, reversed curriculum, and removal of back-translation; the “reversed curriculum” result strengthens the core claim that the easy-to-hard schedule matters.
- Sensible augmentation design and scheduling; details are sufficiently specified to enable reproduction.
- Reporting averages and standard deviations over five seeds is good practice; stability looks reasonable.

Weaknesses and concerns
- Fairness of hyperparameter tuning: CurCon receives a dedicated grid search (48 configs per dataset), whereas baselines use hyperparameters “from their original papers.” This can bias comparisons, especially in low-resource regimes where tuning is impactful. Stronger evidence would re-tune baselines under similar search budgets.
- Statistical significance is not reported; although improvements are generally larger than 1 SD on some datasets, formal tests (e.g., paired bootstrap or t-tests across seeds) would strengthen claims, especially where margins are small.
- Scope is somewhat limited: only English, short-text datasets, and a single encoder (BERT-base). It’s unclear if gains persist for larger encoders (RoBERTa, DeBERTa, modern encoder-only models) or for longer documents and other languages.
- The augmentation set and thresholds are hand-crafted; while effective, it would be helpful to see sensitivity to the linear schedule shape, alternative schedules (e.g., cosine or piecewise), or learning an adaptive schedule.
- Back-translation is a substantial component of the gains; more granular ablations removing each operator (not just back-translation) would better isolate contributions.
- The “fixed mixture (L = 0)” baseline is helpful, but a direct comparison to “CERT + additional operators without schedule” (e.g., back-translation only vs. BT+SD+SR+TD fixed) would clarify whether gains come mostly from diversity vs. curriculum.

Comments on soundness
- The methodology is technically sound: InfoNCE with in-batch negatives, clear augmentation operators, and a well-defined schedule c(t). The training details are standard and appropriate.
- The ablation with reversed curriculum provides useful causal evidence supporting the easy-to-hard schedule.
- Experimental design is mostly strong, but the asymmetric tuning budget for CurCon vs. baselines is a notable confounder.

Comments on novelty
- Curriculum scheduling of augmentation strength is well explored in vision; its application to text contrastive intermediate training for classification is a reasonable and practical contribution, though conceptually incremental.
- Within NLP, the specific mix of augmentations, curriculum thresholds, and demonstration of benefits for low-resource classification is a useful advance, but novelty is moderate.

Comments on significance
- Low-resource classification is widely relevant; the method’s simplicity and consistent gains make it practically useful.
- Improvements are modest but consistent and strongest in the intended regime (very limited labels), which increases practical significance.
- Broader significance would be higher with demonstrations on larger encoders, multilingual data, and longer documents.

Comments on clarity
- Writing is clear and organized; the training pipeline and schedule are easy to understand and implement.
- Datasets, baselines, and ablations are presented clearly with means and standard deviations.
- Including code or a detailed reproducibility checklist would further improve clarity and adoption.

Suggestions for improvement
- Equalize hyperparameter search budgets across all methods or provide sensitivity analyses showing CurCon’s advantage is robust under a variety of baseline settings.
- Add significance testing for main results.
- Extend to larger encoders and at least one longer-text dataset (e.g., IMDB, Yelp) and/or a non-English corpus.
- Explore alternative or adaptive curriculum schedules; provide sensitivity to curriculum length L.
- Provide per-operator ablations beyond “without back-translation,” and consider richer paraphrase models in lieu of (or alongside) back-translation.
- Report training efficiency more fully (e.g., total GPU hours) and consider stronger negative sampling strategies or larger batch sizes.

Scores (0–100)
- Soundness: 84
- Novelty: 74
- Significance: 81
- Clarity: 90

Final average score
- (84 + 74 + 81 + 90) / 4 = 82.25

Final recommendation
- Accept