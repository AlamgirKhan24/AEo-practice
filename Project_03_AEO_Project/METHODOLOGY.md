# AEO audit methodology and scoring framework

## Audit protocol

1. Agree scope, geography, language, important conversions, access, and representative URL set.
2. Record baseline period and source access. Separate public observations, client-supplied data, and recommendations.
3. Select a representative sample: homepage, key service/product pages, category pages, editorial answers, policy/about pages, and templates. Include priority URLs and a random sample.
4. Inspect technical discoverability using authorized crawlers and search-console evidence. A page rendering in a browser does not prove that it is indexed.
5. Review answer readiness and source credibility against the rubric. Save URL, date, screenshot/export, and exact evidence for every non-neutral rating.
6. Test query/prompt set consistently across answer platforms. Log exact wording, engine/version if available, market, language, date, result, cited URL and screenshot. Repeat because answers vary.
7. Prioritize recommendations by user harm/opportunity, reach, confidence, effort, and dependency. Do not infer citations from general SEO scores.
8. Re-run after changes on a matched sample and compare like with like.

## Criteria and weights

| Category | Weight | Criteria (each equally divided within category) |
|---|---:|---|
| Content clarity and completeness | 25 | Direct answer; clear headings; evidence and detail; freshness; unique usefulness |
| Question coverage | 15 | Real user questions; intent mapping; concise answers; related journey coverage |
| Technical discoverability | 20 | Crawl access; index/canonical signals; sitemap/internal links; rendering/mobile; performance/accessibility |
| Structured data | 10 | Syntax/eligibility; visible-data parity; correct entity/offer; breadcrumbs/identity |
| Trust and credibility | 20 | Named expertise/accountability; primary sources; transparent methods; business/contact/policies; review/data provenance |
| Measurement readiness | 10 | Baseline/analytics; repeatable query set; evidence retention; change log/reporting |

AI answer mentions/citations are deliberately excluded from readiness scoring. They are a separate descriptive signal, due to volatile responses, platform variation, personalization, and limited sampling. This separation aligns with Google's current guidance: its AI features use the same SEO fundamentals, have no extra technical/schema requirement, and eligible appearance is not guaranteed. Google reports AI-feature traffic within the overall Web search performance report rather than offering a complete citation-level score in this rubric.

## Rating scale

- **0 — Absent/broken:** checked and evidence shows the requirement is missing or materially fails.
- **1 — Major gap:** weak, inconsistent, or misleading; substantial remediation required.
- **2 — Partial:** present but incomplete or inconsistent across the reviewed sample.
- **3 — Good:** clear and generally consistent; small improvements remain.
- **4 — Strong:** complete, accurate, accessible, maintained, and supported by evidence for the reviewed sample.
- **Not assessed:** insufficient evidence or not checked. Excluded from score, included in coverage denominator.

Category score = mean assessed rating ÷ 4 × 100. Overall readiness = sum(category score × category weight) across categories with at least one assessed criterion, divided by sum of those category weights. Always publish assessed count and weight coverage beside the score. If coverage is below 60%, present the number as preliminary and avoid cross-site rankings. Ratings are evaluator judgments, not an industry standard.

## Finding record

Every issue should include: finding ID; page/template; observed evidence; source and checked date; rating; affected audience/task; recommendation; priority; confidence; owner; verification method. Mark unknowns explicitly.

## Limitations and false positives

- A crawler snapshot may miss personalized, geo-dependent, JavaScript-loaded, or login-gated content.
- Structured-data validators check syntax/eligibility, not factual accuracy or ranking outcomes.
- Robots directives are signals and may be interpreted differently by crawlers; verify actual behavior and each vendor's published guidance.
- A prompt sample is not exhaustive, and AI responses can vary between runs, accounts, locations, and model versions.
- Presence of a citation does not prove traffic, endorsement, correctness, or stable future inclusion.
- Scores depend on sample selection and assessor judgment. Keep evidence, disclose coverage, and use matched re-audits.
- Accessibility and credibility should be reviewed by people; automated checks alone are incomplete.
