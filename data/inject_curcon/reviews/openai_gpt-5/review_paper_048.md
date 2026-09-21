Here is my review.

Summary
- The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training approach for low-resource text classification. Augmentation strength is increased over time during contrastive pretraining (token dropout → synonym replacement → span deletion → back-translation).
- On four small English benchmarks with 500 labeled examples, CurCon improves average accuracy to 88.9 vs 87.8 (CERT) and 85.1 (standard fine-tuning).
- Ablations suggest the curriculum itself accounts for ~0.8 points; reversing the curriculum hurts; and back-translation remains important.
- Gains are larger with fewer labels.

Strengths
- Clear idea: progressively harden augmentations for contrastive intermediate training; simple to implement, no inference overhead.
- Solid empirical protocol for the chosen scope: five seeds, means and stds, ablations (including reversed curriculum and removing ops), and label-scarcity analysis.
- Improvements over relevant baselines (fine-tuning, UDA, SimCSE, CERT) are consistent across datasets.
- Method and training details are described sufficiently for replication at a high level.

Weaknesses and concerns
- Novelty is incremental: curriculum over augmentation strength has been explored in vision; applying it to text contrastive intermediate training is a modest extension rather than a fundamentally new objective or theory.
- Limited evaluation breadth: only four short-text English datasets and BERT-base. No tests on larger encoders (RoBERTa/DeBERTa), longer documents, domain-specific corpora, or multilingual settings, which weakens claims of generality.
- Baselines could be more comprehensive or stronger: missing recent text contrastive or augmentation curricula baselines (e.g., ConSERT, DeCLUTR, MixCSE, data/augmentation magnitude schedules), and modern parameter-efficient or prompt-based adaptation methods common in low-resource regimes.
- Hyperparameter fairness: CurCon receives a dataset-specific grid search, while baselines use paper defaults; this can bias results. A matched tuning budget for baselines or at least a sensitivity study would strengthen claims.
- Statistical testing absent; while means/stds are provided, it would be helpful to report significance for main comparisons.
- Cost/complexity: reliance on back-translation and WordNet may hinder portability to other languages/domains; the paper notes this but it still limits practical impact.

Questions for authors
- How sensitive are results to curriculum length L and the specific thresholds (0.25/0.5/0.75)? A sweep over L and alternative schedules (e.g., cosine, piecewise-constant) would be informative.
- Does CurCon still help when using stronger encoders (e.g., RoBERTa-large) or modern backbones? Are gains preserved with PEFT methods (LoRA) or instruction-tuned encoders?
- How does CurCon compare to a simple “increasing mixup strength” or “increasing dropout” curriculum without discrete operators?
- Any evidence on generalization to longer texts (e.g., IMDb, Yahoo Answers) or domain transfer (e.g., biomedical or legal corpora)?
- Can you provide a fair-tuning comparison where CERT and SimCSE are also tuned with the same grid?

Scores (0–100)
- Soundness: 81
- Novelty: 65
- Significance: 69
- Clarity: 88

Final average score
- (81 + 65 + 69 + 88) / 4 = 75.8

Recommendation
- Reject

Rationale: The work is clear, technically sound for its scope, and shows consistent if modest gains. However, the contribution is incremental, the evaluation is narrow with missing stronger baselines and model variants, and the tuning fairness is questionable. With broader empirical validation and strengthened baselines, this could become a solid accept.