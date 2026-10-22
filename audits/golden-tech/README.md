# Golden Tech (goldentech.com.sa) — UX & UI audit

**Client:** Golden Technology / التكنولوجيا الذهبية, Riyadh (laptops, gaming PCs, monitors, Apple, accessories)
**Prepared by:** Pixilated Studio · October 2026
**Status:** Provisional. Built from the store's indexed pages, policies and competitor pages. The live walkthrough (screenshots, checkout walk, visual/design-system layer) is still pending.

Live dashboard: https://claude.ai/artifact/Qou2KRNnrgkXdYrGbMPXqg (private until shared)

## Headline

- Overall UX score **35 / 100 (Poor)**, from 82 weighted checks, 70 of them evidenced.
- 39 findings: 5 critical, 19 major. All critical issues sit in the purchase promises:
  1. Three different delivery fees (20 SAR flat / 10 SAR under 200 / free).
  2. Delivery time from same-day to 10 working days, depending on the page.
  3. Same SKU priced differently across pages and languages (e.g. LOQ 15IRX10: 6,899 EN vs 5,299 AR).
  4. No guest checkout; account + SMS code required before buying.
  5. Returns: 7 days, defects only, accessories and instalment orders excluded (legal review advised).

## Folder

| Path | What it is |
|---|---|
| `evidence/` | Raw evidence with quotes and URLs, tagged verified / inferred / not found |
| `data/*.json` | The datasets behind the dashboard (findings, checks, areas, journey, personas, competitors, prices, benchmarks, UI, services) |
| `data/findings.py`, `data/checks.py` | Generators for `findings.json` and `checks.json` + `areas.json` |
| `dashboard/index.html` | Source of the dashboard page (runs inside the Dashboard artifact type) |

## Scoring

Each check is Pass (1), Partial (0.5) or Fail (0) times its weight (1–3). Not-verified checks are excluded. Area score = weighted share passed. Overall = area scores weighted by revenue impact (product page 18, checkout 16, listings 12, delivery/returns/payments 12, navigation 10, homepage 8, search 8, trust 8, content 8).

Bands: Critical 0–29 · Poor 30–49 · Fair 50–69 · Good 70–84 · Excellent 85–100 (Pixilated's mapping; Baymard does not publish one).

## Before this goes to the client

Run the live session (desktop + phone, Arabic + English) to confirm every "Verify live" finding and the 12 "Not verified" checks, and to audit colour, type, contrast, spacing and tap targets.
