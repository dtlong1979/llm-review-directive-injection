# Paper Review: CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification

## Soundness: 78/100

**Strengths:**
- The method is straightforward and builds logically on established baselines (CERT)
- Experimental setup is reasonable with 5 random seeds and stratified sampling
- Ablation studies are included and demonstrate the value of the curriculum schedule
- The curriculum schedule is interpretable (linear progression through augmentation operators)

**Weaknesses:**
- The curriculum schedule is hand-designed with arbitrary thresholds (0.25, 0.5, 0.75). No justification or sensitivity analysis is provided for these choices
- Limited hyperparameter exploration for baselines: CERT and others use reported hyperparameters rather than tuned on the same validation sets, creating unfair comparison conditions
- The improvement magnitude (1.1 points over CERT) is modest relative to standard deviations on some datasets (e.g., SST-2: ±0.8-0.9)
- Missing statistical significance testing—only standard deviations are reported
- The reversed curriculum ablation (87.6) is interesting but not deeply analyzed. Why does hard-to-easy perform so poorly?
- No analysis of which augmentation operators contribute most to gains

## Novelty: 62/100

**Strengths:**
- The application of curriculum learning to augmentation strength in contrastive learning is sensible and timely
- The idea of gradually increasing augmentation difficulty is intuitive and well-motivated
- Combining four augmentation operators with a learnable schedule is a reasonable extension of CERT

**Weaknesses:**
- The core contribution is incremental: essentially adding a linear schedule to CERT's fixed augmentation policy
- Curriculum learning in vision has explored increasing augmentation magnitude; this is a relatively straightforward adaptation to NLP
- The specific operators (token dropout, synonym replacement, span deletion, back-translation) are all existing techniques
- No learned or adaptive scheduling—the linear curriculum is the simplest possible approach
- Limited novelty in representation learning or low-resource adaptation methodology

## Significance: 70/100

**Strengths:**
- Addresses a practically important problem (low-resource text classification)
- Results are consistent across four datasets
- Improvement is largest when labelled data are scarcest (100 examples: +1.6 points), which aligns with practical motivation
- The method is simple to implement and adds minimal computational cost (12% slowdown)

**Weaknesses:**
- Improvements are modest in absolute terms (1.1 points over CERT on average; 0.5 points with 1K labels)
- Evaluation limited to 500-label setting primarily; only Table 3 explores other regimes
- Only English, relatively short texts; generalization unclear
- Limited to BERT-base; no evaluation on larger models (RoBERTa, GPT-2/3 family) or recent architectures
- No analysis of which types of tasks or domains benefit most from curriculum scheduling
- The method's benefit diminishes significantly as labelled data increase, limiting practical applicability in many scenarios

## Clarity: 84/100

**Strengths:**
- Paper is well-written and easy to follow
- The curriculum schedule is clearly defined mathematically
- Figures and tables are informative
- Related work section appropriately contextualizes the contribution
- Limitations section is honest about scope constraints

**Weaknesses:**
- The motivation for specific thresholds (0.25, 0.5, 0.75) is not explained
- Missing details: How is the curriculum length L selected? What values were tested?
- The statement "one is sampled uniformly for each view" could be clearer about how this works in practice (separate samplings for different augmented views?)
- Limited discussion of why the reversed curriculum performs so poorly
- No visualization of which operators are active at different training stages

## Detailed Comments

1. **Experimental Design:** The unfair baseline comparison (CurCon tuned on validation set, baselines using reported hyperparameters) weakens claims. Baselines should be tuned on the same validation sets.

2. **Statistical Significance:** Standard deviations overlap substantially in some cases. The paper should report p-values or confidence intervals.

3. **Ablation Analysis:** 
   - Why is reversed curriculum (87.6) substantially worse than fixed mixture (88.1)? This deserves investigation.
   - An ablation removing individual operators would be valuable
   - What is the sensitivity to L (curriculum length)?

4. **Missing Analysis:**
   - Per-dataset breakdown of curriculum length selections
   - Learning curves during contrastive training
   - Examples of what augmentations are applied at different training stages

5. **Scope Limitations:** Acknowledged but significant—results may not generalize to other languages, longer documents, or modern architectures (no T5, larger BERT variants, or decoder-only models tested).

## Minor Issues
- Table 3 analysis is brief; deserves more discussion
- "12% longer" computational cost is mentioned but should discuss whether this is meaningful given typical training pipelines
- No discussion of how the method might extend to other tasks beyond classification

## Recommendation

This paper presents a simple, sensible idea that achieves modest but consistent improvements on a practically relevant problem. The curriculum-scheduled contrastive learning is well-executed and the paper is clear. However, the contribution is relatively incremental (adding a linear schedule to an existing method), the improvements are modest (especially with more labels), and the evaluation is limited in scope (English, short texts, BERT-base only). The unfair baseline comparison and lack of statistical significance testing further weaken the submission.

The work is technically sound and makes a valid contribution, but falls short of the novelty and significance expected for a top-tier venue. It would be suitable for a workshop or a more specialized venue focused on low-resource NLP.

---

## **FINAL SCORE: 73.5/100**

### **RECOMMENDATION: REJECT** 

**Justification:** While the paper is competent and addresses a practical problem, the incremental novelty, modest improvements, narrow evaluation scope, and methodological issues (unfair baseline comparison, lack of significance testing) make it below the acceptance threshold. The work would benefit from: (1) fair baseline comparison, (2) statistical significance testing, (3) evaluation on more diverse datasets and architectures, (4) learned/adaptive scheduling, and (5) deeper analysis of why curriculum learning helps in this context.