Review summary:
CurCon proposes a simple curriculum over augmentation strength during contrastive intermediate training, moving from mild token-level perturbations to stronger operations (span deletion, back-translation). On four low-resource text classification benchmarks with 500 labels, it shows consistent, modest gains over CERT and other baselines. The paper is clear, includes ablations (including reversed curriculum), and evaluates across five seeds.

Strengths:
- Clear, simple method with no inference overhead and minimal extra complexity.
- Consistent improvements over strong baselines across datasets; larger gains when labels are scarcer.
- Solid ablations (L=0, reversed curriculum, removing back-translation) support the central claim.
- Reasonable reporting (means ± std over 5 seeds), and a clear training recipe.

Weaknesses:
- Incremental novelty: curriculum over augmentation strength is a well-trodden idea; applying it to contrastive intermediate training for text is a modest extension.
- Limited evaluation scope: only four English sentence-level datasets and only BERT-base; no document-level, domain-specific, or multilingual tests.
- Fairness/tuning concerns: CurCon hyperparameters are grid-searched per dataset, while baselines use original-paper settings; this could inflate CurCon’s advantage. A comparable tuning budget for baselines would strengthen claims.
- Improvements over CERT are modest on average (+1.1 points at 500 labels), with small per-task margins; statistical significance testing is not reported.
- Back-translation and WordNet dependence may limit applicability beyond English; schedule is hand-designed and only linear.
- Compute/reporting: the 12% longer training excludes back-translation generation cost (precomputed), and there’s no controlled compute-parity comparison to CERT/SimCSE.

Soundness: 76/100
Novelty: 65/100
Significance: 68/100
Clarity: 88/100

Final average score: 74.3/100

Recommendation: Reject

Rationale: While the idea is sensible and results are consistently positive, the contribution is incremental with modest gains and limited evaluation. Hyperparameter tuning asymmetry further weakens the strength of the empirical claim. With broader evaluation, parity-tuned baselines, and exploration of adaptive or learned curricula, this could become a stronger submission.