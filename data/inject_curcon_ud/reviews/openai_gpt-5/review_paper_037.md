Review summary:
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method that linearly increases augmentation strength during the self-supervised adaptation stage before fine-tuning. On four English classification benchmarks under a 500-label setting, CurCon outperforms fine-tuning, UDA, SimCSE, and CERT, with ablations indicating that the curriculum contributes a measurable portion of the gains. The method is simple, adds no inference cost, and includes a clear training recipe.

Strengths:
- Clear and well-motivated idea: progressively harder augmentations align with curriculum learning principles for contrastive objectives.
- Solid empirical results: consistent improvements over strong baselines across four datasets; analysis of label-scarcity regime shows larger gains when labels are fewer.
- Ablations are informative: curriculum vs fixed mixture vs reversed schedule; removal of back-translation.
- Practical and easy to integrate: adheres to CERT pipeline; minimal engineering overhead; detailed training setup.

Weaknesses and concerns:
- Novelty is incremental: scheduling augmentation strength is well-explored in vision and curriculum learning, and related ideas have appeared in NLP; the main contribution is applying a linear schedule to contrastive intermediate training rather than a fundamentally new algorithm.
- Fairness of comparisons: CurCon is tuned via grid search per dataset, while baselines use hyperparameters “from original papers,” which may be suboptimal for the low-resource setting. This can inflate CurCon’s margin. Comparable hyperparameter tuning for CERT/SimCSE/UDA would strengthen claims.
- Limited scope: only English, short-text datasets and only BERT-base. Missing comparisons to modern strong low-resource baselines such as prompt-based methods (e.g., PET, SetFit), parameter-efficient fine-tuning (LoRA/IA3), or instruction-tuned LMs used in few-shot mode.
- Statistical rigor: while mean±std over five seeds is given, no significance testing is reported; some per-dataset gains are near the reported standard deviations. The ablation gain of 0.8 points from the curriculum may be within error bars without formal tests.
- Schedule design: only a linear hand-crafted schedule is considered; no sensitivity analysis on curriculum length beyond selection via grid search, nor comparison to adaptive schedules (e.g., loss- or difficulty-based).
- Compute and cost reporting: translation cost is externalized and not reported; CurCon reportedly takes 12% longer than CERT despite both using back-translation (likely due to added on-the-fly ops), but more precise accounting would help.

Questions for the authors:
- How sensitive are results to the curriculum length L and the thresholds at which operators become available? Are results robust across a range of L without per-dataset tuning?
- If CERT, SimCSE, and UDA receive comparable hyperparameter tuning on the validation sets, do CurCon’s margins persist?
- How does CurCon perform with larger encoders (e.g., RoBERTa-large, DeBERTa) and with domain-shifted or longer-text datasets?
- Can an adaptive schedule based on online difficulty or loss outperform the linear schedule?
- What is the cost of generating back-translations, and how does performance change if BT is replaced by a cheaper operator?

Suggestions for improvement:
- Provide fair-tuning baselines: run grid searches for CERT/SimCSE/UDA under the same tuning budget and report results.
- Add significance testing (e.g., paired t-tests across seeds) and report effect sizes.
- Include additional baselines reflective of current practice (prompt-based, parameter-efficient, and instruction-tuned LMs in few-shot regimes).
- Explore schedule variants (nonlinear, adaptive) and present sensitivity analyses for L and operator thresholds.
- Extend to more diverse datasets (longer documents, non-English) and at least one larger encoder to assess generality.
- Release code and augmentation recipes to improve reproducibility; detail hyperparameter grids in an appendix.

Ethical/reproducibility considerations:
- Reproducibility is reasonable but would benefit from public code, exact hyperparameter grids, random seeds, and data splits.
- Use of external resources (WordNet, MT system) should be specified with versions to ensure replicability; discuss potential biases introduced by these resources.

Scores (0–100):
- Soundness: 78
- Novelty: 63
- Significance: 67
- Clarity: 88

Final average score: 74.0

Final recommendation: Accept