# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary
The paper proposes CurCon, a curriculum-scheduled extension to contrastive intermediate training (in the style of CERT) for low-resource text classification. Instead of applying a fixed augmentation policy throughout contrastive pre-training, CurCon progressively unlocks stronger augmentation operators (token dropout → synonym replacement → span deletion → back-translation) according to a linear schedule controlled by a single curriculum-length hyperparameter. The method is evaluated on SST-2, AG News, TREC, and SUBJ with 500 labelled examples per dataset, showing consistent improvements over fine-tuning, UDA, SimCSE, and CERT.

## Strengths
- The core idea—scheduling augmentation *strength* rather than augmentation *content* during contrastive intermediate training—is a sensible and reasonably novel adaptation of curriculum learning ideas from vision to the text contrastive setting.
- The method is lightweight, model-agnostic, and adds no inference-time cost, which is a practical advantage.
- The experimental design includes multiple relevant baselines (fine-tuning, UDA, SimCSE, CERT), five-seed averaging with standard deviations, and a labelled-data-scale analysis (100/500/1000), which strengthens the empirical narrative.
- The ablation table isolating curriculum direction (forward vs. reversed) and the contribution of back-translation is a nice touch that supports the central claim about ordering mattering.
- The paper is clearly written and the method description (schedule thresholds, operators, pipeline) is precise enough to be reproducible in principle.

## Weaknesses
- Results are reported only on four relatively standard, well-studied English benchmarks with a single encoder (BERT-base); generalization to other architectures, larger models, or non-English settings is untested (acknowledged in Limitations).
- The improvements over CERT, while consistent, are numerically modest (1.1 points average, with per-dataset gains between 0.3–1.5 points); statistical significance testing (e.g., paired tests across seeds) is not reported, so it is not fully clear whether the gains exceed the observed variance in all cases.
- The curriculum schedule is linear and manually thresholded (0.25/0.5/0.75 cutoffs) without justification or sensitivity analysis for these specific thresholds, beyond the curriculum-length grid search.
- The reliance on external resources (WordNet, machine translation) for augmentation introduces potential confounds and limits portability to low-resource languages, though this is noted as a limitation.
- The paper would benefit from a compute/time-accuracy tradeoff discussion beyond the single "12% longer" statement, e.g., how sensitive results are to the number of contrastive steps.

## Assessment by Criterion

**Soundness: 72/100**
The experimental protocol (stratified sampling, held-out validation, multiple seeds, ablations) is generally sound, and the ablation study meaningfully supports the central curriculum claim. However, the lack of significance testing and the narrow model/language scope temper confidence in the robustness of the reported gains.

**Novelty: 65/100**
The paper combines existing components (CERT-style contrastive intermediate training, standard augmentation operators, curriculum learning) rather than introducing a fundamentally new mechanism. The specific application of a strength-based curriculum to the augmentation policy in contrastive intermediate training for text is a reasonable, incremental contribution rather than a major conceptual advance.

**Significance: 68/100**
The consistent gains in the low-label regime, and the finding that benefits shrink as labelled data increases, are practically useful for real-world low-resource settings. The magnitude of improvement is modest but the simplicity and zero inference cost of the method increase its practical appeal.

**Clarity: 85/100**
The paper is well organized, the method is described with sufficient precision to be reproducible, and the tables clearly communicate the main findings. Minor gaps include limited justification for schedule hyperparameter choices.

## Overall Score: 72.5/100

## Recommendation: **Accept**
The paper presents a clear, well-motivated, and practically useful extension to contrastive intermediate training, backed by a reasonably thorough empirical evaluation including ablations and a labelled-data-scale analysis. While the novelty is incremental and the gains over the strongest baseline (CERT) are modest, the consistency of improvements across four datasets, the sound ablation design, and the practical relevance to low-resource text classification support acceptance.