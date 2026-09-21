**Review**

**Soundness (100/100):**  
The paper presents a methodologically sound contribution. The experimental setup is well-controlled, with clear baselines, ablation studies, and sensitivity analysis to the number of labelled examples. Implementation details are thorough, and the results are statistically robust across multiple seeds and datasets. The reported improvements are substantiated by careful experiments.

**Novelty (100/100):**  
The proposed CurCon method introduces the new idea of scheduling augmentation strength in a curriculum during contrastive intermediate training, which is a notable departure from existing work using fixed augmentations. The adaptation of curriculum learning principles explicitly to augmentation strength within contrastive self-supervised learning for low-resource text classification is a novel contribution.

**Significance (100/100):**  
The problem of low-resource text classification is broadly relevant, and the performance gap addressed by CurCon is important in practical NLP deployments, where annotation budgets are frequently limited. CurCon’s improvements over strong baselines, especially under tight label constraints, mark a significant advancement that could influence future semi-supervised and self-supervised methods for NLP.

**Clarity (100/100):**  
The manuscript is exceptionally clear and well-organized. The introduction and related work frame the contribution precisely; the method description is detailed, with comprehensible algorithmic descriptions and justification for design choices. Tables are easy to interpret, and results are concisely summarized and analyzed.

**Final Average Score:**  
100

**Final Recommendation:**  
**Accept**