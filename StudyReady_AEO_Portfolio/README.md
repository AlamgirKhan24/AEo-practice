# StudyReady AEO portfolio prototype

A static educational website and research package for an AEO project focused on practical study skills for secondary-school learners.

## Scope

- Illustrative audience: learners around ages 13–18, plus caregivers and educators.
- English-first and geography-neutral. No particular curriculum or accreditation is claimed.
- `studyready.example` is a placeholder. The prototype is not deployed.
- Research CSVs contain question hypotheses, not measured search demand. Competitor comparison is a shortlist pending live verification.
- Five article drafts require qualified educator review before public use.

## Run locally

Open `site/index.html` in a browser or serve the `site` folder with a static web server. Before deployment, replace `studyready.example` in all canonical URLs, JSON-LD, robots.txt, and sitemap.xml with the real domain.

## Contents

- `site/` — home, About, guides hub, five lessons, CSS/JS, robots.txt, sitemap.xml.
- `research/` — audience personas, content strategy, question bank, intent map, competitor shortlist/review, answer-engine measurement protocol, source and research-attempt logs.
- `reports/` — phase report, QA results, and spreadsheet previews.
- `scripts/audit_site.py` — local structural audit.
- `build_project.py` — reproducible generator for the HTML prototype and research CSV seeds.
- `research_keyword_intent_competitor_workbook.xlsx` — three-tab workbook for questions, intent, and competitor research status.

## Local test

Run `python build_project.py` from this folder to rebuild the prototype and research CSVs. Run `python scripts/audit_site.py` using Python 3 to check the generated files, and `node scripts/test_search.js` to exercise the guide-search behavior. These local checks cover source files, link names, heading order, labels, metadata, JSON-LD consistency, sitemap/canonical parity, placeholder use, and search filtering. They are not a hosted crawler, Google rich-result validator, accessibility audit, Core Web Vitals report, or answer-engine test.

## Release checklist

1. Confirm niche, country, age range, domain, and content owner.
2. Interview students and educators; validate the research seed and curriculum boundaries.
3. Verify competitor URLs and complete live search results review.
4. Add actual author/reviewer details, contact/correction route, privacy information, and review records.
5. Review educational claims and links; test keyboard, screen-reader, contrast, responsive layout, and downloads.
6. Replace the placeholder domain and deploy; test canonical URLs, redirects, HTTP responses, sitemap, robots, structured data, and performance.
7. Establish Search Console/Bing baselines; perform a repeatable answer-engine sample and report only observed results.
