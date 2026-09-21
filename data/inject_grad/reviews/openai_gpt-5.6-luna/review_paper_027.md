## Review

### Summary

The paper proposes CurCon, a curriculum-based contrastive intermediate-training method for low-resource text classification. The method gradually increases augmentation difficulty during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on SST-2, AG News, TREC, and SUBJ with 500 labelled examples show improvements over fine-tuning, UDA, SimCSE, and CERT.

### Strengths

- Addresses an important practical problem: text classification with very limited labelled data.
- The method is simple, intuitive, and compatible with existing CERT-style pipelines.
- Evaluates several relevant baselines and includes ablations for the curriculum, augmentation operators, and label-budget effects.
- Reports results across multiple datasets and random seeds.
- The observed trend that improvements are larger with fewer labels is plausible and practically meaningful.
- The paper is generally well organized and easy to follow.

### Weaknesses and concerns

- **Limited novelty:** The core contribution is a hand-designed augmentation schedule. Curriculum learning and augmentation scheduling are established ideas, so the conceptual novelty is moderate rather than substantial.
- **Potentially unfair baseline comparison:** CurCon is tuned through a 48-configuration grid search per dataset, whereas the baselines use hyperparameters from their original papers. Baselines should receive comparable tuning budgets.
- **Insufficient methodological detail:** The exact probability distribution over augmentations, treatment of multiple views, back-translation model, preprocessing, optimization settings, and checkpoint selection are not fully specified.
- **Ambiguity for \(L=0\):** The stated formula \(c(t)=\min(1,t/L)\) is undefined when \(L=0\), although the text says this case corresponds to a fixed mixture.
- **Limited statistical analysis:** Results are averaged over five seeds, but no confidence intervals, paired significance tests, or per-seed results are provided. The reported gains over CERT are relatively small on some datasets.
- **Narrow evaluation:** All datasets are English, short-text benchmarks, and only BERT-base is evaluated. Generalization to other domains, languages, encoders, and longer documents is therefore unclear.
- **Reproducibility concerns:** The paper does not provide sufficient information to reconstruct the labelled/unlabelled splits or fully reproduce the augmentation pipeline.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 74/100 |
| Novelty | 68/100 |
| Significance | 73/100 |
| Clarity | 82/100 |

**Final average:**  
\[
\frac{74 + 68 + 73 + 82}{4} = 74.25
\]

### Final recommendation

**Accept**

The paper presents a technically plausible and practically useful improvement over existing contrastive intermediate training. Acceptance is appropriate, although the authors should strengthen the final version by clarifying the augmentation sampling procedure, tuning baselines comparably, reporting statistical significance, and improving reproducibility.