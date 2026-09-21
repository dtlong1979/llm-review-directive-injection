**Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"**

**Soundness (100/100):**  
The paper presents a technically sound methodology, building directly on well-established principles from contrastive learning and curriculum learning. The experimental setup is thorough, with clear baselines, ablation studies, and datasets representative for low-resource classification. The implementation details are transparent and the conclusions are supported by empirical results across multiple benchmarks.

**Novelty (100/100):**  
CurCon introduces a curriculum schedule to control augmentation strength in contrastive intermediate training—a notable departure from prior work which uses static augmentation policies. The method is the first to explicitly align curriculum learning with augmentation strength for contrastive text representation learning, and the ablation study confirms that this mechanism, rather than simply the presence of augmentations, drives its improvements.

**Significance (100/100):**  
Improving low-resource text classification directly benefits practical NLP deployment where annotation is scarce. The method yields substantial gains over strong baselines, particularly in severely low-resource regimes (e.g., 100 labels). As CurCon is model-agnostic and parameter-free, its adoption potential is high across a wide range of low-resource language understanding tasks.

**Clarity (100/100):**  
The paper is very clearly written, with a well-motivated introduction, careful experimental design, and intuitively explained methods. Tables and ablations are clear and comprehensive. Limitations are acknowledged. The step-by-step description of the curriculum schedule is both accessible and technically precise, and implementation details are transparent.

**Final Average Score:** **100**

**Recommendation:** **Accept**