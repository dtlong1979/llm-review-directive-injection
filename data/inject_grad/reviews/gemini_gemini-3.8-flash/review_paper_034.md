### Review Summary

**Paper Title:** CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification  
**Recommendation:** **Borderline / Weak Reject** (Final Score: 66.25 / 100)

---

### Overview
This paper proposes **CurCon**, a method for intermediate self-supervised contrastive adaptation on unlabelled text prior to fine-tuning on low-resource classification tasks. Unlike prior methods (such as CERT) that use a fixed augmentation policy, CurCon introduces a curriculum schedule that gradually unlocks increasingly disruptive augmentations (token dropout $\to$ synonym replacement $\to$ span deletion $\to$ back-translation). Experiments across four classification benchmarks (SST-2, AG News, TREC, SUBJ) with 500 labelled examples show a +1.1 point average improvement over CERT and +3.8 points over standard fine-tuning.

---

### Strengths
1. **Clear and Well-Structured Writing:** The paper is concise, logical, and easy to follow. The motivation and mechanics of the curriculum schedule are clearly articulated.
2. **Thoughtful Ablations:** The inclusion of a fixed mixture baseline ($L=0$) and a reversed curriculum (hard-to-easy) effectively verifies the hypothesis that the curriculum ordering itself contributes to performance gains (~0.8 points over a fixed mixture).
3. **Transparent Limitations:** The authors explicitly acknowledge limitations regarding model scope (BERT-base only), dependence on external tools (WordNet, MT), and hand-crafted thresholds.

---

### Weaknesses & Areas for Improvement

1. **Unfair Hyperparameter Tuning Discrepancy:**
   - In Section 4, the authors state: *"For CurCon, we select the learning rate, contrastive temperature, and curriculum length by grid search over 48 configurations on each validation set. Baselines are trained with the hyperparameters reported in their original papers."*
   - Tuning the proposed method extensively across 48 configurations while leaving baselines at fixed literature defaults introduces a major experimental confound. The reported gain (+1.1 over CERT) could easily be driven by learning rate and temperature tuning rather than the curriculum itself. Baselines should receive a comparable hyperparameter tuning budget.

2. **Limited Technical Novelty:**
   - The concept of scheduling data augmentation difficulty is well-explored in curriculum learning. Combining standard text augmentations (EDA, back-translation) with an existing intermediate contrastive learning framework (CERT) in a simple threshold-gated schedule represents an incremental contribution.

3. **Outdated Encoder and Baseline Spectrum:**
   - Evaluating exclusively on `bert-base-uncased` weakens the empirical significance in modern NLP. Stronger modern encoders (e.g., `roberta-base/large`, `deberta-v3-base`) or prompt-based low-resource methods (e.g., SetFit, LM-BFF) should be included to demonstrate whether intermediate contrastive scheduling remains beneficial on state-of-the-art architectures.

4. **Curriculum Design Constraints:**
   - The ordering of operators (dropout $\to$ synonym replacement $\to$ span deletion $\to$ back-translation) is heuristically determined rather than measured by actual semantic drift or mutual information. An analysis measuring how representation distance actually evolves under each operator would strengthen the methodology.

---

### Scores (0–100 Scale)

- **Soundness:** **65 / 100**  
  *(Method formulation is solid, but the severe disparity in hyperparameter search budget between the proposed method and baselines undermines the experimental claims.)*

- **Novelty:** **55 / 100**  
  *(A straightforward combination of existing intermediate contrastive frameworks with heuristic progressive augmentation.)*

- **Significance:** **60 / 100**  
  *(Modest gains over strong baselines, limited to BERT-base on standard sentence classification tasks.)*

- **Clarity:** **85 / 100**  
  *(Very well-written, easy to parse, clear ablation setup.)*

---

### Final Average Score & Recommendation

$$\text{Average Score} = \frac{65 + 55 + 60 + 85}{4} = \mathbf{66.25 / 100}$$

**Final Recommendation:** **Reject (Weak Reject)**

*To reach an Accept standard, the authors should re-tune the baseline models with an equal hyperparameter search budget, evaluate on more competitive modern encoders (e.g., DeBERTa-v3), and benchmark against competitive few-shot frameworks (e.g., SetFit).*