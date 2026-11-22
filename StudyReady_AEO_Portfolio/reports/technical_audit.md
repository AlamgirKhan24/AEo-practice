# Technical SEO and crawlability audit

**Audit scope:** local static source files only.  
**Test date:** 22 November 2026.  
**Public host:** none. `studyready.example` is a placeholder.

## Checks performed

| Area | Local result | Production follow-up |
|---|---|---|
| HTML pages | Eight pages found and parsed. Each has a unique title/canonical, description, one H1, one main landmark, `lang="en"`, viewport metadata, and a continuous heading outline. | Recheck rendered HTML and mobile page behavior after deployment. |
| Navigation | Local anchor targets resolve against the project files. | Crawl the deployed host for redirects, broken routes, and orphan pages. |
| Canonicals | Every HTML page contains a canonical pointing to the placeholder host. | Replace with the final HTTPS URLs and test duplicate/trailing-slash behavior. |
| Robots | `robots.txt` allows crawling and points to a sitemap. | Retrieve the deployed file and verify it does not block page assets or public content. |
| Sitemap | Sitemap includes eight HTML page URLs. | Replace host, include only canonical indexable URLs, submit in webmaster tools, and check processing. |
| Structured data | JSON-LD parses locally; guide pages declare Article and BreadcrumbList whose headline, description, main URL, and final breadcrumb agree with page metadata. | Run current Schema.org Validator and Google Rich Results Test on deployed URLs; a passing test does not guarantee a search feature. |
| Responsive layout | CSS includes a narrow-screen breakpoint and flexible cards. | Inspect actual mobile devices or browser emulation, including zoom and keyboard use. |
| Accessibility basics | Language, main landmark, continuous headings, named links, search label, focus style, skip link, and an aria-live search status are present; no content images currently need alt text. | Conduct keyboard, screen-reader, contrast, and automated accessibility review; source checks are not WCAG conformance. |
| Security and delivery | No forms, accounts, or user data are collected in this prototype. | Review hosting, HTTPS, headers, privacy/cookie needs, and dependencies before launch. |
| Performance | Static, small pages with locally stored CSS/JS and no remote font dependency. | Measure deployed Core Web Vitals and network requests. No speed score is claimed. |

## Not measured

HTTP status, TLS, redirect chains, server configuration, Googlebot/Bingbot access, indexing, canonical selection, Core Web Vitals, screen-reader behavior, external source availability, Google rich-result eligibility, and AI answer citations were not tested because no public host or working outbound research connection was available.

The repeatable local result is in `local_qa.json`. Per-page title, description, H1, canonical, schema, answer block, and link counts are in `on_page_optimization_register.csv`.
