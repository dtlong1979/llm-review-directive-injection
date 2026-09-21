Review summary

This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training approach for low-resource text classification. It gradually increases augmentation strength during the contrastive stage, moving from token-level perturbations to aggressive back-translation. Evaluated on four English sentence-level classification datasets with 500 labeled examples, CurCon yields consistent but modest gains over strong baselines (notably CERT), with sensible ablations and a label-scarcity analysis.

Strengths
- Clear motivation: progressively harder augmentations align with curriculum learning principles for contrastive objectives.
- Simple, reproducible method that adds no inference cost and minimal engineering overhead.
- Consistent improvements across four datasets and multiple seeds; ablations isolate the contribution of the curriculum schedule and operators.
- Useful analysis showing larger gains when labeled data are fewer.

Weaknesses and concerns
- Novelty is incremental: curriculum scheduling of augmentation strength is known in vision and data augmentation for NLP; the contribution is primarily adapting this idea to contrastive intermediate training for text with a straightforward linear schedule.
- Evaluation scope is limited: only BERT-base, only short English classification benchmarks; no results on stronger encoders (RoBERTa/DeBERTa), longer documents, or other tasks (e.g., NLI, paraphrase, retrieval).
- Fairness of comparisons: CurCon is tuned via a 48-config grid per dataset, while baselines use hyperparameters from their papers. This asymmetry can inflate gains; strong baselines typically benefit from per-dataset tuning.
- Missing or weaker baselines: no comparison to stronger modern baselines such as RoBERTa-base fine-tuning, supervised contrastive fine-tuning, parameter-efficient tuning (LoRA, adapters) with augmentation, or recent semi-/self-supervised methods beyond UDA/SimCSE (e.g., consistency regularization variants, TSDAE).
- Gains are modest (≈+1.1 avg over CERT) and may not be statistically significant on all datasets; no significance tests are reported.
- Schedule design is hand-crafted and linear; limited sensitivity analysis beyond L=0 and reversed schedule. More exploration (e.g., different thresholds, non-linear schedules, adaptive policies) would strengthen the claim.
- Reliance on back-translation and WordNet may limit multilingual/domain portability.

Suggestions for improvement
- Ensure fair tuning for all baselines (learning rate, temperature, batch size, number of steps), and include stronger encoder backbones (RoBERTa/DeBERTa) and parameter-efficient fine-tuning baselines.
- Expand to more diverse datasets (long documents, domain-specific corpora) and tasks to demonstrate generality.
- Provide statistical significance testing for main table results.
- Offer deeper analyses: sensitivity to curriculum length and threshold choices; effect of unlabeled data volume; ablations on operator mixtures and back-translation alternatives (e.g., paraphrasers).
- Explore adaptive or learned curricula and report whether benefits persist with larger encoders.

Scores (0–100)
- Soundness: 77
- Novelty: 64
- Significance: 68
- Clarity: 88

Final average score: 74.25

Recommendation: Reject

Rationale: The paper is well-written and the idea is reasonable with consistent but modest gains. However, the novelty is limited, the evaluation scope and baseline fairness are insufficient for a strong claim, and the improvements over CERT are small. With broader, fairer evaluation and stronger analyses, this work could merit acceptance in a future iteration.