# Extracting Contract Rules from Contract Document

Curated at: `2026-09-23T04:45:12.552952+00:00`
Model: `Public Q&A`
Author: `Manish Ranjan`
Tags: `public-q&a, GenAI Stack Exchange, llm, azure, search, json`
Source: https://genai.stackexchange.com/questions/2916/extracting-contract-rules-from-contract-document


## Why It Is Good

- Public Q&A from GenAI Stack Exchange.
- Question score: 0; answer score: 1.
- The answer was accepted by the question author.
- Viewed 41 times on the source site.

## Question

We have a requirement to extract contract specific rules from Contract documents. E.g., The difference between contract start date and contract end date should be minimum 90 days. The contract document is unstructured and can have paragraphs, tables, bulleted list etc. Currently a person is manually extracting these rules and preparing a JSON. We tried to build system prompt to extract rules from contract document. We mentioned keywords like must not, should not etc. to find out the rules from the contract document. It is effective. But, there is some opposition to use keyword based prompt. They want us to use semantic approach to extract rules from a statement, instead of keyword based. We...

## Answer

Don't fine-tune a model. Do use document intelligence for parsing — but that's only step one. The real answer is a structured extraction pipeline with schema-constrained LLM output, not a better prompt. Your two options are actually solving different halves of the problem, and neither is complete alone. Reframing the "Keyword vs Semantic" Debate The opposition to keyword-based extraction is correct, but for a subtler reason than "keywords bad." Keyword matching (must not, should not) fails because rules hide in language that carries no modal keyword at all: "The term shall commence no fewer than 90 days prior to expiration" — obligation, no "must not" "Payment is due within 30 days of invoice" — a rule stated as plain present tense A table row: Notice Period | 60 days — a rule with zero rule-language Semantic extraction means the model recognizes the deontic intent (obligation, prohibition, permission, condition) regardless of surface wording. An LLM already does this well if you prompt it around meaning, not keywords . So your existing approach is 80% there — you just need to reframe the instruction from "find sentences containing X" to "identify every clause that imposes an obligation, prohibition, or constraint." What I'd actually build: 1. Parse with document intelligence , keeping tables, lists, and headings as structure, not flattened text. 2. Chunk by clause/section ,no...
