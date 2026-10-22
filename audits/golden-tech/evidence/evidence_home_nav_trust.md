# goldentech.com.sa: evidence for homepage, navigation, search, trust and localisation

**Method and caveats.** I used WebSearch (extended mode) only, because the container network and WebFetch were down. I ran 45 queries. 40 returned results; the last 5 were refused because the shared per-turn web-search budget (200 calls across all agents) ran out. All evidence comes from search-index titles and snippets, which are cached and may be stale. I could not render or inspect any live page, so I have no direct evidence for layout, visual hierarchy, mobile behaviour, autocomplete, page speed or the live HTML `<head>`.

Tags:
- **[verified: quote+URL]**: the text is quoted from the indexed title or snippet of that URL. Snippet text passes through a search summariser, so treat wording as near-verbatim, not byte-exact.
- **[inferred]**: a deduction from indirect evidence.
- **not found in index**: I searched for it and nothing surfaced. This is not proof that it is absent from the site.

---

## 0. Highest-severity issues for the audit (summary)

1. **A "Demo" duplicate of the homepage is live and indexed.**
   - `https://goldentech.com.sa/en/home-page-02-66d465ea485bb` uses the same `<title>` as the real homepage, "Golden Technology Home of Laptop & Computers in KSA".
   - Its breadcrumb or page label reads "Golden EN Home Page Demo". [verified: title+URL, label via snippet summary]
   - Impact: duplicate content, plus users may land on a template or test page.
2. **The store's own search-results pages are indexed.**
   - Example: `https://goldentech.com.sa/en/catalogsearch/result/?amnoroute=&q=laptop+lenovo+ideapad+5+intel+core+i5+1135g7+processor+2+4+ghz+8gb+ram+512gb+ssd+m+2+integrated+intel+iris+xe+graphics+14+fhd+display+1920x1080+free+dos+platinum+grey`, titled "Search results for: 'laptop lenovo ideapad 5 intel core i5 1135g7 processor 2 4 ghz 8gb ram 512gb ssd m 2 integrated intel iris xe graphics 14 fhd di'". [verified]
   - That page shows *different* products: a Lenovo IdeaPad 5 2-in-1 with Core Ultra 5, and a Dell Pro 14 with Core Ultra 7. [verified via snippet summary]
   - [inferred] A discontinued product URL probably redirects to an on-site search, and that search does not return an exact match.
   - [inferred] The `amnoroute` parameter points to Amasty extensions (Improved Layered Navigation or Shop by Brand).
