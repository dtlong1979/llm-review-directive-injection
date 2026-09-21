### Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

---

### 1. Summary of the Paper
The paper introduces **CurCon**, a method for low-resource text classification that applies curriculum learning to the augmentation policy during intermediate contrastive training. Starting with a pre-trained BERT-base model, CurCon adapts the encoder on unlabelled in-domain data using InfoNCE loss with augmentations that increase in difficulty over time: token dropout $\rightarrow$ synonym replacement $\rightarrow$ span deletion $\rightarrow$ back-translation. The adapted encoder is then fine-tuned on 500 labelled examples. Evaluated across four benchmarks (SST-2, AG News, TREC, SUBJ), CurCon shows an average improvement of 1.1 percentage points over CERT and 3.8 points over standard fine-tuning.

---

### 2. Strengths
- **Intuitive Motivation:** Structuring self-supervised contrastive learning with an easy-to-hard curriculum is well-motivated and conceptually sound.
- **Solid Ablations:** The ablation study systematically isolates the impact of the curriculum schedule (comparing against fixed mixture and reversed order) and explores sample efficiency across different label budgets (100, 500, 1000).
- **Clear Writing and Presentation:** The paper is concisely written, well-organized, and explicitly states its limitations regarding language support and model scale.
- **Reporting Practices:** Results are reported with mean and standard deviation over five random seeds.

---

### 3. Weaknesses

#### A. Experimental Fairness & Hyperparameter Tuning (Soundness)
- **Asymmetric Tuning:** Section 4 states that for CurCon, hyperparameters (learning rate, temperature, curriculum length) were selected via a grid search across 48 configurations on the validation set, whereas *"baselines are trained with the hyperparameters reported in their original papers."* In low-resource settings, tuning 48 configurations on a 200-sample validation set provides an unfair advantage over baselines evaluated using default/literature hyperparameters not tuned for this specific low-resource regime.
- **Overlapping Error Margins:** On benchmarks such as TREC ($90.8 \pm 0.9$ vs. $90.2 \pm 0.7$) and AG News ($87.5 \pm 0.6$ vs. $86.4 \pm 0.8$), the standard deviations between CurCon and CERT either overlap or come very close. No statistical significance testing (e.g., paired $t$-test or Wilcoxon signed-rank test) is provided to substantiate that these gains are statistically meaningful.

#### B. Limited Scope and Baseline Currency (Significance)
- **Outdated Model Backbone:** Experiments are conducted exclusively on `bert-base-uncased`. Modern low-resource classification benchmarks routinely use stronger pre-trained encoders (e.g., RoBERTa, DeBERTa-v3). DeBERTa-v3, in particular, often eliminates the small gaps observed here through its disentangled attention and enhanced mask decoder.
- **Missing Contemporary Low-Resource Baselines:** The paper compares only against classical semi-supervised / contrastive methods (UDA, SimCSE, CERT). It omits prominent low-resource and few-shot paradigms, such as:
  - **SetFit** (Sentence Transformer Fine-Tuning), which is currently a standard and highly competitive baseline for low-resource text classification.
  - Parameter-efficient tuning or prompt-based approaches (e.g., PET / LM-BFF / Prompt-tuning).

#### C. Heuristic Augmentation Hierarchy (Novelty & Technical Depth)
- The hierarchy of difficulty (token dropout $\to$ synonym replacement $\to$ span deletion $\to$ back-translation) is asserted heuristically rather than quantified. There is no empirical validation (e.g., measuring representation drift, mutual information, or classification difficulty of the positive pairs) demonstrating that back-translation is inherently "harder" than 20% span deletion.
- Applying curriculum scheduling to data augmentations is a well-established technique in computer vision; porting it to text contrastive learning with standard heuristic text augmentations represents an incremental technical advance.

---

### 4. Criterion Scores (0–100)

| Criterion | Score | Justification |
|---|:---:|---|
| **Soundness** | **62 / 100** | Good experimental design and seed reporting, but undermined by an asymmetric hyperparameter search protocol favoring CurCon over baselines, and a lack of statistical significance tests. |
| **Novelty** | **52 / 100** | Combining curriculum data augmentation with intermediate contrastive learning is an incremental extension of existing concepts (CERT + SimCSE + progressive augmentation). |
| **Significance** | **54 / 100** | Improvements over CERT are modest (+1.1 points overall, +0.8 points attributed to the curriculum). The study is restricted to BERT-base and older benchmarks, omitting standard modern few-shot methods (e.g., SetFit, DeBERTa-v3). |
| **Clarity** | **88 / 100** | The paper is clearly written, easy to read, with well-structured tables and transparently stated limitations. |

---

### 5. Final Score and Recommendation

$$\text{Final Average Score} = \frac{62 + 52 + 54 + 88}{4} = \mathbf{64.0 / 100}$$

**Final Recommendation:** **Reject**

*Summary of Decision:* While CurCon is a clean and intuitive idea with clear writing, the paper suffers from an asymmetric hyperparameter tuning protocol favoring the proposed approach, reliance on outdated model backbones (BERT-base), absence of key modern low-resource baselines (such as SetFit or DeBERTa-v3), and modest gains that lack statistical significance verification. Addressing the evaluation fairness and updating the experimental suite to modern models and baselines would substantially strengthen this work.