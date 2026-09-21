# CurCon: Curriculum-Scheduled Contrastive Intermediate Training for Low-Resource Text Classification

## Abstract

Pre-trained encoders such as BERT achieve strong results on text classification when large labelled datasets are available, but their performance drops sharply when only a few hundred labelled examples exist. Intermediate contrastive training on unlabelled in-domain text has emerged as an effective way to adapt encoders before fine-tuning. However, existing approaches apply a fixed augmentation strength throughout contrastive training, which ignores the observation that representation learning benefits from progressively harder training signals. We propose CurCon, a curriculum-scheduled contrastive intermediate training method that increases augmentation strength linearly during the contrastive stage, starting from mild token-level perturbations and ending with aggressive back-translation and span deletion. We evaluate CurCon on four text classification benchmarks under a low-resource setting of 500 labelled examples per dataset. CurCon achieves an average accuracy of 88.9, compared with 87.8 for CERT and 85.1 for standard fine-tuning. Ablation studies indicate that the curriculum schedule contributes 0.8 points of the average improvement, and the gains are largest when fewer labelled examples are available.

## 1 Introduction

Text classification underpins many practical applications, from customer-feedback analysis to content moderation and clinical triage. Pre-trained Transformer encoders have made high accuracy attainable on standard benchmarks, but these results typically rely on thousands of labelled examples. In many real deployments, annotation is expensive, slow, or requires domain experts, and practitioners must work with only a few hundred labelled instances. In this regime, direct fine-tuning is unstable across random seeds and tends to overfit.

A common remedy is to exploit unlabelled in-domain text. Semi-supervised consistency methods such as UDA regularise the classifier to produce stable predictions under input perturbations, while intermediate contrastive training methods such as CERT first adapt the encoder with a self-supervised contrastive objective on unlabelled data and then fine-tune it on the labelled set. Contrastive intermediate training is attractive because it is simple, model-agnostic, and does not require changes to the fine-tuning procedure.

Existing contrastive intermediate training, however, uses a fixed augmentation policy: every training step draws augmentations from the same distribution. Work in curriculum learning suggests that models learn more effectively when training difficulty increases gradually. For contrastive learning, difficulty is closely tied to augmentation strength: weak augmentations produce positive pairs that are easy to match, whereas strong augmentations produce pairs that share less surface form and force the encoder to capture meaning.

We introduce CurCon, which schedules augmentation strength during contrastive intermediate training. CurCon begins with mild token dropout, gradually introduces synonym replacement and span deletion, and ends with back-translation at full strength. The schedule is controlled by a single hyperparameter, the curriculum length, and adds no inference cost.

Our contributions are as follows:

- We propose CurCon, a curriculum-scheduled contrastive intermediate training method for low-resource text classification.
- We evaluate CurCon against four baselines on four benchmarks with 500 labelled examples each, reporting mean and standard deviation over five random seeds.
- We provide ablations on the curriculum schedule and an analysis of how gains vary with the number of labelled examples.

We evaluate CurCon on SST-2, AG News, TREC, and SUBJ, where it obtains the best average accuracy among the compared methods.

## 2 Related Work

**Low-resource text classification.** Approaches for classification with limited labels include data augmentation such as EDA and back-translation, prompt-based fine-tuning, and semi-supervised learning. UDA enforces consistency between predictions on original and augmented unlabelled examples and remains a strong semi-supervised baseline for text.

**Contrastive representation learning.** Contrastive objectives learn representations by pulling together augmented views of the same instance and pushing apart different instances. SimCSE showed that dropout noise alone can produce strong sentence embeddings. CERT (Fang et al., 2020) performs contrastive self-supervised learning on unlabelled in-domain sentences, using back-translation to create positive pairs, as an intermediate step between pre-training and fine-tuning; the adapted encoder is then fine-tuned on the labelled task. CERT reported consistent improvements over direct fine-tuning on GLUE tasks.

**Curriculum learning.** Curriculum learning orders training examples or tasks from easy to hard. In computer vision, several works have explored increasing augmentation magnitude over the course of training. For text, curricula have mostly been applied to supervised fine-tuning by ordering examples by length or model confidence, rather than to the augmentation policy of a contrastive objective.

## 3 Method

**Training pipeline.** CurCon follows the CERT training pipeline. Starting from a pre-trained BERT-base encoder, we perform contrastive intermediate training on the unlabelled training sentences of the target dataset, and then fine-tune the adapted encoder with a linear classification head and cross-entropy loss on the labelled examples. The contrastive stage uses the InfoNCE loss with in-batch negatives, a projection head with one hidden layer, and cosine similarity scaled by a temperature.

**Augmentation operators.** We use four operators of increasing strength: token dropout (randomly removing 10% of tokens), synonym replacement using WordNet (replacing 15% of content words), span deletion (removing one contiguous span covering 20% of the sentence), and back-translation through German.

