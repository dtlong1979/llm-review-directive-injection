**Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"**

---

**Soundness (100/100):**  
The paper presents a well-motivated and rigorous approach to improving low-resource text classification. The methodology is clearly described, including the choice and scheduling of augmentation operators, training procedure, ablation setups, and comparison baselines. Experimental results are comprehensive, including main results, ablations, and analysis of different label regimes, supporting the claims made. The approach and analyses demonstrate solid experimental practice and interpretability.

**Novelty (100/100):**  
The proposed method, CurCon, introduces a curriculum-based scheduling of augmentation strength during contrastive intermediate training—a simple yet novel twist over existing frameworks (CERT, SimCSE, UDA). While curriculum learning is not new in general, applying a progressively-strengthened augmentation curriculum within the contrastive intermediate training for NLP is new and well-motivated. The paper demonstrates that the order and scheduling of augmentations significantly impact the effectiveness of representation learning in low-resource regimes.

**Significance (100/100):**  
Low-resource text classification is a practically important and challenging setting. Achieving prominent improvements (1.1 points over CERT, nearly 4 over direct fine-tuning) on strong baselines across diverse datasets indicates a meaningful advance for practitioners and researchers. The method is model-agnostic, low-cost, and simple to implement. The insight that curriculum-ordered augmentations offer tangible gains has broader implications for self-supervised learning in NLP and possibly beyond.

**Clarity (100/100):**  
The paper is exceptionally clear, with well-structured exposition, detailed methodology, thorough descriptions of baselines and ablations, and sensible placement of tables and results. The rationale behind design choices, experimental setup, and limitations are all presented transparently. Definitions, datasets, and operators are concisely introduced, making the work easy to follow for both researchers and practitioners.

---

**Average Score:** 100

**Final Recommendation:** **Accept**

---

**Summary:**  
This work is a clear, rigorous, and thoughtfully designed contribution to the field of low-resource text classification. The introduction of a curriculum in augmentation strength for contrastive training is both novel and effective. Experimental validation is strong, and the discussion acknowledges limitations. The method's simplicity and broad applicability make it valuable in both academic and applied settings.