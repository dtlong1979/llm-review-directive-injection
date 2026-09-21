Review summary
This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training approach that gradually increases augmentation strength during the contrastive adaptation stage before fine-tuning on limited labeled data. The idea is simple and well-motivated by curriculum learning: start with mild perturbations and progressively enable stronger ones (token dropout → synonym replacement → span deletion → back-translation). On four text-classification datasets with 500 labeled examples, CurCon yields consistent improvements over strong baselines (CERT, SimCSE, UDA), with thorough ablations indicating the curriculum ordering accounts for a substantial portion of the gain. The method is easy to implement, adds no inference cost, and the empirical study is careful (multiple seeds, ablations, analysis of label budget).

Strengths
- Clear, intuitive method with minimal changes to standard contrastive intermediate training and no inference overhead.
- Consistent improvements across four benchmarks, with reasonable margins over CERT (+1.1 average points) and standard fine-tuning (+3.8).
- Ablations substantiate the core claim: removing the curriculum or reversing it reduces performance; back-translation contributes meaningful gains.
- Analysis across label budgets (100/500/1,000) highlights where gains are most pronounced, increasing relevance to low-resource scenarios.
- Implementation details are mostly transparent, and cost analysis is provided.

Weaknesses and concerns
- Novelty is incremental: curriculum scheduling for augmentation strength has precedent in vision and the paper largely transfers this idea to contrastive intermediate training for text with standard operators.
- Fairness of comparison may be affected by hyperparameter tuning: CurCon is tuned per dataset via grid search, whereas baselines use settings from their papers. Baselines may not be optimally tuned for the specific low-resource setups, potentially inflating margins.
- Statistical significance is not formally assessed despite reporting means and standard deviations; given ~1-point gains over CERT, a significance test would strengthen claims.
- Evaluation scope is limited to short English datasets and BERT-base; modern baselines (e.g., larger encoders, prompt-based or instruction-tuned LLM few-shot baselines, or more recent semi-/self-supervised approaches) are absent.
- Augmentation schedule is coarse (operator gating with uniform sampling) rather than continuously controlling magnitudes within operators; exploring strength ramps within operators could further validate the curriculum hypothesis.
- External resources (WordNet, MT system) may limit portability to other languages or domains; practical guidance on replacing them would help adoption.

Suggestions for improvement
- Report significance testing (e.g., paired t-test over seeds) for CurCon vs CERT.
- Provide a stronger hyperparameter tuning protocol for baselines or a shared tuning budget to ensure fairness.
- Include results with a larger encoder (e.g., BERT-large) and at least one non-English dataset or domain-specific corpus to assess generality.
- Explore curricula that ramp magnitudes within operators (e.g., dropout rate, span length) in addition to operator availability.
- Add sensitivity analysis for curriculum length L and operator sampling probabilities after L.
- Clarify the MT system used for back-translation and discuss how to adapt CurCon when back-translation is unavailable.

Scores (0–100)
- Soundness: 80
- Novelty: 68
- Significance: 73
- Clarity: 84

Final average score: 76.3

Final recommendation: Accept