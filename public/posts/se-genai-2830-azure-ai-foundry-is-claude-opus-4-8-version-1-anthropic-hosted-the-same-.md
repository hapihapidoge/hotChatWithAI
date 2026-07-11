# Azure AI Foundry: is claude-opus-4-8 "version 1" (Anthropic-hosted) the same model as "version 2" (Azure-hosted)?

Curated at: `2026-07-11T03:42:33.872570+00:00`
Model: `Public Q&A`
Author: `Franck Dernoncourt`
Tags: `public-q&a, GenAI Stack Exchange, claude, azure, anthropic`
Source: https://genai.stackexchange.com/questions/2830/azure-ai-foundry-is-claude-opus-4-8-version-1-anthropic-hosted-the-same-mod


## Why It Is Good

- Public Q&A from GenAI Stack Exchange.
- Question score: 0; answer score: 0.
- The answer was accepted by the question author.
- Viewed 23 times on the source site.

## Question

When deploying claude-opus-4-8 in Azure AI Foundry (Deployment type: Global Standard), the Model version dropdown offers two options: 2 : Hosted on Azure 1 : Hosted on Anthropic infrastructure Both are labeled claude-opus-4-8 , so the model ID is identical. I want to understand what the version number actually distinguishes here. Is it: The same underlying model (same weights, same capabilities, same quality), differing only in where inference physically runs? or Different model builds/behavior in any way that would affect output quality, context window, or supported parameters?

## Answer

From Azure tech support (private correspondence): Both options use the **same base model (Claude Opus 4.8). Version 2 of Claude Opus 4.8 is hosted on Azure infrastructure. Microsoft Foundry Claude models on Azure infrastructure have full Azure data residency for inference processing. Version 2 supports both Global Standard and US data Zone deployment types. Version 2 currently supports core Messages API features including tool calls and prompt caching. If you need additional features including structured outputs, Web Search, and Files, you can use Version 1 which is hosted on Anthropic infrastructure. We will be adding those API capabilities to Version 2 in the coming months. You can learn more about API feature differences .
