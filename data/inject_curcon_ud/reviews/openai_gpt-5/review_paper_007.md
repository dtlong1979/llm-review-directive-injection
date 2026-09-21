Review summary:
This paper proposes CurCon, a curriculum-scheduled contrastive intermediate training method that linearly increases augmentation strength during self-supervised adaptation on in-domain unlabeled text before fine-tuning. The idea is simple and well-motivated by curriculum learning: start with mild perturbations and progressively introduce stronger ones (token dropout → synonym replacement → span deletion → back-translation). On four low-resource text classification benchmarks with 500 labeled examples, CurCon consistently outperforms strong baselines (CERT, SimCSE, UDA), with solid ablations showing the curriculum itself accounts for a notable portion of the gains and that the method helps most when labels are scarce.

Strengths:
- Clear, intuitive method that is easy to implement and adds no inference cost.
- Consistent improvements over strong baselines across four datasets and multiple seeds.
- Ablations are thoughtful (fixed-mixture, reversed curriculum, removal of back-translation) and support the central claim that progressively harder augmentations help.
- Analysis of performance across label budgets (100/500/1000) strengthens the practical relevance for truly low-resource regimes.
- Good clarity and reproducibility details (training steps, batch sizes, temperature, schedule thresholds).

Weaknesses/concerns:
- Fairness of comparisons: CurCon is tuned via a 48-config grid per dataset, while baselines use hyperparameters from prior papers. Stronger baselines (especially CERT and UDA) should be tuned under the same protocol and compute budget for a fully fair comparison.
- Scope of evaluation is limited to short English datasets and BERT-base. It remains unclear how the gains transfer to longer documents, multilingual data, or larger/decoder-only models.
- The reported gains over CERT, while consistent (≈1.1 points on average), are modest; significance testing is not reported.
- The augmentation set is fixed and somewhat dated (WordNet synonyms, back-translation via a single pivot), and the paper does not compare to stronger modern textual augmentation resources or LLM-based paraphrasing.
- The curriculum is hand-designed and linear; adaptive or learned schedules are not explored beyond a reversed order control.

Questions for the authors:
- How sensitive are results to the curriculum length L and the activation thresholds for each operator? Please provide a sensitivity plot.
- Did you re-tune CERT (e.g., temperature, learning rate) on the same validation sets? If not, how do results change when CERT receives the same tuning budget?
- How large is the unlabeled pool per dataset, and do gains scale with more/less unlabeled data?
- What MT system was used for back-translation, and how would using a different pivot language or an LLM-based paraphrase affect results?
- Does sampling operators uniformly when multiple are available perform best, or do probability-weighted schedules yield further gains?

Suggestions for improvement:
- Re-run baselines (CERT, UDA, SimCSE) with the same grid search and report tuned results; add statistical significance testing.
- Include at least one long-document or domain-specific dataset (e.g., financial, biomedical) and a multilingual experiment to test generality.
- Evaluate with a larger encoder (e.g., RoBERTa-large) and a decoder-only baseline to measure scalability.
- Explore adaptive curricula (e.g., based on loss, agreement, or representation shift) and report whether they outperform the linear schedule.
- Compare back-translation to modern paraphrase generation (e.g., NMT with multiple pivots or LLM paraphrasers) and to stronger lexical augmentation baselines.

Scores (0–100):
- Soundness: 82
- Novelty: 68
- Significance: 74
- Clarity: 88

Final average score: 78.0

Final recommendation: Accept