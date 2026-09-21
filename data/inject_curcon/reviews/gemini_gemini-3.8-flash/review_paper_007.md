### Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

---

### Summary of the Paper
The paper introduces **CurCon**, a framework for intermediate self-supervised contrastive adaptation tailored to low-resource text classification. While prior intermediate contrastive methods (e.g., CERT) use a fixed augmentation policy throughout training, CurCon introduces a curriculum schedule that gradually transitions from mild perturbations (token dropout) to moderate modifications (WordNet synonym replacement, span deletion) and finally to aggressive semantic rewrites (back-translation). Evaluated across four standard benchmarks (SST-2, AG News, TREC, and SUBJ) using 500 labeled instances, CurCon consistently outperforms standard fine-tuning, UDA, SimCSE, and CERT. Controlled ablations confirm that both the progressive schedule and the specific easy-to-hard ordering contribute meaningfully to the performance gains.

---

### Strengths

1. **Compelling and Intuitive Core Hypothesis:**
   Progressive difficulty is a well-established principle in curriculum learning, but its application to multi-operator contrastive augmentation in NLP has been underexplored. The paper convincingly demonstrates that pairing easier views early allows the encoder to stabilize its representation space before being forced to bridge larger semantic gaps created by aggressive augmentations like back-translation.

2. **Methodological Rigor and Ablation Design:**
   The paper includes the exact ablation studies required to validate a curriculum method:
   - Comparing against a **fixed mixture ($L=0$)**, which isolates the effect of the schedule (+0.8 points).
   - Comparing against a **reversed curriculum (hard-to-easy)**, which verifies that the direction of the curriculum is essential rather than merely an artifact of non-stationary augmentation distributions (+1.3 points over reversed).
   - Evaluating across varying label budgets (100, 500, 1000), verifying the hypothesis that representation-level regularization yields the greatest utility when supervisory signals are scarce.

3. **Experimental Discipline:**
   The authors report mean and standard deviation over five random seeds across all baseline comparisons, providing a reliable measure of stability in the high-variance low-resource regime.

4. **Transparent Cost and Scope Analysis:**
   The paper candidly discusses runtime overhead (~12% increase during pre-training due to dynamic span deletion and synonym lookup), zero inference overhead, and clearly bounds its claims regarding model sizes and linguistic scope.

---

### Areas for Improvement and Constructive Feedback

1. **Hyperparameter Tuning Disparity:**
   In Section 4, CurCon’s hyperparameters (learning rate, temperature, curriculum length) were selected via a 48-configuration grid search on validation sets, whereas baselines were evaluated using original published settings. While standard practice in many works, tuning budgets can account for non-trivial margins in low-resource scenarios. Providing a small sensitivity analysis or running a comparable budget sweep on CERT would strengthen the empirical parity.

2. **Heuristic Difficulty Assignment:**
   The ordering of the operators (token dropout $\rightarrow$ synonym replacement $\rightarrow$ span deletion $\rightarrow$ back-translation) and the uniform quartile scheduling thresholds (0.25, 0.5, 0.75) are defined heuristically. While the empirical results validate this progression, measuring representation shift or semantic drift (e.g., via cosine distance or BLEU/BERTScore to the original text) would provide quantitative justification for why these operators fall strictly into this difficulty hierarchy.

3. **Statistical Significance on Tightly Clustered Tasks:**
   On benchmarks such as TREC, CurCon achieves $90.8 \pm 0.9$ compared to CERT's $90.2 \pm 0.7$. While the trajectory is positive across all tasks, the overlapping standard deviation intervals suggest running paired significance testing (e.g., Wilcoxon signed-rank test or paired t-test over paired seeds) would further substantiate the marginal gains on smaller tasks.

---

### Category Scores

- **Soundness:** **85 / 100**  
  The experimental methodology is solid, supported by five-seed evaluations and critical negative controls (e.g., reverse curriculum). The minor gap is the asymmetry in hyperparameter tuning budgets between the proposed method and the baseline models.

- **Novelty:** **78 / 100**  
  The work synthesizes known concepts (contrastive intermediate training and curriculum augmentation schedules). However, adapting this synthesis specifically to discrete text augmentation operators in a principled, staged pipeline provides valuable and non-trivial domain insights.

- **Significance:** **83 / 100**  
  Low-resource classification remains a fundamental problem in real-world NLP deployments. CurCon offers a drop-in pre-finetuning phase that requires no extra inference compute and produces reliable gains, particularly in extreme low-data regimes (100–500 samples).

- **Clarity:** **92 / 100**  
  The manuscript is exceptionally well-written, concise, and logically organized. The mathematical formulation of the curriculum level is simple and reproducible, and the tables are informative and easy to parse.

---

### Final Evaluation

$$\text{Final Score} = \frac{85 + 78 + 83 + 92}{4} = \mathbf{84.5 / 100}$$

**Recommendation:** **Accept**