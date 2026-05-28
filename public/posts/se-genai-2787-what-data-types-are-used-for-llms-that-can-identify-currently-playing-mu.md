# What data types are used for LLMs that can identify currently playing music?

Curated at: `2026-05-28T04:39:37.987863+00:00`
Model: `Public Q&A`
Author: `Mario`
Tags: `public-q&a, GenAI Stack Exchange, llm, training`
Source: https://genai.stackexchange.com/questions/2787/what-data-types-are-used-for-llms-that-can-identify-currently-playing-music


## Why It Is Good

- Public Q&A from GenAI Stack Exchange.
- Question score: 1; answer score: 0.
- The answer was accepted by the question author.
- Viewed 37 times on the source site.

## Question

Do LLMs with music identification support use acoustic fingerprints used in traditional music identifiers (Shazam and the like), or music files that get processed (like on an transformer encoder), or something else as data for training?

## Answer

It's not the best answer, little searching about the process, I found this GH repo: Song Identification Using Audio Fingerprinting and Deep Learning , so you could clone and try output; however, you can have a look at this paper about process: Robust Neural Audio Fingerprinting using Music Foundation Models "Figure 1:The contrastive learning framework for neural audio fingerprinting. Original and augmented audio (e.g., audio with noise, reverb, time/pitch changes) are passed through a shared encoder, followed by a projection head. The resulting embeddings (z and z′) are optimized using a contrastive loss to encourage invariance to audio degradations."
