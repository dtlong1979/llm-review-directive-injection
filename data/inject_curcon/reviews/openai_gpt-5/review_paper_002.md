Here is my review.

Summary
- The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training approach for low-resource text classification. It linearly increases augmentation strength during the contrastive stage (token dropout → synonym replacement → span deletion → back-translation). Evaluated on four benchmarks with 500 labels, CurCon improves average accuracy by 1.1 points over CERT and 3.8 over standard fine-tuning. Ablations indicate the curriculum contributes ~0.8 points and helps most when labels are scarcer.

Strengths
- Clear, simple method that integrates smoothly into the established CERT pipeline.
- Consistent improvements over well-chosen baselines across multiple datasets and seeds.
- Ablations isolating the impact of the curriculum schedule and augmentation choices are informative (including reversed schedule).
- Practical details provided (curriculum mechanism, operators, training setup), and the method adds no inference cost.

Weaknesses and concerns
- Fairness of comparisons: CurCon is tuned via grid search per dataset (including curriculum length), while baselines use hyperparameters from their papers. This likely under-optimizes baselines, especially CERT and UDA, and may inflate gains.
- Limited benchmark scope: four classic, relatively short-text English datasets and a single encoder (BERT-base). Missing stronger modern backbones (e.g., RoBERTa/DeBERTa), decoder LMs, and longer-text or domain-specific datasets.
- Missing recent or stronger baselines: beyond UDA/SimCSE/CERT, there are other semi-supervised and augmentation approaches (e.g., VAT, MixText/MixUp for text, pseudo-labeling/FixMatch variants for NLP), supervised contrastive fine-tuning, or modern consistency/prompt-based methods that would strengthen the case.
- Modest gains: while consistent, the average +1.1 over CERT is relatively small and may diminish with stronger encoders or better-tuned baselines; also, 12% longer training plus offline back-translation cost are not fully accounted for in the compute comparison.
- Hand-designed linear schedule; no exploration of adaptive or learned schedules, which might be more robust across datasets.

Questions and suggestions for improvement
- Tune baselines on the same validation protocol and report results; include a sensitivity analysis for CERT’s augmentation mix/temperature to assess headroom.
- Add comparisons with stronger encoders (e.g., RoBERTa-base/large, DeBERTa-v3) and optionally a decoder-only model to show generality.
- Evaluate on additional, more challenging or domain-specific datasets (e.g., longer documents, noisy user text, biomedical/finance) and include multilingual results to test reliance on WordNet/MT quality.
- Report statistical significance for main results; include per-dataset effect sizes relative to standard deviations.
- Account for the true compute cost, including offline back-translation generation; discuss efficiency–accuracy trade-offs.
- Explore simple adaptive schedules (e.g., schedule based on loss/gradient norms) or curriculum mixing weights rather than discrete operator availability.

Scores (0–100)
- Soundness: 76
- Novelty: 72
- Significance: 68
- Clarity: 88

Final average score: 76.00

Recommendation: Reject

Rationale: The paper is well written and the idea is reasonable with consistent improvements, but the novelty is incremental and the empirical evaluation is limited and potentially unfairly tuned in favor of the proposed method. Strengthening baselines, expanding datasets and model backbones, and providing more rigorous analysis of compute and schedules would make this a stronger submission.