# E-commerce UX audit research: KSA store rubric (store-agnostic, plus an electronics add-on)

Compiled 2026-10-22. **How the figures were checked:** WebFetch failed for every host in this environment (DNS `ENOTFOUND`, even example.com), so no page could be opened directly. Every figure below comes from WebSearch result excerpts that quote the cited page. Tags:
- **[S]** Stated on the cited primary page, as quoted in search excerpts (baymard.com, nngroup.com, gov.sa and similar). Several were confirmed by two or more separate queries.
- **[S2]** From a secondary source that quotes the primary.
- **[U]** Unverified: sources conflict, the source is a vendor claim, or the number could not be traced. Do not quote it as fact.

Baymard publishes slightly different numbers for the same guideline in different articles, because the benchmark rounds and samples differ. Where that happens, the newest article is listed first.

---

## 1. Baymard Institute (primary source)

### 1.1 Cart abandonment ([lists/cart-abandonment-rate](https://baymard.com/lists/cart-abandonment-rate), "50 Cart Abandonment Rate Statistics 2026", updated around 22 Sep 2025)
- The average documented cart abandonment rate is **70.22%**, the mean of **50 studies**. **[S]** Some other Baymard pages and secondary sources quote 70.19%.
- **42%** of US online shoppers abandoned a cart in the past 3 months because they were "just browsing / not ready to buy". Baymard treats this group as largely unavoidable. **[S]**
- The reasons below are each a share of US shoppers who abandoned during checkout, with "just browsing" excluded. **[S]** Two separate baymard.com queries returned the same values.

