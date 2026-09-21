Review

Summary
The paper proposes CurCon, a curriculum-scheduled contrastive intermediate training approach for low-resource text classification. It gradually increases augmentation strength during the contrastive stage (from token dropout to synonym replacement, span deletion, and back-translation), then fine-tunes on 500 labeled examples per dataset. On four benchmarks (SST-2, AG News, TREC, SUBJ), CurCon improves average accuracy to 88.9 vs. 87.8 for CERT and 85.1 for standard fine-tuning. Ablations show the curriculum contributes about 0.8 points on average, with larger gains when fewer labeled examples are available.

Strengths
- Clear, simple idea with a strong motivation: scheduling augmentation strength aligns with curriculum learning principles.
- Consistent improvements over strong baselines (CERT, SimCSE, UDA) across four datasets, with statistically reasonable reporting (mean ± std over five seeds).
- Solid ablations isolating the effect of the curriculum design (including reversed curriculum and removing back-translation).
- Practicality: model-agnostic, small code changes, no inference overhead, and modest additional training cost.
- Good analysis of label-scarcity regimes, showing larger gains at 100 labeled examples.

Weaknesses and concerns
- Baseline tuning fairness: CurCon’s hyperparameters are tuned by grid search per dataset, but baselines use settings from original papers. This may understate baselines in the specific low-resource, in-domain setting; at minimum, a sensitivity/tuning sweep for CERT/SimCSE/UDA on the same validation sets would strengthen claims.
- Scope of evaluation: Only English and relatively short-text benchmarks, and only BERT-base. It would be valuable to test RoBERTa/DeBERTa or a decoder-only model to show generality.
- Limited task diversity: All are sentence/small-text classification. Including longer documents or a domain-specific dataset (e.g., biomedical or legal) would help establish robustness.
- Augmentation design: The choice of thresholds (0.25/0.5/0.75), operator strengths, and uniform sampling among available operators are fixed. An adaptive or learned schedule, or a brief exploration of different thresholds/mixings, could provide more insight.
- Fairness to CERT: Since CERT primarily uses back-translation, a variant of CERT with a matched mixture policy (no curriculum) and matched compute would clarify how much benefit comes from the curriculum per se vs. diversity of augmentations.

Suggestions for improvement
- Tune baselines under the same validation-driven protocol used for CurCon, and report their best scores to ensure fairness.
- Add results with a stronger encoder (e.g., RoBERTa-base/large) to assess whether gains persist or grow with model capacity.
- Evaluate on at least one longer-text and one domain-specific dataset; consider non-English settings to stress test dependence on WordNet and MT quality.
- Provide a brief analysis of representation quality (e.g., transfer to STS/sentence retrieval) to substantiate the claim that the curriculum yields better semantic representations.
- Explore simple adaptive schedules (e.g., ramping based on training loss or temperature) or different operator mixings to test robustness of the curriculum design.
- Report compute more precisely (GPU hours) and ensure matched contrastive steps and data exposure across methods.

Scores (0–100)
- Soundness: 83
- Novelty: 76
- Significance: 77
- Clarity: 90

Final average score: 81.5

Final recommendation: Accept