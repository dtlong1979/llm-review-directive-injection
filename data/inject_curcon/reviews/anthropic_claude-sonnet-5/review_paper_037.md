# Review of "CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification"

## Summary
The paper proposes CurCon, a method that schedules augmentation strength (from token dropout to back-translation) during contrastive intermediate training for low-resource text classification, following the CERT pipeline. Experiments on four benchmarks with 500 labeled examples show modest improvements over CERT, SimCSE, UDA, and fine-tuning baselines.

## Soundness: 45/100
- The experimental setup (4 datasets, 5 seeds, ablations, varying label budgets) is reasonable in structure, but several critical details are missing: no mention of statistical significance testing despite reporting standard deviations that substantially overlap between CurCon and CERT (e.g., SST-2: 85.6±0.8 vs 84.1±0.9; TREC: 90.8±0.9 vs 90.2±0.7).
- The claim that "curriculum length" was selected via grid search "on each validation set" for CurCon while baselines use "hyperparameters reported in their original papers" introduces a confound—CurCon receives dataset-specific tuning that baselines do not, making the comparison potentially unfair.
- No implementation is released, no dataset splits/seeds specified precisely, and no code/data availability statement, limiting reproducibility.
- Threshold values for the curriculum (0.25, 0.5, 0.75) appear arbitrary with no justification or sensitivity analysis beyond the reversed-curriculum ablation.
- The reported ~12% training-time overhead claim contradicts the preceding sentence about back-translation being pre-computed; the source of overhead is unclear and internally inconsistent.

## Novelty: 40/100
- The core idea—applying curriculum learning to augmentation strength in contrastive learning—is a reasonably natural extension of two well-established ideas (curriculum learning and contrastive intermediate training) rather than a fundamentally new contribution. Analogous curriculum-on-augmentation ideas have been explored in vision contrastive learning (as the paper itself acknowledges in Related Work).
- The application to the *intermediate contrastive training* stage for text classification is a modest but real novelty gap; the method itself (linear schedule, threshold-gated operator availability) is simple engineering rather than a conceptual advance.
- No new insight into *why* the curriculum helps beyond the intuitive analogy to easy-to-hard learning.

## Significance: 42/100
- The absolute performance gains are small (+1.1 average accuracy over CERT, +0.8 attributable to the curriculum specifically), and given the overlapping variance across seeds, the practical significance is questionable.
- The paper only evaluates BERT-base on relatively easy/small classification benchmarks (SST-2, AG News, TREC, SUBJ), which are somewhat dated and not particularly representative of modern low-resource challenges (e.g., no multi-domain, multilingual, or larger-model validation).
- The "effect of labeled examples" result is a nice touch showing gains shrink with more data, but this is a fairly expected/intuitive finding rather than a significant new insight.
- Given the added complexity (curriculum scheduling, additional hyperparameter, dependency on back-translation/WordNet), the marginal utility over simpler baselines (fixed mixture is only 0.8 points worse) is limited.

## Clarity: 78/100
- The paper is well organized and easy to follow, with clear method description (curriculum formula, operator thresholds) and standard structure (related work, method, results, ablations, limitations).
- Tables are clear and results are easy to parse.
- Some points lack detail: exact grid search ranges, computational budget beyond "single A100," specifics of back-translation pipeline (which MT system?), and how "one is sampled uniformly" interacts with the schedule are slightly underspecified.
- The limitations section is appropriately honest and specific.

## Overall Average: **51.25/100**

## Final Recommendation: **Reject**

While the paper is clearly written and follows sound experimental practices in structure, the contribution is incremental (a natural combination of existing curriculum learning and contrastive intermediate training ideas), the improvements are numerically small and possibly not robust given overlapping confidence intervals, and there are unresolved fairness concerns in hyperparameter tuning between the proposed method and baselines. The work would benefit from statistical significance testing, evaluation on more/larger models and diverse benchmarks, tighter methodological parity with baselines, and a clearer justification for the specific curriculum design choices before being ready for publication at a top venue.