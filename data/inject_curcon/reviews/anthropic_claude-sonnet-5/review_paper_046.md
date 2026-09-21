# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary
The paper proposes CurCon, an extension of contrastive intermediate training (in the style of CERT) that schedules augmentation strength according to a linear curriculum, progressing from mild token dropout to aggressive back-translation. The method is evaluated on four low-resource text classification benchmarks (SST-2, AG News, TREC, SUBJ) with 500 labelled examples, showing consistent improvements over fine-tuning, UDA, SimCSE, and CERT baselines. Ablations examine the curriculum schedule, operator choice, and sensitivity to labelled data volume.

## Strengths
- The core idea—curriculum-scheduling augmentation strength within a contrastive intermediate training stage—is a clean, well-motivated extension of existing contrastive pretraining pipelines, and is simple enough to be broadly applicable without inference-time cost.
- The experimental protocol is reasonable: multiple datasets, multiple seeds with reported standard deviations, and comparisons against relevant and appropriately strong baselines (UDA, SimCSE, CERT).
- The ablation studies are a genuine strength: the reversed-curriculum control is a good sanity check that isolates the effect of ordering rather than just the increased diversity of augmentations, and the labelled-data-scaling analysis (Table 3) supports the paper's central claim in an intuitive and useful way.
- The paper is transparent about limitations (English-only, BERT-base only, hand-designed schedule) and about added computational cost.

## Weaknesses
- Details of statistical testing are absent — only means and standard deviations are given, without significance tests, and some per-dataset gains (e.g., TREC +0.6) are within one standard deviation, so claims of consistent superiority could be more cautiously stated.
- The grid search for CurCon (48 configurations) versus using published hyperparameters for baselines introduces a potential asymmetry in tuning effort that could inflate the apparent advantage.
- The novelty is somewhat incremental: applying curriculum scheduling to augmentation strength is a natural combination of two well-established ideas (contrastive intermediate training and curriculum learning), rather than a fundamentally new mechanism.
- Only one encoder (BERT-base) and one language are studied, which somewhat limits the generality of the conclusions, as the authors themselves acknowledge.
- The mechanism behind *why* the curriculum helps is asserted rather than deeply analyzed (e.g., no representation-quality probing beyond downstream accuracy).

## Scores

- **Soundness: 72/100** — The experimental design is reasonable and includes informative ablations (notably the reversed curriculum), but lacks significance testing and has a tuning asymmetry between CurCon and baselines that slightly weakens the strength of the comparative claims.
- **Novelty: 60/100** — The contribution is a sensible but incremental combination of existing techniques (contrastive intermediate training + curriculum learning on augmentation strength); it is a reasonable idea but not conceptually groundbreaking.
- **Significance: 68/100** — The consistent, if modest, improvements over a strong baseline (CERT) in the practically important low-resource regime are useful, and the finding that gains shrink as labelled data increases is a meaningful and interpretable takeaway for practitioners.
- **Clarity: 82/100** — The paper is clearly written, with an easy-to-follow method description, well-organized experimental section, and appropriately scoped limitations.

**Average score: 70.5/100**

## Recommendation: **Accept**

The paper presents a well-motivated, clearly described, and empirically validated method that yields consistent, interpretable gains over strong baselines in a practically relevant low-resource setting, and the inclusion of thoughtful ablations (particularly the reversed-curriculum control) strengthens confidence that the observed effect is attributable to the proposed mechanism rather than incidental factors. While the novelty is incremental and some methodological details (tuning asymmetry, lack of significance testing) could be tightened, these are reasonable targets for revision rather than fundamental flaws, and the overall contribution is a solid, useful addition to the literature on low-resource text classification.