# Instagram Growth Analyst

A Codex skill for diagnosing Instagram post performance, auditing Reels, comparing public competitor patterns, and turning evidence into better content experiments.

It does **not** promise virality or claim access to Instagram's private ranking algorithm. It works with the evidence you provide—Insights screenshots or exports, post history, media, captions, and public competitor pages—and clearly separates facts from hypotheses.

## What it does

- Classifies a post as breakout, promising, typical, underperforming, or insufficient evidence.
- Compares performance with the creator's own format-appropriate baseline.
- Audits the stop, hook, hold, reward, share, and conversion stages.
- Examines public competitor patterns without copying their creative work.
- Produces prioritized edits, experiments, hooks, and content concepts.
- Includes a dependency-free CSV baseline analyzer.

## Install

Copy the `instagram-growth-analyst` directory into your Codex skills directory, or clone your GitHub repository URL there:

```bash
git clone <repository-url> ~/.codex/skills/instagram-growth-analyst
```

Restart Codex if needed so it discovers the new skill. Invoke it explicitly with `$instagram-growth-analyst`, or ask naturally for an Instagram post-performance diagnosis.

## Example prompts

```text
Use $instagram-growth-analyst to review this Reel and these Insights screenshots.
Tell me whether it is outperforming my normal posts, why, and what to test next.
```

```text
Use $instagram-growth-analyst to compare my last 20 Reels with these five competitor accounts.
Find repeatable content gaps and propose five original experiments.
```

## CSV analysis

The optional helper compares a selected post with the median of historical posts of the same format:

```bash
python scripts/analyze_metrics.py assets/example-posts.csv --post-id reel-current
```

Required column: `post_id`. Recommended columns are shown in [`assets/example-posts.csv`](assets/example-posts.csv). Missing metrics are skipped. The helper produces descriptive ratios, not a viral prediction.

## What to provide

Best results come from:

- the Reel or post media, cover, caption, publication time, and age;
- Instagram Insights exports or screenshots;
- 10–20 or more comparable historical posts;
- the audience, niche, and desired outcome; and
- competitor handles or links when comparison is requested.

The skill can still perform a creative-only audit with less data, but it will lower its confidence and label performance conclusions as hypotheses.

## Repository structure

```text
instagram-growth-analyst/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── creative-audit.md
│   ├── competitor-research.md
│   └── metrics-and-scoring.md
├── scripts/analyze_metrics.py
└── assets/example-posts.csv
```

## Privacy and responsible use

Remove personal or sensitive audience information before sharing files. Use authorized exports for private account data. Public competitor research should cite its sources and should extract patterns—not reproduce someone else's scripts, branding, or creative expression.

## Roadmap

- Optional authorized Instagram Graph API connector
- Age-matched performance snapshots and momentum curves
- Reusable visual report template
- Multilingual hook and caption analysis

Contributions and issue reports are welcome. Please include a minimal, anonymized example and the outcome you expected.

## License

MIT. See [`LICENSE`](LICENSE).
