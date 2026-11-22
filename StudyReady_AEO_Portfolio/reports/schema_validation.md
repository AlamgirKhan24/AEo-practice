# Structured data implementation and validation record

## Implemented types

- `Organization` on the home and About pages for the illustrative StudyReady site entity.
- `Article` on each of the five guide pages, with visible title, description, language, prototype publisher and team byline.
- `BreadcrumbList` on each guide page, matching the visible Home → Guides → article path.

No `Person` markup was added because no real author identities or credentials were supplied. No `FAQPage` or `HowTo` markup was added as a shortcut to answer-engine placement. Visible question-and-answer content remains for learners.

## Local validation performed

The local audit parses every JSON-LD script as JSON and checks for `Article` and `BreadcrumbList` on guide pages. The result is in `../reports/local_qa.json`.

## Not validated

The code was not submitted to Schema.org Validator or Google Rich Results Test because outbound access failed and no public URLs exist. Local JSON parsing checks syntax only; it does not verify every vocabulary/property, search-feature eligibility, crawling, or display. Re-run the current official validators after deployment and confirm markup matches the rendered page.
