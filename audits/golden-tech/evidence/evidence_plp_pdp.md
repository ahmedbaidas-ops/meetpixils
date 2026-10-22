# Evidence: PLP + PDP, goldentech.com.sa (Golden Technology / التكنولوجيا الذهبية)

**How this was gathered:** about 50 WebSearch (extended) queries were run on 2026-10-22. The container network and WebFetch were down, so no live page was opened. The shared search budget for the turn ran out before every planned query was sent; the facet query for the gaming-monitor PLP was the one that did not run.

- **[verified: quote+URL]** means the search summariser quoted the text from the indexed copy of that URL. Index snapshots have **different, mostly unknown dates**: some pages were flagged as about 500 to 580 days old. A price mismatch between two URLs can therefore be a real inconsistency or just a timing difference. Each case below says which.
- **[inferred]** means my own reading of the evidence.
- **not found in index** means the search could not surface the item. It does not mean the item is absent from the live site.

---

## 1. PLP: category structure and naming

- **[verified: URLs]** Laptops are split **by type and then by brand**: `/en/laptop/gaming.html` → `/en/laptop/gaming/asus.html`, `/acer.html`, `/lenovo.html`, `/hp.html`, `/dell.html`, `/gigabyte.html`. `/en/laptop/business.html` has the same pattern (`/business/hp.html`, `/business/dell.html`, `/business/asus.html`). There are also brand-only pages such as `/en/laptop/asus.html`, `/en/laptop/hp.html` and `/en/laptop/apple.html`, plus `/en/laptop/2-in-1.html`.
- **[verified: quote+URL]** The type facet on https://goldentech.com.sa/en/laptop.html is "Laptop, 2-in-1 Laptop, Business Laptop, 2-in-1 Business Laptop, Gaming Laptop, and Mobile workstation".
- **[verified: not found in index]** No **student** or **creator / content-creation** category was found. The nearest page is a seasonal landing page, https://goldentech.com.sa/en/back-to-school-offers.html ("Back to School Offers Laptops & Tablets").
- **[verified: URLs]** PC Gaming sub-categories are cut **by component**: `/en/pc-gaming/intel-core-i5.html`, `/en/pc-gaming/intel-core-i9.html`, `/en/pc-gaming/rtx.html`.
- **[verified: URLs]** Gaming monitors are cut **by spec**: `/en/gaming-monitors/hdmi-2-1.html`, `/240hz.html`, `/oled.html`, `/2k.html`, `/4k.html`. Apple is cut by line and size: `/en/apple/apple-air/13-inch.html`, `/15-inch.html`, `/en/apple/apple-pro/14-inch.html`.
- **[inferred]** Spec values such as refresh rate, resolution and CPU are built as **separate category pages instead of filters**. This works for SEO, but a shopper cannot combine them (for example 240Hz + OLED + 27").
- **[verified: URLs]** There are many overlapping offer landing pages: `/en/offers.html`, `/en/laptops-computers-and-gaming-monitors-offers.html`, `/en/laptop-pc-gaming-offers.html`, `/en/mega-sale.html`, `/en/business-laptops-offers.html`, `/en/hp-offers.html`, `/en/saudi-national-day-offers.html`, `/en/deal-of-the-day.html`, `/en/back-to-school-offers.html`, `/en/gaming.html` ("Shop Gaming Computers & Laptops offers").
- **[verified: quote+URL]** A **test category is public and indexed**: https://goldentech.com.sa/en/category-test.html, with the page title "Category Test" and the heading "Best PC Gaming Offer". It lists real gaming-PC products, including one at special price 8,499.
- **Meta-title and copy defects:**
  - **[verified: title+URL]** "Shop best Gaming laptop with in KSA" (https://goldentech.com.sa/en/laptop/gaming.html)
  - **[verified: title+URL]** "Shop best Business dell laptop in KSA" (https://goldentech.com.sa/en/laptop/business/dell.html)
  - **[verified: title+URL]** "ٍShope Computer Wireless Keyboards", which has a stray Arabic diacritic and the typo "Shope" (https://goldentech.com.sa/en/accessories/keyboard.html)
- **[verified: title+URL]** The Arabic ASUS PLP title is "اشتر كمبيوتر لابتوب أسوس بضمان عامين" (https://goldentech.com.sa/ar/laptop/asus.html). The gaming PLP carries "2 years warranty & best price in KSA" (https://goldentech.com.sa/en/laptop/gaming.html).

## 2. PLP: filters, sorting, pagination

- **[verified: quote+URL]** Sort options on the gaming laptop PLPs are "Position, Best Sellers, and Most Viewed" plus a wishlist-count option and a "Set Descending Direction" toggle (https://goldentech.com.sa/en/laptop/gaming/asus.html).
  - **Price sort** on the standard PLPs: not found in index.
  - The Deal of the Day page sorts "by biggest saving or price" (https://goldentech.com.sa/en/deal-of-the-day.html).
  - **[inferred]** Leading with "Position / Most Viewed / wishlists" and possibly having no price sort is weak for spec- and price-driven buyers.
- **[verified: quote+URL]** Filters on the gaming brand PLPs:
  - Processor family: "Intel Core i5, Intel Core i7, Intel Core Ultra 7, Intel Core Ultra 9, Intel Core i9, AMD Ryzen 5, AMD Ryzen 7, and Show more" (https://goldentech.com.sa/en/laptop/gaming/lenovo.html).
  - RAM from 8 GB to 64 GB (asus.html).
  - Storage, graphic card and display (https://goldentech.com.sa/en/laptop/gaming/gigabyte.html).
  - **Price buckets** "0.00 - 10000.00" and "10000.00 - 20000.00" (gigabyte.html). **[inferred]** A single 0 to 10,000 SAR bucket covers almost the whole catalogue, so it is useless.
- **[verified: quote+URL]** Business PLP facets (https://goldentech.com.sa/en/laptop/business.html):
  - Memory: "8 GB 16items; 16 GB 74items; 24 GB 4items; 32 GB 24items", plus a separate "24GB DDR5" value, which is a duplicate attribute value.
  - Storage: "1TB 48items; 256GB 3items; 512GB 68items". **[inferred]** This is sorted as text rather than by size, and the counts have no space ("16items").
  - Graphics: "Intel, NVIDIA 2GB, NVIDIA 4GB".
  - **Processor** and **screen-size** facets on this page: not found in index.
- **[verified: quote+URL]** The PC Gaming facets are GPU memory ("NVIDIA 6GB ... 32GB, plus AMD 16GB") and Price (https://goldentech.com.sa/en/pc-gaming.html). The Core i9 PLP has storage, graphics card, operating system and colour (https://goldentech.com.sa/en/pc-gaming/intel-core-i9.html).
- **Refresh-rate and screen-size facets:** not found in index. Refresh rate is handled by category URL (`/gaming-monitors/240hz.html`). The search budget ran out before the monitor-PLP facet query.
- **[verified: quote+URL]** Pagination uses numbered pages, not load-more. The main laptop page shows "Items 1-32 of 323", with page links to 5 and "Next" (https://goldentech.com.sa/en/laptop.html), and the business PLP shows "Items 1-32 of 119".
  - There is a "Show per page" control. Its options were not found in index.
  - The Apple PLP is paginated with `?p=2` (https://goldentech.com.sa/en/apple.html?p=2).

## 3. PLP: product card content

- **Title format** **[verified: titles+URLs]**: the titles are long spec strings of about 115 to 140 characters, with the category word placed first and spec separators that vary. Examples:
  - "Laptop Asus ROG Strix G614PR Gaming AMD Ryzen 9-8940HX Processor, 32GB Ram, 1TB SSD M.2, NVIDIA GeForce RTX 5070 Ti 12GB,16-inch Display" (136 chars; no space after the comma)
  - "Laptop Lenovo LOQ 15IRX10 Gaming Intel Core i7-13645HX Processor, 16GB Ram, 512GB SSD M.2, NVIDIA GeForce RTX 5060 8GB Graphics, 15.6-inch" (138 chars)
  - "PC Gaming Intel Core i5-14400F Processor, 16GB Ram, 1TB SSD M.2, RTX 3050 6GB GPU, Windows 11 Professional - Black" (114 chars)
  - The card example in the brief, "Asus TUF Gaming FA607NUQ AMD Ryzen 7-170 Processor, 32GB Ram, 1TB SSD M.2, NVIDIA GeForce RTX 4050 6GB, 16-inch", was confirmed on https://goldentech.com.sa/en/laptop/gaming.html.
- **Price block** **[verified: quote+URL]**: the cards read "Special Price 3199 Regular Price 3499 -9% Tax included" and "Special Price 22999 Regular Price 25799 -11% Tax included" (https://goldentech.com.sa/en/laptop/gaming/asus.html).
  - So each card shows a was-price, a percentage discount badge and a VAT-inclusive note.
  - In Arabic: "سعر خاص 469 السعر العادي 699".
  - **[inferred]** No "SAR"/"ر.س" text appears next to the numbers in the EN snippets. The currency may be an icon glyph, so check this visually.
- **Stock on card** **[verified: quote+URL]**: "Not available" shows on the RTX 5060 Ti build at 6,249 (7,549) on https://goldentech.com.sa/en/pc-gaming/intel-core-i5.html. Out-of-stock items stay listed in the PLP.
- **Wishlist and compare** **[verified: quote+URL]**: the listings show a "Wish List Compare" button pair (https://goldentech.com.sa/en/laptop/2-in-1.html and others).
- **Rating on card** **[verified: quote+URL]**: the brand PLP shows review counts, for example the Golden Tech RTX 5070 PC with "1 review" and a white variant with "2 reviews" (https://goldentech.com.sa/en/shop-by-brand/golden_tech).
- **Add-to-cart on card:** not found in index.
- **Installment price on card:** not found in index. Installments appear only as page-level banner copy, such as "installment on 4 months" on https://goldentech.com.sa/en/business-laptops-offers.html.

## 4. PDP samples (9 products)

### PDP-1: Gaming laptop, ASUS ROG Strix G16 G614PR
https://goldentech.com.sa/en/laptop-asus-rog-strix-g16-g614pr-gaming-golden-technology.html

- **[verified]** "Special Price 9799 Regular Price 10999", tax included, in stock, "24-month ASUS warranty".
- **[verified]** Delivery: "Riyadh 24 hours, other cities 3-6 business days".
- **[verified]** Model "G614PR-RV009W". Specs: 16" WUXGA IPS 165Hz with G-Sync, 32GB DDR5, Windows 11 Home.
- **[verified]** Payment copy: "No down payment – pay in 3 months with no fees, or up to 36 months". The provider was not named in the snippet.
- **[verified: URL]** There is a **duplicate PDP** for the same SKU: https://goldentech.com.sa/en/laptop-asus-rog-strix-gaming-g614pr-rv009w-ryzen-9-8940hx-90nr0nj7-m000e0.html ("Asus ROG Strix G16 G614PR Gaming Laptop").
- **[inferred]** The URL slug includes "-golden-technology", which looks like keyword stuffing.

### PDP-2: Gaming laptop, Lenovo LOQ 15IRX10 83JE01BWAD
https://goldentech.com.sa/en/laptop-gaming-lenovo-loq-15irx10-intel-core-i7-13645hx-83je01bwad.html

- **[verified]** "Special Price 6899 Regular Price 7499", tax included.
- **[verified]** Spec lines "Full HD 1920x1080, IPS, 144Hz, 100% sRGB, Free Dos - Luna Grey", "Warranty Period: 24 Months" and "Model Number: LOQ 15IRX10". These are structured spec lines.
- **[verified]** The Arabic version of the same SKU, https://goldentech.com.sa/ar/laptop-gaming-lenovo-loq-15irx10-intel-core-i7-13645hx-83je01bwad.html, shows **5299 (5699)**.
- **[inferred]** The EN and AR stores show a 1,600 SAR gap for one SKU. This could be a snapshot-timing difference, but it is worth checking live.
- **Stock:** not found in index.

### PDP-3: Gaming PC, own brand, Core i5-14400F + RTX 5060 (SKU P10/25)
https://goldentech.com.sa/en/pc-gaming-intel-core-i5-14400f-rtx-5060-8gb-gpu-p10-25.html

- **[verified]** "Special Price 3999 Regular Price 4999". The snapshot was flagged as about 503 days old.
- **[verified]** "Free shipping - Installments in 4 payments" and "24 Months Warranty by Golden Tech".
- **[verified]** Named component list: "GIGABYTE GeForce RTX 5060 WINDFORCE OC 8GB", "T-Force Delta (2x8) DDR4 3600MHz RGB", "GIGABYTE H610MH", "XIGMATEK M-Power 700 Watt". **[inferred]** This is a good, transparent component list.
- **[verified]** RAM type conflicts between pages (some say DDR4, others DDR5).
- **[verified]** The same URL has been indexed under two titles: "PC Gaming Intel Core i5-14400F CPU, RTX 5060 8GB GPU" and "...Processor, 16GB Ram, 1TB SSD M.2, RTX5060 8GB GPU, Windows 11 Professional - Black" (no space in "RTX5060").

### PDP-4: Gaming PC, Arabic store, Core i7-14700K + RTX 5080 (P08/25)
https://goldentech.com.sa/ar/pc-gaming-intel-core-i7-14700k-rtx-5080-16gb-gpu-p08-25.html

- **[verified]** Tamara plans: 2 payments of 6,949.5 SAR and 3 payments of 4,633 SAR "with no fees", and **4 payments of 3,474.75/month "includes fees"**.
- **[verified]** Marked unavailable, with a 24-month store warranty.

### PDP-5: Monitor, Samsung Odyssey OLED G6 27" 360Hz (LS27DG602SMXUE)
https://goldentech.com.sa/en/samsung-odyssey-oled-g6-gaming-monitor-27-inch-ls27dg602smxue.html

- **[verified]** "Special Price 3399 Regular Price 4799", tax included, "Not available".
- **[verified]** "24 Months Warranty by Samsung" and the 24-hour Riyadh / 3-6 business days delivery line.
- **[verified]** The AR PDP shows "سعر خاص 3099 السعر العادي 4799": https://goldentech.com.sa/ar/samsung-odyssey-oled-g6-gaming-monitor-27-inch-ls27dg602smxue.html
- **[verified]** The HDMI 2.1 PLP shows a Samsung 1440p OLED at "Special Price 2799 Regular Price 4799": https://goldentech.com.sa/en/gaming-monitors/hdmi-2-1.html
- **[inferred]** The SKU appears at three different prices against the same 4,799 regular price, so the "regular price" anchor looks static.
- **[verified]** Spec conflict on a sibling product: https://goldentech.com.sa/ar/samsung-odyssey-3d-g90xf-gaming-monitor-27-inch-ls27fg900xmxue.html has a title that says 4K and a description that says "FHD 1920x1080". Its PDP showed only installment figures, with no clear total price.

### PDP-6: Desktop, Dell Pro Tower QCT1250, Core Ultra 7 265
https://goldentech.com.sa/en/desktop-dell-pro-tower-qct1250-intel-core-ultra-7-265.html

- **[verified]** "Special 3,799 / Regular 4,299", in stock, **SKU DT1042**, "24 months" Dell warranty.
- **[verified]** Configuration: 8GB RAM, 512GB M.2, integrated graphics, wired keyboard and mouse, Free DOS.
- **[verified]** The page also shows other prices (3,499, 2,899, 999) that are not tied to this SKU. **[inferred]** These are probably a related-products block.
- **[inferred]** SKU "DT1042" is an internal code. The Dell part number was not surfaced, which makes cross-shopping harder.

### PDP-7: Apple, MacBook Air M4 (three SKUs)
- **[verified]** 13" 16/256 Midnight **MW123AB/A**: "Special Price 4199 Regular Price 4499", tax included. https://goldentech.com.sa/en/laptop-apple-macbook-air-13-inch-m4-chip-mw123aba.html
- **[verified]** 13" 24/512 **MC6C4AB/A**: 5999 (6399), in stock. Payment copy: "no down payment … 3 months with no fees or up to 36 months" and "four interest-free payments of 1499.75". https://goldentech.com.sa/en/laptop-apple-macbook-air-13-inch-m4-chip-mc6c4aba.html
- **[verified]** 15" 16/512 **MW1H3AB/A**: 5999 (6499), "Not available", "4 Payments 1499.75/mo" with fees, Apple 24-month warranty, Arabic-English keyboard. https://goldentech.com.sa/en/laptop-apple-macbook-air-15-inch-m4-chip-silver-mw1h3aba.html
- **[verified]** 13" 16/512 **MW0X3AB/A**: "5449 Tax included" with no special price, not available, "24 Months Warranty by Apple". Tamara "4 Payments 1362.25/mo" is labelled شاملة الرسوم (includes fees). Its title ends "- Silver| MW0X3AB/A". https://goldentech.com.sa/en/laptop-apple-macbook-air-13-inch-m4-chip-silver.html

### PDP-8: Accessory, Redragon S101-BA-2 4-in-1 combo
https://goldentech.com.sa/en/redragon-4in1-combo-rgb-led-backlit-gaming-s101-ba-2.html

- **[verified]** "Special Price 229 Regular Price 249", tax included, **SKU S101-BA-2**, In stock.
- **[verified]** Delivery: "Riyadh … 24 hours, and other cities: 3-6 business days".
- **[verified]** "Pay 4 interest-free payments of SAR 57.25" and "24 Months Warranty by Redragon".
- **[verified]** The gaming-mice PLP and the Deal of the Day page list the same item at **199 (249)**: https://goldentech.com.sa/en/gaming/mice.html and https://goldentech.com.sa/en/deal-of-the-day.html

### PDP-9: High-end gaming laptop, Lenovo Legion Pro 7 16IAX10H (83F5005MAD)
https://goldentech.com.sa/en/laptop-gaming-lenovo-legion-pro-7-16iax10h-intel-core-ultra-9-rtx-5080-83f5005mad.html

- **[verified]** 14,499 (16,999), in stock, tax included, 24-month Lenovo warranty.

### Cross-PDP observations

- **Spec sheet:** structured "Label: value" lines (for example "Warranty Period: 24 Months" and "Model Number: …"). **[inferred]** This is probably the Magento "More Information" attributes tab. Whether key specs sit above the fold was not found in index.
- **Images (count, lifestyle vs stock, video, 360):** not found in index.
- **Reviews and ratings** **[verified]**: native ratings exist but are sparse.
  - The i7-14700F RTX 5070 build had "no ratings yet": https://goldentech.com.sa/en/pc-gaming-intel-core-i7-14700f-rtx-5070-12gb-gpu-p12-25.html
  - The i7-12700F RTX 5070 build had "2 reviews averaging 5/5": https://goldentech.com.sa/en/pc-gaming-intel-core-i7-12700f-rtx-5070-12gb-gpu-p03-25.html
  - **Q&A:** not found in index.
- **Related, upsell and cross-sell** (bags, mice, Office, extended warranty): not found in index. The site does sell mice and bags under `/en/accessories.html` and `/en/accessories/mouse.html`.
- **CTA labels** (Add to Cart / Buy Now / أضف للسلة) and **quantity selector:** not found in index. **Compare** is present on listings (see section 3).

## 5. Delivery, shipping fee, warranty and returns: conflicting promises

- **[verified]** The PDP line is "Riyadh 24 hours, other cities 3-6 business days" (PDP-1, PDP-5, PDP-8).
- **[verified]** The PC Gaming PLP advertises "same-day delivery in Riyadh" (https://goldentech.com.sa/en/pc-gaming.html).
- **[verified]** The FAQ says delivery comes "within the period announced on the product page … between 3 to 7 days". Fees there are "10 SAR if the order value is less than 200 SAR" and free at 200 SAR or more, and "Click and Collect" is available (https://goldentech.com.sa/en/faqs and https://goldentech.com.sa/ar/faqs).
- **[verified]** The Terms say "The process of delivery within the city of Riyadh takes 3 to 7 working days, and outside the city of Riyadh is within 7 to 10 working days". They also list "Product delivery cost: 20 SAR per order" and a 20 SAR cash-on-delivery charge (https://goldentech.com.sa/en/terms-and-conditions).
- **[verified]** The return policy reads "the right to return or exchange the products within (7) days from the date of receipt". Repairs or non-qualifying returns carry a 79 SAR fee (https://goldentech.com.sa/en/return-exchange). A return snippet next to the CTA was not found in index.
- **[verified]** Marketing copy says "Free shipping" (PDP-3) and "extra 5% discount with free delivery" (https://goldentech.com.sa/en/offers.html). An X post says "شحن مجاني وسريع لكل مدن المملكة" (https://x.com/GoldenTechSA/status/1852731613991301162).
- **[inferred]** Riyadh delivery is quoted four ways (same day, 24h, 3-7 days, 3-7 working days) and the fee three ways (free, 10 SAR under 200, 20 SAR per order). This is a trust and legal-exposure issue.

## 6. Payment and BNPL messaging

- **[verified]** Tamara instalment tables are on the PDPs (PDP-4, PDP-7). The Lenovo desktop PLP mentions Tabby and Tamara (https://goldentech.com.sa/en/desktop/lenovo.html).
- **[verified]** X posts:
  - Apr 2025: "اختر تقسيطك مع تابي أو تمارا أو MIS، أو الراجحي" (https://x.com/GoldenTechSA/status/1911419101878026726)
  - Nov 2024: "خيارات تقسيط مريحة عبر تابي/تمارا/MISpay/أموال" (https://x.com/GoldenTechSA/status/1852731613991301162)
- **[verified]** The PDPs also carry "pay in 3 months with no fees, or up to 36 months" (PDP-1, PDP-7). The provider was not named.
- **[inferred]** The 4-instalment wording contradicts itself: "4 interest-free payments" (PDP-7, PDP-8) versus "4 payments … includes fees" (PDP-4, PDP-7 MW1H3/MW0X3). The 3- and 36-month plans add a third message.
- **mada / Apple Pay / Tasheel** on the PDP: not found in index.

## 7. Data-quality defects

**Prices**
- **[verified]** The PC Gaming i5-14400F + RTX 5060 appears at four prices:
  - Homepage Deal of the Day: "Special Price 6999 Regular Price 8999" (https://goldentech.com.sa/en/)
  - Offers page: "Special Price 5299 Regular Price 6999" (https://goldentech.com.sa/en/offers.html)
  - Homepage card: 5,599 (7,949)
  - PDP P10/25: 3,999 (4,999), an old snapshot
  - **[inferred]** A "deal" priced above the regular listing of a near-identical build is the clearest credibility problem.
- **[verified: quote; URL is one of the Lenovo/gaming PLPs or the homepage]** Lenovo Legion 5 (i7-14650HX/16GB/512GB) shows "Special Price 16449 Regular Price 16999". Its PDP 83DG005SAD shows 6299 (7199): https://goldentech.com.sa/en/laptop-gaming-lenovo-legion-5-16irx9-83dg005sad.html
  - **[inferred]** This is probably a typo of the same kind as the reported LOQ 15 at 19,999.
  - The **LOQ 15 at 19,999 / 21,999 itself was not found in index**. Two dedicated queries returned only LOQ prices between 2,899 and 7,499.
- **[verified]** Other same-SKU differences between pages:
  - LOQ 15ARP10E: 2,899 (3,299) on the PLP vs 3,299 (3,499) on the PDP
  - LOQ 15AHP10: 4,599 vs 4,649
  - Redragon combo: 229 vs 199
  - Glorious GMMK2: 499 (559) vs 399 on the deal page
  - Samsung OLED G6: 3,399 / 3,099 / 2,799
  - Golden Tech Ryzen 9-9900X RTX 5070 PC: 9,299 vs 10,049 (https://goldentech.com.sa/en/shop-by-brand/golden_tech vs https://goldentech.com.sa/en/pc-gaming.html)

**Naming conventions** **[verified: titles]**
- The word order varies across titles:
  - "Laptop Lenovo Gaming LOQ 15ARP10E…"
  - "Laptop Lenovo LOQ 15IRX10 Gaming…"
  - "Laptop Asus ROG Strix G614PR Gaming…"
  - "Desktop Lenovo ThinkCentre neo 50a 24 All in one Intel core i7…"
  - "Lenovo Desktop ThinkCentre neo 50t Intel Core i5-13400 CPU, 8GB Ram, 512GB **SDD**" (https://goldentech.com.sa/en/lenovo-desktop-thinkcentre-neo-50t-gen-4-12jd0042ax.html)
- The Apple M5 titles drop the "Laptop" prefix and change format: "Apple MacBook Air 13-inch M5 Chip, 16GB Ram, 1TB, 10‑core GPU (Silver) MDH84AB/A" (https://goldentech.com.sa/en/laptop-apple-macbook-air-13-inch-m5-chip-silver-mdh84aba.html).
- Token variants: "RTX5050" / "RTX 5050", "RTX 5060TI" / "RTX 5060 Ti", "Processor" / "CPU", "Ram" / "RAM", "Intel core" / "Intel Core".

**URL and title mismatches** **[verified]**
- https://goldentech.com.sa/ar/laptop-lenovo-loq-15irx9-gaming-83dv01l6ad.html has a slug that says 15IRX9 while the title says 15IRX10. It shows two variants: 4999 (5999) and 6499 (6999).

**Arabic store (RTL) defects** **[verified: title+URL]**
- The AR title "لابتوب لينوفو العاب LOQ 15IRX10 معالج انتل كور آي 13645HX-7" breaks "i7-13645HX" into "13645HX-7". **[inferred]** This is an RTL/bidi rendering error in the source string.
- The AR MacBook title ends "منتصف الليل| MC6L4AB/A" (https://goldentech.com.sa/ar/laptop-apple-macbook-air-15-inch-m4-chip-mc6l4aba.html).
- **English-only content on /ar/ PDPs:** not found in index. The sampled AR PDP titles were translated.
- **[verified: URLs]** The reverse problem was found: Arabic content on the EN store. Examples are blog posts such as https://goldentech.com.sa/en/blog/post/%D8%A7%D9%81%D8%B6%D9%84%20%D9%84%D8%A7%D8%A8%D8%AA%D9%88%D8%A8%20hp ("تسوق افضل لابتوب hp من خلال التكنولوجيا الذهبية"). The search engine also showed /en/laptop/gaming.html with the Arabic title "أحدث لابتوب قيمنق لتلبية احتياجات اللاعبين".

**Stale or out-of-date listings** **[verified]**
- M3 MacBook Air PDPs are still indexed (`…-m3-chip-mrxq3ab.html`, `…-m3-chip-13-6-inch-mxcu3aba.html`) next to M4 and M5.
- Lenovo LOQ 15IRX9 and Legion 5 16IRX9 (2024 generation) are still listed.
- Some index copies are very old: PDP P10/25 was flagged at about 503 days and the OLED G8 EN page at about 583 days.

**Other**
- **[verified]** "Category Test" is a live, indexed page (section 1).

## 8. Competitor comparison (same or similar SKUs, SAR, VAT incl. unless stated)

| Product | Golden Tech | Competitor price(s) | Match quality |
|---|---|---|---|
| MacBook Air 13" M4 16/256 Midnight (MW123AB/A) | **4,199** (4,499). [GT](https://goldentech.com.sa/en/laptop-apple-macbook-air-13-inch-m4-chip-mw123aba.html) | **Jarir 3,999** ("SR 3,999 Inclusive of VAT -11% SR 4,499", trade-in "up to SR 1,200"; snapshot ~393 days). [Jarir](https://www.jarir.com/sa-en/apple-macbook-air-laptops-654285.html). **eXtra 3,824** (structured data). [eXtra](https://www.extra.com/ar-sa/computer/laptops/macbook/apple-macbook-air-m4-16gb-256gb-ssd-13-inch-8-core-gpu-midnight/p/100396506). Aleph 3,899 (OOS). noon / amazon.sa SAR price: not found in index | Exact SKU. GT is about 200 to 375 SAR (5 to 10%) higher [verified figures; dates differ] |
| Lenovo LOQ 15IRX10 i7-13645HX / RTX 5060 / 16GB / 512GB | **6,899** (7,499) EN; **5,299** (5,699) AR. [GT](https://goldentech.com.sa/en/laptop-gaming-lenovo-loq-15irx10-intel-core-i7-13645hx-83je01bwad.html) | **Amazon.sa 5,799**, Win 11 Pro, "FREE delivery 20 - 21 October". [Amazon](https://www.amazon.sa/-/en/Lenovo-15IRX10-i7-13645HX-Graphics-Windows/dp/B0H3HFN5XK). **eXtra 4,799** for i7 / **32GB / 1TB** / RTX 5060, in stock. [eXtra](https://www.extra.com/en-sa/computer/laptops/gaming-laptops/lenovo-loq-15irx10-gaming-intel-core-i7-32gb-1tb-15-6-inch-fhd-144hz-rtx-5060-luna-grey/p/100487319). eXtra 4,299 for i7 / 16 / 512 / RTX 5050 with "shipping rate of SAR 25 to Al Khobar". [eXtra](https://www.extra.com/en-sa/computer/laptops/gaming-laptops/lenovo-loq-15irx10-intel-core-i7-16gb-512gb-rtx5050-15-inch-fhd-luna-grey/p/100508906) | Similar. At the EN price GT is up to 2,100 SAR above eXtra for a lower spec [inferred] |
| ASUS ROG Strix G16 G614PR R9-8940HX / 5070 Ti / 32 / 1TB | **9,799** (10,999). [GT](https://goldentech.com.sa/en/laptop-asus-rog-strix-g16-g614pr-gaming-golden-technology.html) | Microless 9,686.78 ("Sorry, this item is no longer available"). [Microless](https://saudi.microless.com/product/asus-rog-strix-g16-g614pr-gaming-laptop-16-wuxga-ips-165hz-display-amd-ryzen-9-8940hx-32gb-ram-1tb-ssd-geforce-rtx-5070-ti-12gb-gpu-english-arabic-k-b-win11-eclipse-gray-90nr0nj7-m000e0/). eXtra / Jarir / noon: not found in index | Exact. Roughly at parity |
| Dell Pro Tower QCT1250 Ultra 7 265 | **3,799** (4,299), **8GB / 512 / FreeDOS**. [GT](https://goldentech.com.sa/en/desktop-dell-pro-tower-qct1250-intel-core-ultra-7-265.html) | **Amazon.sa 3,636** for **16GB / 512 / Win 11 Pro**. [Amazon](https://www.amazon.sa/-/en/Dell-Tower-QCT1250-Ultra-512GB/dp/B0FR2M7WD2). PC Palace 4,090 (16 / 512). Computech 3,685.75 (8 / 512 / Ubuntu). Microless 4,566.96 (16 / 1TB) | Similar. GT costs more for half the RAM and no OS [inferred] |
| Samsung Odyssey OLED G6 27" 360Hz (LS27DG602SMXUE) | **3,399 / 3,099 / 2,799** (all against 4,799). [GT](https://goldentech.com.sa/en/samsung-odyssey-oled-g6-gaming-monitor-27-inch-ls27dg602smxue.html) | Microless **2,636.55** (third-party seller, 2-5 day delivery). [Microless](https://saudi.microless.com/product/samsung-odyssey-oled-g6-g60sd-gaming-monitor-27-qhd-oled-display-360hz-refresh-rate-0-03ms-gtg-response-time-amd-freesync-premium-pro-technology-silver-ls27dg602smxue/). Amazon.sa "2 offers from SAR 3,208.36" (SNXZA variant). [Amazon](https://www.amazon.sa/-/en/SAMSUNG-27-Inch-Odyssey-Anti-Glare-LS27DG602SNXZA/dp/B0D1DPFZLZ) | Exact or near |
| Samsung Odyssey OLED G6 500Hz (LS27FG602SMXUE) | **3,199** (3,799) AR. [GT](https://goldentech.com.sa/ar/samsung-odyssey-oled-g6-gaming-monitor-27-inch-2k-qhd-2560x1440-hdr10-oled-panel-technology-0-03ms-response-time-500hz.html) | Samsung SA official 3,249. [Samsung](https://www.samsung.com/sa_en/monitors/gaming/odyssey-oled-g6-g60sf-27-inch-500hz-oled-qhd-ls27fg602smxue/). Amazon.sa 2,937.72 (search page) | Exact. GT is competitive |
| Redragon S101-BA-2 combo | **229** PDP / **199** PLP | Amazon.sa 224.99 ([search](https://www.amazon.sa/-/en/redragon-combo/s?k=redragon+combo)). Blink 229 (old). KanBkam 259.12 (OOS) | Exact. Parity |

**Competitor PDP and service messaging** **[verified]**
- **Jarir** promises delivery "within 1-3 days to major cities and within a maximum of 5 days to other cities" (https://www.jarir.com/sa-en/macbook-air-m4-2025).
  - Payments: Tabby and Tamara.
  - Dedicated BNPL promo pages exist: "Tabby 10 Payment Terms" (SR 400 to 5,000; the 7 to 13 Sep 2025 window has expired) and "Tamara 12 months Installment" (expired) (https://www.jarir.com/sa-en/tabby-10-payment-terms, https://www.jarir.com/sa-en/tamara-12-months-installment).
  - It also offers trade-in on the PDP.
- **eXtra** shows a "split it your way buy now pay later" banner with tabby and tamara logos on the MacBook PLP (https://www.extra.com/en-sa/computer/laptops/macbook/c/3-303-11/facet/featureEnSeriesName:MacBook%20Air%2015). Its PDPs show a city-specific shipping fee ("SAR 25 to Al Khobar").
- **Amazon.sa** gives a dated delivery ETA ("FREE delivery 20 - 21 October") and an optional accidental-damage protection plan on the LOQ PDP (https://www.amazon.sa/-/en/Lenovo-precision-cooling-built-demanding-multitasking/dp/B0FGQDW8Q6).
- **Microless** shows "2-5 days delivery" and extended warranty options (2 or 3 years) on the PDP.
- **[inferred]** Golden Tech has none of the following that competitors show: a date-specific ETA, trade-in, extended-warranty or protection upsell, or one consistent BNPL message.
