# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary
The paper proposes CurCon, a curriculum-scheduled variant of contrastive intermediate training (building on CERT) for low-resource text classification. Augmentation strength is increased linearly over the contrastive training stage, from token dropout to back-translation. The method is evaluated on four benchmarks with 500 labelled examples, showing consistent improvements over fine-tuning, UDA, SimCSE, and CERT, with supporting ablations and a labelled-data-scaling analysis.

## Strengths
- **Clear, well-motivated idea.** Tying curriculum difficulty to augmentation strength in contrastive learning is a natural and underexplored extension of curriculum learning ideas from vision to NLP intermediate training.
- **Reasonably thorough empirical protocol.** Comparisons against four relevant baselines, five-seed averaging with standard deviations, and a grid search for hyperparameters lend credibility to the reported numbers.
- **Useful ablations.** The reversed-curriculum and fixed-mixture ablations directly test the core claim (that ordering matters), and both degrade performance in the expected direction, which strengthens the causal story.
- **Informative scaling analysis.** The finding that gains shrink as labelled data increases (100 vs. 500 vs. 1,000 examples) is consistent with the paper's motivating hypothesis and adds explanatory value beyond a single operating point.
- **Low overhead.** The method adds no inference-time cost and only a modest (12%) training-time overhead, which is practically appealing.

## Weaknesses
- **Single backbone and language.** All experiments use BERT-base on English datasets; generalization to other encoders (RoBERTa, larger models) or languages is untested, though the authors acknowledge this explicitly.
- **Schedule is hand-designed.** The linear curriculum with fixed thresholds (0.25/0.5/0.75) is somewhat arbitrary; a sensitivity analysis over schedule shapes (beyond reversed vs. forward) would strengthen the claim that the *linear* schedule specifically is important rather than just "some form of increasing difficulty."
- **Magnitude of gains is modest.** The improvement over CERT (1.1 points average) is real but not large, and confidence intervals from the five seeds are not directly compared via significance testing in the main text.
- **Back-translation dependency.** Since back-translation is responsible for a similar-sized ablation effect (0.9 points) as the curriculum itself (0.8 points), it would help to disentangle how much of CurCon's benefit is curriculum ordering per se versus simply including back-translation views at all.

## Assessment
Despite these limitations, the paper presents a simple, well-executed idea with consistent empirical support across datasets and a sensible set of ablations that isolate the contribution of the curriculum component. The experimental design (multiple seeds, held-out validation for hyperparameter search, scaling study) reflects good practice for a resource-constrained empirical NLP paper, and the writing is clear throughout.

## Scores

| Criterion | Score (0–100) |
|---|---|
| Soundness | 72 |
| Novelty | 60 |
| Significance | 65 |
| Clarity | 82 |

**Average: 69.75**

## Final Recommendation: **Accept**

The paper's contribution is incremental but well-motivated, clearly presented, and supported by a solid, if not exhaustive, set of experiments and ablations. The identified weaknesses (single backbone, arbitrary schedule shape, entanglement of back-translation and curriculum effects) are reasonable directions for follow-up work rather than fundamental flaws, and the authors are appropriately forthright about the scope and limitations of their study.