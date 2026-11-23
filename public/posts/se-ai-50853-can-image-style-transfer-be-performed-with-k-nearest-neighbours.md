# Can image style transfer be performed with k-nearest neighbours?

Curated at: `2026-11-23T07:38:27.542712+00:00`
Model: `Public Q&A`
Author: `chessprogrammer`
Tags: `public-q&a, AI Stack Exchange, style-transfer, k-nearest-neighbors`
Source: https://ai.stackexchange.com/questions/50853/can-image-style-transfer-be-performed-with-k-nearest-neighbours


## Why It Is Good

- Public Q&A from AI Stack Exchange.
- Question score: 1; answer score: 1.
- The answer was accepted by the question author.
- Viewed 47 times on the source site.

## Question

Can image style transfer be performed with k-nearest neighbours, using a set of multiple reference images in a RAG-like architecture and an input image, without specific finetuning on particular styles?

## Answer

Yes it can! Here is an approach on this topic from 2022: "Neural Neighbor Style Transfer" https://arxiv.org/pdf/2203.13215 And a more recent work building off of it: "Image Realism Enhancement Method Based on Improved Neural Neighbor Style Transfer" https://ieeexplore.ieee.org/document/10865483 Related to the idea of Nearest Neighbors, this work uses neighbors to form a graph and apply a GNN, and is also very related: "Learning Graph Neural Networks for Image Style Transfer" https://link.springer.com/chapter/10.1007/978-3-031-20071-7_7