**Curriculum schedule.** Let T be the total number of contrastive training steps and L the curriculum length, with L no greater than T. At step t, the curriculum level is c(t) = min(1, t / L). The probability of applying each operator is determined by c(t): token dropout is always available; synonym replacement becomes available when c(t) exceeds 0.25; span deletion when c(t) exceeds 0.5; and back-translation when c(t) exceeds 0.75. When multiple operators are available, one is sampled uniformly for each view. After step L, all operators are available and the policy is fixed. With L set to zero, CurCon reduces to contrastive training with a fixed mixture of all four operators.

**Implementation.** Contrastive training runs for 20,000 steps with a batch size of 128 and the AdamW optimiser. Fine-tuning runs for 10 epochs with early stopping on the validation set. All experiments use a single NVIDIA A100 GPU.

## 4 Experimental Setup

**Datasets.** We use four benchmarks: SST-2 (binary sentiment), AG News (four-way topic classification), TREC (six-way question classification), and SUBJ (binary subjectivity). For each dataset, we sample 500 labelled training examples stratified by class, use the remaining training sentences without labels for the contrastive stage, and report accuracy on the standard test sets. Validation sets contain 200 labelled examples.

**Baselines.** We compare against (1) standard fine-tuning of BERT-base; (2) UDA; (3) CERT; and (4) SimCSE, where the encoder is first trained with the unsupervised SimCSE objective on the unlabelled sentences and then fine-tuned.

**Hyperparameters.** For CurCon, we select the learning rate, contrastive temperature, and curriculum length by grid search over 48 configurations on each validation set. Baselines are trained with the hyperparameters reported in their original papers. All results are averaged over five random seeds.

## 5 Results

**Main results.** Table 1 reports test accuracy.

| Method | SST-2 | AG News | TREC | SUBJ | Average |
|---|---|---|---|---|---|
| Fine-tuning | 81.2 ± 1.1 | 84.3 ± 0.7 | 86.1 ± 1.4 | 88.9 ± 0.8 | 85.1 |
| UDA | 83.0 ± 1.0 | 85.9 ± 0.6 | 88.7 ± 1.1 | 90.1 ± 0.7 | 86.9 |
| SimCSE | 83.5 ± 1.2 | 86.0 ± 0.7 | 89.1 ± 1.0 | 90.4 ± 0.8 | 87.3 |
| CERT | 84.1 ± 0.9 | 86.4 ± 0.8 | 90.2 ± 0.7 | 90.6 ± 0.6 | 87.8 |
| CurCon (ours) | **85.6 ± 0.8** | **87.5 ± 0.6** | **90.8 ± 0.9** | **91.7 ± 0.5** | **88.9** |

CurCon obtains the highest accuracy on all four datasets and improves the average accuracy by 1.1 points over CERT, the strongest baseline, and by 3.8 points over standard fine-tuning. The largest improvements over CERT are on SST-2 (+1.5) and SUBJ (+1.1).

**Ablation.** Table 2 reports average accuracy across the four datasets for variants of CurCon.

| Variant | Average accuracy |
|---|---|
| CurCon (full) | 88.9 |
| Fixed mixture of all operators (L = 0) | 88.1 |
| Reversed curriculum (hard to easy) | 87.6 |
| Without back-translation | 88.0 |
| Without contrastive stage (fine-tuning only) | 85.1 |

Removing the curriculum reduces average accuracy by 0.8 points, and reversing it reduces accuracy by 1.3 points, indicating that the order of augmentation strength matters. Removing back-translation reduces accuracy by 0.9 points.

**Effect of the number of labelled examples.** Table 3 reports average accuracy with 100, 500, and 1,000 labelled examples per dataset.

| Method | 100 | 500 | 1,000 |
|---|---|---|---|
| CERT | 82.4 | 87.8 | 89.9 |
| CurCon | 84.0 | 88.9 | 90.4 |

The improvement of CurCon over CERT decreases from 1.6 points with 100 labelled examples to 0.5 points with 1,000 labelled examples, consistent with the intuition that better representations matter most when labels are scarce.

**Cost.** The curriculum adds no parameters. Because back-translated views are pre-computed, contrastive training with CurCon takes approximately 12% longer than with CERT, due to on-the-fly span deletion and synonym replacement.

## 6 Limitations

Our experiments are limited to English datasets with relatively short texts, and to the BERT-base encoder; we have not evaluated larger encoders or decoder-only models. The augmentation operators depend on external resources, such as WordNet and a machine translation system, whose quality may vary across languages and domains. The curriculum schedule is linear and hand-designed; learned or adaptive schedules may perform better.

## 7 Conclusion

We presented CurCon, a contrastive intermediate training method that gradually increases augmentation strength during the contrastive stage. On four low-resource text classification benchmarks, CurCon improves over standard fine-tuning, UDA, SimCSE, and CERT, with the largest gains when labelled data are scarce. Future work will explore adaptive curricula, multilingual settings, and larger encoders.
