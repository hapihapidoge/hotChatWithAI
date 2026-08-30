# How can transformers.generate() select a token outside top_k?

Curated at: `2026-08-30T05:24:34.063152+00:00`
Model: `Public Q&A`
Author: `Amadan`
Tags: `public-q&a, GenAI Stack Exchange, transformers, token, token-usage`
Source: https://genai.stackexchange.com/questions/2892/how-can-transformers-generate-select-a-token-outside-top-k


## Why It Is Good

- Public Q&A from GenAI Stack Exchange.
- Question score: 2; answer score: 2.
- The answer was accepted by the question author.
- Viewed 57 times on the source site.

## Question

I was trying to isolate an issue I had in a larger program. Here are the relevant bits. [code omitted] The output comes out as Wow, look at those mountains! That cloud per壳ched atop Table Mountain like a hat[...] It does obey the (fully English) text prompt, and does describe the image input. Except... there is "壳" stuck inside an English word. This also happens with other seeds, other models, other hardware... Even switching to Pipeline , with the same seed, results in the same output. Even if I switch to a non-Qwen model. (Not specifically "壳"; sometimes it is Thai, sometimes Arabic, sometimes a code token like setLogger ...) Investigating this specific output, I determined that the gener...

## Answer

It seems the cause is a bug in the MPS implementation of torch.multinomial . It was reported as issue #192577 and apparently resolved in commit 9810655 , though it is not yet in a released pytorch version. The garbage token we observed on CUDA was found to be unrelated: the token had a minuscule but non-zero probability. We did not manage to elicit a zero-probability choice behaviour there. This makes our confirmed bug match the reported MPS issue exactly.
