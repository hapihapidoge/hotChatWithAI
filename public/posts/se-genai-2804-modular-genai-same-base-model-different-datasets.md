# 'Modular' genAI: same base model, different datasets

Curated at: `2026-06-17T05:16:46.548562+00:00`
Model: `Public Q&A`
Author: `Franck Dernoncourt`
Tags: `public-q&a, GenAI Stack Exchange, fine-tuning, rag`
Source: https://genai.stackexchange.com/questions/2804/modular-genai-same-base-model-different-datasets


## Why It Is Good

- Public Q&A from GenAI Stack Exchange.
- Question score: 2; answer score: 1.
- Viewed 17 times on the source site.

## Question

I have discovered the power of Small Language Models, whose strength is their specialised dataset which can allow them to outperform generic LLMs in a specific field, as well as consume much smaller amounts of energy and computational resources. All the Hugging Face quantised models I've downloaded still occupy ~5GB each, which adds up when going for the 1 LM per job type system. Is this inevitable or can a generic genAI still perform well with a dataset it can query on the fly? The closest I've got to is using a LightRAG MCP server, but I feel like if it hasn't been previously trained on the material it will be slow, clunky and inaccurate nevertheless - still, I'd be curious to know if sep...

## Answer

Totally depends on your use case, tolerable model size and required model quality. RAG, LORA adapters and other light techniques to adapt a base model are useful for some but not all tasks.
