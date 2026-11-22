# AEO Audit System — Portfolio Prototype

An offline, client-side prototype for organizing a repeatable Answer Engine Optimization (AEO) audit. It combines editable evidence-led checks, a transparent readiness score, a manual AI answer observation log, competitor query comparisons, a JSON-LD helper, and report export.

## Run it

Open `index.html` in a modern browser. No installation, server, API key, or network connection is required. Browser data is saved locally in that browser's local storage. Use **Export JSON** to keep a portable audit backup and **Export report** for a client-ready HTML snapshot.

## What is automated and what is manual

- **Automated locally:** scoring arithmetic, score coverage, JSON syntax parsing, presence checks for a few structured-data properties, local persistence, and file export.
- **Manual/evidence-led:** crawling, indexing interpretation, content quality, credibility, query selection, competitor review, and all AI answer/citation observations. The prototype does not fetch arbitrary websites or call Google, OpenAI, Microsoft, Perplexity, or any other answer engine.
- **No actual integrations:** no credentials, crawlers, search APIs, analytics, or AI platform API connections are included.

## Scoring

Readiness score = weighted average of assessed criteria only, normalized from a 0–4 rating to 0–100. “Not assessed” criteria are excluded from the denominator; coverage is displayed separately so a high score based on a tiny sample is visible. The weights are an explicit portfolio methodology, not industry benchmarks. AI mentions/citations are tracked separately and do not raise the readiness score.

## Files

- `index.html` — working responsive dashboard
- `METHODOLOGY.md` — audit protocol, scorecard, limitations
- `SYSTEM_REQUIREMENTS.md` — requirements and architecture
- `COMPETITOR_TOOLS.md` — tool landscape and research boundary
- `SAMPLE_AUDIT.md` — clearly synthetic demonstration report
- `TESTING.md` — executed checks and prototype validation
- `PERFORMANCE_EVALUATION.md` — KPIs and improvement plan
- `data/audit_criteria.csv` — criteria and weights
- `data/sample_prompt_set.csv` — reusable prompt test set
- `data/source_register.md` — official documentation references

## Evidence rule

Every factual finding should include a URL or artifact, check date, method, and confidence. Never enter an AI citation unless it was observed in the named product for the exact logged prompt and date. Keep platform visibility observations separate from technical/content readiness.
