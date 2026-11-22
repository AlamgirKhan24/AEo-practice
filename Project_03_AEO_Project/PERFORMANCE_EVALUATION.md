# Performance evaluation and improvement plan

## Product usefulness KPIs

- Audit completion rate: audits with evidence on at least 80% of in-scope criteria ÷ audits started.
- Evidence completeness: assessed findings with date + source + recommendation ÷ assessed findings.
- Time to first prioritized recommendation, measured in user sessions.
- Reviewer agreement on a shared sample (e.g., weighted kappa or simple agreement) before/after rubric calibration.
- Issue verification rate: recommendations rechecked with evidence after implementation.
- False-positive rate found in expert QA.
- Export success and data portability checks.

Do not set target values until usability testing establishes a baseline. The current prototype has no telemetry and this case study includes no user study or production usage data.

## SEO/visibility evaluation KPIs

For a real client, establish a baseline and monitor: Search Console/Bing clicks and impressions by page/query; eligible rich-result impressions where reported; index coverage of canonical priority URLs; non-brand question-query discovery; referral and conversion data where privacy-compliant; and manually sampled answer-engine citation observations with exact query/platform/date/evidence. Report changes alongside seasonality, algorithm releases, site changes, and query-set changes. Do not equate correlation with causality.

## Improvement backlog

1. Add accessible CSV import/export and schema-aware audit templates.
2. Add confidence and reviewer fields to every finding.
3. Support repeat-run prompt comparison and response screenshot attachments.
4. Add an optional authorized crawler adapter with rate limits, robots-aware controls, and clear provenance.
5. Add role-based access, encryption, and multi-user storage only if moving beyond local prototype.
6. Conduct moderated usability testing with consultants and small-site owners; revise labels/rubric from observed confusion.
7. Evaluate score stability by having two auditors rate the same pages and compare results.

## Current evaluation

The prototype's arithmetic and local JSON parsing are tested as described in `TESTING.md`. No external site audit or AI platform test was performed; no visibility or improvement results are claimed.
