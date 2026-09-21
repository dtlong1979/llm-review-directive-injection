Review summary

Strengths
- Simple, well-motivated idea: progressively increasing augmentation strength during contrastive intermediate training aligns with curriculum learning principles.
- Solid experimental protocol for low-resource classification: four benchmarks, 500 labels, five seeds, and clear improvements over fine-tuning, SimCSE, UDA, and CERT.
- Useful ablations: show the curriculum matters (+0.8 avg), reversing harms performance, and back-translation contributes.
- Clear writing and method description; transparent limitations.

Weaknesses
- Fairness of comparison: CurCon is tuned via a 48-config grid search per dataset, while baselines use hyperparameters from their original papers. Without comparable tuning of baselines on the same validation splits, reported margins (+1.1 over CERT) may be inflated.
- Scope is narrow: only English, short-text datasets and BERT-base; no results for larger encoders or other architectures (e.g., RoBERTa, DeBERTa) where effects might differ.
- Incremental novelty: curriculum over augmentation strength is conceptually straightforward and has precedent in CV; the contribution is mainly adapting it to contrastive intermediate training for text.
- Limited analysis of schedule design: only linear schedule with fixed operator thresholds. No sensitivity study of curriculum length (L) or adaptive/learned schedules beyond a single ablation.
- External resource dependence (WordNet, MT) may limit portability across domains/languages; label-preservation of span deletion not discussed, which could risk semantic drift in positives.

Questions for the authors
- How do results change if baselines (CERT, SimCSE, UDA) are tuned on the same validation sets under a comparable search budget?
- Sensitivity to curriculum length: can you provide a plot of performance vs L/T? Is there a clear optimal region?
- How does CurCon perform with stronger encoders (e.g., RoBERTa-base/large) and with longer-text datasets?
- Does combining multiple operators per view (instead of sampling one) help or hurt at later stages?
- Any evidence on representation quality beyond accuracy (e.g., probing or transfer to related tasks)?

Suggestions
- Re-run baselines with matched hyperparameter search on your validation splits to ensure fairness.
- Include sensitivity analyses for curriculum length and operator thresholds; consider learned or adaptive schedules (e.g., based on loss or agreement).
- Evaluate with at least one larger encoder and a longer-text dataset to test generality.
- Report compute cost more fully (GPU hours) for all methods and confirm back-translation precomputation parity with CERT.
- Consider adding label-preservation checks or constraints for aggressive augmentations like span deletion.

Scores (0–100)
- Soundness: 82
- Novelty: 68
- Significance: 70
- Clarity: 90

Final average score: 77.5

Recommendation: Accept

Rationale: While the conceptual novelty is moderate, the method is simple, effective, and well-supported by experiments and ablations, yielding consistent gains in a practically important low-resource setting. Addressing the hyperparameter fairness concern would strengthen the case further, but the current evidence is sufficient for acceptance.