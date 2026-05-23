# How to Evaluate my RAG System using Local / free tier API model

Curated at: `2026-05-23T04:07:54.031579+00:00`
Model: `Public Q&A`
Author: `Arnaud`
Tags: `public-q&a, Stack Overflow, machine-learning, deep-learning, artificial-intelligence, evaluation, rag`
Source: https://stackoverflow.com/questions/79939816/how-to-evaluate-my-rag-system-using-local-free-tier-api-model


## Why It Is Good

- Public Q&A from Stack Overflow.
- Question score: 1; answer score: 1.
- Viewed 116 times on the source site.

## Question

I have build a self-evaluating RAG System now i want to evaluate it so i can know what my system performance for that i used DeeEval framework but the thing is i don’t have OpenAI API key as i’m broke so i’m using free tier API from Groq/Cerebra’s or local model but the thing is local model like llama 3.1 8b model is giving invalid json and keep failing like out of 25 question it’s failing on 15-19 question and when i use free tier api from cerebra’s in DeepEval it’s Rate limit just max out as DeevEval generate 3-4 response per question ,

## Answer

you can use the Open source project vllm. https://github.com/vllm-project/vllm vLLM enables you to serve and infer from your local model and provide you an OpenAI compatible interface. once you setup vllm you can use - this will be provide you an open ai interface to your model. [code omitted] you can then call the OpenAI Completions API with vLLM : [code omitted] Since you are already using a local model, I assume you have enough resources to run it. more details on local serving : https://docs.vllm.ai/en/stable/getting_started/quickstart/
