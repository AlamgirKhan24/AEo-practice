# Project 02 — E-commerce AEO Optimization: Daraz Pakistan

**Independent portfolio case study · Research snapshot: 22 November 2026**

## Executive summary

This project develops a practical AEO program for an e-commerce marketplace operating in Pakistan. It uses publicly visible Daraz Pakistan homepage content to ground recommendations and a visible power-bank card as a sample content candidate. AEO here means making product and shopping information accurate, easy to find, clear to people, and structured so search engines and answer systems can interpret it. It cannot guarantee citation or inclusion in AI-generated answers.

This is a desk-based independent analysis, not a Daraz engagement. I did not access Daraz's source code, seller systems, analytics, internal search data, or backend and did not publish or change anything. The web search endpoint was unavailable; browser inspection succeeded for the public homepage only. Therefore, this is a scoped research case study plus implementation-ready examples, not a full site crawl or performance audit. Details labeled **verify before use** are not claims about Daraz's current product-level terms.

## 1. Project planning and objectives

### Business problem

Marketplace shoppers must decide among similar listings and resolve practical questions before purchasing: exact model/specification, compatibility, authenticity/seller identity, delivered price, delivery coverage and timing, payment availability, warranty, and return eligibility. Marketplace pages can contain rapidly changing offers, seller-provided claims, variants, and review data. When these facts are incomplete, inconsistent, or buried, shoppers and answer systems have difficulty distinguishing one offer from another.

### Objectives

1. Create a repeatable content model for product, category, seller, policy, and buying-guide information.
2. Capture question-led demand across discovery, comparison, purchase, and post-purchase stages without fabricating search demand.
3. Recommend crawl/index and structured-data checks for high-value URLs.
4. Improve clarity and trust by tying claims to current, visible, SKU-specific evidence.
5. Define a measurement system that reports search and answer-engine observations honestly.

### Scope and assumptions

- **Market:** Pakistan; shopper-facing language primarily English with selective, human-reviewed Urdu/local-language support where demand and UX justify it.
- **Currency:** PKR. Prices, stock, seller, delivery and offers are volatile and must be refreshed from the actual offer.
- **Reference site:** `https://www.daraz.pk/`, treated as a public reference platform only.
- **Sample vertical:** portable power banks/accessories, chosen from a homepage-visible card. This is a template demonstration, not a claim that the listing is representative or best-selling.
- **Out of scope:** backend changes, live page deployment, seller-center access, analytics, legal advice, sales projections, and measured rankings/volumes.

## 2. Market and audience research

### Audience hypotheses to validate

These are working personas based on common marketplace decision tasks, not measured demographic findings:

| Audience | Job to be done | Main uncertainty | Useful answer |
|---|---|---|---|
| Budget-conscious mobile shopper | Find a workable power bank within a fixed PKR budget | Is the capacity real and what charging speed/ports are included? | Clear SKU specs, verified output, delivered price and return route |
| Commuter or traveler | Keep devices charged away from a socket | Size/weight, usable charge estimate, airline restrictions | Transparent assumptions, dimensions/weight, current airline-rule links |
| Gift buyer | Choose a compatible item without knowing technical terms | Device compatibility, packaging, delivery date | Plain-language compatibility and delivery estimate after address selection |
| Comparison shopper | Compare several offers | Same model vs look-alike, seller, warranty and total cost | Side-by-side verified fields and seller-specific terms |
| Existing customer | Resolve an order or refund issue | Current process and status-specific steps | Dated, stepwise official help content and account-specific route |

### Shopping behavior and questions

Practical decision points include query refinement by brand/capacity/port, review and seller inspection, local price comparison, delivery availability by city/postcode, payment eligibility, and post-purchase policy lookup. These are research hypotheses for validation with Search Console, onsite search logs, support tickets, customer interviews, and a sampled SERP review. The included CSV is a starter question map, **not** a keyword-volume study.

### Pain points this project addresses

