Summary
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training approach for low-resource text classification. It gradually increases augmentation strength during the contrastive stage, moving from token dropout to synonym replacement, span deletion, and back-translation. Evaluated on four sentence-level English datasets with 500 labeled examples each, CurCon improves average accuracy by 1.1 points over CERT and 3.8 over standard fine-tuning. Ablations suggest ~0.8 points of the gain stem from the curriculum, and improvements are larger when fewer labeled examples are available.

Strengths
- Simple, practical idea that integrates smoothly into the standard contrastive intermediate training pipeline with no inference overhead.
- Consistent improvements across all four datasets and multiple seeds; gains are largest in the lowest-label regime, matching the motivation.
- Clear curriculum design and ablations, including reversed curriculum and removal of back-translation, which help isolate the contribution of the schedule.
- Reasonably thorough experimental details (datasets, steps, batch sizes, loss, temperature) and seed averaging.

Weaknesses and concerns
- Fairness of baseline tuning: CurCon is tuned via grid search per dataset, while baselines use hyperparameters from prior papers. This likely disadvantages baselines (especially CERT and UDA) on these specific datasets and settings. Stronger fairness would require comparable tuning budgets for all methods.
- Limited scope: Only four short-text English classification datasets, all sentence-level and fairly standard. It’s unclear whether results transfer to longer documents, non-English data, or other tasks (e.g., NLI, retrieval).
- Modest absolute gains: The average improvement over CERT is 1.1 points, with 0.8 attributable to the curriculum—useful but incremental for a new method, especially given the tuning asymmetry.
- Missing statistical significance testing: While means and standard deviations are provided, there is no explicit significance testing across seeds (e.g., paired t-tests).
- Cost reporting omits MT generation: Back-translation is precomputed, but the compute and latency cost to generate back-translations is non-trivial and not accounted for in the overall cost comparison.
- Related work coverage: Curriculum on augmentation magnitude is established in vision and variations exist in NLP; the paper could more explicitly position differences from prior curriculum strategies for contrastive learning in text.

Questions for the authors
- Did you try tuning CERT and UDA with similar grid searches on the same validation splits? If so, what are the results? If not, can you provide those to ensure a fair comparison?
- What are the typical best curriculum lengths L found by grid search across datasets, and how sensitive is performance to L?
- How large are the in-domain unlabeled corpora per dataset, and do you sample with replacement across the 20k steps?
- How does CurCon perform without any external resources (i.e., without WordNet and without back-translation), relying on token-level drops/spans only?
- Could you include results on at least one non-English dataset or a longer document classification benchmark to assess generality?

Suggestions for improvement
- Re-run baselines with comparable hyperparameter tuning budgets and report results to ensure fairness.
- Add statistical significance tests across seeds for key comparisons.
- Expand to more diverse datasets (longer documents, multilingual, domain-specific) and include at least one larger encoder or a decoder-only backbone to test robustness.
- Provide a cost analysis that includes the amortized cost of generating back-translations.
- Compare against an alternative schedule (e.g., smoothly increasing augmentation magnitude within a single operator, or adaptive schedules based on loss/variance) to further isolate the value of the curriculum mechanism.

Scores (0–100)
- Soundness: 76
- Novelty: 65
- Significance: 70
- Clarity: 85

Final average score
- (76 + 65 + 70 + 85) / 4 = 74.0

Recommendation
- Reject

Rationale: The idea is sensible and results are promising but incremental. The evaluation, while careful in some respects, has fairness issues due to asymmetric hyperparameter tuning and is limited in scope. With stronger, fair baseline tuning, broader validation, and clearer significance and cost analyses, this work could be competitive.