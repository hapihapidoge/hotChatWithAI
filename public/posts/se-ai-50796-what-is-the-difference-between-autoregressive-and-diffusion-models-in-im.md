# What is the difference between autoregressive and diffusion models in image generation?

Curated at: `2026-10-25T04:41:11.490562+00:00`
Model: `Public Q&A`
Author: `programjames`
Tags: `public-q&a, AI Stack Exchange, image-generation`
Source: https://ai.stackexchange.com/questions/50796/what-is-the-difference-between-autoregressive-and-diffusion-models-in-image-gene


## Why It Is Good

- Public Q&A from AI Stack Exchange.
- Question score: 0; answer score: 1.
- The answer was accepted by the question author.
- Viewed 49 times on the source site.

## Question

What is the difference between transformers and autoregressive models in image generation? Are autoregressive models better at photorealism, text rendering and instruction following, given architecture choice and training data?

## Answer

Autoregressive comes from 'auto' + 'regressive', which means to extrapolate from its own outputs. In language models this looks like predicting a word, then using that word as input to predict the next word, and so on. In image models, that looks like predicting a patch of the image, using that patch to predict the next patch, continuing to fill in the image in that manner. Diffusion specifically refers to Langevin diffusion models, but has taken on a more general connotation of any flow model—normalizing flows, rectified flows, flow-matching, flow maps, etc. A diffusion model trains trajectories between datasets, most famously mapping a normal distribution to an image distribution. Autoregression and diffusion are not incompatible. Autoregression is a data architecture, while diffusion is a learning model. Or, to put it another way, autoregression deals with what data you look at, while diffusion deals with how you generate that data. Diffusion language models autoregressively produce chunks of tokens using a language diffusion model. Many video models autoregressively produce frames using image diffusion models. Why not do diffusion on the entire video? Some models do, but quadratic attention scales... quadratically. It becomes very expensive to diffuse on every patch in an entire video, and much cheaper to compress earlier frames in the video, which you can do if you genera...