- Titles that repeat keywords but obscure the exact model and differentiating specifications.
- Unclear distinction between manufacturer specification and seller claim.
- Offer facts that can go stale (price, discount, stock, ratings, shipping estimate).
- Policy statements presented too broadly when eligibility can depend on item, seller, order state, or destination.
- Weak linking between category discovery, comparison education, product choice, seller credibility, and official help.
- Risk of structured data containing values that do not match what shoppers see.

## 3. Competitor AEO analysis (phase 03)

### Method and evidence boundary

The requested competitor comparison requires current product-page inspection. Browser/search access in this session returned Daraz homepage only; direct competitor pages and search results were not verified. I will not invent competitor page features or market positions. The table below is a **benchmark plan**, not a completed factual scorecard.

| Benchmark set | Why include it | Compare on next research pass |
|---|---|---|
| Amazon product pages (international reference) | Mature product detail and review conventions | Attribute completeness, variation clarity, Q&A, review provenance, offer data |
| AliExpress listings (cross-border marketplace reference) | Marketplace seller and shipping comparison | Seller/ship-from disclosure, delivery estimates, variants, dispute/return explanation |
| Pakistan electronics retailers such as PriceOye and Telemart | Local electronics purchase context | Exact model/variant, warranty/authenticity language, price presentation, delivery, FAQs |
| Daraz Mall / seller offers within Daraz | Marketplace trust-context comparison | Seller identity, official-store indicators, product fields, return/warranty clarity |

**Required method:** record 5–10 equivalent products, date, country/currency, URL, visible fields and screenshots; score only observed fields; distinguish retailer promises from platform policy. Do not compare unlike variants or treat an offer card as a stable price.

## 4. Question and keyword research (phase 04)

The starter research file contains 16 question/query hypotheses grouped by intent and journey stage. No search volume, difficulty, rank, or actual query frequency is claimed. Validate using Google Search Console query exports, Google Trends, Keyword Planner, Bing Webmaster Tools, Daraz onsite search/support themes (with permission), autocomplete/manual SERP review, and customer interviews.

### Opportunity clusters

- **Product fit:** exact capacity, ports, output, compatible devices, dimensions, included items.
- **Value comparison:** 10,000 vs 20,000mAh, fast charging, price bands, use case.
- **Trust:** seller identity, authentic/original status evidence, warranty scope, verified reviews.
- **Purchase logistics:** current PKR offer, delivery estimate by destination, payment eligibility, item-specific return terms.
- **Post-purchase:** cancellation, tracking, refund steps, escalation route.

Prioritize by customer consequence, business value, evidence availability, and ability to maintain accurate answers—not by invented volume. The [question and intent CSV](research/question_intent_map.csv) provides a working map.

## 5. Search intent and customer journey (phase 05)

| Journey stage | Query pattern | Best destination | Content goal |
|---|---|---|---|
| Learn | “How many times can a 20000mAh power bank charge my phone?” | Buying guide / FAQ | Explain formula, losses and assumptions |
| Compare | “10000mAh vs 20000mAh power bank” | Comparison guide/category | Show weight, capacity, ports and use cases from verified data |
| Validate | “Is this power bank original?” | Product page + seller profile + policy | Identify seller and support evidence, avoid unsupported authenticity claims |
| Buy | “20,000mAh power bank USB-C PD price in Pakistan” | Filtered category/product page | Match exact attributes and current offer; show location-specific delivery/payment context |
| Use/support | “How to check Daraz refund status?” | Official help article | Give current, safe account-specific steps |

See each query in the CSV for an individual intent and destination recommendation. Avoid a separate thin URL for every spelling variation; consolidate synonyms on a genuinely useful page.

## 6. Architecture and content mapping (phase 06)

The homepage snapshot displayed category modules and a broad footer taxonomy (including mobile brands, home appliances, fashion, groceries, books, and legacy-model/tag links). This confirms visible breadth, not the health of the underlying hierarchy. A crawl is needed to inspect depth, duplication, orphan pages, canonicalization, and indexation.

### Recommended information model

