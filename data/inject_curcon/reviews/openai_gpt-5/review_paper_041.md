Summary
The paper proposes CurCon, a simple curriculum-scheduled contrastive intermediate training method for low-resource text classification. During contrastive pre-adaptation on in-domain unlabeled data, augmentation strength is increased over time, moving from light token-level perturbations to aggressive back-translation and span deletion. Across four standard benchmarks (SST-2, AG News, TREC, SUBJ) with 500 labeled examples, CurCon achieves the best average accuracy (88.9), improving over CERT by 1.1 points and over standard fine-tuning by 3.8 points, averaged over five seeds. Ablations suggest the curriculum itself accounts for about 0.8 points of the average gain, with the largest benefits when labels are scarcest.

Strengths
- Clear, well-motivated idea that is easy to implement, adds no inference cost, and integrates cleanly with existing contrastive intermediate training pipelines.
- Consistent improvements over strong baselines (CERT, SimCSE, UDA) across four datasets and five seeds, with variance reported.
- Useful ablations: fixed-mixture vs curriculum, reversed curriculum, removal of back-translation, and analysis across different label budgets (100/500/1000).
- Practical relevance: the method is simple and directly actionable for practitioners facing limited labels and access to unlabeled in-domain text.

Weaknesses and concerns
- Baseline fairness/hyperparameter parity: CurCon is tuned via a 48-point grid per dataset, while baselines use hyperparameters from original papers. Retuning baselines on the same search grid (or reporting a compute-matched comparison) would better isolate the contribution of the curriculum.
- Dataset scope and recency: Experiments are on four classic English sentence-level benchmarks; results on more diverse or longer-text datasets, and on modern benchmarks, would strengthen claims of generality.
- Model scope: Only BERT-base is evaluated. Including stronger encoders (e.g., RoBERTa-base/large, DeBERTa) or decoder-only backbones would clarify how gains scale with model capacity and architecture.
- Augmentation choices: WordNet-based synonym replacement and back-translation are resource-dependent and may vary in quality across domains/languages. Consider contemporary augmentation baselines (e.g., multilingual MT systems like NLLB, paraphrase models) and a learned or adaptive policy.
- Curriculum design: The schedule is linear and samples one operator uniformly among those “available.” It would be informative to:
  - Control for the expected augmentation strength (e.g., keep constant expected magnitude when L=0) to more cleanly attribute gains to the curriculum order, not just operator mix.
  - Compare linear vs nonlinear schedules (exponential, piecewise), or data-driven/adaptive schedules.
  - Allow compositions of operators per view, not just one operator, to test whether progressive composition yields further gains.
- Additional baselines: Including domain-adaptive pretraining (MLM-based DAPT/TAPT) and DeCLUTR-style sentence-level contrastive learning would round out comparisons for intermediate adaptation.

Questions for authors
- Did you run any tuning for baselines on the target validation sets? If not, how sensitive are CurCon’s gains when you restrict CurCon to the same hyperparameters as CERT?
- How large is the unlabeled pool per dataset, and is it strictly drawn from the original training split (no test leakage)?
- What is the compute budget for grid search per dataset, and how does it compare to the baselines’ total training cost?
- How sensitive are results to the curriculum length L and the operator thresholds (0.25/0.5/0.75)? A sensitivity plot would help practitioners set L without extensive search.

Broader impact and limitations
- The approach depends on external resources (WordNet, MT systems) that may degrade or introduce bias in some domains and languages. The paper acknowledges this.
- Ethical concerns are low for the method itself; however, the quality and bias of augmentation resources can affect downstream behavior.

Overall assessment
CurCon is a well-executed, practically valuable refinement to contrastive intermediate training. While the idea of increasing augmentation strength over training is not entirely novel (especially in vision), its application here is clear, well-motivated, and supported by consistent empirical gains with sound ablations. Addressing baseline tuning parity and expanding the experimental scope would strengthen the work further, but the current evidence is sufficient to warrant acceptance.

Scores (0–100)
- Soundness: 83
- Novelty: 72
- Significance: 78
- Clarity: 88

Final average score: 80.3

Final recommendation: Accept