# Does Codex use quota while waiting for tests or CI?

Curated at: `2026-10-31T05:40:54.452117+00:00`
Model: `Public Q&A`
Author: `JBallin`
Tags: `public-q&a, GenAI Stack Exchange, openai, quota, codex`
Source: https://genai.stackexchange.com/questions/2958/does-codex-use-quota-while-waiting-for-tests-or-ci


## Why It Is Good

- Public Q&A from GenAI Stack Exchange.
- Question score: 1; answer score: 2.
- The answer was accepted by the question author.
- Viewed 40 times on the source site.

## Question

Does time spent waiting for commands, tests, or CI count toward my ChatGPT plan’s Codex usage limit?

## Answer

Not by elapsed time alone. OpenAI Support states that Codex usage is not based on wall-clock time. Its usage guidance lists factors such as the model, task complexity, context, and tools. If Codex invokes the model to check progress or process test output, that is additional model activity, not merely waiting. I would expect that activity to consume usage even while a test or CI job is still running. The sources don't specifically explain progress checks during tests or CI. That part is my interpretation of the general usage guidance, rather than an explicitly documented rule for this scenario.
