# Claude over multiple Visual Studio solutions

Curated at: `2026-09-06T04:38:53.584458+00:00`
Model: `Public Q&A`
Author: `ReflectYourCharacter`
Tags: `public-q&a, GenAI Stack Exchange, llm, claude, github-copilot, visual-studio`
Source: https://genai.stackexchange.com/questions/2903/claude-over-multiple-visual-studio-solutions


## Why It Is Good

- Public Q&A from GenAI Stack Exchange.
- Question score: 1; answer score: 2.
- Viewed 418 times on the source site.

## Question

In my company, we regularly use GitHub Copilot for development purposes. For historical reasons, our code is distributed over multiple Visual Studio solutions, each of them holding multiple projects. Due to Copilot limitations, there is one Claude per solution (you can imagine that "Claude" refers to "Claude Sonnet" or "Claude Opus", the LLMs mostly used by Copilot). It happens more and more that issues are cross-solution, which means that Claude1 says I need to ask Claude2, and Claude2 just answers to ask Claude1. Until now, I have created temporary solutions in which I have merged the projects from the solutions, relevant to my problems, but this is just a temporary solution of this probl...

## Answer

If I understood your question correctly, then one possible solution is to make the relevant projects/repos available in a shared workspace or Copilot Space, instead of temporarily merging the solutions. This way, you can use multiple repositories as context, which, in my opinion, makes it much more future-proof for cross-solution questions. Sources: About GitHub Copilot Spaces Collaborating with others using GitHub Copilot Spaces Speeding up development work with GitHub Copilot Spaces Introducing Copilot Spaces: A new way to work with code and context Your New Context Hub for AI Development
