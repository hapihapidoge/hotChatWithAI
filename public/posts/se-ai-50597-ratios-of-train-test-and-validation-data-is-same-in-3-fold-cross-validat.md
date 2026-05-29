# ratios of train, test and validation data is same in 3-fold cross validation

Curated at: `2026-05-29T04:43:03.530418+00:00`
Model: `Public Q&A`
Author: `treeoid`
Tags: `public-q&a, AI Stack Exchange, machine-learning, comparison, cross-validation, validation-datasets, k-fold-cv`
Source: https://ai.stackexchange.com/questions/50597/ratios-of-train-test-and-validation-data-is-same-in-3-fold-cross-validation


## Why It Is Good

- Public Q&A from AI Stack Exchange.
- Question score: 0; answer score: 1.
- The answer was accepted by the question author.
- Viewed 40 times on the source site.

## Question

In Stratified K Fold Cross Validation, we use 1 fold as validation, 1 fold as evaluation, and remaining 3 folds for training data. This process is represented in the following figure: However, in my experiments, the number of samples are very less and that is why, my supervisor suggested me to perform 3 fold cross validation. As per my understanding, in case of 3 folds, 1 fold will be used as training, 1 will be used as test, and 1 fold will be used validation fold. However, this is absolutely ridiculous as the number of samples in train and validation folds are same. Is there any issue in my understanding? How can I correctly implement 3-fold cross validation for small sampled low dimensio...

## Answer

After reading several papers and blogs, I think, I have got the answer of my question. Now, I am sharing it for future reference. For 3-fold cross-validation, usually 2 folds are considered as training set and remaining 1 fold is treated as test set. This process is illustrated in this figure: In case of validation set, we can divide training set into train and validation set in 80:20 ratio. [code omitted] Full flow will be in this outlined steps: [code omitted] Then we will report average test performance over 3 folds as final result. Full implementation code is provided here: [code omitted] The shuffle=True flag in StratifiedKFold will create reproducible folds only if random_state is fixed. Setting Same folds every run? shuffle=False YES shuffle=True + fixed random_state YES shuffle=True + no random_state NO