| # | Reason | % |
|---|---|---|
| 1 | Extra costs too high (shipping, tax, fees) | **40%** (a May 2026 Baymard guide gives 39%) |
| 2 | Delivery was too slow | **20%** |
| 3 | Didn't trust the site with credit card info | **19%** (confirmed in the [perceived-security article](https://baymard.com/blog/perceived-security-of-payment-form), "2025 survey") |
| 4 | Site wanted me to create an account | **18%** (the [guest-checkout article](https://baymard.com/research-articles/make-guest-checkout-prominent) gives 19%) |
| 5 | Too long / complicated checkout | **17%** |
| 6 | Website had errors / crashed | **17%** |
| 7 | Returns policy wasn't satisfactory | **13%** |
| 8 | Couldn't see / calculate total order cost up front | **12%** (another Baymard guide gives 14%) |
| 9 | Credit card was declined | **10%** |
| 10 | Not enough payment methods | **9%** |
| — | "I don't know" | 7% |

- Earlier survey rounds gave higher numbers, so cite the year with any figure: 2024 had extra costs at 48% **[S2]** ([Contentsquare](https://contentsquare.com/guides/cart-abandonment/reasons/)), and 2023 had 47%, account creation 25%, slow delivery 24% and trust 19% **[S2]** ([OptinMonster](https://optinmonster.com/cart-abandonment/)).

### 1.2 Checkout benchmark ([research/checkout-usability](https://baymard.com/research/checkout-usability), [checkout-flow-average-form-fields](https://baymard.com/research-articles/checkout-flow-average-form-fields))
- An average large e-commerce site can gain **35.26%** in conversion rate through better checkout design. This is a potential figure that counts only usability issues shown to be solvable. **[S]**
- The average US checkout shows **23.48 form elements** by default, or **14.88** counting form fields only. **[S]** Older benchmarks gave 12.8 fields in 2019 and 19.9 elements, so the definitions have changed over time.
- An ideal checkout can be as short as **12–14 form elements**, or **7–8 form fields**. **[S]** Applying the field-reduction tactics typically cuts visible fields by **20–60%**. Those tactics are: billing address defaults to the shipping address, Address Line 2 sits behind a link, and name is a single "Full Name" field. **[S]**
- Overall rating: **64%** of leading US and EU sites are "mediocre" or worse on desktop checkout, **63%** on mobile, and only **2%** rate "good" on mobile. [Checkout UX 2025](https://baymard.com/research-articles/current-state-of-checkout-ux) **[S]**
- Checkout UX 2025 pitfalls, with the share of sites failing each **[S]** ([current-state-of-checkout-ux](https://baymard.com/research-articles/current-state-of-checkout-ux)):
  - Guest checkout is not the most prominent option: **62%**. The standalone [guest-checkout article](https://baymard.com/blog/make-guest-checkout-prominent) gives 47%.
  - Password rules are too complex: **65%**.
  - Delivery speed is shown instead of a delivery date: **48%**. The [dedicated article](https://baymard.com/research-articles/shipping-speed-vs-delivery-date) gives 41%.
  - Not all fulfilment options (for example store pickup) are in the shipping selector: **52%**.
  - Required and optional fields are not both marked: **61%**. A [separate article](https://baymard.com/research-articles/required-optional-form-fields) says only 14% mark both.
  - Wrong interface type for optional inputs, for example Address Line 2 not collapsed: **32%**.
  - Generic validation error messages: **94%**. The mobile article gives 93% for missing adaptive error messages.
  - Phone number required without explaining why: **49%**.
  - Cart quantity controls (97%) and countdown cut-off times for delivery (83%) are also listed. **[U]** Their headings were not confirmed.
- Forms and addresses:
  - No inline validation at all: **31%** of sites. **[S]** ([inline-form-validation](https://baymard.com/research-articles/inline-form-validation); the same article also says 32%). Validate when the user leaves a field, not while they type.
  - No fully automatic address lookup: **55%**. **[S]** ([automatic-address-lookup](https://baymard.com/blog/automatic-address-lookup))
  - No address validator: **47%**. **[S]** ([address-validator](https://baymard.com/blog/address-validator))
  - On mobile, no address validator or lookup: **54%**. **[S]** ([mobile-ux-ecommerce](https://baymard.com/blog/mobile-ux-ecommerce))
  - Card data is cleared after a validation error: **34%** of sites. **[S]** ([preserve-card-details-on-error](https://baymard.com/research-articles/preserve-card-details-on-error))
- Perceived payment security:
  - Visually group the card fields (border or shading) and put 1–2 security icons inside that area. Users judge security by how the page looks.
  - **66–68%** of sites don't do this, against 89% in 2012. **[S]** ([visually-reinforce-sensitive-fields](https://baymard.com/blog/visually-reinforce-sensitive-fields))
  - Any recognisable seal matters more than which seal is used. **[S]** ([site-seal-trust](https://baymard.com/blog/site-seal-trust))
- Order review and confirmation:
  - Users mistake a review step for the confirmation and leave. Add a second or sticky "Place Order" button. **[S]** ([post-checkout UX](https://baymard.com/blog/post-checkout-ux-best-practices))
  - Ask for account creation on the confirmation step, carrying over guest details so only a password is needed: **42%** of sites don't. **[S]** ([delayed-account-creation](https://baymard.com/blog/delayed-account-creation))
  - Show a clear success message, order number and order details.

### 1.3 Homepage and category navigation ([ecommerce-navigation-best-practice](https://baymard.com/research-articles/ecommerce-navigation-best-practice), 2026)
- **61%** of desktop and **65%** of mobile sites are "mediocre" to "poor". The basis is 17,000+ performance scores across 180+ US and EU sites. **[S]**
- The current scope is not highlighted in the main navigation on **96%** of sites (94% on mobile). **[S]**
- Intermediary category pages don't feature subcategories as the main content on **38%** of sites. **[S]**
- **22%** of mobile sites don't make product categories the top level of the main navigation. An older article gives 33%. **[S]**
- There is no "View All" option at every catalogue level on **42%** of mobile sites. **[S]**

### 1.4 Search ([ecommerce-search-query-types](https://baymard.com/blog/ecommerce-search-query-types), 2026, and the [on-site search collection](https://baymard.com/blog/collections/on-site-search))
- **56%** of sites have issues with search query types. "Exact" queries fail on 12% of sites and "Product type" queries on 20%. **[S]**
- Autocomplete is offered by about 80% of sites, but only **19%** get every detail right. **[S]** ([autocomplete-design](https://baymard.com/blog/autocomplete-design))
- **69%** of sites give no relevant autocomplete suggestions for close misspellings. **[S]** ([offer-autocomplete-suggestions-for-misspellings](https://baymard.com/blog/offer-autocomplete-suggestions-for-misspellings))
- **58%** of sites don't copy the active autocomplete suggestion into the search field. **[S]** Keep the suggestion list to about 10 items on desktop and about 8 on mobile.
- No search submit button next to the field: **27%** of mobile sites. **[S]**
- Older benchmark (about 11 years old): **70%** can't handle product-type synonyms, and **34%** return useless results for model-number searches or one-character typos. **[S]** Users conclude "they don't sell it" when a model number fails ([mobile-ecommerce-search-and-navigation](https://baymard.com/research-articles/mobile-ecommerce-search-and-navigation)).
- Search scope: sites need several of the five scope features, such as category suggestions in autocomplete. **[S]** ([search-scope](https://baymard.com/blog/search-scope))

### 1.5 Product list and filtering ([current-state-product-list-and-filtering](https://baymard.com/research-articles/current-state-product-list-and-filtering), 2025)
- **58%** of desktop and **78%** of mobile sites are "mediocre" or worse. **[S]**
- 2025 pitfalls, with the share of sites failing each **[S]**:
  - Variants not combined into one list item: 42%.
  - Fewer than 3 thumbnails per item: 80%.
  - No unit price: 67%.
  - Multiple values can't be selected within one filter: 14%.
  - Missing the essential filters (price, rating, colour, size, brand): 51%.
  - No overview of applied filters: 20%. Another article gives [28%](https://baymard.com/blog/promoting-product-filters).
  - Not all four sort options offered (price, rating, best-selling, newest): **69%**.
- Other filtering gaps:
  - Important filters not promoted: **61%** of sites. **[S]** ([promoting-product-filters](https://baymard.com/blog/promoting-product-filters))
  - Industry-specific filters not explained: **62%**. **[S]** ([explain-industry-specific-filters](https://baymard.com/blog/explain-industry-specific-filters))
  - No filter for every attribute shown in list items: **38%**. **[S]** ([have-filters-for-list-item-info](https://baymard.com/blog/have-filters-for-list-item-info))
  - No thematic filters: 20%. No category-specific filters: 42% (older Macy's case study). **[S]**
- **50%** get list-item information wrong, meaning list items don't show the key differentiating attributes. **[S]** ([product-listing-information](https://baymard.com/blog/product-listing-information))
- Items already in the cart are not highlighted in lists on **96%** of sites. **[S]**

### 1.6 Product page ([current-state-ecommerce-product-page-ux](https://baymard.com/research-articles/current-state-ecommerce-product-page-ux), 2026, updated 18 Mar 2026)
- **52%** of desktop, **62%** of mobile and **64%** of app sites are "mediocre" or worse. No site reaches "State of the Art". **[S]**
- 2026 pitfalls, with the share of sites failing each **[S]**:
  - No "in scale" image: 37% of sites. **42%** of users try to judge size from the images. A 2017 article gave 28%.
  - Size options not shown as buttons: 57%.
  - No model image for worn products: 23%.
  - Save or wishlist features hard to reach, or unavailable to guests: 89%. 21% of 1,193 respondents rely on "Save".
  - No unit price: 81%.
  - **No estimated total cost near the buy section: 67%.**
  - **Return policy not linked from the main product content: 44%.**
  - No gifting options: 78%.
  - Negative reviews not answered: 89%.
  - Reviewer photos can't be browsed across reviews: 63%.
- Shipping cost estimate missing from the product page: **43%**. **[S]** ([show-shipping-costs-on-product-pages](https://baymard.com/blog/show-shipping-costs-on-product-pages)) Show it as the lowest flat rate, a location-based estimate, or a range with its conditions.
- Free shipping shown only in a site-wide banner: **32%** get it wrong. **56%** have bloated "Buy" sections (warranty upsells, wishlists and so on). **[S]** ([avoid-banners-only-free-shipping](https://baymard.com/blog/avoid-banners-only-free-shipping))
- Description not structured by "highlights": **78%** of sites. **[S]** No descriptive text or graphics on some images: **52%**. **[S]** ([structure-descriptions-by-highlights](https://baymard.com/blog/structure-descriptions-by-highlights), [product-images-descriptive-text](https://baymard.com/blog/product-images-descriptive-text))
- Alternatives and supplementary products: only **42%** recommend both. **[S]** ([product-page-suggestions](https://baymard.com/blog/product-page-suggestions))
- Image zoom, image resolution and review sorting: no current percentages could be verified. **[U]** NN/g: users want review summaries and ways to sort or filter reviews, and seek out negative reviews ([NN/g product pages](https://www.nngroup.com/articles/ecommerce-product-pages/)). **[S]**

### 1.7 Mobile ([mobile-ux-ecommerce](https://baymard.com/blog/mobile-ux-ecommerce), 2026)
- **75%** of 150+ mobile sites are "Mediocre", **95%** are "Mediocre" or "Decent", one site is "Good" and none is "Perfect". **[S]**
- Minimum tap target **7 mm × 7 mm**. **[S]** ([button-design](https://baymard.com/blog/button-design)) For a sticky add-to-cart button, keep it visually distinct with white space around it, and don't make it full-width. **[S]**
- Mobile apps: **90%** lack a search submit control. **[S]** ([mobile-app-ux-trends](https://baymard.com/research-articles/mobile-app-ux-trends))
- The touch keyboard covers about half the screen during checkout, which argues for fewer fields and the correct input type. **[S]** ([mobile-ecommerce-checkout-forms](https://baymard.com/research-articles/mobile-ecommerce-checkout-forms)) No percentage for "wrong keyboard type" was found. **[U]**

### 1.8 Accessibility ([accessibility-benchmark-launch](https://baymard.com/research-articles/accessibility-benchmark-launch))
- **94%** of the largest sites are not compliant with WCAG 2.1 AA (33 sites, 4 areas). **[S]**
- Issue rates by area **[S]**:
  - Images: 82%.
  - Links: 73%.
  - Keyboard navigation: 64%.
  - Form field markup: 58%.
- Keyboard detail **[S]**:
  - 45% have functions that can't be operated by keyboard.
  - 48% lose the visible focus indicator.
  - 9% have keyboard focus traps.
- Informational images lack meaningful ALT text on **55%** of sites. **[S]**

### 1.9 Baymard scoring and severity model (to copy in our rubric)
- Rating labels used across benchmarks: **Broken → (Very) Poor → Poor → Mediocre → Decent → Good → State of the Art / Perfect**. **[S]** The labels appear in benchmark write-ups. The exact score-to-label mapping is not published openly. **[U]**
- Scale of the benchmark data:
  - The checkout benchmark describes each guideline as scored on a **"7-point weighted scale"**. **[S]**
  - Scores are "weighted UX performance scores": 275,000+ scores across 810 guidelines, 344 sites and 54 benchmark rounds. **[S]** ([methodology](https://baymard.com/research/methodology))
  - Guidelines are ordered by importance, which combines how often the issue occurs and how severe it is. **[S]** The source text is truncated.
  - Guidelines are also tagged by implementation cost, for example "Low Cost". **[S]**
- Prioritising issues:
  - Audits prioritise by **frequency × severity**, where severity means how likely the issue is to cause abandonment. **[S]** ([audit-checkout-flow-hidden-friction](https://baymard.com/blog/audit-checkout-flow-hidden-friction))
  - Severity should reflect impact on users. Implementation effort belongs in prioritisation, not in the severity rating. **[S]** ([heuristic-evaluation-find-ux-issues](https://baymard.com/blog/heuristic-evaluation-find-ux-issues))
- Research basis **[S]**:
  - 200,000+ hours of testing, 18,000+ users, 4,400+ think-aloud sessions and 700+ guidelines.
  - About 20 participants find 95% of issues that have an occurrence rate of 14% or more (binomial calculation).
  - Baymard's guidelines come only from "medium-to-severe" issues.

---

## 2. Global e-commerce patterns now considered standard

- **Sticky / persistent add to cart and add-to-cart feedback**
  - NN/g: show clear, persistent feedback after adding (cart badge plus popover or overlay) without hiding the product information, and never grey out the button after an add. **[S]** ([nngroup cart-feedback](https://www.nngroup.com/articles/cart-feedback/))
  - Baymard's sticky-button guidance is in §1.7.
- **One-tap wallet checkout (Apple Pay / Shop Pay)**
  - Shopify claims Shop Pay lifts conversion by up to **50%** against guest checkout and by **≥10%** against other accelerated checkouts. **[S2]** The source is a 2023 study with an undisclosed consulting firm. ([Shopify](https://www.shopify.com/enterprise/blog/faster-checkout-process))
  - Merchant case (Princess Polly): **+4.1%**. **[S2]**
  - Independent A/B tests point both ways (+35% in one store, −37% in another where wallet use was low). **[S2]** ([Blend Commerce](https://blendcommerce.com/blogs/ab-tests-shopify/35-increase-in-conversion-rate))
  - Treat the lift as real but modest. Put wallet buttons on the PDP or in the mini-cart, and at the top of checkout.
- **BNPL messaging on the PDP**
  - Stripe tested more than 150,000 sessions and found **up to +14% revenue** where BNPL was eligible to show at checkout. **[S]** ([Stripe](https://stripe.com/blog/testing-the-impact-of-buy-now-pay-later))
  - PayPal says upstream messaging gives +4.4% overall sales. **[S2]**, vendor figure ([PayPal](https://www.paypal.com/us/brc/article/bnpl-ecommerce-landscape))
  - Klarna's often-quoted +20–30% conversion and +40% AOV are **[U]**.
- **Delivery-date promise ("Get it by Thursday")**
  - Show a date, not "2–5 business days". **41–48%** of sites don't (see §1.2).
  - Show it on the PDP where possible.
  - Users treat the date as a promise, so it must be accurate. **[S]** ([Baymard #543](https://baymard.com/research-articles/shipping-speed-vs-delivery-date))
- **Total cost transparency:** estimated total or shipping cost near the buy section. 67% and 43% of sites miss these (see §1.6).
- **Social proof and reviews:** rating summary, distribution, filtering, customer photos, Q&A, and replies to negative reviews (89% of sites don't reply) (§1.6, [NN/g](https://www.nngroup.com/reports/ecommerce-ux-product-pages-including-reviews/)).
- **Size and fit tools (fashion: Zalando, ASOS)**
  - Zalando reports about **10% fewer size-related returns** on items that carry size advice.
  - About **one third** of Zalando returns are size-related. **[S]**, company claim ([Zalando corporate](https://corporate.zalando.com/en/node/10413))
  - The electronics equivalent is compatibility checking (see §5).
- **Saved carts, wishlists and persistent carts**
  - Make sure the cart persists across sessions and offers "save for later". **[S]** ([Baymard audit checklist](https://baymard.com/blog/audit-checkout-flow-hidden-friction))
  - 89% of sites make "Save" hard to use or unavailable to guests (§1.6).
- **Order tracking and post-purchase:** confirmation page with the order number, an account-creation offer after purchase, and tracking details (§1.2). The 6-detail order-tracking article ([integrate-tracking-info](https://baymard.com/blog/integrate-tracking-info)) could not be read in full. **[U]**
- **Visual search** (Amazon Lens, ASOS Style Match), **AR** (IKEA Place) and **trade-in or pickup** (Apple Store): these are well-known patterns. No verified conversion statistics were retrieved, so score them as "nice to have". **[U]**

---

## 3. KSA / GCC specifics

### Market and devices
- Market size estimates for 2025 vary a lot by publisher:
  - Mordor: **USD 27.96B**, growing to 54.87B by 2031.
  - Ken Research: USD 24.6B.
  - Markntel: USD 19.3B.
  - PS Market Research: USD 16.3B.
  - IMARC's USD 251B uses a different definition. **[U]**
  - Sources: [Mordor](https://www.mordorintelligence.com/industry-reports/saudi-arabia-ecommerce-market), [Ken](https://www.kenresearch.com/industry-reports/saudi-arabia-e-commerce-market), [Markntel](https://www.marknteladvisors.com/research-library/saudi-arabia-e-commerce-market.html), [PSMR](https://www.psmarketresearch.com/market-analysis/saudi-arabia-e-commerce-market-report).
- Smartphones made up **77.98%** of B2C e-commerce revenue in 2025, and **consumer electronics** were **27.06%** of B2C e-commerce revenue. **[S2]** (Mordor, single paid report)
- **92%** smartphone ownership in 2024 **[S2]**. About **25.2M** online buyers in 2025 and 99% internet penetration **[S2]** (PSMR, Ken).

### Payments
- **SAMA (official):** e-payments were **85% of retail payments in 2025**, up from **79% in 2024**, with about 14.6B transactions. Growth was driven by **mada** at point of sale and in e-commerce. **[S]** ([SAMA](https://www.sama.gov.sa/en-US/MediaCenter/News/pages/news-1139.aspx), [SPA](https://www.spa.gov.sa/en/N2558262))
- mada e-commerce spend: **SAR 69.3B in Q1 2025**, against about SAR 44B in Q1 2024. **[S2]** ([khaleejseo, citing SAMA](https://khaleejseo.com/blog/saudi-digital-payments-statistics/)) mada handles "over 70% of online transactions". **[U]** (vendor guides)
- Checkout.com MENA report:
  - **26%** of Saudi consumers name digital wallets as their #1 online payment method, nearly double the 2021 level.
  - Preference for cash fell from **27% to 20%**. **[S]**
  - Source: [Checkout.com](https://www.checkout.com/newsroom/e-commerce-enters-high-growth-stage-in-saudi-arabias-thriving-digital-economy)
- **Cash on delivery** share today: estimates of about 10% or 15–20% are **[U]**. Treat COD as an expected option, not the main one.
- **Apple Pay** share: no reliable figure. Claims of 36% of consumers or more than 20% of wallet checkouts are **[U]**. **STC Pay** (now STC Bank) appears as a common wallet. **[U]**
- **BNPL:** Tabby and Tamara are both licensed by SAMA. Tamara received the first consumer finance licence in March 2025. **[S2]** ([Argaam](https://www.argaam.com/en/article/articledetail/id/1857615), [Sacra](https://sacra.com/research/tabby))
  - Tabby reports about 25M users and about 70K merchants. **[U]** ([CrowdfundInsider](https://www.crowdfundinsider.com/2026/09/310324-saudi-fintech-firm-tabby-reports-233m-funding-round-at-6-5b-valuation-as-it-moves-beyond-bnpl))
  - BNPL at "25–30% of checkouts in fashion and beauty" is **[U]**.
- **Rubric implication:** expect mada, Visa/MC, Apple Pay, Tabby and/or Tamara, plus optional COD and STC Pay. Show BNPL instalment messaging on the PDP. The mada logo must be visible. **[U]**: this is industry practice, and no regulation or UX test was found.

### Address and delivery
- **National Address is mandatory:**
  - The Transport General Authority (TGA) announced in Apr 2025 that from **1 Jan 2026** parcel carriers must **reject shipments without a valid National Address**.
  - Enforcement started 1 Jan 2026, with fines of **SAR 5,000–50,000** for non-compliant carriers. **[S]** ([SPA announcement](https://www.spa.gov.sa/en/N2300857), [SPA enforcement](https://www.spa.gov.sa/en/N2479878), [Arabian Business](https://www.arabianbusiness.com/industries/transport/saudi-arabia-enforces-national-address-rule-for-parcels-imposes-fines))
  - Residents get their address through the National Address platform, Absher, Tawakkalna, Sehhaty or SPL. **[S]**
  - The **Short Address** format is 4 letters + 4 digits, e.g. RAGI2929. **[S2]** ([iHerb help](https://information.iherb.com/hc/en-us/articles/41136974163092-Saudi-Post-SPL-National-Address-Short-Code-Explained), [Quiqup](https://www.quiqup.com/post/saudi-arabia-national-address-ecommerce))
  - **Rubric:** checkout needs a dedicated, labelled Short Address field with a format check, map or lookup autofill, and a "find my short address" help link.
- **Delivery benchmarks from leaders:**
  - **Amazon.sa:** same-day delivery in the **Riyadh and Jeddah** metro areas. It is free for Prime on orders over SAR 100 placed before 12 PM, otherwise SAR 24. Prime gets free next-day delivery in Dammam, Khobar, Makkah, Madinah and Taif. **[S]** ([Amazon.sa help](https://www.amazon.sa/-/en/gp/help/customer/display.html?nodeId=GTFUTRQF459U3H3Y))
  - **eXtra:** express same-day delivery with cut-off times (11:00 for small items, 15:00 for large) and click & collect. **[S2]** ([extra.com/delivery](https://www.extra.com/en-sa/delivery)) The page shows € prices, so verify on the live site.
  - "67% of Saudis will pay for faster delivery" and "same-day is standard in Riyadh/Jeddah": no named survey, **[U]**.

### Language and RTL
- **Material 3 bidirectionality rules** **[S]** ([m3 bidirectionality](https://m3.material.io/foundations/layout/bidirectionality-rtl)):
  - Mirror directional icons (back/forward, chevrons, progress).
  - Do **not** mirror media controls, clocks, or physical-object icons.
  - Slashes are generally not mirrored.
- Western digits (0–9) are the norm in Saudi commerce interfaces. Keep phone numbers and SKUs LTR inside Arabic text, use `dir="auto"` on inputs, and test the full checkout in Arabic. **[S2]** (agency guides: [ofqtech](https://ofqtech.com.sa/en/blog/arabic-rtl-ui-design), [esmnt](https://esmnt.com/insights/articles/arabic-website-design-rtl-ux))
- No Saudi survey on language preference was found. **[U]**

### WhatsApp
- WhatsApp reach in KSA is about **75–86%**, depending on the denominator. **[U]** (DataReportal-based tables, vendor blogs: [ycloud](https://www.ycloud.com/blog/whatsapp-statistics-for-businesses), [weddingkart](https://www.weddingkart.co/blog/whatsapp-vs-email-adoption-by-country))
- A BCG figure that about 9 in 10 adults use it daily is quoted secondhand. **[U]** ([Jawlah](https://jawlah.co/en/59423))
- **Rubric:** a WhatsApp click-to-chat entry point on the PDP, in checkout and in the order status page counts as table stakes. This is expert judgement, not a measured result.

### Trust and legal requirements
- **Store registration moved from Maroof to the Business Platform:**
  - The Ministry of Commerce asked e-stores on 29 Mar 2023 to register on the **Saudi Business Center "Business Platform" ([business.sa](https://business.sa/)) instead of Maroof**. **[S]** ([MC press release](https://mc.gov.sa/en/mediacenter/News/Pages/29-03-23-02.aspx), [Saudi Gazette](https://saudigazette.com.sa/article/631184/SAUDI-ARABIA/E-stores-must-be-registered-via-nbspBusiness-platform-instead-of-Maroof))
  - Salla documents how to verify a store on the Business Platform ([Salla help](https://help.salla.sa/en/article/verify-store-on-business-platform-instead-of-maroof/gno9ilestioyspm61yu5buzp)).
  - **Rubric:** check for the Business Platform authentication badge or link in the footer. A Maroof badge alone is now outdated.
- **E-Commerce Law (Royal Decree M/126, 2019) and Implementing Regulations (2020):**
  - The store must disclose contact details, its name and address (if not registered with the certification platform), the name on its CR, a privacy policy, and its **VAT number** where applicable. **[S2]** ([Global Compliance News](https://www.globalcompliancenews.com/2020/03/16/saudi-arabia-regulates-e-commerce/))
  - Consumers can cancel within **7 days of receipt** if the item is unused. There are exceptions, such as custom-made goods, software and downloads, and publications. **[S2]**
  - Consumers can cancel if delivery is more than **15 days** late, and the store must state the delivery deadline and warn about delays. **[S2]**
  - Penalties go up to **SAR 1M**, plus suspension or blocking of the store. **[S2]** ([Saudipedia](https://saudipedia.com/en/e-commerce-law-in-saudi-arabia), [Arab News](https://www.arabnews.com/node/1696931/saudi-arabia))
- **VAT and ZATCA e-invoicing:**
  - VAT registration is mandatory above **SAR 375,000** in taxable supplies over 12 months. **[S2]**
  - B2C "simplified" invoices need a **QR code**. Phase 2 adds the hash, signature and public key, for up to 9 fields, and invoices must be reported to ZATCA within 24 hours. **[S2]**
  - Phase 2 integration Wave 24 covers businesses above SAR 375K with a deadline of 30 Jun 2026. **[S2]** Wave 25 (SAR 187.5K, Feb 2027) is **[U]**.
  - Sources: [Mercans](https://mercans.com/glossary/zatca-e-invoicing-fatoora/), [ClearTax](https://www.cleartax.com/sa/ksa-einvoicing).
  - **Rubric:** the VAT number is visible (footer or checkout), prices include VAT and say so, and the order confirmation or invoice has the ZATCA QR code.

### Platforms
- **Salla:** about 68–80K active merchants, as reported by the company. **[U]**
- **Zid:** about 12K+ merchants. **[S2]**
- **Share of tracked stores (ShopRank, 41.5K stores):** Zid **12.1%**, Salla **9.3%**, Shopify **5.8%**. **[S2]** ([ShopRank](https://shoprank.com/countries/saudi-arabia))
- **Audit tip:** when the store runs on Salla or Zid, many checkout elements are fixed by the platform. Score them, but mark them "platform-constrained" in the recommendations.

---

## 4. Audit methodology

- **Heuristic evaluation:** Nielsen's 10 heuristics (1994, refined from 249 problems) **[S]** ([NN/g](https://www.nngroup.com/articles/ten-usability-heuristics/)):
  1. Visibility of system status
  2. Match between the system and the real world
  3. User control and freedom
  4. Consistency and standards
  5. Error prevention
  6. Recognition rather than recall
  7. Flexibility and efficiency of use
  8. Aesthetic and minimalist design
  9. Help users recognize, diagnose and recover from errors
  10. Help and documentation
- **Number of evaluators:** use **3–5 evaluators**, preferably usability specialists. **[S]** ([NN/g tech transfer](https://www.nngroup.com/articles/technology-transfer-of-heuristic-evaluation/)) A single evaluator finds about **42%** of major problems on average. **[S]** ([NN/g](https://www.nngroup.com/articles/usability-problems-found-by-heuristic-evaluation/))
- **Severity scale, Nielsen 0–4** **[S]** ([NN/g severity](https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/)):
  - 0 = not a problem
  - 1 = cosmetic
  - 2 = minor
  - 3 = major
  - 4 = usability catastrophe
  - Severity combines **frequency, impact and persistence**, and market impact is also considered. Rate after the evaluation, not during it.
- **Guideline benchmarking (Baymard style):**
  - Score each guideline per site as an adherence level on a weighted scale, then roll scores up by theme into labels from Broken to State of the Art (§1.9).
  - Prioritise by frequency × severity and keep implementation cost separate.
- **Cognitive walkthrough:** persona-driven, step-by-step task walkthrough. Ask four questions at each step **[S]** ([NN/g](https://www.nngroup.com/articles/cognitive-walkthroughs/), [workshop](https://www.nngroup.com/articles/cognitive-walkthrough-workshop/)):
  1. Will users try to achieve the right result?
  2. Will they notice the correct action is available?
  3. Will they associate the action with their goal?
  4. Will they see that progress is being made? (This fourth question is from the canonical method. The snippet was truncated.)
- **Journey or touchpoint mapping:** a visualisation of the process a person follows to reach a goal. **[S]** ([NN/g journey mapping](https://www.nngroup.com/articles/journey-mapping-101/))
  - Suggested touchpoints: discovery (ads, social, WhatsApp), homepage, navigation and search, PLP, PDP, cart, checkout, payment, confirmation, delivery tracking, returns and warranty, and support.
- **Scoring 0–100 (recommended construction):**
  - Map each guideline result to points, for example Broken 0 / Poor 20 / Mediocre 40 / Decent 60 / Good 80 / State of the Art 100. This mapping is our own convention, not Baymard's published one. **[U]**
  - Weight each guideline by severity (Nielsen 1–4 or Baymard importance) and each journey stage by its effect on revenue. Checkout and PDP should carry the most weight, since that is where the 35% lift potential and the abandonment reasons sit.
  - For a sanity check, a **SUS** survey on a 0–100 scale averages **68** (50th percentile, grade C). Above **80.3** is an A (top 10%), and below **51** is an F. **[S]** ([MeasuringU](https://measuringu.com/interpret-sus-score/))
- **Audit output** (Baymard guide): a prioritised issue list with severity ratings, benchmarked against best in class. **[S]** ([ecommerce-ux-research-audit-guide](https://baymard.com/learn/ecommerce-ux-research-audit-guide), [UX-Ray](https://baymard.com/lp/ux-benchmark-tool))

---

## 5. Electronics-specific UX (target: Golden Technology, goldentech.com.sa: laptops, gaming PCs, monitors)

### Baymard findings
- **Electronics & Office UX Benchmark 2026:** 9 sites, 500+ parameters, released around 31 Mar 2026. **[S]** ([electronics-and-office-ux-benchmark-2026](https://baymard.com/research-articles/electronics-and-office-ux-benchmark-2026))
  - Main finding: "inconsistent attributes, insufficient imagery, and underpowered comparison tools" forced users into extra navigation and manual tracking.
  - Per-site percentages are paywalled.
- **Spec sheets** **[S]** ([product-spec-sheet-ux-design](https://baymard.com/blog/product-spec-sheet-ux-design), [spec-sheet-scannability](https://baymard.com/blog/spec-sheet-scannability)):
  - **64%** of sites have "poor" or "mediocre" spec sheets.
  - **23%** don't group specs into titled sections. Sheets with more than 20 specs need subsections.
  - **23%** lack row striping or lines.
  - **20%** use confusing multi-column layouts that look like a comparison.
  - Only **3%** add a key-spec summary for long sheets.
  - **30%** have severe inconsistencies in labels, order or units across same-type products.
  - Append units to values and explain jargon with tooltips.
  - Older (2018) headline: **50%** get spec scannability wrong.
- **Comparison tools** **[S]** ([provide-comparison-features](https://baymard.com/blog/provide-comparison-features), [user-friendly-comparison-tools](https://baymard.com/blog/user-friendly-comparison-tools)):
  - **17%** of spec-driven sites offer no comparison feature.
  - **67%** of test participants used comparison features on spec-driven sites.
  - Best practice:
    - an "only show differences" toggle, or highlighted differences
    - attributes grouped by category
    - sticky column headers with name, thumbnail and price
    - horizontal row styling
- **Compatibility** **[S]** ([ecommerce-compatibility-databases](https://baymard.com/blog/ecommerce-compatibility-databases), [mobile search and navigation](https://baymard.com/research-articles/mobile-ecommerce-search-and-navigation)):
  - **56%** of mobile sites that sell compatibility-dependent products fail to list compatible items on the PDP. The usual cause is no compatibility database.
  - Use contextual notices, for example "compatible with the [laptop] in your cart".
  - Don't label accessories "Recommended" unless compatibility is guaranteed.
  - Offer "see accessories for this product" in search.
- **Technical filtering** **[S]**:
  - **62%** don't explain industry-specific filters, for example with tooltips for "refresh rate" or "TDP".
  - **38%** lack filters for attributes shown in list items.
  - **51%** lack the essential filters.
  - **50%** show the wrong list-item information. Laptop and monitor lists should show the key specs: CPU, GPU, RAM, storage, screen size, refresh rate and resolution.
  - Model-number search must work. Users assume the product isn't sold if it fails (34% of sites failed in the older benchmark).
- **Warranty and after-sales** **[S]**:
  - Baymard guideline **#819, "Warranty Upgrades on Product Pages"**: basic warranty information alone isn't enough for users weighing extended coverage ([guideline](https://baymard.com/guidelines/819-warranty-upgrades-on-product-pages), paywalled).
  - Avoid warranty upsells crowding the buy box. 56% of sites have bloated "Buy" sections ([source](https://baymard.com/blog/avoid-banners-only-free-shipping)).
  - **Rubric:** show the warranty length, provider (official agent vs store) and claim process on the PDP. Offer the extended warranty as a secondary option.

### KSA electronics leaders
- **eXtra** **[S2]** ([extra.com](https://www.extra.com/en-sa/delivery), [Tamara × eXtra](https://tamara.co/en-sa/stores/extra), [Tabby offer](https://www.extra.com/en-sa/apple-tabby-offer/cp/8329)):
  - Tabby offers of up to 10 instalments (promotional), Tamara 12-month splits on laptops, and Baseeta financing.
  - "Official Saudi warranty" shown on PDPs.
  - Express same-day delivery with cut-off times, and click & collect.
- **Jarir** **[S2]** ([Jarir FAQ](https://www.jarir.com/sa-en/customer-care/faq), [Jarir app](https://apps.apple.com/us/app/jarir-bookstore/id535777677), [returns](https://www.jarir.com/sa-en/return-and-exchange2)):
  - Instalments through Tamara and several financing partners.
  - Showroom "Order & Collect", plus product comparison and reviews in the app.
  - Policy: 3-day returns and 7-day exchanges.
  - The 2-year minimum electronics warranty is stated on the **UAE** site. For KSA it is **[U]**.
- **Amazon.sa** ([help](https://www.amazon.sa/-/en/gp/help/customer/display.html?nodeId=GTFUTRQF459U3H3Y)): same-day delivery in Riyadh and Jeddah, next-day delivery in Dammam and Khobar (see §3). Also a delivery-date promise on the PDP, comparison tables and customer Q&A. The PDP features are well known but were not verified here. **[U]**
- **noon:**
  - "noon Minutes" quick commerce is now inside the Jahez app (Oct 2025). **[S2]** ([Wamda](https://www.wamda.com/2025/10/noon-jahez-unite-connect-quick-commerce-food-delivery-kingdom))
  - noon's electronics delivery SLAs: no data found. **[U]**
- **Baseline for a Riyadh electronics retailer:**
  - spec-rich PDPs with grouped specs
  - comparison
  - BNPL (Tabby/Tamara) messaging on the PDP
  - clear warranty
  - delivery date with same/next-day options in Riyadh
  - click & collect if there is a showroom
  - National Address capture
  - WhatsApp support
  - visible VAT number and CR
  - Business Platform badge
  - Arabic and English, with correct RTL
