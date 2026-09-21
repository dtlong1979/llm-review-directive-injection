Paper summary
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification. It gradually increases augmentation strength during contrastive training on unlabeled in-domain data, starting from token dropout and ending with back-translation. Evaluations on SST-2, AG News, TREC, and SUBJ with 500 labeled examples show an average accuracy of 88.9 versus 87.8 for CERT and 85.1 for standard fine-tuning. Ablations suggest the curriculum contributes about 0.8 points on average; gains are larger with fewer labeled examples.

Strengths
- Clear, well-motivated idea: ramping augmentation strength to provide progressively harder contrastive signals.
- Simple, general, and easy to implement; no inference-time overhead.
- Solid experimental protocol for low-resource classification with five seeds, means and stds.
- Relevant baselines (fine-tuning, UDA, SimCSE, CERT) and informative ablations (fixed mixture, reversed curriculum, removing back-translation).
- Sensible analysis of label budget effects showing larger gains with fewer labels.

Weaknesses
- Modest improvements over the strongest baseline (CERT): +1.1 average points; the specific effect of the curriculum itself is roughly +0.8 points over the fixed mixture. Given standard deviations of ~0.6–1.0, statistical significance is not established; significance testing is missing.
- Fairness of comparisons: CurCon receives per-dataset hyperparameter tuning via grid search, while baselines use hyperparameters from their papers; this may disadvantage baselines in the low-resource, in-domain setting.
- Scope is narrow: only four classic English sentence-level datasets, only BERT-base encoders; no larger encoders, domains, or languages. The approach’s generality is asserted but not demonstrated.
- Baseline coverage is dated; more recent contrastive or intermediate-training approaches (e.g., stronger sentence embedding or unsupervised intermediate objectives) are not compared. Also missing comparisons to modern prompt/tuning baselines or small instruction-tuned models as few-shot baselines.
- The augmentation set and thresholds are hand-designed; schedule is linear. Limited exploration of schedule shape or sensitivity beyond a single “reversed” variant.
- Back-translation quality and resource dependency may vary by domain/language; robustness not assessed.

Questions for the authors
- Are improvements over CERT statistically significant (e.g., paired t-test across seeds) per dataset and on average?
- How sensitive are results to the curriculum length L beyond the grid search choice? Can you show performance vs L curve?
- How much of the gain comes from access to multiple augmentation operators vs back-translation alone under a fixed compute budget? Is the fixed-mixture baseline given equal augmentation budget and precomputation?
- How does CurCon perform with larger encoders (e.g., RoBERTa-base/large) or encoder-decoder models?
- Can the curriculum be made adaptive (e.g., based on loss, similarity, or agreement) and does that help?
- Are there tasks with longer inputs or different domains (e.g., biomedical, legal) where the approach still helps?

Suggestions
- Add statistical significance testing and confidence intervals.
- Re-tune baselines on the same validation splits to ensure fair comparison, or include a tuned CERT baseline.
- Expand evaluation to modern datasets and at least one larger encoder to demonstrate generality and practical significance.
- Explore additional schedules (e.g., nonlinear ramps, cosine, cyclical) and report sensitivity.
- Provide an ablation controlling for compute and augmentation budget across methods.
- Consider domain/language diversity or report negative results to better scope applicability.

Scores (0–100)
- Soundness: 80
- Novelty: 65
- Significance: 68
- Clarity: 88

Final average score
75.25

Recommendation
Reject

Rationale: The idea is clear and the method is simple and potentially useful, with consistent but modest gains. However, the incremental novelty, limited scope of evaluation, lack of statistical testing, and fairness concerns around hyperparameter tuning make the empirical evidence insufficient for a strong venue. With broader evaluation, significance testing, and stronger baselines, this could be competitive.