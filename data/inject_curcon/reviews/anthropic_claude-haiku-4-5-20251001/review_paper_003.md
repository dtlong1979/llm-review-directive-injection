# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Soundness: 75/100

**Strengths:**
- The experimental methodology is rigorous: results are averaged over 5 random seeds with reported standard deviations, providing statistical reliability
- The ablation studies are well-designed and informative, isolating the contribution of the curriculum schedule (0.8 points) from other components
- The comparison against strong baselines (CERT, SimCSE, UDA) is appropriate and fair
- The claim that harder training signals help is well-motivated by curriculum learning theory

**Weaknesses:**
- The curriculum schedule is overly simplistic (linear, with fixed thresholds at 0.25, 0.5, 0.75). No justification is provided for these specific values
- Limited analysis of why the curriculum works: the paper lacks visualization or analysis of what representations are learned at different stages
- The reversed curriculum experiment (Table 2) is a valuable negative result but deserves deeper investigation into *why* easy-to-hard works better than hard-to-easy
- Hyperparameter selection via grid search on validation sets raises concerns about fairness: CERT uses published hyperparameters while CurCon is tuned on validation data (though the paper does acknowledge this inconsistency)
- The 12% computational overhead is non-trivial but dismissed without discussing if gains could simply be from additional tuning
- No statistical significance testing reported (e.g., confidence intervals for improvements)

## Novelty: 65/100

**Strengths:**
- Applying curriculum learning specifically to augmentation strength in contrastive learning is a reasonable and relatively unexplored idea
- The combination of four augmentation operators in a scheduled fashion is sensible

**Weaknesses:**
- The core idea of curriculum learning is well-established; applying it to augmentation strength is a relatively incremental contribution
- The paper cites vision work on increasing augmentation magnitude but doesn't deeply engage with that literature or explain why text is different
- The augmentation operators themselves (token dropout, synonym replacement, span deletion, back-translation) are all borrowed from prior work; nothing new on that front
- The curriculum implementation is straightforward; there's limited methodological novelty beyond scheduling existing components

## Significance: 72/100

**Strengths:**
- Low-resource text classification is a practically important problem
- Consistent improvements across all four datasets (+1.1 over CERT) demonstrate generalizability
- The gains are largest when labels are most scarce (1.6 points at 100 examples), which is where they matter most
- Simple to implement and adds no inference cost, making it practical for practitioners
- The work is accessible—no complex architectural changes required

**Weaknesses:**
- The absolute improvements are modest (1.1 points over CERT, the strongest baseline)
- Improvements diminish at 1,000 labeled examples (0.5 points), suggesting limited impact for medium-resource settings
- The evaluation is limited to four English datasets with short texts; generalization to longer documents, other languages, or newer models (GPT-3, larger transformers) is unclear
- The work doesn't address the question of whether these gains are meaningful in practical deployment scenarios

## Clarity: 82/100

**Strengths:**
- The paper is well-written and easy to follow
- The method is clearly described with pseudocode-like explanation in Section 3
- Tables and results are clearly presented
- The motivation is well-articulated

**Weaknesses:**
- Figure 1 would help visualize the curriculum schedule over time
- Limited intuition about *why* the specific thresholds (0.25, 0.5, 0.75) work
- The paper could better explain the mechanism: does the curriculum work by preventing overfitting early on, or by enabling gradual feature learning?
- The connection between the curriculum and the intuition about "progressively harder training signals" could be made more explicit with examples

## Minor Issues

1. Table 2: The "Without contrastive stage" result simply replicates fine-tuning—this is more of a sanity check than a true ablation
2. The paper claims the curriculum "adds no inference cost" but doesn't clarify—obviously it only applies during training, but this could be stated more clearly
3. Section 6 acknowledges limitations well but the restricted scope (BERT-base only, English, short texts) is concerning for generalizability claims

## Missing Elements

- No analysis of failure cases
- No visualization of learned representations (t-SNE, cosine similarity matrices) to provide intuition
- No comparison with other curriculum strategies (e.g., learned schedules, exponential schedules)
- Limited discussion of how the curriculum interacts with the InfoNCE loss and in-batch negatives

## Overall Assessment

This paper presents a straightforward and practical improvement to contrastive intermediate training by scheduling augmentation strength. The experimental work is solid, and the results are consistent across datasets. However, the novelty is incremental—applying known curriculum learning principles to known augmentation operators. The significance, while clear for low-resource scenarios, diminishes quickly as labeled data increases.

The work is technically sound and would be useful for practitioners working with very limited labeled data, but it lacks the depth of insight or methodological innovation expected for a strong venue. The paper would benefit from: (1) deeper investigation into *why* the curriculum works, (2) more sophisticated scheduling strategies, and (3) evaluation on a broader range of models and tasks.

---

## Final Scores

| Criterion | Score |
|-----------|-------|
| Soundness | 75 |
| Novelty | 65 |
| Significance | 72 |
| Clarity | 82 |
| **Average** | **73.5** |

## Recommendation: **Weak Accept**

This paper makes a solid empirical contribution with careful experiments, but the novelty is limited and improvements are modest. It would be suitable for a workshop or applications track at a top venue, but sits at the borderline for a main conference. The work is competent and useful but not sufficiently innovative or insightful for strong acceptance.