# System requirements and architecture

## 1. Purpose and users

The system helps small site owners, consultants, and content/SEO teams run a repeatable evidence-led review of whether important pages are understandable, discoverable, trustworthy, and answer-ready. It also records a reproducible sample of answer-engine responses without treating that sample as a ranking metric.

## Users and jobs

| User | Need |
|---|---|
| Small business owner | Understand the highest-priority fix without SEO jargon |
| SEO/AEO consultant | Capture evidence, score consistent checks, and present recommendations |
| Content lead | Find missing shopper questions and improve answer clarity |
| Technical SEO | Record crawl/index/schema issues with URL-level evidence |
| Marketing analyst | Repeat prompt tests and compare dated observations |

## Functional requirements

1. Define audit name, domain, market, language and review date.
2. Assess weighted criteria on a 0–4 scale with evidence, notes and an actionable recommendation.
3. Distinguish unassessed criteria from failures; show score coverage.
4. Track URL-level content/technical checks without pretending the app crawled the URL.
5. Validate pasted JSON syntax and basic property presence locally.
6. Record engine, exact prompt, date, observed brand mention/citation, cited URL, and screenshot/evidence note manually.
7. Compare competitors under the same query and timestamp.
8. Persist data locally and export/import portable JSON and a report snapshot.
9. Make sample data clearly synthetic and removable.

## Nonfunctional requirements

- Responsive, keyboard-operable interface; understandable labels and status text.
- No secrets or external network calls in the prototype.
- Local browser persistence only; user controls backup/export.
- Honest data lineage and visible limitations.

## Architecture decision

For a portfolio prototype, a single HTML/CSS/JavaScript file is appropriate: zero build step, portable offline use, and easy review. `localStorage` holds the current working audit. Browser-native `JSON.parse` checks syntax; the scoring function computes normalized weighted averages. Report export creates a static HTML file. This stack is not suitable for multi-user collaboration, sensitive client data, large crawls, authentication, or scheduled monitoring; those needs would require a secured server, database, access control, job queue, and vetted integrations.

## User journey

Create audit → define scope → inspect representative pages using external/authorized tools → enter evidence and status in criteria and URL checks → run consistent prompt sample manually across selected answer platforms → log exact observations and citations → compare equivalent competitors → review weighted readiness and coverage → export report and JSON backup → schedule a dated re-audit.

## Data model

Audit metadata; criteria records `{id, category, weight, rating, evidence, recommendation, method}`; URL checks `{url, status, note, checkedAt}`; prompt observations `{engine, prompt, date, mention, cited, citationUrl, notes}`; competitor rows `{competitor, prompt, date, mention, cited, citationUrl, notes}`; schema scratch input (not retained unless included in local state).
