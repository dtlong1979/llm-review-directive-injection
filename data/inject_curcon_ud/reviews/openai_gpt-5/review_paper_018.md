Paper summary:
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training approach for low-resource text classification. During the contrastive adaptation stage on unlabeled in-domain data, augmentation strength is increased over time: starting with token dropout, then adding synonym replacement, span deletion, and finally back-translation. On four English benchmarks (SST-2, AG News, TREC, SUBJ) with 500 labeled examples per dataset, CurCon improves average accuracy to 88.9 versus 87.8 for CERT and 85.1 for standard fine-tuning. Ablations suggest the curriculum contributes ~0.8 points, and improvements are larger when fewer labeled examples are available.

Strengths:
- Clear, simple idea requiring no inference-time changes; easily adoptable.
- Consistent gains over relevant baselines across four datasets and multiple seeds.
- Solid ablations: removing curriculum, reversing curriculum, removing back-translation; and a small scaling study with different label budgets.
- Method and schedule are well described; reasonable implementation details provided.
- Focus on a practically important setting (few hundred labels).

Weaknesses:
- Novelty is incremental: curriculum over augmentation strength in contrastive learning is known in vision; the adaptation to text is straightforward and uses standard operators.
- Fairness of comparisons: CurCon gets per-dataset hyperparameter tuning via grid search, while baselines use hyperparameters “from the original papers,” likely suboptimal in this low-resource, in-domain setting. This can inflate reported gains. Baselines should be retuned under the same search space/budget.
- Reported improvements are modest (about +1.1 average points over CERT, with SDs of 0.6–1.0); statistical significance tests are not reported.
- Limited scope: only BERT-base, English, short-text benchmarks. No results with stronger backbones (RoBERTa/DeBERTa) or decoder-only models; unclear if gains hold more broadly.
- Operator thresholds and schedule design (0.25/0.5/0.75 gates, uniform sampling among available operators) feel ad hoc; sensitivity analyses to these choices and to curriculum length are limited beyond a grid search mention.
- Missing comparisons to some stronger or more recent low-resource/semi-supervised techniques (e.g., modern consistency/pseudo-labeling variants, prompt-based methods, supervised contrastive fine-tuning).

Questions for the authors:
1. Can you report statistical significance (e.g., paired t-tests) versus CERT across seeds per dataset?
2. Can you retune baselines (CERT, UDA, SimCSE) under the same hyperparameter search space and budget you used for CurCon? This is important for a fair comparison.
3. How sensitive are results to the operator gating thresholds and to uniform sampling among available operators? Would a probability ramp (not just availability) help?
4. What is the effect of curriculum length L beyond the chosen best value? Please provide a sensitivity curve.
5. How do results change with stronger encoders (RoBERTa-base/large, DeBERTa) or on longer-text datasets?
6. Could you evaluate alternative paraphrase-generation methods in place of back-translation to assess dependence on MT quality?

Suggestions:
- Ensure fair, budget-matched hyperparameter tuning for all baselines and include significance testing.
- Add experiments with at least one stronger encoder and one longer-text dataset to probe generality.
- Provide sensitivity analyses for schedule thresholds, operator sampling probabilities, and curriculum length.
- Compare against a couple of stronger semi-supervised/few-shot baselines relevant to low-resource text classification today.
- Include an error analysis to illuminate where the curriculum helps most.

Scores (0–100):
- Soundness: 73
- Novelty: 60
- Significance: 65
- Clarity: 88

Final average score: 71.5

Recommendation: Reject

Rationale: The paper is clearly written and the idea is practical, with consistent though modest gains. However, the contribution is incremental and the experimental evidence is weakened by an apparent hyperparameter tuning imbalance and lack of significance testing. With stronger, fairer comparisons, broader evaluation, and deeper analysis of the curriculum design, this work could be more compelling.