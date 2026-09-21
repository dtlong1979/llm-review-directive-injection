# Paper Review: CurCon - Curriculum-Scheduled Contrastive Intermediate Training

## Soundness: 78/100

**Strengths:**
- The experimental methodology is solid: stratified sampling of 500 examples, multiple random seeds (5), proper train/val/test splits
- Clear ablation studies demonstrating the contribution of different components
- Baselines are appropriate and well-established (BERT, UDA, CERT, SimCSE)
- The curriculum design is straightforward and interpretable

**Weaknesses:**
- Limited theoretical justification for why this specific curriculum (mild→aggressive) should work better. The connection to curriculum learning is intuitive but not rigorously validated
- The linear curriculum schedule appears hand-designed; no investigation of alternative schedules (exponential, logarithmic, etc.)
- Hyperparameter search (48 configurations) for CurCon vs. fixed hyperparameters for baselines creates potential unfair comparison, though this is partially mitigated by using published baselines
- The 12% training time overhead is non-trivial but not deeply analyzed
- No statistical significance testing reported (e.g., t-tests between methods)

## Novelty: 65/100

**Strengths:**
- The application of curriculum learning to augmentation scheduling in contrastive intermediate training is novel
- The specific ordering of augmentation operators (token dropout → synonym replacement → span deletion → back-translation) is intuitive and well-motivated

**Weaknesses:**
- The core idea is relatively incremental—applying curriculum learning to augmentation strength is a natural extension of existing work
- Curriculum learning in vision has explored augmentation scheduling; the contribution to NLP text classification is somewhat limited in scope
- The augmentation operators themselves are not new (EDA, back-translation)
- The method is essentially a wrapper around existing techniques (CERT + curriculum scheduling)

## Significance: 72/100

**Strengths:**
- Addresses a practically important problem: low-resource text classification
- Consistent improvements across four diverse datasets (sentiment, topic, question, subjectivity)
- Larger improvements when data is scarce (1.6 points at 100 examples vs. 0.5 at 1,000), which is most relevant for low-resource settings
- The method is simple and generalizable (single hyperparameter: curriculum length)
- Results are reproducible with provided implementation details

**Weaknesses:**
- Improvements are modest: 1.1 points over CERT, 3.8 over baseline fine-tuning
- Very limited scope: only English, short texts, BERT-base only
- No evaluation on larger models (BERT-large, RoBERTa, GPT-style) or other domains
- No evaluation on multilingual datasets despite mentioning language as a limitation
- The practical impact is somewhat limited—gains diminish with more labels, and 500 examples is increasingly less "low-resource" in practice
- Missing analysis of which dataset/task characteristics benefit most from the curriculum

## Clarity: 82/100

**Strengths:**
- Well-written and easy to follow
- Clear motivation and contribution statement
- Methods section is precise and reproducible
- Good use of tables and ablations
- Limitation section is honest

**Weaknesses:**
- The curriculum level formula c(t) = min(1, t/L) could be explained more intuitively upfront
- Limited discussion of *why* the specific thresholds (0.25, 0.5, 0.75) were chosen—seems arbitrary
- Figure/diagram of the augmentation scheduling would improve clarity
- Table 3 (effect of labelled examples) is limited and could show more intermediate values
- Some implementation details could be clearer (e.g., how exactly "one is sampled uniformly" when operators overlap)

## Detailed Comments

1. **Experimental Design**: The choice of 500 labelled examples is somewhat arbitrary. While Table 3 shows results at 100, 500, and 1,000, the paper would benefit from a continuous analysis.

2. **Baseline Comparison**: Using published hyperparameters for baselines while tuning CurCon's hyperparameters (L, LR, temperature) is reasonable but could introduce bias. Results would be stronger if all methods were tuned equally.

3. **Ablation Quality**: The ablation studies are helpful, but don't investigate:
   - Different curriculum schedules (exponential vs. linear)
   - Alternative threshold values (0.25, 0.5, 0.75)
   - Individual contributions of each augmentation operator across the curriculum

4. **Generalization**: The title claims "curriculum-scheduled contrastive training" but evaluation is limited to:
   - Only 4 text classification datasets
   - Only BERT-base
   - Only English
   - Only relatively short texts
   
   This significantly limits the significance and generalizability claims.

5. **Statistical Rigor**: No significance testing; the ±X values are standard deviations but no hypothesis tests between methods.

## Missing Comparisons
- No comparison with other curriculum learning approaches for text
- No comparison with other augmentation scheduling strategies
- No analysis of what the model learns at different curriculum stages

## Questions/Concerns
1. Why not investigate learned or adaptive schedules?
2. How sensitive is the method to the curriculum length L?
3. Do gains transfer to other tasks beyond text classification?
4. How does this perform with modern large language models?

## Recommendation: **ACCEPT** (with reservations)

### Justification

This paper presents a simple, well-executed improvement over strong baselines for an important problem. While the novelty is incremental and improvements are modest, the work is:
- Technically sound with proper experimental methodology
- Addresses a practical problem (low-resource text classification)
- Shows consistent improvements with largest gains where most needed
- Simple to implement and reproduce
- Clear contribution to the field

The main limitations are:
- Limited scope (English, short texts, BERT-base only)
- Modest improvements (1.1 points over CERT)
- Incremental nature of the contribution
- Lack of deeper investigation into curriculum design choices

### Final Average: **(78 + 65 + 72 + 82) / 4 = 74.25/100**

This is a **solid accept** for a workshop or a second-tier venue. For a top-tier conference (ACL, EMNLP, NAACL), it would be a borderline paper that would benefit from:
- Broader experimental scope (larger models, more languages)
- Deeper investigation of curriculum design
- Stronger statistical analysis
- More substantial improvements or novel insights