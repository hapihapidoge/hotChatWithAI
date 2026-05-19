# How accurate are modern AI content detectors?

Curated at: `2026-05-19T05:51:31.549883+00:00`
Model: `Public Q&A`
Author: `Franck Dernoncourt`
Tags: `public-q&a, GenAI Stack Exchange, genai-ecosystem`
Source: https://genai.stackexchange.com/questions/2781/how-accurate-are-modern-ai-content-detectors


## Why It Is Good

- Public Q&A from GenAI Stack Exchange.
- Question score: 1; answer score: 1.
- The answer was accepted by the question author.
- Viewed 30 times on the source site.

## Question

Is there a report on how accurate are modern (2024 and beyond) AI-generated content detectors?

## Answer

It's an entire field of research. A few pointers: 2024 papers with many citations: MAGE. Li et al., ACL 2024. https://arxiv.org/abs/2305.13242 . 447k generations from 27 LLMs across 10 domains; foundational in-the-wild generalization benchmark. RAID. Dugan et al., ACL 2024. https://arxiv.org/abs/2405.07940 . 6.2M-generation adversarial benchmark; "99% accurate" detectors collapse under attacks/unseen generators. M4GT-Bench. Wang et al., ACL 2024. https://arxiv.org/abs/2402.11175 . Multilingual, multi-domain, multi-generator benchmark with span-level boundary detection (basis of SemEval-2024 Task 8). Perkins et al., 2024 ("GenAI Detection Tools, Adversarial Techniques..."). Int. J. Ed. Tech. in Higher Ed. https://arxiv.org/abs/2403.19148 . Six commercial detectors at 39.5% baseline accuracy, dropping 17.4% under simple adversarial manipulation. DF40. Yan et al., NeurIPS 2024 D&B. https://arxiv.org/abs/2406.13495 . 40 distinct deepfake generation techniques across face-swap/reenactment/synthesis/editing; cross-generator generalization benchmark. DetectRL. Wu et al., NeurIPS 2024 D&B. https://arxiv.org/abs/2410.23746 . Real-world adversarial benchmark in abuse-prone domains; SOTA detectors underperform under prompt attacks, paraphrasing, perturbations. More recent papers from 2025–2026: Deepfake-Eval-2024. Chandra et al., TrueMedia.org/UW, March 2025. https://arxiv.org/abs/2503.0...
