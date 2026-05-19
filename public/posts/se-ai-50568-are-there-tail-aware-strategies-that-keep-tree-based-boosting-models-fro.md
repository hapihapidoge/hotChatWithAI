# Are there tail-aware strategies that keep tree-based boosting models from underpredicting extreme values at the tails of data?

Curated at: `2026-05-19T05:31:08.641659+00:00`
Model: `Public Q&A`
Author: `Stewie pixel`
Tags: `public-q&a, AI Stack Exchange, machine-learning, regression, gradient, gradient-boosting`
Source: https://ai.stackexchange.com/questions/50568/are-there-tail-aware-strategies-that-keep-tree-based-boosting-models-from-underp


## Why It Is Good

- Public Q&A from AI Stack Exchange.
- Question score: 1; answer score: 2.
- Viewed 35 times on the source site.

## Question

I’m facing a regression problem where rare extreme values dominate the real objective, and all tested models systematically underpredict them. Inputs are window statistical parameters of operational signals; the target is a pair of ordered global extremes per fixed window, later post‑processed into fatigue damage (highly nonlinear in amplitude). Histogram‑based gradient boosting, XGBoost/LightGBM, and linear AR models all fit the bulk distribution well (good RMSE/R²) but consistently shrink the upper tail, even after aggressive sample weighting (range‑based, power‑law, sequence‑aware), custom loss functions emphasizing tail errors (log‑space histogram loss, explicit underprediction penaltie...

## Answer

Gradient boosting minimizes average loss across the distribution. Even with sample weights, the model's leaf values are means of samples in that leaf, so that means a leaf containing 95% normal values and 5% extremes will always predict something closer to the mean. So you may consider these Reframe as an Extreme Value Theory (EVT) problem Instead of regressing the raw target, fit the tail distribution using a Generalized Extreme Value (GEV) or Generalized Pareto Distribution (GPD). Your model predicts the distribution parameters (location, scale, shape), and you sample or compute expected maxima from that. You can use the scipy.stats.genextreme and pyextremes libraries in python. Quantile regression targeting the upper tail Drop RMSE entirely. Train separate models for q=0.90, 0.95, 0.99 quantiles using pinball loss. Your fatigue damage estimate then uses the high quantile prediction rather than the mean. LightGBM has native quantile support (objective='quantile'). Two-stage model: bulk + extreme classifier Stage 1: binary classifier "is this window likely to contain an extreme?" Stage 2a: standard regressor for normal windows Stage 2b: separate regressor trained only on windows with confirmed extremes Are your input features themselves extreme during peak-stress windows, or are the extremes dynamically generated? If the extreme isn't visible in the features, no model can pre...