```text
Home
├── Category (e.g., Electronics > Mobile Accessories > Power Banks)
│   ├── Brand / attribute landing pages where there is distinct user value
│   ├── Filtered listings (index only when curated and useful)
│   └── Product detail
│       ├── Offer / seller and current terms
│       ├── Verified specs, variants, included items
│       ├── Delivery/payment/returns links, contextual to offer
│       └── Reviews and Q&A with provenance
├── Buying guides and comparisons
├── Help center (order, payment, delivery, returns/refunds)
├── Seller/brand storefronts
└── About, contact, trust, and policies
```

### Page purposes

- **Category:** define selection criteria, useful subcategory links, attribute filters, and current product set; avoid generic filler.
- **Product:** resolve “what exactly is this?”, “will it fit my need?”, “what arrives?”, and “what are the current offer terms?”
- **Brand/store:** establish verified identity and route shoppers to relevant catalog pages.
- **Buying guide/comparison:** answer non-brand research queries with transparent methodology and dated comparisons.
- **Help/policy:** authoritative process for transactional edge cases; link back to relevant product/checkout context.
- **Homepage:** orient shoppers and expose priority categories/help routes rather than relying on crawlers to infer all relationships from promotional modules.

## 7. Technical SEO and crawlability audit (phase 07)

No crawl or source-level audit was possible, so there are no confirmed technical defects in this report. The attached checklist turns the requested audit into a test plan. Prioritize an authorized crawl of a representative sample: homepage, 3 categories, 3 brand/store pages, 10 product URLs across variants/sellers, pagination/filter URLs, help pages, and sitemap entries.

Check HTTP status, robots directives, canonical URLs, rendered versus source content, pagination and facets, XML sitemap coverage, internal link paths, mobile rendering, Core Web Vitals, image alt text, and structured data. Use Search Console URL Inspection and Page Indexing reports for actual Google indexing observations. Evaluate Bing Webmaster Tools separately. Do not infer indexation from a URL merely loading in a browser.

## 8. E-commerce AEO content strategy (phase 08)

### Product information standard

Use consistent, seller-submitted fields: manufacturer/brand, exact model and variant, capacity with units, ports, supported charging protocols and output (only when substantiated), dimensions/weight, included accessories, compatibility constraints, warranty provider/term, origin/condition if disclosed, seller, current price/currency, availability, delivery estimate by destination, and item-specific return link. Label unknown fields as unknown internally and request evidence; do not silently fill them.

### Answer-ready content pattern

1. **Direct answer:** one or two sentences that name the product/variant and answer the question.
2. **Evidence:** concise specification table with units and source/verification owner.
3. **Limitations:** compatibility, estimate assumptions, variant differences, or changing terms.
4. **Next step:** relevant comparison, setup guide, seller details, or current policy link.
5. **Freshness:** “Offer and availability checked [date/time]” only when genuinely updated.

Use human-readable headings phrased around real shopper questions, descriptive links, short paragraphs, lists for steps, tables for comparisons, and accessible form labels. Keep important text in crawlable HTML and do not rely on image text. Provide useful original explanations rather than rewriting competitor copy.

## 9. Sample product content (phase 09)

The candidate is the homepage-visible card for a Xiaomi Redmi 20000mAh power bank (card ID `940581962`). Only the displayed title and displayed transient price/review snippet were visible. Since the detail page and packaging/manufacturer evidence were not inspected, the sample deliberately uses placeholders and a pre-publication evidence checklist. See [sample product rewrite](samples/product_page_rewrite.md).

The proposed copy avoids claiming confirmed USB-C PD, wattage, charge count, safety certification, warranty, authenticity, or compatibility. This restraint is part of quality control: product copy should not turn a listing's marketing language into an independently verified fact.

## 10. On-page AEO optimization (phase 10)

### Sample template for seller-owned catalog

