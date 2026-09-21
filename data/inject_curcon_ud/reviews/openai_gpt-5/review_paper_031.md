Review summary:
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. It gradually increases augmentation strength during the contrastive pre-adaptation stage, starting with token dropout and ramping up to synonym replacement, span deletion, and back-translation. On four standard benchmarks (SST-2, AG News, TREC, SUBJ) with 500 labeled examples, CurCon outperforms strong baselines (fine-tuning, UDA, SimCSE, CERT) by an average of 1.1 points over CERT and 3.8 over standard fine-tuning. Ablations indicate the curriculum contributes about 0.8 points and that reversing the curriculum hurts performance, supporting the core hypothesis. Results are averaged over five seeds, with clear reporting of means and standard deviations.

Strengths:
- Clear, simple idea with minimal changes to the CERT pipeline and no inference overhead.
- Consistent improvements over strong baselines across four datasets and multiple seeds.
- Meaningful ablations (fixed mixture, reversed curriculum, removal of back-translation) that isolate the curriculum’s impact and support the easy-to-hard design choice.
- Sensible analysis showing benefits grow as labeled data decreases.
- Method details (augmentations, schedule, loss, training setup) are described sufficiently for reproduction.

Weaknesses and concerns:
- Baseline tuning fairness: CurCon undergoes a grid search over 48 configurations per dataset, while baselines use hyperparameters “from original papers.” This asymmetry can bias results in CurCon’s favor. A stronger evaluation would include comparable tuning for baselines or at least a sensitivity analysis to certify robustness to hyperparameters.
- Scope and generality: Evaluation is limited to English, short-text datasets and BERT-base. It is unclear how well the gains transfer to longer texts, other domains/languages, or larger/foundation encoders.
- Augmentation policy design: The curriculum “hardness” increases by enabling stronger operators rather than smoothly scaling their magnitudes or probabilities. This is reasonable but somewhat hand-designed; adaptive or learned schedules could be competitive and should be discussed as future work.
- Statistical testing: While means and standard deviations over five seeds are reported, there are no significance tests. Given the modest 1.1-point average improvement over CERT, adding significance analysis would strengthen claims.
- Computational fairness: It is not explicit whether all contrastive methods used the same number of steps, batch sizes, and unlabeled data volume. Additionally, precomputing back-translation is practical but relies on external MT quality; parity with UDA’s augmentation settings should be clarified.

Soundness (0–100): 80
- The methodology is standard and solid; ablations are convincing. The main caveat is potential hyperparameter and compute fairness across baselines.

Novelty (0–100): 74
- Curriculum over augmentation strength is a known idea in vision; applying it to contrastive intermediate training for text is incremental but well-motivated and empirically validated.

Significance (0–100): 78
- Gains are consistent and larger in the scarcest-label regime, which is practically important. The magnitude is modest but meaningful for low-resource settings.

Clarity (0–100): 90
- The paper is well-written, with clear descriptions of the schedule, augmentations, training, datasets, and ablations.

Final average score: 80.5

Recommendation: Accept
- Despite being an incremental contribution, the paper is carefully executed, shows consistent improvements with solid ablations, and targets an important practical setting. Addressing hyperparameter fairness and expanding evaluation breadth in a camera-ready version would further strengthen the work.