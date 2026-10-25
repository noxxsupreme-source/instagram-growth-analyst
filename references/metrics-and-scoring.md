# Metrics and scoring

Use this reference for performance diagnosis. Metrics differ by format and account, so compare like with like and show the baseline behind every conclusion.

## Evidence hierarchy

Prefer, in order:

1. authorized Instagram Insights exports or clearly labeled screenshots;
2. user-maintained post history with definitions and timestamps;
3. public counts captured with URLs and dates; and
4. generic benchmarks only when an authoritative, current source is cited and the limitation is explicit.

## Core calculations

For a metric `x`, calculate `current x / median x for comparable historical posts`. Comparable means the same format and, when possible, similar post age. Use median absolute deviation or percentile ranges when enough history exists; otherwise avoid false precision.

Useful signals include:

- **Momentum:** reach or views relative to baseline and change in growth rate over time.
- **Retention:** average watch time divided by video duration, completion rate, and early drop-off when available.
- **Shareability:** shares or sends per reached account.
- **Save value:** saves per reached account.
- **Audience expansion:** non-follower reach divided by total reach.
- **Conversion:** follows, profile visits, leads, or sales per reached account, depending on the goal.
- **Engagement quality:** prioritize shares, saves, meaningful comments, and conversions over likes alone.

Never reconstruct missing reach or unique viewers from plays. Do not compare a 2-hour-old post with lifetime totals from older posts without age-matched snapshots.

## Verdict language

Use account-relative ratios as descriptive signals, not universal scientific thresholds:

- **Breakout:** several important goal-aligned signals are substantially above baseline and distribution is still accelerating.
- **Promising:** early signals are above baseline, but age or sample size limits confidence.
- **Typical:** performance remains inside the account's normal range.
- **Underperforming:** multiple relevant signals are below baseline after a meaningful observation window.
- **Insufficient evidence:** no defensible baseline, ambiguous definitions, or too little elapsed time.

Always disclose which metrics drive the label. A post with strong reach but weak conversion may be a reach success and a business-goal failure at the same time.

## Confidence

- **High:** reliable Insights plus an age- and format-matched history.
- **Medium:** useful metrics with a small, imperfect, or non-age-matched baseline.
- **Low:** creative-only review, public counters, screenshots with missing definitions, or very young content.

The included script uses simple ratios and deliberately does not calculate a universal “viral score.”