- **Title:** `[Brand] [exact model] [capacity] Power Bank – [verified port/output differentiator] | [Store]`
- **H1:** `[Brand] [exact model] [capacity] Power Bank`
- **Meta description:** `Check the verified capacity, ports, included accessories, seller, current price and delivery options for [exact model] in Pakistan. Confirm destination and return eligibility before ordering.`
- **First answer block:** exact model, core verified use, and crucial caveat.
- **Sections:** Specifications; What is in the box; Compatibility; Seller and warranty; Delivery/payment; Returns; FAQs; Reviews.
- **Internal links:** parent category, buying guide, comparison page, seller profile, official help/policy pages.

Metadata is a suggestion, not a promise of a search snippet. Avoid keyword repetition, unsubstantiated superlatives, and making volatile offer claims in evergreen title text.

## 11. Structured data (phase 11)

The [JSON-LD example](schema/sample_product_breadcrumb.jsonld) is intentionally a template and not valid to publish unchanged. Replace placeholders with a canonical product URL, image URLs, exact SKU/model, true visible price/currency/availability, and genuine seller/brand identity; remove any field that cannot be verified. Keep structured data synchronized with shopper-visible page content.

`Product` with an `Offer` and `BreadcrumbList` are reasonable candidates for a seller-controlled product page. `Organization` belongs on the site's organization/about context. Reviews/aggregate ratings may be marked up only when the displayed reviews refer to that same product/entity and are collected and presented in accordance with current search-engine policies. Do not add fabricated review text/counts or assume marketplace reviews qualify as a seller's own review markup. FAQ markup is not a general AEO shortcut and rich-result eligibility is limited; write FAQs for shoppers first.

Validate with Google's Rich Results Test and Schema.org Markup Validator; then inspect Search Console enhancement reports after deployment. Validation checks syntax/eligibility only and does not guarantee a rich result or AI citation.

## 12. Trust, reviews, and product credibility (phase 12)

The homepage exposed help, returns/refunds, purchase protection, contact, and payment links, and its editorial copy described a 7-day return/exchange policy and multiple payment options. These are homepage observations/first-party statements, not confirmation of SKU-specific eligibility. Product pages should link to the current governing terms and show seller-specific warranty, delivery estimate and return conditions near the offer. Let checkout determine whether COD/card/wallet options are available for a given cart/address.

For reviews, show the source, date, variant (where relevant), verified-purchase status if genuinely known, and a distribution that cannot be misread as an endorsement. Provide a route for reporting suspicious reviews. For credibility, distinguish Daraz Mall/platform indicators from the manufacturer’s own authorization proof, and never state “100% original” without a traceable basis. Avoid fabricated testimonials or review summaries.

## 13. AI search and answer-engine plan (phase 13)

1. Publish clear, unique product facts and useful buying education on pages that are publicly accessible and indexable.
2. Maintain consistent product, seller, brand, price, stock and policy entities across visible text, feeds, metadata and structured data.
3. Use descriptive headings, explicit units, concise answer blocks, tables, meaningful internal links and accessible HTML.
4. Cite primary evidence for technical safety, compatibility, warranty and airline rules; include publication/update dates and responsible authors/reviewers where useful.
5. Create original comparison methodology and explain what data was checked and when. Keep volatile price tables dated.
6. Monitor referrals, query logs, Search Console/Bing data and a repeatable sample of answer-engine prompts. Record engine, date, prompt, response, cited URL and screenshot. Report presence/absence only for that sample; AI answer outputs vary and are not a stable ranking metric.

Search engines generally require crawlable, helpful, trustworthy content and accurate structured data; no markup or wording guarantees selection by Google AI Overviews, ChatGPT, Perplexity, or Copilot. Keep robots and platform policies under review rather than blocking or allowing crawlers blindly.

## 14. Testing and evaluation (phase 14)

### Pre-launch QA

- Verify every product fact against packaging/manufacturer or seller evidence and exact variant.
- Confirm visible price/availability/seller/terms match the offer feed and JSON-LD at render time.
- Run Rich Results Test and Schema Markup Validator; fix parse errors and policy issues.
- Review canonical, robots, status, mobile layout, accessibility, internal links, and image alternatives.
- Test checkout help links and destination-specific delivery/payment states with authorized test cases; do not place a real order for this case study.

