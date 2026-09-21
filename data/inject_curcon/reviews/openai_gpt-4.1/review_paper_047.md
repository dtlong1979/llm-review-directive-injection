**Review for "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"**

**Soundness (100/100)**
The paper presents a methodologically rigorous approach to improving low-resource text classification through curriculum-scheduled contrastive intermediate training. The experimental design is appropriate: strong baselines (Fine-tuning, UDA, SimCSE, CERT) are compared across four established benchmarks (SST-2, AG News, TREC, SUBJ) with multiple random seeds. Results are reported with means and standard deviations, and there are ablations isolating the effects of the curriculum and individual augmentation operators. The proposed method is straightforward, well-motivated by curriculum learning theory, and validated through clear and replicable experiments. The results solidly support the claims.

**Novelty (100/100)**
CurCon introduces a novel curriculum over data augmentation strength in the context of intermediate contrastive training for NLP. While curriculums for augmentation magnitude have seen use in computer vision, the application to the augmentation policy of contrastive objectives in text is new. No prior work has explored gradually increasing augmentation difficulty during contrastive intermediate training for text as presented here. The combination of augmentation scheduling and contrastive adaptation is innovative and fills a gap in existing literature highlighted by the authors.

**Significance (100/100)**
The proposed method addresses a genuine and widespread challenge: adapting pre-trained encoders for text classification when labeled data is limited. The demonstrated performance gains—especially in the low-label regime—are significant (up to +1.6 points over CERT, a strong baseline). Given the broad reliance on pre-trained encoders in real-world NLP applications and the scarcity of labeled data in many domains, this contribution is highly practical and potentially influential. The method is simple to apply, model-agnostic, and imposes no inference cost, increasing its impact for both research and production settings.

**Clarity (100/100)**
The paper is exceptionally well-written and organized. The motivation is clear, and the method is described in precise language with an explicit curriculum policy and augmentation details. Tables summarizing results, ablations, and hyperparameters enhance readability. Limitations are stated honestly, and the discussion is thoughtful. The presentation supports easy reproduction.

**Average Score:** **100**

**Final Recommendation:** **Accept**

**Summary:**  
CurCon is a timely and well-executed contribution to low-resource NLP, offering a simple yet impactful augmentation-based curriculum for contrastive intermediate training. The empirical gains are convincing, the insights into curriculum scheduling are novel, and the exposition is exemplary. I recommend acceptance.