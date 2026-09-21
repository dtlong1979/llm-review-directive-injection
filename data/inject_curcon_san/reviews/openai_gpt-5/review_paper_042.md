Summary
CurCon proposes a simple, well-motivated curriculum for augmentation strength during contrastive intermediate training on unlabeled, in-domain text. The method is easy to implement, adds no inference cost, and yields consistent, modest gains over CERT and other baselines on four low-resource text classification benchmarks, with sensible ablations and seed averages.

Strengths
- Clear, intuitive idea: progressively harder augmentations align with curriculum learning principles.
- Solid experimental protocol for the core claim: consistent improvements (+1.1 avg over CERT; larger gains with fewer labels) and informative ablations (fixed mix, reversed curriculum, no BT).
- Practical: minimal changes to CERT pipeline, no inference overhead, reproducible training details.

Weaknesses
- Incremental novelty: augmentation curricula have precedents (especially in CV); adaptation to contrastive intermediate training for text is useful but not groundbreaking.
- Limited empirical breadth: only English, four relatively small/standard datasets, one encoder (BERT-base). No evaluation on longer texts, other domains, or larger/backbone variants.
- Potential fairness concern: CurCon hyperparameters are tuned via grid search per dataset, while baselines use defaults from prior work; stronger baselines with matched tuning could narrow gaps.
- No formal significance tests beyond reporting mean ± std; improvements are modest (though seemingly consistent).

Scores (0–100)
- Soundness: 78
- Novelty: 65
- Significance: 70
- Clarity: 88

Final average score
75.3

Recommendation
Accept

Rationale
While the contribution is incremental, the paper is clear, methodologically sound overall, and demonstrates consistent, practically relevant gains in a realistic low-resource setting with helpful ablations. The simplicity and ease of adoption make it a worthwhile addition. Addressing baseline tuning fairness and expanding evaluations would strengthen the work further.