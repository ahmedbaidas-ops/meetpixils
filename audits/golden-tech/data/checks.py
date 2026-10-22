import json, sys
D = sys.argv[1]
areas = [
 ("Homepage & landing",8,"First impression, offers and where paid traffic lands"),
 ("Navigation & IA",10,"Menus, category structure and paths to the right product"),
 ("Search",8,"On-site search quality and search hygiene"),
 ("Category pages",12,"Listings, filters, sorting and product cards"),
 ("Product page",18,"Specs, price, delivery, warranty, reviews and buying confidence"),
 ("Cart & checkout",16,"Account, address, payment and order placement"),
 ("Delivery, returns & payments",12,"The promises a shopper weighs before paying"),
 ("Trust & support",8,"Proof of legitimacy and help when something goes wrong"),
 ("Content & localisation",8,"Arabic and English quality, page titles and hygiene"),
]
json.dump([{"area":a,"weight":w,"order":i+1,"scope":d} for i,(a,w,d) in enumerate(areas)], open(D+"/areas.json","w"), ensure_ascii=False, indent=1)
S = {"Pass":1,"Partial":0.5,"Fail":0}
# area, check, weight(1-3), status, evidence, finding
C = [
("Homepage & landing","States what the store sells and why buy here",2,"Partial","Title 'Home of Laptop & Computers in KSA'; meta copy in broken English","F28"),
("Homepage & landing","Category and brand entry points",2,"Pass","New Arrivals, Shop by brand, PC Gaming tiers linked",""),
("Homepage & landing","One clear destination for offers",2,"Fail","8+ offer pages, duplicate titles","F15"),
("Homepage & landing","Featured deals are credible",1,"Partial","Deal of the day at -4%","F16"),
("Homepage & landing","Paid traffic lands on an intent-matched page",2,"Fail","Google Ads click opens the homepage","F14"),
("Homepage & landing","No public test or duplicate homepages",1,"Fail","'Golden EN Home Page Demo' indexed","F25"),
("Homepage & landing","Above-the-fold hierarchy on mobile",2,"Not verified","Needs a live screenshot",""),
("Navigation & IA","Top level organised by product type",2,"Pass","Laptops, Desktops, PC Gaming, Monitors, Apple, Accessories, Printers",""),
("Navigation & IA","Paths by need or budget (study, gaming, work, create)",2,"Partial","Gaming and Business exist; no student, creator or price-band paths","F17"),
("Navigation & IA","Category labels match their contents",2,"Fail","'Gaming' lists peripherals","F18"),
("Navigation & IA","No dead-end or single-product categories",1,"Fail","Servers holds one product","F18"),
("Navigation & IA","One canonical path per category",1,"Fail","Duplicate Microsoft and PC Gaming paths","F18"),
("Navigation & IA","Consistent shop-by-brand",1,"Partial","Exists, but under three URL patterns","F18"),
("Navigation & IA","Business / bulk-buying path",2,"Fail","No quote or corporate page","F32"),
("Navigation & IA","Mobile menu usability",2,"Not verified","Needs a live session",""),
("Search","Search result pages kept out of Google",1,"Fail","/catalogsearch/result/ indexed","F26"),
("Search","Retired products send shoppers to the successor",2,"Partial","Retired URL lands on generic search results","F26"),
("Search","Autocomplete with products and categories",3,"Not verified","Needs a live session",""),
("Search","Model-number and part-number matching",3,"Not verified","Needs a live session",""),
("Search","Typo and Arabic↔English tolerance (لابتوب / laptop)",2,"Not verified","Needs a live session",""),
("Category pages","Filters for key specs (CPU, GPU, RAM, storage)",3,"Pass","Processor, RAM, storage, graphics and display filters on gaming listings",""),
("Category pages","Spec filters can be combined",2,"Fail","Refresh rate, panel and resolution are separate pages","F19"),
("Category pages","Useful price filter",2,"Fail","Two buckets: 0–10,000 and 10,000–20,000","F19"),
("Category pages","Sort by price, rating, newest and best-selling",3,"Fail","Only Position, Best Sellers, Most Viewed, wishlist count found","F20"),
("Category pages","Cards show price, saving and VAT status",2,"Pass","Special / regular price, % badge, 'Tax included'",""),
("Category pages","Scannable card titles with key specs",2,"Fail","115–140 character spec strings","F21"),
("Category pages","Stock status and out-of-stock handling",1,"Partial","'Not available' shown; out-of-stock items mixed into results",""),
("Category pages","Ratings on cards",1,"Partial","Shown, but 0–2 reviews per product","F22"),
("Category pages","Compare and wishlist from the listing",1,"Pass","'Wish List / Compare' on cards",""),
("Product page","Structured spec sheet",3,"Pass","'Label: value' attribute lines (warranty, model number, display)",""),
("Product page","Price shown with VAT status",2,"Pass","'Tax included' / 'شاملة الضريبة'",""),
("Product page","Price matches listings and the other language",3,"Fail","EN 6,899 vs AR 5,299 for the same SKU","F03"),
("Product page","Delivery promise matches the policy",3,"Fail","'24 hours Riyadh' vs '3 to 7 working days'","F02"),
("Product page","Delivery shown as a date",2,"Fail","Shown as a range of days","F23"),
("Product page","Warranty length and provider stated",2,"Pass","'24 Months Warranty by Samsung / Apple / Golden Tech'",""),
("Product page","Instalment price shown",2,"Partial","Tabby / Tamara tables, but fee wording conflicts","F10"),
("Product page","Customer reviews",3,"Fail","0–2 reviews per product","F22"),
("Product page","Stock status",1,"Pass","'In stock' / 'Not available'",""),
("Product page","Specs accurate and consistent",2,"Partial","4K vs FHD conflict; wrong model in URL","F24"),
("Product page","Image gallery, zoom and in-scale images",2,"Not verified","Needs a live session",""),
("Product page","Accessory cross-sell and protection plans",1,"Not verified","None found in the index","F23"),
("Cart & checkout","Guest checkout",3,"Fail","Registration required","F04"),
("Cart & checkout","Phone verification placed late in the flow",2,"Fail","SMS code at sign-up, before buying","F04"),
("Cart & checkout","Total cost known before checkout",3,"Fail","Three delivery-fee rules","F01"),
("Cart & checkout","mada and cards",2,"Pass","Visa, Mastercard, mada with no extra fee",""),
("Cart & checkout","Apple Pay / wallet",2,"Fail","Not on the payment methods page","F11"),
("Cart & checkout","Buy now, pay later at checkout",2,"Pass","Tabby merchant page; Tamara tables on products",""),
("Cart & checkout","Cash on delivery with fee shown upfront",1,"Partial","COD +20 SAR, disclosed only in the Terms","F12"),
("Cart & checkout","Showroom pickup option",2,"Partial","'Click and Collect' in FAQ; no checkout option found","F13"),
("Cart & checkout","National Address (short address) capture",2,"Not verified","No field found in the index","F39"),
("Cart & checkout","Order review before payment",1,"Pass","FAQ: review step before completing the purchase",""),
("Cart & checkout","Inline validation and clear errors",2,"Not verified","Needs a live session",""),
("Delivery, returns & payments","Delivers to all regions of KSA",1,"Pass","FAQ: delivery covers all regions",""),
("Delivery, returns & payments","One delivery fee rule",3,"Fail","20 SAR / 10 SAR under 200 / free","F01"),
("Delivery, returns & payments","One delivery time promise",3,"Fail","Same-day to 10 working days","F02"),
("Delivery, returns & payments","Competitive speed in Riyadh (1–2 days)",2,"Partial","'24 hours' on products, '3–7 working days' in Terms","F02"),
("Delivery, returns & payments","Change-of-mind return window of 14+ days",2,"Fail","7 days, defects only","F06"),
("Delivery, returns & payments","Accessories and instalment orders returnable",1,"Fail","Both excluded","F06"),
("Delivery, returns & payments","Refund timing stated once",1,"Fail","1–5 vs 3–30 days","F07"),
("Delivery, returns & payments","Self-service returns and cancellation",2,"Fail","Phone or email only; 59 SAR cancel fee after shipping","F31"),
("Delivery, returns & payments","Payment options breadth",2,"Pass","mada, cards, card instalments, Tabby/Tamara, COD",""),
("Delivery, returns & payments","Payment page lists every option",1,"Fail","BNPL providers missing","F10"),
("Delivery, returns & payments","Warranty length stated",1,"Pass","Two years via the brand agent",""),
("Delivery, returns & payments","Store owns the warranty claim",2,"Fail","'not considered the responsibility of The Golden Technology'","F09"),
("Trust & support","CR and VAT numbers shown",2,"Pass","CR 1010276436, VAT 311258900400003 in the footer",""),
("Trust & support","Business Platform (SBC) authentication shown",2,"Not verified","No badge found in the index","F29"),
("Trust & support","Showroom address and opening hours",1,"Pass","Olaya computer market, Sat–Thu 9am–10pm",""),
("Trust & support","Contact details consistent",1,"Fail","Two sets of landline hours, two emails","F30"),
("Trust & support","WhatsApp or live chat",2,"Fail","None on the site","F30"),
("Trust & support","On-site review volume",2,"Fail","0–2 reviews per product","F22"),
("Trust & support","Off-site reputation",1,"Pass","4.5–4.8 on arabplaces, Cybo, magicpin",""),
("Trust & support","Professional legal copy and one entity name",2,"Fail","'Technology gold'; 'foundation' vs 'Trading Company'","F08"),
("Trust & support","Named brand authorisations",1,"Fail","'authorized distributors' with no brand named","F29"),
("Trust & support","Order tracking",2,"Not verified","No tracking page found in the index","F31"),
("Content & localisation","Full Arabic store",2,"Pass","Complete /ar/ store view",""),
("Content & localisation","English and Arabic kept separate (hreflang, titles)",2,"Fail","Arabic titles on /en/ URLs; Arabic posts under /en/blog/","F27"),
("Content & localisation","Native-quality English",2,"Fail","'Shop best Gaming laptop with in KSA'","F28"),
("Content & localisation","Consistent brand and product naming",1,"Fail","Store named four ways; 'Asus' vs 'اسوس'","F27"),
("Content & localisation","Customer-facing page titles; no test pages",2,"Fail","'FAQ EN', 'Category Test'","F25"),
("Content & localisation","VAT label in both languages",1,"Pass","'Tax included' / 'شاملة الضريبة'",""),
("Content & localisation","Buying guides",1,"Partial","Blog exists; no posts after Aug 2025",""),
("Content & localisation","New Saudi Riyal symbol",1,"Not verified","Not found in the index","F37"),
]
rows=[]
for i,(a,c,w,st,ev,f) in enumerate(C):
    rows.append({"id":"C%02d"%(i+1),"area":a,"check":c,"weight":w,"status":st,"points":S.get(st),"evidence":ev,"finding":f})
json.dump(rows, open(D+"/checks.json","w"), ensure_ascii=False, indent=1)
# preview scores
from collections import defaultdict
agg=defaultdict(lambda:[0,0,0,0])
for r in rows:
    g=agg[r["area"]]
    g[3]+=1
    if r["points"] is not None:
        g[0]+=r["weight"]*r["points"]; g[1]+=r["weight"]; g[2]+=1
tot=0;wt=0
for a,w,_ in areas:
    e,k,n,t=agg[a]; sc=round(100*e/k); tot+=sc*w; wt+=w
    print(f"{a:32s} {sc:3d}  checks {n}/{t}")
print("overall", round(tot/wt,1), "checks", len(rows), "verified", sum(1 for r in rows if r['points'] is not None))
