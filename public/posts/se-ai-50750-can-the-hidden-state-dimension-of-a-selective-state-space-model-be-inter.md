# Can the hidden-state dimension of a selective state-space model be interpreted as an effective tensor-network bond dimension?

Curated at: `2026-10-01T05:54:07.090418+00:00`
Model: `Public Q&A`
Author: `Enzo Carpanetti`
Tags: `public-q&a, AI Stack Exchange, neural-networks, machine-learning, deep-learning, computational-learning-theory, representation-learning`
Source: https://ai.stackexchange.com/questions/50750/can-the-hidden-state-dimension-of-a-selective-state-space-model-be-interpreted-a


## Why It Is Good

- Public Q&A from AI Stack Exchange.
- Question score: 1; answer score: 1.
- Viewed 42 times on the source site.

## Question

I am trying to understand whether there is a precise tensor-network interpretation of the state dimension in modern selective state-space models such as Mamba/SSD. Consider a selective state-space update $$ h_t = A(x_t)h_{t-1} + b(x_t). $$ By augmenting the state, $$ z_t = \begin{pmatrix} h_t\\ 1 \end{pmatrix}, $$ the recurrence can be written as $$ z_t = M(x_t)z_{t-1}, $$ and therefore $$ z_T = M(x_T)M(x_{T-1})\cdots M(x_1)z_0. $$ This looks structurally similar to a chain of local tensor contractions. There are known connections between recurrent neural networks and tensor networks, and tensor-train methods have also been applied to state-space models. What I have not been able to determi...

## Answer

Good question, I think there is no formal named theorem that explicitly connects selective SSMs to tensor networks under that exact terminology. Input-dependent parameters dynamically construct local site tensors per token, but state propagation across any temporal cut remains a sequential contraction operating strictly within an (N + 1)-dimensional vector space; ergo, selectivity grants dynamic flexibility in choosing which correlation channels to activate, but it cannot physically expand the dimensionality of the vector space itself; only stacking multiple selective layers with non-linearities and channel mixing transforms the architecture into a deep tensor network where global correlation capacity can exceed N.
