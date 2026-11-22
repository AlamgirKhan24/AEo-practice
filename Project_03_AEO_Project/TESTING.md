# Testing and validation record

## Executed checks

- Parsed the dashboard's inline JavaScript with Node.js syntax checking.
- Parsed the sample JSON-LD as JSON.
- Checked the criteria CSV imports successfully and its individual criterion weights sum to 100.
- Confirmed the UI source contains the expected 27 rubric criteria and 6 category labels.
- Ran `node tests/smoke_test.cjs`: initial state, score normalization, coverage, observation persistence, and valid/invalid JSON syntax paths passed using a dependency-free fake DOM.

## Not yet tested

- Full real-browser behavior, export/import round trips, keyboard/screen-reader behavior, and responsive rendering have not yet been verified.
- The local schema helper has not been exercised with positive/negative cases in a browser; the full eligibility and visible-data checks still require official external validators and a real page.
- No website was crawled and no AI platform prompt was run for this portfolio deliverable.

## Audit-method validation plan

The portfolio methodology should be calibrated using at least two reviewers scoring the same representative URLs. Resolve disagreements with evidence and examples, revise ambiguous criteria, and re-score before using results to compare sites. Validate schema against official tools, inspect canonical/index signals using site-owner Search Console, and repeat prompt runs over multiple dates. These external checks require a target website and authorized data; they are not represented as completed here.

## Known limitations

- Static client-side app; local storage is tied to one browser profile and is not encrypted collaboration storage.
- No crawl or API integrations.
- JSON checks are intentionally basic; they do not fully validate JSON-LD context, types, Google policies, or visible-data parity.
- Criteria definitions are a portfolio rubric and need calibration before commercial benchmarking.
- Browser automation/accessibility review is limited; conduct assistive-technology testing before deployment.
