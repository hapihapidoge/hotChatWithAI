# Can Federated IID and Non-IID training for datasets with various censoring rates be simplified to a single batch size?

Curated at: `2026-05-20T04:36:49.427119+00:00`
Model: `Public Q&A`
Author: `Stewie pixel`
Tags: `public-q&a, AI Stack Exchange, deep-learning, batch-size, benchmarks, federated-learning, survival`
Source: https://ai.stackexchange.com/questions/50584/can-federated-iid-and-non-iid-training-for-datasets-with-various-censoring-rates


## Why It Is Good

- Public Q&A from AI Stack Exchange.
- Question score: 0; answer score: 2.
- The answer was accepted by the question author.
- Viewed 25 times on the source site.

## Question

I am working with a benchmark comparison of federated survival models. My plan is to experiment with these models on centralized, IID and non-IID settings. I have already distributed global training, validation and test data among 5 clients. Each client’s data consists of 5 folds. 3 folds are used to train the model, 1 fold is used as a validation set and another fold is used as a test fold. For global Learning, I train the survival model using this process: i) Calculate forward pass on a batch ii) Calculate loss and get gradient for that batch iii) Apply the gradients to update the network iv) Repeat For Federated Learning (FL), I am using this process: i) Use client devices/data to calcul...

## Answer

Your results are actually not wrong, but the assumption that centralized > IID > Non-IID is a heuristic, not a law. Maybe these are the cases: 1. Implicit Regularization from Federated Averaging Each federated round averages gradients across 5 clients, which acts like an ensemble effect. This can reduce overfitting, especially on small datasets (3241 rows is not large for survival analysis). 2. Your Batch Size is Likely Too Large for Centralized With 3241 samples, 3 training folds ≈ ~1944 samples. A batch size of 64 means only ~30 gradient updates per epoch. In federated settings, each client trains on ~389 samples with batch 64, giving ~6 updates per client per round — but aggregated across 5 clients, the effective gradient diversity is higher. 3. Early Stopping Asymmetry Centralized: 25-epoch patience on the full model Federated: 25-epoch patience at both server and client level The federated model gets two regularization signals, which can be beneficial. 4. Censoring Rate Interaction (38.72%) The UnempDur dataset has ~38.72% censored observations. Federated splitting can accidentally create better-stratified censoring distributions per client, improving the C-Index signal. General Rules: Batch size ∝ local dataset size : aim for ~10–20 batches per epoch minimum For survival models (e.g., Cox PH loss), very small batches (<8) destabilize the risk set calculation Non-IID clie...
