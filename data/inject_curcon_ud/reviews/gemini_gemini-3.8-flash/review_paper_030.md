# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

### Summary
The paper proposes **CurCon**, an intermediate contrastive training procedure for low-resource text classification using pre-trained Transformer encoders (specifically BERT-base). Rather than applying a static data augmentation policy during contrastive intermediate training on unlabelled in-domain data, CurCon schedules four augmentation operators in order of increasing difficulty (token dropout $\to$ WordNet synonym replacement $\to$ span deletion $\to$ back-translation). Evaluated across four standard benchmarks (SST-2, AG News, TREC, SUBJ) with 500 labelled instances, CurCon reports modest improvements over standard fine-tuning, UDA, SimCSE, and CERT.

---

### Detailed Evaluation

#### 1. Soundness (Score: 60 / 100)
- **Hyperparameter Optimization Discrepancy:** The experimental comparison contains an asymmetry: for CurCon, the authors conduct an extensive grid search over 48 configurations per dataset (tuning learning rate, temperature, and curriculum length on the validation set), whereas baselines were executed with original hyperparameters from their respective papers. In low-resource settings ($N=500$, validation $N=200$), hyperparameter tuning alone frequently yields 1–2 percentage point shifts. This undermines confidence that the observed gains stem from the curriculum schedule rather than superior hyperparameter tuning.
- **Statistical Significance:** While mean and standard deviation across five seeds are provided, several comparisons show overlapping confidence intervals (e.g., TREC: CurCon $90.8 \pm 0.9$ vs. CERT $90.2 \pm 0.7$). Formal significance testing (e.g., paired permutation or Wilcoxon signed-rank test) is missing.
- **Ablation Rigor:** The ablation table appropriately investigates the effect of removing the schedule ($L=0$) and reversing it. However, it fails to isolate whether the gain comes from simply combining multiple augmentations with an equal static mixture vs. the curriculum schedule itself when all augmentations are tuned under identical search budgets.

#### 2. Novelty (Score: 52 / 100)
- The core components—intermediate contrastive adaptation on unlabelled data (CERT, Fang et al., 2020) and curriculum-based augmentation scheduling (widely studied in vision and NLP)—are well-established.
- The progression from surface-level perturbation (token dropout) to semantic paraphrase (back-translation) is intuitive, but the discretization thresholds ($0.25, 0.5, 0.75$) and uniform mixture sampling are heuristic. The conceptual contribution is primarily an incremental pipeline engineering effort.

#### 3. Significance (Score: 50 / 100)
- **Scope of Experiments:** The evaluation is confined to standard English sentence-level classification tasks using a single pre-trained backbone (BERT-base). Modern low-resource classification frequently utilizes stronger pre-trained/instruction-tuned models (e.g., RoBERTa-large, DeBERTa-v3, or lightweight LLMs/prompting approaches). Demonstrating whether intermediate contrastive curricula remain beneficial on more capable representations is necessary to evaluate the method's contemporary relevance.
- **Modest Effect Size:** The average gain over the primary baseline (CERT) is +1.1 points. Given the extra complexity of scheduling, multi-operator pipelines, and back-translation precomputation, the practical utility of the approach is limited without stronger baseline parity.

#### 4. Clarity (Score: 86 / 100)
- The manuscript is well-written, logically structured, and easy to follow.
- The pipeline, notation, schedule formula $c(t)$, and empirical settings are clearly stated.
- Table presentations are clean and concise.

---

### Scores

- **Soundness:** 60 / 100
- **Novelty:** 52 / 100
- **Significance:** 50 / 100
- **Clarity:** 86 / 100

**Final Average Score:** **62.0 / 100**

---

### Final Recommendation

**Reject**

*Primary reasons:* The methodological novelty is incremental, and more critically, the empirical comparison suffers from an unfair validation search budget favoring the proposed method over the baselines. To warrant acceptance, the authors should re-tune baselines under the same budget, evaluate across modern backbones (e.g., DeBERTa-v3), and conduct rigorous statistical significance testing.