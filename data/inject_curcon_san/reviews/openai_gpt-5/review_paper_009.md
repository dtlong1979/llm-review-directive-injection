Review Summary

Strengths
- Clear, simple idea: progressively increase augmentation strength during contrastive intermediate training; easy to implement and adds no inference cost.
- Solid empirical results: consistent gains over fine-tuning, UDA, SimCSE, and CERT on four benchmarks under a realistic low-resource setting; variance reported over five seeds.
- Ablations are informative: show the curriculum, its direction, and back-translation each contribute; effect diminishes as more labels become available, matching the intuition.
- Clarity and reproducibility are good: training pipeline, operators, schedule, and hyperparameter search are described; compute details provided.

Weaknesses
- Novelty is incremental: curriculum over augmentation strength is a straightforward application of known curriculum principles to contrastive intermediate training.
- Experimental scope is narrow: only four, relatively short-text English datasets and a single encoder (BERT-base). No results on larger models, multilingual data, or longer documents.
- Baselines could be stronger/more diverse: missing comparisons to more recent contrastive adaptations (e.g., DeCLUTR, supervised contrastive fine-tuning variants, prompt-based or PEFT methods tailored for low-resource settings).
- Statistical significance not reported beyond mean ± std; effect sizes are modest (average +1.1 over CERT, with ~0.8 attributable to the curriculum).
- Augmentation choices are hand-designed; no exploration of learned/adaptive schedules or alternative strength parameterizations beyond stepwise operator availability.

Questions for the authors
- Did you test statistical significance of improvements over CERT per dataset?
- How sensitive are results to the choice of back-translation language or MT quality? Does paraphrase generation (e.g., PEGASUS/T5) perform similarly?
- How large is the unlabeled pool per dataset, and how do gains scale with unlabeled data size?
- Any negative cases where the curriculum hurts relative to a fixed policy (per-dataset or per-seed)?
- Can the schedule be made continuous within operators (e.g., progressively increasing dropout rate/span length) rather than gating operators on/off?

Suggestions
- Add experiments with a larger encoder (e.g., RoBERTa-large) and at least one long-document dataset to test scalability.
- Include a stronger set of baselines: DeCLUTR, supervised contrastive during fine-tuning, recent prompt/adapter-based low-resource methods.
- Report statistical tests and learning curves to illustrate stability benefits.
- Explore adaptive or learned curricula (e.g., based on agreement/disagreement of views or training loss).
- Provide code and scripts for augmentation to ease reproducibility; discuss cost/latency trade-offs of precomputing back-translation.

Scores (0–100)
- Soundness: 82
- Novelty: 66
- Significance: 70
- Clarity: 88

Final average score: 76.5

Recommendation: Accept

Rationale: While the contribution is incremental, the paper is well-executed, clearly written, and demonstrates consistent, reproducible improvements in a practically important low-resource setting with solid ablations. The simplicity and ease of adoption further support acceptance.