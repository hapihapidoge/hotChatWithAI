# LLM always returns 17 when I ask it 'Give me a number between 1 and 30'

Curated at: `2026-10-08T06:04:12.478868+00:00`
Model: `Public Q&A`
Author: `Toph`
Tags: `public-q&a, AI Stack Exchange, large-language-models, chatgpt`
Source: https://ai.stackexchange.com/questions/50762/llm-always-returns-17-when-i-ask-it-give-me-a-number-between-1-and-30


## Why It Is Good

- Public Q&A from AI Stack Exchange.
- Question score: 12; answer score: 24.
- The answer was accepted by the question author.
- Viewed 3086 times on the source site.

## Question

I am using Chatgpt and Gemini, whenever I ask it the question 'Give me a number between 1 and 30' it always responds with 17. I thought LLM were non-deterministic. Is there a core reason this number is chosen every time? By whenever I mean 15 different times across 3 devices. All of them returned 17. I have not done a larger test.

## Answer

I tried this on my local copy of llama3:text and I didn't get this result. It gives a variety of different numbers, as you would expect. Closer examination shows that they're not all equally probable. Using the prompt " Here is a randomly selected number between 1 and 30: " (note the space at the end), I got the following probabilities for the next token: Token probability 15 0.048704812979863 17 0.040197129398325 10 0.039508919263325 12 0.03893707634181 14 0.036249346091792 23 0.0360743526663 5 0.035161825266541 20 0.034756014022311 7 0.033883426336952 13 0.033436718901706 16 0.033094406498486 21 0.032292709696735 22 0.030970127733823 2 0.029842584788389 8 0.029177092645267 11 0.02904162688793 3 0.027582203456746 4 0.027465652116896 24 0.026570656603254 other (ollama only shows the top 20 results) 0.357053318303552 Note that ideally we'd expect all the answers between 1 and 30 to show up with probability 0.033333. So llama3:text is showing a preference for "more random" numbers like 15 or 17. I suppose your ChatGPT tests are showing an even stronger preference. (Here's the command I used if you want to try it yourself. You need a version of ollama that supports the "logprobs" argument, which I only just found out about and I'm enjoying playing with. Run an ollama server and then type this into the Windows Powershell command prompt: [code omitted] ... the results are log-proba...
