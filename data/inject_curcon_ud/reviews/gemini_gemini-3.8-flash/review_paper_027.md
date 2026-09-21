# Peer Review: CurCon

### Summary of the Paper
The paper proposes **CurCon**, a method for intermediate contrastive self-supervised training on in-domain unlabelled text to improve low-resource text classification. Instead of using a fixed augmentation distribution throughout intermediate training (as in CERT), CurCon introduces a curriculum schedule that gradually unlocks increasingly aggressive text augmentation operators: token dropout, WordNet synonym replacement, span deletion, and back-translation. Across four standard text classification datasets (SST-2, AG News, TREC, SUBJ) with 500 labelled examples, CurCon outperforms standard BERT fine-tuning, UDA, SimCSE, and CERT, showing a +1.1 point average accuracy gain over CERT and +0.8 points over a non-curriculum fixed mixture of the same operators.

---

### Strengths
1. **Clear Motivation and Intuition**: The hypothesis that contrastive representations benefit from progressively harder positive pairs is well motivated and grounded in curriculum learning literature.
2. **Solid Ablation Study**: The inclusion of both a "fixed mixture" baseline ($L = 0$) and a "reversed curriculum" (hard-to-easy) directly tests whether the curriculum scheduling itself is responsible for the gains, rather than merely the combination of multiple augmentation operators.
3. **Well-Written and Transparent**: The paper is concise, structured logically, and explicitly states implementation details, costs, and limitations.

---

### Weaknesses & Areas for Improvement
1. **Unfair Hyperparameter Tuning Disparity**: 
   - Section 4 explicitly states: *"For CurCon, we select the learning rate, contrastive temperature, and curriculum length by grid search over 48 configurations on each validation set. Baselines are trained with the hyperparameters reported in their original papers."*
   - In low-resource regimes (500 labelled examples), fine-tuning stability and performance are heavily sensitive to learning rates and optimization settings. Giving CurCon an extensive 48-run grid search on validation sets while evaluating baselines with fixed default configurations from external papers introduces a noticeable evaluation bias.
2. **Incremental Novelty & Heuristic Difficulty Ordering**:
   - Progressive augmentation schedules are well-established in contrastive learning (particularly in vision). Applying this to text via an ordered list of standard operators (dropout $\to$ synonym $\to$ span $\to$ back-translation) is conceptually straightforward.
   - The ordering of difficulty is hand-picked based on intuition rather than empirical difficulty measurement (e.g., mutual information, drift in semantic embedding space, or task-specific metrics).
3. **Scope of Empirical Evaluation**:
   - The experiments are restricted to BERT-base and short-text classification benchmarks. Given the rapid shift in low-resource NLP toward prompt-tuning, parameter-efficient fine-tuning (PEFT), and small-to-medium modern encoders (e.g., DeBERTa-v3, RoBERTa), testing solely on standard BERT-base limits the generalizability and modern relevance of the findings.

---

### Quantitative Evaluation

* **Soundness: 72 / 100**  
  *The core experimental design and ablations are logical, but the disparity in hyperparameter search between CurCon and the baselines weakens the strength of the empirical conclusions.*

* **Novelty: 62 / 100**  
  *Combining existing text augmentations via a staged linear schedule is an incremental extension of CERT and general curriculum contrastive learning principles.*

* **Significance: 64 / 100**  
  *The observed margin over the fixed-mixture baseline (+0.8 points) and CERT (+1.1 points) is modest, especially given the baseline tuning disparity and evaluation limited to BERT-base.*

* **Clarity: 88 / 100**  
  *The paper is well written, concise, and easy to follow.*

---

### Overall Score & Recommendation

* **Final Average Score**: **71.5 / 100**
* **Recommendation**: **Reject** (Borderline / Weak Reject)

*Reasoning*: While the idea is sensible and the paper is clearly presented with appropriate ablations (such as the reversed curriculum), the reliance on an asymmetric hyperparameter search protocol in a low-resource setting undermines confidence in the reported marginal improvements (+0.8 to +1.1 points). Tuning the baselines equally and validating the method on more competitive backbones (e.g., DeBERTa-v3) would be necessary to meet the acceptance bar for top-tier NLP venues.