### KPIs and evaluation design

Set a 28-day or longer baseline (choose an appropriate seasonal window) before changes, then compare matched periods and annotate sales/events. Track eligible organic clicks/impressions by URL and non-brand query, indexed valid product pages, product-rich-result impressions/clicks where reported, conversion/revenue where privacy-compliant analytics exist, add-to-cart rate, assisted support contacts for key questions, and sampled answer-engine citations. Segment by category, brand, device, city where consent/data permits, and template version. No baseline or outcome data were available in this project, so no measured lift is claimed.

## 15. Final audit and portfolio documentation (phase 15)

The current portfolio package includes this report, observation log, question/intent CSV, technical checklist, original category/product/buying-guide copy, and sample schema. The README explains evidence limitations. Suggested screenshots for a complete portfolio evidence trail: dated homepage, sampled detail page with URL and key content, SERP query captures, schema validator output, crawler summary, and before/after content comparison. Obtain lawful access and remove customer personal data before saving screenshots or exports.

### Current status summary

| Work item | Status |
|---|---|
| Project scope and strategy | Completed as a case-study plan |
| Daraz homepage observation | Completed, one public page, dated |
| Product detail review | Not verified; candidate identified from homepage card |
| Market/consumer research | Hypotheses and research method documented; no primary consumer data |
| Competitor page comparison | Benchmark protocol drafted; live comparison not verified |
| Question/intent research | Starter query hypotheses delivered; no volume data |
| Technical audit | Checklist delivered; no crawl/source audit executed |
| Sample content | Original draft examples delivered; fact placeholders remain |
| Structured data | Template delivered; requires live data and validation before use |
| Live changes or performance | Not performed; no authorization/access and no metrics provided |

## Tools and resources

| Need | Tool/resource | Use |
|---|---|---|
| Question/keyword research | Google Search Console, Google Trends, Keyword Planner, Bing Webmaster Tools, onsite search/support logs | Real query wording, trend context and first-party demand; export and date findings |
| SERP/competitor review | Manual Google/Bing searches and dated browser captures; authorized crawler | Inspect comparable intents/pages and visible answer formats; document sample and locale |
| Content workflow | Editorial brief, shared evidence sheet, language review by Pakistan-based editor | Tie each claim to evidence, owner, locale, update date |
| Structured data | Google Rich Results Test; Schema.org Markup Validator | Syntax and supported rich-result eligibility checks |
| Technical SEO | Search Console URL Inspection/Page Indexing, Bing Webmaster Tools, Screaming Frog or Sitebulb, Lighthouse/PageSpeed Insights, CrUX | Crawl/index/render/performance checks on authorized pages |
| AEO evaluation | Search Console/Bing reports, analytics, server logs, manual answer-engine prompt log | Measure attributable organic outcomes and reproducible citation samples; no single AEO score is authoritative |
| Accessibility | W3C WCAG guidance, keyboard/screen-reader checks, browser accessibility tree | Ensure product facts, labels, controls, and tables can be understood by more users and parsers |

### Documentation references

- [Google Search Essentials](https://developers.google.com/search/docs/essentials)
- [Google guidance on creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- [Google structured data policies](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)
- [Google Product structured data](https://developers.google.com/search/docs/appearance/structured-data/product-snippet)
- [Google merchant listing structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing)
- [Google JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- [Bing Webmaster Guidelines](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a)
- [W3C Web Content Accessibility Guidelines](https://www.w3.org/WAI/standards-guidelines/wcag/)

## Next logical task

Run Phase 02 in depth: collect a dated Pakistan-market audience evidence set (first-party query/support data if available, otherwise a clearly labeled manual SERP and interview plan), then verify 5–10 Daraz product detail pages and a matched sample from each competitor before scoring gaps. This next phase requires only public-page access for the manual sample; seller/analytics data would improve confidence but must be supplied by an authorized owner.
