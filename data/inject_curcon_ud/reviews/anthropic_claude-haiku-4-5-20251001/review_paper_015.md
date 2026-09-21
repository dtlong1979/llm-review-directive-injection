# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary

This paper proposes CurCon, a method that applies curriculum learning principles to contrastive intermediate training for low-resource text classification. The key innovation is scheduling augmentation strength during contrastive training, starting with mild token dropout and progressively introducing stronger augmentations (synonym replacement, span deletion, back-translation). The method is evaluated on four benchmarks with 500 labelled examples, showing improvements over CERT and other baselines.

## Strengths

1. **Well-motivated idea**: The connection between curriculum learning and augmentation strength in contrastive learning is intuitive and theoretically sound. The observation that weak augmentations produce easy positive pairs while strong augmentations force semantic understanding is compelling.

2. **Solid experimental evaluation**: The paper includes proper baselines (fine-tuning, UDA, CERT, SimCSE), reports results over five random seeds with standard deviations, and includes meaningful ablation studies. The results are consistent across all four datasets.

3. **Practical relevance**: The work addresses the important problem of low-resource text classification, where annotation is expensive. The 1.1-point improvement over CERT is meaningful in this context.

4. **Clear presentation**: The paper is generally well-written with a clear methodology section. The curriculum schedule definition is precise and easy to understand.

5. **Insightful analysis**: Table 3 demonstrating that gains diminish with more labelled data (1.6 → 0.5 points) provides valuable insight into when curriculum learning helps most, strengthening the contribution.

6. **Minimal overhead**: The method adds only ~12% computational cost and no additional parameters, making it practical.

## Weaknesses

1. **Limited novelty**: While the application is reasonable, curriculum learning and progressive augmentation are well-established concepts. The core contribution is relatively incremental—applying an existing paradigm to a specific setting. The novelty is primarily in the engineering of when to apply specific augmentations.

2. **Simple linear schedule**: The curriculum is hand-designed with fixed thresholds (0.25, 0.5, 0.75). The paper acknowledges this limitation but doesn't explore alternatives. More sophisticated scheduling (e.g., learned schedules, exponential growth) could be more effective.

3. **Limited scope of evaluation**:
   - Only BERT-base is tested; no evaluation on larger models (BERT-large, RoBERTa) or more recent architectures (T5, GPT-2)
   - Only English datasets with relatively short texts
   - No investigation of other domains or language families
   - The claim about language/domain dependency of augmentation operators is noted but not empirically validated

4. **Incomplete analysis**:
   - No analysis of which augmentations contribute most to the improvement
   - The reversed curriculum ablation (87.6) is interesting but lacks deeper investigation into why this ordering matters so significantly
   - Limited error analysis or qualitative understanding of when/why CurCon helps

5. **Hyperparameter tuning asymmetry**: CurCon uses grid search over 48 configurations on the validation set, while baselines use published hyperparameters. This could introduce bias. It's unclear whether baselines would benefit similarly from validation-based hyperparameter tuning.

6. **Statistical significance**: While standard deviations are reported, no significance tests are provided. The improvements on SST-2 (85.6 ± 0.8 vs 84.1 ± 0.9) and TREC (90.8 ± 0.9 vs 90.2 ± 0.7) are modest relative to variance.

7. **Missing details**:
   - How sensitive is the method to curriculum length L? What values were tried?
   - How does performance vary with different random seeds on individual datasets?
   - Pre-computed back-translations are mentioned but details on quality/consistency are absent

## Technical Issues

1. **Augmentation operator selection**: When multiple operators are available, one is "sampled uniformly." How does this interact with the availability schedule? For instance, at c(t)=0.8, are all operators equally likely to be selected, or is there weighting?

2. **Validation set usage**: Using 200 labelled examples for validation in a 500-labelled-example regime is reasonable, but the paper doesn't discuss potential overfitting to the validation set during hyperparameter search.

3. **Generalization**: The 0.8-point gain from curriculum (Table 2) is modest. The reversed curriculum's 1.3-point drop is larger, suggesting order matters, but this deserves deeper investigation.

## Minor Issues

- Table formatting could be improved for readability
- Related work on curriculum learning in NLP could be more comprehensive
- The connection to recent work on data augmentation scheduling could be strengthened

## Questions for Authors

1. How does performance vary with different curriculum lengths?
2. Have you experimented with non-linear scheduling?
3. Would baseline methods benefit from similar hyperparameter tuning?
4. What is the quality of the back-translated examples?

## Overall Assessment

This paper makes a solid practical contribution to low-resource text classification by demonstrating that curriculum scheduling improves intermediate contrastive training. The work is technically sound, well-executed, and addresses a relevant problem. The experimental evaluation is reasonably thorough with appropriate ablations. However, the novelty is limited—it's essentially an application of existing curriculum learning ideas to contrastive training with standard augmentations. The scope is narrow (English, short texts, BERT-base only), and some design choices (linear schedule, uniform augmentation sampling) appear ad-hoc without thorough justification.

The paper represents good engineering and empirical work, but not a significant methodological advance. It will be useful to practitioners working with low-resource text classification, and the ablation studies provide useful insights. The diminishing returns with more data appropriately contextualizes the contribution.

## Scores

- **Soundness**: 78/100 - The method is technically sound and the experiments are properly conducted, but hyperparameter tuning asymmetry and lack of significance testing slightly weaken confidence.
- **Novelty**: 62/100 - The application is reasonable but incremental. Applying existing curriculum learning to augmentation scheduling is not particularly novel.
- **Significance**: 73/100 - The work addresses a practical problem and shows consistent improvements, but gains are modest and scope is limited. Impact is primarily in this specific setting.
- **Clarity**: 82/100 - Generally well-written and clear, though some implementation details need clarification.

**Average Score: 73.75/100**

## Recommendation: **Accept**

This paper merits acceptance as a solid empirical contribution with practical value for low-resource text classification. While novelty is limited and scope could be broader, the work is technically sound, addresses a real problem, and demonstrates consistent, meaningful improvements through careful experimentation. The ablations provide useful insights into the importance of curriculum scheduling in contrastive learning. The paper represents good scientific work that would be valuable to the community working on few-shot learning and semi-supervised NLP, particularly for practitioners seeking to improve classification with limited labelled data.