# How can I configure Claude or Slack so that it doesn't add "Sent using @Claude" when sending a message on Slack using Claude Desktop?

Curated at: `2026-08-14T02:45:50.844506+00:00`
Model: `Public Q&A`
Author: `ReflectYourCharacter`
Tags: `public-q&a, GenAI Stack Exchange, claude, claude-desktop, slack`
Source: https://genai.stackexchange.com/questions/2849/how-can-i-configure-claude-or-slack-so-that-it-doesnt-add-sent-using-claude


## Why It Is Good

- Public Q&A from GenAI Stack Exchange.
- Question score: 4; answer score: 5.
- Viewed 972 times on the source site.

## Question

How can I configure Claude or Slack so that it doesn't add "Sent using @Claude" when sending a message on Slack using Claude Desktop?

## Answer

It appears that there is currently no official setting or configuration in Claude Desktop or Slack to remove the footer 'Sent using @Claude' (or 'Sent using Claude'). Problem Messages sent via the Slack MCP server include a "Sent using Claude" footer that cannot be disabled. For users and organizations with policies against AI attribution in communications, there is no way to opt out of this branding. ... Feature: Add option to disable 'Sent using Claude' message footer #25 This diagram visually illustrates the exact data flow and security boundaries when you use the Claude tag in Slack. It also explains, in part, why you cannot disable the 'Sent using Claude' message locally, all requests are processed through external servers, and this is currently the intended behavior. Inside Claude Tag: How Anthropic’s Slack-Native Agent Actually Works
