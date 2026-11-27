# Are PRNGs used for weight initialization during model training?

Curated at: `2026-11-27T08:33:05.706894+00:00`
Model: `Public Q&A`
Author: `Poly Trendy`
Tags: `public-q&a, AI Stack Exchange, training`
Source: https://ai.stackexchange.com/questions/50854/are-prngs-used-for-weight-initialization-during-model-training


## Why It Is Good

- Public Q&A from AI Stack Exchange.
- Question score: 1; answer score: 1.
- The answer was accepted by the question author.
- Viewed 60 times on the source site.

## Question

Are PRNGs (pseudorandom number generators) used for weight initialization during model training? If yes, do they use standard algorithms like WELL, Mersenne Twister or Xorshift, or they use specialized algorithms?

## Answer

Yes, they are. Weight initialization just draws from the framework's default random number generator, so the answer depends on which framework and device you use. In PyTorch the default CPU generator is Mersenne Twister (mt19937), while on CUDA it is Philox (Philox4x32-10). JAX uses Threefry by default, and TensorFlow's stateless random ops use Philox or Threefry. The exact generator hardly affects training quality, since any decent PRNG gives samples that are statistically fine for initialization. What matters more is the seed: fixing it (torch.manual_seed, jax.random.PRNGKey) is what makes an initialization reproducible, and results can still differ between CPU and GPU because they use different generators. Drafted with help from an AI model (Claude).