3. **Shipping and delivery terms contradict each other across policy pages.**
   - FAQ: "if the order needs delivery and its value is less than 200 SAR, the delivery fee will be 10 SAR … 200 SAR or more, the delivery will be free of charge" (https://goldentech.com.sa/en/faqs). [verified]
   - Terms: "product delivery cost: 20 SAR per order", plus cash on delivery for "an additional 20 riyals" (https://goldentech.com.sa/en/terms-and-conditions). [verified]
   - Delivery times disagree too:
     - FAQ: "between 3 to 7 days".
     - Terms: "within the city of Riyadh … 3 to 7 working days", "outside the city of Riyadh … within 7 to 10 working days", and up to "20 working days" during holidays.
     - Product pages: Riyadh delivery "within 24 hours", other cities "3–6 working days" (e.g. https://goldentech.com.sa/ar/laptop-acer-aspire-lite-al16-54p-intel-core-i5-nx-d76em-003.html; Surface product pages also say "Riyadh delivery within 24 hours"). [verified via snippet summaries]
4. **Garbled machine-translated English in the policy pages** (quotes in section 6).
   - The warranty page calls the company "Technology gold", "The Gold Technology" and "the gold technology".
   - The return terms say "A colored dot or colored or dead pixel is not considered a defect or a manufacturing defect if it is less than 4 points".
5. **The language versions bleed into each other.**
   - Arabic `<title>` strings are indexed against `/en/` URLs. Examples: `/en/` → "التكنولوجيا الذهبية أكبر متجر لأجهزة اللابتوب والكمبيوتر ..."; `/en/laptop.html` → "تسوق كمبيوتر لابتوب بأفضل الأسعار"; `/en/desktop.html` → "أحدث جهاز كمبيوتر مكتبي بأفضل الأسعار"; `/en/terms-and-conditions` → "الشروط والأحكام".
   - Arabic blog posts sit under `/en/blog/post/…`.
   - Details are in section 5.
6. **I found no Saudi Business Center or Maroof e-commerce authentication badge or number in the index.**
   - The CR and VAT numbers are reportedly in the footer.
   - An X post claims the store was "listed in the Saudi e-stores directory", but I could not verify which directory.

---

## 1. Homepage

- **URL and title.** `https://goldentech.com.sa/en/` has the title "Golden Technology Home of Laptop & Computers in KSA". [verified]
  - The title has a grammar issue: it should be "Laptops" (plural), and there is no separator between the brand and the descriptor.
- **Meta description and intro copy:** "Now can get your Laptop, Computer, Apple Mac, Printers, Servers, Gaming Laptop with best price in KSA from Golden Technology" (https://goldentech.com.sa/en/). [verified]
  - This is broken English: it is missing a subject ("Now [you] can get…") and capitalisation is inconsistent.
- **Root-domain and Arabic homepage title:** "التكنولوجيا الذهبية أكبر متجر لأجهزة اللابتوب والكمبيوتر بالسعودية" ("Golden Technology, the largest laptop and computer store in Saudi Arabia"), indexed at `https://goldentech.com.sa/?gad_source=1`. [verified]
  - A Google Ads click parameter URL (`gad_source=1`) is indexed. That is a canonicalisation and parameter-handling flaw.
  - [inferred] The root domain serves the Arabic store view by default.
  - The claim "the largest store" (أكبر متجر) is an unsubstantiated superlative.
- **Hero and banner promotions:**
  - "End Of Year Offers", "Discount till 61%" and a "Shop Now" CTA (indexed on the homepage or the demo homepage). [verified via snippet summary]
    - "Discount till 61%" is non-native English; "Up to 61% off" would be natural.
  - A back-to-school banner for laptops, computers and printers. [verified via snippet summary]
  - Links to PC gaming, Dell and Gigabyte gaming laptops, and MacBook Air and Pro offers. [verified via snippet summary]
  - [inferred] The cache mixes seasonal campaigns: End of Year, Back to School and National Day. Whether they run at the same time could not be confirmed.
- **Homepage sections:**
  - **"New Arrivals"**: Lenovo ThinkBook 16 Gen 9, MacBook Pro 14 M5 Pro, HP EliteBook 640 G11, Lenovo IdeaPad Slim 3. [verified via snippet summary, https://goldentech.com.sa/en/]
  - **"Deal of the day"**: for example a MacBook Pro 14 M5 at "Special Price 9499 Regular Price 9899 -4% Tax included". [verified]
    - The deal is only 4% off; a weak "deal of the day".
  - **"Shop by brand"**: "Lenovo Dell HP Apple Asus Acer". [verified]
  - **"Best Sellers" and "Most Viewed" tabs**: these appear on offer and category pages (e.g. `/en/laptops-computers-and-gaming-monitors-offers.html`, `/en/laptop/gaming/gigabyte.html`), not clearly on the homepage. [verified via snippet summary]
  - The PC Gaming i5, i7 and i9 subcategories are linked from the homepage. [verified via snippet summary]
- **Full section order: not determinable** from the index. [not found in index]
- **Separate offer landing pages that compete for attention** (8 or more indexed):
  - `/en/offers.html`: "Golden Offers on laptops, computers & gaming monitors"
  - `/en/laptops-computers-and-gaming-monitors-offers.html`: "Golden Offers on laptops, computers & gaming monitors". This is the **same title** as `/en/offers.html`, so it is a duplicate title. [verified]
  - `/en/mega-sale.html`: "Special Offers on Laptops & PC Gaming". Copy includes "free shipping, Coupons, and installments for 4 months", with category discounts from about 20% up to 56% on gaming monitors and 47% on Apple. The Arabic version (`/ar/mega-sale.html`) says up to 51% off Apple and laptops. [verified]
    - The URL slug says "mega-sale", the title says "Special Offers", and the content is "Back To School Offer". The slug, title and content don't match.
  - `/en/laptop-pc-gaming-offers.html`: "Shop Now Laptop Gaming, PC Gaming & Monitors Gaming". The title is word-order translated from Arabic: "Laptop Gaming" and "Monitors Gaming". [verified]
  - `/en/business-laptops-offers.html`: "Top Business Laptops Offers in KSA". [verified]
  - `/en/back-to-school-offers.html`: "Back to School Offers Laptops & Tablets". [verified]
  - `/en/saudi-national-day-offers.html`: "Saudi National Day 96 Offers on Laptops & Computers". [verified]
  - `/en/hp-offers.html`: "HP Laptops, Computers & Printers". [verified]
  - `/en/new-arrival.html`: "New Arrival". This is a singular, thin title. [verified]
  - The `/en/laptops-computers-and-gaming-monitors-offers.html` page also claims an "extra 5% discount with free delivery". [verified via snippet summary]
  - [inferred] With 8 or more parallel offer hubs and overlapping names, no single "Offers" destination is clear. The cognitive load is high and the pages cannibalise each other in search.

## 2. Header, mega-menu and information architecture

- **No clean copy of the header is indexed.** The tree below is rebuilt from category URLs and titles. [inferred structure; each URL verified]
- **Laptops** `/en/laptop.html`, titled "Shop Laptops offers with best price" (intro: "Discover all new Laptops computers with 2 years warranty & best price in KSA from Golden Technology").
  - **Brand pages**, all following the title template "Shop X laptop with best price in KSA":
    - `/en/laptop/dell.html`, `/hp.html`, `/lenovo.html`, `/asus.html`, `/acer.html`
    - `/en/laptop/apple.html`: "Shop Apple Mac laptop with best price in KSA"
    - `/en/laptop/microsoft.html`
    - Brand filter counts: "Lenovo 91items", "Dell 41items". The missing space in "91items" is a UI typo.
  - **`/en/laptop/gaming.html`**: "**Shop best Gaming laptop with in KSA**". This title is ungrammatical ("with in"). [verified]
    - Brand sub-pages: `/gaming/asus.html`, `/gaming/gigabyte.html` ("Shop best Gaming GIGABYTE laptop in KSA"), `/gaming/hp.html`, `/gaming/lenovo.html`, `/gaming/acer.html`.
  - **`/en/laptop/business.html`**: "Shop Business laptop with best price in KSA".
    - Sub-pages `/business/dell.html` ("Shop best Business dell laptop in KSA", with "dell" in lowercase) and `/business/hp.html`.
  - **`/en/laptop/2-in-1.html`**: "2 in 1 - Laptop". This is a default Magento "Category - Parent" title, so it has no custom SEO title. [verified]
- **Desktops** `/en/desktop.html`, titled "Shop Desktop Computers with best price".
  - Sub-pages: `/desktop/dell.html`, `/desktop/hp.html`, `/desktop/all-in-one.html`.
  - Filters: "Desktop 45items", "Desktop All in one 55items", "Workstation 8items", "Server 1item".
- **PC Gaming** `/en/pc-gaming.html`, titled "Shop PC Gaming Desktop Computers at Best Prices in Saudi Arabia".
  - Sub-pages: `/pc-gaming/intel-core-i5.html`, `/intel-core-i7.html`, `/intel-core-i9.html`, `/pc-gaming/rtx.html` ("NVIDIA RTX PC Gaming - Shop High-Performance Graphics").
  - **Inconsistent path:** `/en/gaming/pc-gaming/amd-ryzen-7.html` sits under a different parent. That suggests duplicate or orphaned category trees. [verified URLs; inferred issue]
  - Builds are pre-configured, from an i5-14400F with RTX 5060 up to an i9-14900K with RTX 5090 32GB, mostly with Windows 11 Pro. [verified via snippet summary]
- **Gaming** `/en/gaming.html`, titled "Shop Gaming Computers & Laptops offers".
  - The **content is peripherals under a "Gaming Parts" heading** (Redragon and Glorious mice, keyboards, soundbar), so the title and the content don't match. [verified via snippet summary]
  - Sidebar filters: brand "Redragon 7 items", "Glorious 7 items"; categories gaming mice, keyboards, headsets, 4-in-1 combos, sound bars, "65% keyboards".
- **Monitors** `/en/monitors.html`, titled "Best Computer Monitor Brands in Saudi Arabia".
  - Sub-pages: `/monitors/pc-monitors.html` ("PC Monitors - Superior Display Choices and Performance") and gaming monitors, filterable by refresh rate and resolution.
- **Apple** `/en/apple.html`, titled "Apple MacBook Air & Pro, iMac, Mac Mini, Mac Studio, iPad Pro". The Arabic version `/ar/apple.html` is titled "تسوق أحدث أجهزة ابل ماك بوك في السعودية".
- **Microsoft** `/en/microsoft.html`, titled "Microsoft Devices - Best Deals on Surface Laptops, Tablets, and Accessories| golden tech".
  - The brand name is lowercase and there is no space before the pipe.
  - Duplicate category paths exist in Arabic: `/ar/laptop/microsoft.html` and `/ar/microsoft/laptop.html`. [verified URLs]
- **Accessories** `/en/accessories.html`, titled "Shop Laptops Accessories offers| Golden Technology".
  - Menu: Bags, Keyboard, Docking Station, Power Extension, Arm Monitor, Headsets, Adaptor, Mouse, Hub.
  - Sub-pages: `/accessories/bags.html` ("Shop Laptops bags offers| Golden Technology"), `/docking-station.html`, `/power-extension.html` ("Power Extension - Accessories"), `/adaptor.html` ("Adaptor - Accessories").
  - "Adaptor - Accessories" and "Power Extension - Accessories" are default-template titles.
  - "Arm Monitor" is non-native English for "monitor arm".
  - The accessories index lists only one mouse product. The catalogue looks thin. [verified via snippet summary]
- **Promate sub-shop** `/ar/promate-products/cables.html`, titled "تشكيلة من كابلات الشحن ونقل البيانات". [verified]
- **Printers** `/en/printers.html`, titled "Buy High-Quality Printers at Reasonable Prices Online".
  - HP and Xerox only; filters "LaserJet 31items", "OfficeJet 6items".
  - `/en/printers/hp.html`: "Buy High-quality HP Printers Online".
- **Servers** `/en/servers.html`, titled "Servers - High-Performance Computing Solutions".
  - **Only one product** is indexed: Dell PowerEdge R750xs at 17,999. A top-level category holding a single SKU is a dead-end IA node. [verified via snippet summary]
- **Projectors** `/en/projector.html`, titled "Projector - High-Quality Projectors for Photos and Videos". Brands: ViewSonic, BenQ, Epson.
- **Scanners:** filters for HP, Canon, Epson and Fujitsu appear in the navigation. No listing page is indexed.
- **Tablets:** there is no generic tablets category; iPad sits under Apple and Surface under Microsoft. [verified via snippet summary]
- **Shop by brand: three different URL patterns coexist.** [verified URLs; inferred issue]
  - `/en/all-brands-page`, titled "All Brands Page" (an A–Z index).
    - Its boilerplate copy reads "Browse the list below to find just the label you're looking for!". That is default Amasty "Shop by Brand" text: "label" is record-label wording and was never localised.
  - `/en/brands/lg`, titled "LG". It is thin, listing 2–3 monitors.
  - `/en/shop-by-brand/golden_tech`, titled "Golden Tech". The slug uses an underscore. [inferred] This is a house brand.
  - `/ar/shop-by-brand/aoc`, titled "AOC".
- **Account, cart, wishlist and compare:**
  - "Sign In" and "Create an Account" links are present (https://goldentech.com.sa/en/checkout/cart/). The login page title is "Sign In to Golden Tech" (https://goldentech.com.sa/en/customer/account/login). [verified]
  - The cart page shows the labels "cart" and "Cart Mobile". [verified via snippet summary]
  - "Add to Wish List" and "Add to Compare" appear on product tiles (https://goldentech.com.sa/en/gaming.html). [verified]
  - [inferred] This is the standard Magento Luma-derived compare and wishlist.
- **Top-bar messages:**
  - Promotional text says "free shipping to all cities in KSA" on some pages. [verified via snippet summary]
  - The exact global top-bar copy (free shipping, installments) was not found in the index.
- **Language switcher:** I could not confirm the "العربية" or "English" toggle label from the index. [not found in index] Both `/en/` and `/ar/` store views exist (section 5).
- **Header phone and WhatsApp:** not found in the index for the header. The footer has a phone number (section 4).

## 3. Site search

- **Results URL pattern:** `/en/catalogsearch/result/?q=…`, the Magento default. The `amnoroute=` parameter suggests Amasty. [verified URL]
- **Search results pages are indexable and indexed**: there is no `noindex` on search results. [verified]
- **Search quality:** a long product-name query (the exact title of a discontinued Lenovo IdeaPad 5 i5-1135G7) returned other models rather than "no results" or the nearest match. [verified via snippet summary; inferred conclusion]
- **Autocomplete or instant search:** not found in the index, and it cannot be verified without a live render. [not found in index]
- **Search synonyms, spelling tolerance and Arabic↔English transliteration** (e.g. "لابتوب" vs "laptop"): not testable. [not found in index]

## 4. Trust and compliance

- **Legal entity on the terms page:** "Golden Technology foundation" ("we" / "goldentech"), at https://goldentech.com.sa/en/terms-and-conditions. [verified]
- **The About page names a different legal entity:** "The Golden Technology Trading Company and E-marketing had established in Riyadh, Kingdom of Saudi Arabia in 2009" (https://goldentech.com.sa/en/about-us). [verified]
  - The terms say "foundation" (مؤسسة, a sole establishment) and About says "Trading Company". The entity naming is inconsistent.
  - "had established" is a grammar error.
- **CR and VAT numbers:** "C.R. No. 1010276436.VAT ID 311258900400003", reportedly in the footer. A search summary attributed it to the terms and footer, at https://goldentech.com.sa/en/terms-and-conditions. [verified via snippet summary; I could not confirm the exact string in a second search]
  - The VAT ID fits the ZATCA format: 15 digits, starting and ending with 3.
  - The missing space after "1010276436." shows a sloppy footer.
  - I did not check either number against the ZATCA or MoC registers.
- **Saudi Business Center or Maroof e-commerce authentication:** no badge, certificate number or business.sa link was found in the index. [not found in index]
  - An X post from @GoldenTechSA announces that the store was listed in "the Saudi e-stores directory". The directory is not named and the post date is unclear (https://x.com/GoldenTechSA). [verified via snippet summary]
  - Context: MoC moved e-store authentication from Maroof to the Saudi Business Center's Business Platform (https://mc.gov.sa/ar/mediacenter/News/Pages/29-03-23-02.aspx).
- **Physical location:** "Computer market, Olaya", Riyadh (footer and contact block). Directory listings give "Olaya St, Al Olaya, Riyadh 12211". [verified]
  - The FAQ mentions "cash at the showrooms" and "Click and Collect … pickup from stores".
  - **No individual showroom addresses, branch list or map page was found.** [not found in index]
  - The About page says it sells "at its exhibitions in Riyadh and via its website".
- **Phone:**
  - "+966506412556", in the footer and on the terms page. [verified]
  - Landline "011 2166686", in the return policy text: "The customer should contact the customer service team by calling 011 2166686 during working hours" (https://goldentech.com.sa/en/return-exchange). [verified via one snippet summary; a second search did not reproduce it]
- **WhatsApp:** no WhatsApp number or link was found on goldentech.com.sa in the index. magicpin shows a WhatsApp button, but the number is unknown. [not found in index]
- **Email:**
  - info@goldentech.com.sa (footer, terms, return policy). [verified]
  - online@goldentech.com.sa (Facebook page). [verified]
  - There are two addresses with no explanation of which one to use.
- **Hours:** "Saturday - Thursday 09:00 AM - 10:00 PM / Friday: Closed". [verified]
- **Social accounts:**
  - X: @GoldenTechSA, "التكنولوجيا الذهبية", joined March 2019. Bio: "متخصصة في بيع أجهزة الكمبيوتر المكتبي والمحمول والأكسسوارات وقطع غيار الكمبيوتر,سيرفرات الشركات,الطابعات والماسح" (https://x.com/GoldenTechSA). [verified]
  - Facebook: facebook.com/goldentechsa ("Golden Technology (@goldentechsa)", phone +966 50 641 2556). [verified]
  - Instagram: @goldentechsa, "14K followers, 0 following, 1,884 posts" (https://www.instagram.com/goldentechsa/). [verified]
  - Snapchat: @goldentechsa, "Last updated: 10/26/2025" (https://www.snapchat.com/@goldentechsa). [verified]
  - YouTube: @GoldenTechKSA ("Golden Tech"). The about-page metadata shows an interactionStatistic of 557, probably subscribers (https://www.youtube.com/@GoldenTechKSA/about). [verified; the meaning of 557 is inferred]
    - The YouTube handle is "GoldenTechKSA" while every other platform uses "goldentechsa". The handles are inconsistent.
  - LinkedIn: /company/goldentechsa, "65 followers", 11–50 employees. [verified]
  - TikTok: no official goldentechsa TikTok was found. The TikTok @golden.tech.store belongs to a different "Golden tech store". [not found in index]
- **Authorised-reseller claims:**
  - About page: "one of the authorized distributors of international private companies in the field of computers". This is generic: **no brand is named**. [verified]
  - No ASUS, Dell, Lenovo, HP or Apple partner badges or "Authorised Reseller" pages were found. [not found in index]
  - The warranty is "by the agent". The warranty page says "Warranty and maintenance services … that are provided by the agent are not considered the responsibility of The Golden Technology. The customer must contact directly with the agent." (https://goldentech.com.sa/en/warranty-maintenance) [verified]
- **Third-party ratings:**
  - magicpin: 4.8 from 379 ratings. The listing sits under "Al-Shumaisi" while the address is Olaya St, and it **miscategorises the business as an "IT Staffing and Consulting firm"** (https://magicpin.com/saudi-arabia/Riyadh/Al-Shumaisi/Electronics/Golden-Technology/store/228503c). [verified via snippet summary]
  - arabplaces: 4.5 from 43 reviews, category "Computer Store"; reviews praise staff, prices and online instalments (https://sa.arabplaces.com/riyadh/golden-technology-184930). [verified]
  - Cybo: 4.5 from 173 reviews (https://www.cybo.com/SA-biz/golden-technology-التكنولوجيا-الذهبية). [verified]
  - reviewsaudi.com: 48 reviews, mostly positive, latest from January 2024 (https://reviewsaudi.com/riyadh/golden-technology-65509). [verified via snippet summary]
  - PrimeBizList: "(402) reviews". [verified via snippet summary]
  - Google Maps: no live figure retrievable. [not found in index]
  - Trustpilot: no listing for goldentech.com.sa. The goldentech.com Trustpilot page is a different company, a US lift-chair maker. [verified]
  - **On-site product reviews or ratings: not found in index.** [not found in index]
- **ScamAdviser:** "High trust rating"; "very likely not a scam but legit and reliable"; a valid SSL certificate was found; "link-shortening" is listed as a negative (https://www.scamadviser.com/check-website/goldentech.com.sa). [verified]
  - No numeric score was visible, and the cache is about 17 months old.
- **Payments:**
  - "Visa and MasterCard credit cards and Mada cards", with "no extra fees", plus "Pay in installments with a credit card", where plans vary by bank (https://goldentech.com.sa/en/payment-methods). [verified]
  - **Tabby and Tamara were not found.** [not found in index]
  - Apple Pay and STC Pay were not found in the index either.
  - Promotions advertise "تقسيط بدون فوائد" (interest-free instalments) and "installments for 4 months". [verified]
- **Returns:**
  - Window: "should not exceed 7 Days from the date of receipt" (https://goldentech.com.sa/en/return-exchange).
  - Excluded: "all computer accessories and computer software".
  - Returns go "through our authorized shipping service providers or personally to the headquarters".
  - A 79 SAR fee applies in some cases.
  - [verified] The accessories exclusion is consumer-unfriendly.
- **Warranty:**
  - "all electronic devices from Technology gold have been guaranteed for two years by the agent".
  - A 79-riyal device transport fee applies in areas without a service centre (https://goldentech.com.sa/en/warranty-maintenance). [verified]
- **Loyalty programme:** 1,000 points = 10 SAR. Points are online-only, non-transferable, and expire after an unstated period. The programme "can amend, suspend, or end … at any time without prior notice" (https://goldentech.com.sa/en/loyalty-program). [verified via snippet summary]
- **Brand-confusion risk from similarly named domains:**
  - goldentech-sa.com: a B2B IT company in Al Hamra, Riyadh, with different phone numbers.
  - goldentechksa.com: "جولدن تيك ستور Golden Tech Store", selling PS5 bundles.
  - goldentech.tech: Egypt.
  - goldentechmarket.com.
  - [verified that these exist; inferred risk] The site does nothing visible to distinguish itself from them.

## 5. Localisation

- **A full Arabic store view exists at `/ar/`.** [verified] Examples:
  - `/ar/laptop-asus-tuf-gaming-fa607nug-rl154-amd-ryzen-7-7445hs-rtx-4050.html`: "لابتوب العاب Asus TUF FA607N معالج AMD رازين 7-7445HS". Arabic and Latin are mixed in one product title.
  - `/ar/desktop/hp.html`: "اشترِ أجهزة كمبيوتر مكتبي hp بضمان عامين". The brand is lowercase "hp".
  - `/ar/laptop-acer-aspire-lite-al16-54p-intel-core-i5-nx-d76em-003.html`: "لابتوب Acer Aspire Lite AL16 بمعالج Intel Core i5-1334U - رام 16GB".
  - `/ar/laptop-asus-rog-zephyrus-g16-gu605cr-qr216w-gaming-ultra-9-90nr0lz6-m00bd0.html`: "اشتر الان لابتوب اسوس روج زيفروس G16 GU605CR للألعاب". Here the brand is transliterated (اسوس روج زيفروس), whereas the TUF title keeps "Asus" in Latin, so brand naming is inconsistent across Arabic titles.
  - `/ar/laptop-lenovo-thinkpad-e16-intel-core-ultra-5-226v-22ay0000ad.html`: "لاب توب لينوفو ثينك باد E16 معالج انتل كور ألترا 5-226V, الرامات 16 جيجابايت…". This title spells "لاب توب" (two words) while others use "لابتوب". It also uses Latin commas.
  - `/ar/laptop/business.html`: "تسوق أفضل أجهزة لابتوب للأعمال بالسعودية| التكنولوجيا الذهبية".
  - `/ar/laptop-pc-gaming-offers.html`: "عروض ذهبية على لابتوب قيمنق وبي سي قيمنق وشاشات قيمنق". "قيمنق" is a colloquial transliteration of "gaming".
- **Arabic titles are indexed on `/en/` URLs** (all [verified] as title+URL pairs):
  - `/en/` → "التكنولوجيا الذهبية أكبر متجر لأجهزة اللابتوب والكمبيوتر ..."
  - `/en/laptop.html` → "تسوق كمبيوتر لابتوب بأفضل الأسعار"
  - `/en/laptop/gaming.html` → "أحدث لابتوب قيمنق لتلبية احتياجات اللاعبين"
  - `/en/desktop.html` → "أحدث جهاز كمبيوتر مكتبي بأفضل الأسعار"
  - `/en/saudi-national-day-offers.html` → "عروض اليوم الوطني السعودي على اللابتوبات والشاشات ..."
  - `/en/terms-and-conditions` → "الشروط والأحكام"
  - The same URLs also index with English titles. [inferred] Possible causes: hreflang or canonical misconfiguration, store-view cookies or IP-based switching serving Arabic content on `/en/` URLs, or Google choosing the Arabic title for Arabic queries. Treat this as a **likely hreflang or canonical defect, to be confirmed live**.
- **Arabic blog posts live under the English path**:
  - `/en/blog/post/كيفية-معرفة-مواصفات-الكمبيوتر-الخاص-بك-بسهولة`
  - `/en/blog/post/مواقع بيع لابتوبات في السعودية`. This slug contains **literal spaces (%20)**.
  - [verified]
- **Policy page naming:** "FAQ EN" (`/en/faqs`) and "FAQs AR" (`/ar/faqs`) are indexed as the actual page titles. These are internal CMS labels exposed as `<title>`. [verified]
- **Currency display:**
  - Arabic pages use "ر.س", e.g. "سعر خاص 2499 ر.س … شاملة الضريبة" (https://goldentech.com.sa/ar/laptop/microsoft.html). [verified via snippet summary]
  - English snippets show bare numbers with "Tax included", e.g. "Special Price 2299 Regular Price 2499 -8% Tax included Save 200" (https://goldentech.com.sa/en/laptop/hp.html). [verified]
    - [inferred] The currency label is possibly missing or icon-only on EN, to be confirmed live.
  - **The new Saudi Riyal symbol (⃁) was not found.** [not found in index]
- **VAT-inclusive labelling:** "Tax included" (EN) and "شاملة الضريبة" (AR) are present on price boxes. [verified]
- **Price-box microcopy:** "Special Price … Regular Price … -8% … Save 200". The discount is shown as both a percentage and an amount. [verified]

## 6. SEO and content-quality red flags (quotes)

- **Ungrammatical or broken titles and copy:**
  - "Shop best Gaming laptop with in KSA": `/en/laptop/gaming.html` [verified]
  - "Now can get your Laptop, Computer, Apple Mac, Printers, Servers, Gaming Laptop with best price in KSA from Golden Technology": homepage [verified]
  - "Shop Now Laptop Gaming, PC Gaming & Monitors Gaming": `/en/laptop-pc-gaming-offers.html` [verified]
  - "Discover all new Laptops computers with 2 years warranty & best price in KSA": `/en/laptop.html` [verified]
  - "Shop best Business dell laptop in KSA": `/en/laptop/business/dell.html` [verified]
  - "Microsoft Devices - Best Deals on Surface Laptops, Tablets, and Accessories| golden tech": `/en/microsoft.html` [verified]
  - "Golden Tech Terms and Conditions |Golden Tech online": `/en/terms-and-conditions` [verified]
  - "Shop Laptops Accessories offers| Golden Technology" and "Shop Laptops bags offers| Golden Technology" [verified]
  - "Discount till 61%": homepage or demo [verified via snippet summary]
  - "The Golden Technology Trading Company and E-marketing had established in Riyadh…": About [verified]
- **Garbled policy text:**
  - Warranty (https://goldentech.com.sa/en/warranty-maintenance): [verified]
    - "All electronic devices from Technology gold have been guaranteed for two years by the agent."
    - "Accessories and accessories maybe have guaranteed for one year by the agent or The Gold Technology in case there is no agent for the product in the kingdom of Saudi Arabia."
    - "The warranty of the devices that are assembled by the customer (gaming devices is only on the internal parts by the agent or from the gold technology, and excludes from the warranty service attempts to repair them by non-authorized parties." The opening parenthesis is never closed.
    - "…are not considered the responsibility of The Golden Technology. The customer must contact directly with the agent."
  - Terms and returns:
    - "A colored dot or colored or dead pixel is not considered a defect or a manufacturing defect if it is less than 4 points." [verified via snippet summary]
    - "The use of the website services is only available to people who are able to legally represent themselves in accordance with the system of the Kingdom of Saudi Arabia." [verified]
  - The company name is rendered four different ways in English: "Golden Technology", "Golden Tech", "golden tech", "Technology gold" / "The Gold Technology" / "the gold technology". The Arabic is التكنولوجيا الذهبية.
- **Default or template titles (thin SEO):** "2 in 1 - Laptop", "Adaptor - Accessories", "Power Extension - Accessories", "New Arrival", "All Brands Page", "FAQ EN", "FAQs AR", "LG", "AOC", "Golden Tech". [verified]
- **Duplicate titles:**
  - `/en/offers.html` and `/en/laptops-computers-and-gaming-monitors-offers.html` both use "Golden Offers on laptops, computers & gaming monitors".
  - `/en/` and `/en/home-page-02-66d465ea485bb` both use "Golden Technology Home of Laptop & Computers in KSA".
  - [verified]
- **Indexed URL junk:**
  - `/?gad_source=1`
  - `/en/catalogsearch/result/?amnoroute=&q=…`
  - `/en/laptop/dell.html?p=2`, i.e. pagination is indexed
  - `/en/hp-offers.html?p=2`
  - [verified]
- **Inconsistent product URL slugs:**
  - `laptop-microsoft-microsoft-surface-7-edition-snapdragon-x-elite-15-inch-zhq-00014.html`, with "microsoft" doubled.
  - `microsoft-surface-laptop-4-13-inch-5pb00040.html`, which has no "laptop-" prefix.
  - `laptop-acer-gaming-nitro-v-15-anv15-51-76hp-1.html`, with a "-1" duplicate suffix.
  - [verified]
- **Product title style inconsistency:**
  - Some product titles end with "|Golden Tech KSA", e.g. "Laptop Acer Gaming Nitro v 15 Intel Core i9-13900H CPU, RTX 4060 8GB |Golden Tech KSA". That title also has a lowercase "v". Others have no suffix.
  - Missing spaces such as "Graphics,13-inch Touch Display".
  - [verified]
- **Stale or legacy products still indexed:** "Laptop Microsoft Surface Pro 8 … Windows 10 Pro - Platinum" (`/en/laptop-microsoft-surface-pro-8-intel-core-i7-1086.html`). [verified; current stock status unknown]
- **Counts with no space:** "91items", "41items", "3items", "1item". [verified]
- **Typo'd prices:** none found in the index. [not found in index]
- **Meta descriptions:** the actual `<meta name="description">` could not be extracted. Snippets show templated intros: "Discover [X] with 2 years warranty & best price in KSA from Golden Technology". [verified pattern; inferred to be the meta template]

## 7. Content, tools, B2B

- **Blog** `/en/blog` ("Blog"). [verified]
  - Indexed posts are from August 2025:
    - Best Dell laptops (14 Aug 2025)
    - Laptop specs for programming (11 Aug 2025)
    - Choosing a work laptop (7 Aug 2025)
    - Where to buy printers (26 Aug 2025)
    - كيفية معرفة مواصفات الكمبيوتر الخاص بك بسهولة
    - مواقع بيع لابتوبات في السعودية
  - Posts are in Arabic but under the `/en/` path.
  - No posts after August 2025 were found, so the blog may be stale. [inferred]
- **Buying guides:** only the blog posts above. There is no dedicated buying-guide hub. [not found in index]
- **PC builder or configurator: not found in the index.** PC Gaming is sold only as pre-built SKUs grouped by CPU (i5, i7, i9, Ryzen 5/7/9) and by RTX. [verified that pre-builts exist; not found for a configurator]
  - The warranty page mentions "devices that are assembled by the customer (gaming devices", which implies custom builds happen offline. [inferred]
- **Compare tool:** the standard Magento "Add to Compare" exists. No dedicated spec-comparison page was found. [verified / not found]
- **Corporate, B2B or wholesale:**
  - The About page says "the wholesale at the local level" division exists. [verified]
  - **No corporate-sales page, RFQ or quotation form, or B2B portal was found** on goldentech.com.sa. [not found in index]
  - The "Business laptops" category and the business offers page are consumer-style category pages.
  - goldentech-sa.com, a different entity, has a "B2B Solutions" section, which could confuse B2B searchers. [verified that it exists]
- **Loyalty programme:** exists, see section 4.
- **Click and Collect:** mentioned in the FAQ ("Click and Collect" service for pickup from stores). [verified via snippet summary] No store-picker page was found.

## 8. Gaps: not searched or not resolved (search budget exhausted)

These were planned but never ran, because the shared search budget ran out. Each needs a live check:
- The X post about the "Saudi e-stores directory": exact wording, date, and which directory.
- The Arabic homepage section labels (وصل حديثاً / صفقة اليوم / تسوق حسب الماركة).
- The Arabic return-policy text, to compare with the English for translation drift.
- A dedicated contact-us page, map, or branch list.
- Product-page microcopy: warranty label, SKU, out-of-stock and "notify me" behaviour.
- Things that need a live render:
  - autocomplete
  - language-switcher label and placement
  - top-bar copy
  - mega-menu layout
  - the live `<link rel="alternate" hreflang>` and canonical tags (to confirm the EN/AR title bleed)
  - footer badges (SBC/Maroof, VAT certificate, payment logos)
  - currency symbol on EN prices
  - whether the new Riyal sign ⃁ is used

## 9. Live probe from the audit environment (22 Oct 2026)

- After the environment allowed goldentech.com.sa, both `curl` and headless Chromium (Playwright) received **HTTP 403 "Sorry, you have been blocked"** from Cloudflare (Ray ID a4e7a33b8e8c5d04, IAD data centre). The block is a firewall rule on the client, not a JS challenge. No bypass was attempted. A live walkthrough has to run from a normal network (e.g. the auditor's laptop in KSA).
- The response's HTTP 103 Early Hints exposed the front-end stack [verified]:
  - **Magento 2**, theme **`Sm/venuse`** (SM Venuse, a commercial Magento theme): `/static/version1791448477/frontend/Sm/venuse/en_US/…`
  - **Aramex** shipping with Aramex location/address validators: `Aramex_ApiLocationValidator/js/location_validator.min.js`, `Aramex_Shipping/js/location_validator.min.js`. Some address validation likely exists at checkout; F39 (National Address) still needs a live check.
  - **Amasty AJAX cart**: `js/rebind-amcart.min.js`, matching the `amnoroute` search parameter (Amasty extensions).
  - Static assets are served from merged/minified bundles (`_cache/merged/…min.css`, `styles-l.min.css`).
