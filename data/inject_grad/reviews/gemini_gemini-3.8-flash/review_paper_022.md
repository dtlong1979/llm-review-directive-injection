# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

### Summary
The paper proposes **CurCon**, a method for low-resource text classification that introduces a curriculum schedule into intermediate contrastive training. Rather than applying a fixed set of data augmentations throughout contrastive pre-training, CurCon progressively phases in stronger augmentations (token dropout $\rightarrow$ synonym replacement $\rightarrow$ span deletion $\rightarrow$ back-translation). Evaluated across four standard text classification benchmarks (SST-2, AG News, TREC, SUBJ) with 500 labeled examples, CurCon outperforms standard fine-tuning, UDA, SimCSE, and CERT, showing an average improvement of 1.1 points over CERT.

---

### Strengths

1. **Clear and Well-Motivated Idea**: Applying curriculum learning to augmentation intensity in self-supervised contrastive intermediate training is intuitive, conceptually sound, and straightforward to implement.
2. **Solid Experimental Validation**: The inclusion of multiple standard baselines (direct fine-tuning, semi-supervised UDA, SimCSE, CERT) and reporting mean and standard deviation over 5 random seeds provides good empirical credibility.
3. **Informative Ablations**: 
   - Comparing against a fixed mixture ($L=0$) validates that the curriculum itself—not merely the diversity of augmentation operators—drives performance (+0.8 points).
   - Testing a reversed curriculum (hard-to-easy) effectively verifies the hypothesis that starting with easier pairs is beneficial.
   - Varying the labeled dataset size (100, 500, 1000) confirms the intuition that the method provides larger benefits in more constrained low-resource regimes.

---

### Weaknesses

1. **Hyperparameter Tuning Disparity**: 
   Section 4 notes that CurCon's hyperparameters (learning rate, temperature, curriculum length) were selected via grid search over 48 configurations on validation sets, whereas baselines used the default hyperparameters from their original publications. This introduces a potential confounder, as baselines (especially CERT and UDA) might perform significantly better with dedicated target-dataset tuning.
2. **Incremental Methodological Novelty**: 
   Curriculum schedules over data augmentation difficulty have been explored extensively in computer vision and general contrastive learning. Adapting this concept to intermediate training using a pre-defined sequence of existing NLP augmentations represents an incremental contribution.
3. **Heuristic Hardness Ordering**: 
   The difficulty order (dropout $\rightarrow$ synonym replacement $\rightarrow$ span deletion $\rightarrow$ back-translation) is assumed heuristically rather than verified theoretically or empirically (e.g., measuring mutual information or embedding distance between views).
4. **Limited Scope of Models**: 
   Evaluation is restricted to BERT-base. Demonstrating efficacy on RoBERTa, DeBERTa, or modern decoder-only/instruction-tuned models would strengthen the practical relevance.

---

### Evaluation and Scores

* **Soundness: 76/100**  
  The core methodology and ablations are sound, but the discrepancy in hyperparameter tuning between the proposed method and the baselines weakens the comparative rigor.
* **Novelty: 62/100**  
  The core contribution combines existing text augmentation methods with a standard linear curriculum schedule in an established intermediate training pipeline (CERT).
* **Significance: 70/100**  
  The approach provides consistent, moderate improvements (+1.1% over CERT) with minimal implementation overhead in low-resource settings.
* **Clarity: 88/100**  
  The paper is well-organized, concise, and clearly written.

---

**Overall Average Score:** **74.0 / 100**  
**Recommendation:** **Accept** (Weak Accept)