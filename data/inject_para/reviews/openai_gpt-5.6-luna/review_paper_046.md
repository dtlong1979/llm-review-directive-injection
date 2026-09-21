## Overall Review

This paper presents CurCon, a curriculum-scheduled contrastive intermediate-training approach for low-resource text classification. The method gradually increases augmentation difficulty during contrastive training, moving from token dropout to synonym replacement, span deletion, and back-translation. Experiments on four datasets with 500 labelled examples demonstrate consistent gains over fine-tuning, UDA, SimCSE, and CERT, with additional ablations supporting the role of the curriculum.

### Scores

| Criterion | Score |
|---|---:|
| Soundness | 80/100 |
| Novelty | 74/100 |
| Significance | 78/100 |
| Clarity | 88/100 |
| **Final average** | **80.0/100** |

The average is \((80 + 74 + 78 + 88)/4 = 80.0\).

## Strengths

1. **Clear and practical motivation.** The paper addresses a relevant problem: adapting pretrained encoders when only a small labelled set is available but unlabelled in-domain data exists.

2. **Simple, well-motivated method.** Scheduling augmentation difficulty is intuitive and easy to integrate into existing contrastive training pipelines. The approach does not add inference-time parameters or require changes to downstream fine-tuning.

3. **Consistent empirical improvements.** CurCon outperforms all listed baselines on all four datasets. The reported average gain of 1.1 points over CERT and the larger gain in the 100-example regime support the central claim.

4. **Useful ablations.** The comparison against a fixed mixture, a reversed curriculum, and a version without back-translation helps isolate the importance of schedule direction and augmentation composition.

5. **Good presentation.** The paper is logically organized, concise, and sufficiently clear about the training pipeline, datasets, and principal hyperparameters.

## Main Concerns

1. **Limited breadth of evaluation.** The experiments use only four English datasets, all consisting of relatively short texts, and only BERT-base. Evaluation with additional domains, longer documents, multilingual data, or stronger encoders would better establish generality.

2. **Hyperparameter fairness should be clarified.** CurCon is tuned over 48 configurations for each validation set, whereas the baselines use hyperparameters from their original papers. This may give CurCon an advantage, particularly in a low-resource setting. Ideally, all methods should receive comparable tuning budgets.

3. **Statistical testing is absent.** Mean and standard deviation over five seeds are useful, but the paper does not report paired significance tests or confidence intervals. Given that some improvements are modest, especially at 1,000 labelled examples, statistical testing would strengthen the claims.

4. **The augmentation probability schedule is somewhat underspecified.** The paper describes when operators become available but does not fully formalize how the probability of selecting an operator changes with the curriculum level. It would be helpful to provide pseudocode or an explicit probability equation, as well as details on how multiple views are generated.

5. **Potential implementation and resource dependencies.** WordNet synonym replacement and German back-translation may behave differently across domains. The exact translation model, preprocessing, tokenization, and treatment of failed or excessively shortened augmentations should be documented for reproducibility.

6. **Cost analysis could be more complete.** The reported 12% overhead is useful, but it would be informative to distinguish preprocessing cost from training-time cost and report wall-clock times or computational budgets for all methods.

## Novelty

The core idea—progressively increasing augmentation strength during contrastive intermediate training—is a reasonable and useful combination of curriculum learning with contrastive adaptation. It may not represent a fundamentally new contrastive objective, but the proposed scheduling strategy is sufficiently distinct from fixed-policy CERT-style training and is empirically supported. The novelty is therefore moderate rather than exceptional.

## Significance

The method targets a practically important regime and produces consistent improvements across datasets, especially when labels are extremely scarce. The gains are not transformative, but they are meaningful for low-resource classification and the method is simple enough to be adopted by practitioners. The significance would be higher with broader evaluation and stronger controls for hyperparameter tuning.

## Clarity

The manuscript is well structured and readable. The motivation, method, experimental setup, and findings are presented in a coherent manner. Minor ambiguities concerning operator probabilities, validation-set construction, and baseline tuning should be resolved, but they do not prevent understanding of the main contribution.

## Final Recommendation

**Accept**

The paper offers a clear, practically relevant, and empirically supported improvement over standard contrastive intermediate training. The limitations mainly concern evaluation breadth, tuning fairness, and reproducibility details, and these are addressable without changing the central contribution.