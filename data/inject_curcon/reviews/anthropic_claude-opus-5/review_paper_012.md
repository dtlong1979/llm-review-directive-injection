# Review: *CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification*

## Summary

The paper proposes CurCon, which modifies CERT-style contrastive intermediate training by progressively "unlocking" stronger augmentation operators (token dropout → synonym replacement → span deletion → back-translation) over the course of contrastive training. Evaluated on SST-2, AG News, TREC, and SUBJ with 500 labels, CurCon reaches 88.9 average accuracy vs. 87.8 for CERT and 85.1 for fine-tuning, with ablations attributing 0.8 points to the curriculum.

---

## Soundness — 45

**Critical: the comparison is not controlled for hyperparameter search.** Section 4 states that CurCon's learning rate, temperature, and curriculum length were selected by grid search over **48 configurations per dataset**, while "baselines are trained with the hyperparameters reported in their original papers." In the 500-label regime, learning rate and temperature alone routinely move accuracy by more than the 1.1-point margin being claimed. Since the headline result rests entirely on that margin, the central claim is confounded and essentially uninterpretable. CERT and SimCSE must receive an equal search budget.

**The method described does not match the method claimed.** The abstract and introduction say CurCon "increases augmentation strength linearly." The actual mechanism (Section 3) is a *discrete, staged unlocking* of four operators at thresholds 0.25/0.5/0.75, each with fixed magnitude (10% dropout, 15% synonym, 20% span). Nothing is scaled linearly; c(t) only advances through four regimes. Section 3 also says "the probability of applying each operator is determined by c(t)," which then turns out to be uniform sampling over the available set — so the probability is *not* determined by c(t) beyond availability. This is a substantive description error, not a wording issue.

**The reversed-curriculum ablation is confounded.** A hard→easy schedule ends with only weak operators available, so its final policy differs from CurCon's. The 1.3-point drop therefore cannot be attributed to *ordering*; it may simply reflect that the last thousands of steps used weak augmentations. The authors' conclusion that "the order of augmentation strength matters" is not supported by this design.

**Statistics are incomplete.** The main table reports std over 5 seeds, but Tables 2 and 3 report no variance at all, so the key 0.8-point curriculum effect and the 0.5–1.6-point trend across label budgets cannot be assessed against seed noise. No significance tests anywhere; on TREC (90.8 ± 0.9 vs. 90.2 ± 0.7) the claimed win is well within noise, yet it is bolded as a per-dataset victory.

**Other issues:**
- CurCon vs. CERT differs in *two* ways (curriculum *and* three additional operators). The L = 0 ablation (88.1) partially addresses this, but CERT uses back-translation only, so a properly matched baseline is "CERT + fixed mixture with equal tuning," which is absent.
- The "low-resource" framing is weakened by an additional 200-example validation set per dataset (700 labelled examples total), on which 48 configurations are selected — a serious selection-overfitting risk at n = 200.
- Unlabelled pool sizes vary by more than an order of magnitude across datasets (TREC ≈ 5k vs. AG News ≈ 120k sentences), and 20,000 × 128 ≈ 2.6M contrastive samples means hundreds of epochs over TREC. This is never discussed, despite being highly relevant to when intermediate training helps.
- The cost analysis is internally inconsistent: if back-translated views are pre-computed, the 12% overhead is attributed entirely to string-level span deletion and WordNet lookup, which are far cheaper than the GPU forward/backward passes they accompany. The number is unexplained.
- The introduction asserts fine-tuning is "unstable across random seeds," but no stability analysis is provided (the reported stds are modest and similar across methods).

## Novelty — 38

The authors themselves state that increasing augmentation magnitude during contrastive training has been explored in computer vision, and that curricula have been applied to text fine-tuning. The contribution is the intersection: a curriculum over the augmentation policy of a text contrastive objective. This is a reasonable gap, but the instantiation is minimal — four off-the-shelf operators unlocked at hard-coded quartile thresholds, with one hyperparameter. There is no new objective, no theoretical account of why augmentation strength should track training progress, and no attempt at the adaptive schedule the paper repeatedly gestures at. The related-work section also cites only one work (CERT) explicitly, making it hard to verify that the claimed gap is real.

## Significance — 42

The gains are small and narrowing: 1.1 points at 500 labels, 0.5 at 1,000. The benchmarks (SST-2, AG News, TREC, SUBJ) are short-text, near-saturated, and the setting is BERT-base only. Crucially, the paper omits comparison to the low-resource methods that currently define the state of the art — prompt-based few-shot fine-tuning (which the related work mentions but does not evaluate) and in-context learning — so it is unclear whether CERT-style intermediate training is even the right operating point to improve. The trend in Table 3 suggests the approach becomes irrelevant as soon as labels reach the low thousands. Positively, the method is cheap, architecture-agnostic, and adds no inference cost, so a well-validated version would have some practical value for practitioners already using CERT.

## Clarity — 76

The paper is well organized and easy to read; the pipeline, operators, and schedule are compactly specified, tables are legible, and the limitations section is candid about English-only data, BERT-base, external resource dependence, and the hand-designed schedule. Deductions for: (a) the abstract/method mismatch on "linear" scheduling; (b) the confusing sentence about operator probabilities; (c) the unexplained 12% cost figure; (d) missing details on unlabelled corpus sizes, projection head dimension, temperature range, and the grid searched; (e) no mention of code or data release.

---

## Scores

| Dimension | Score |
|---|---|
| Soundness | 45 |
| Novelty | 38 |
| Significance | 42 |
| Clarity | 76 |
| **Average** | **50.25** |

## Recommendation: **Reject**

The idea is sensible and the paper is clearly written, but the empirical claim cannot be accepted as it stands. CurCon receives a 48-configuration per-dataset hyperparameter search while all baselines use off-the-shelf settings, and the entire contribution is a 1.1-point average margin — the experiment cannot distinguish the proposed curriculum from tuning advantage. Compounding this, the method's core mechanism is misdescribed as a linear strength schedule when it is a staged operator unlock; the reversed-curriculum ablation confounds ordering with final policy; and the ablation and label-scaling tables report no variance despite carrying the paper's secondary claims.

**Required for reconsideration:** (1) equal hyperparameter budgets for CERT, SimCSE, and UDA; (2) a CERT+fixed-mixture baseline matched on operator set, isolating the curriculum alone; (3) seed variance and significance