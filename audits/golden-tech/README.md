# Golden Tech (goldentech.com.sa) — UX & UI audit

**Client:** Golden Technology / التكنولوجيا الذهبية, Riyadh (laptops, gaming PCs, monitors, Apple, accessories)
**Prepared by:** Pixilated Studio · October 2026
**Status:** Live-evidence version. A desktop walkthrough in Arabic and English (homepage → search → category → product → cart → checkout → sign-in, 22 Oct 2026) plus the store's policy pages and competitor/Baymard benchmarks. Phone layout and Safari (Apple Pay) still to test.

Live dashboard: https://claude.ai/artifact/Qou2KRNnrgkXdYrGbMPXqg (private until shared)

## Headline

- Overall UX score **48 / 100 (Poor, two points under Fair)** from 110 weighted checks, 102 evidenced.
- 42 findings: 2 critical, 16 major. 12 strengths to keep (instant search, PC finder, spec filters, spec table, sticky buy bar, guest checkout, store pickup, local payments, Riyal symbol, full Arabic store).
- Critical: (1) delivery promise contradicts the Terms ("Riyadh: 24 hours" vs "3 to 7 working days"); (2) returns are 7 days, defects only, accessories and instalment orders excluded (legal review advised).
- Major highlights: cart summary doesn't add up at a glance; checkout stalls on an unclear "Send Otp" step; primary buttons in five styles; no reviews; gaming PCs share one rendered image; no WhatsApp; no quote path for business buyers.
- The live walkthrough corrected three provisional findings: guest checkout exists, store pickup exists, price sort and the new Riyal symbol are in place.

## Folder

| Path | What it is |
|---|---|
| `evidence/` | Raw evidence with quotes and URLs, tagged verified / inferred / not found |
| `data/*.json` | The datasets behind the dashboard (findings, checks, areas, journey, personas, competitors, prices, benchmarks, UI, services) |
| `data/findings.py`, `data/checks.py` | Generators for `findings.json` and `checks.json` + `areas.json` |
| `dashboard/index.html` | Source of the dashboard page (runs inside the Dashboard artifact type) |
| `dashboard/shot_*.js` | Annotated homepage screenshots embedded as data URLs |

## Scoring

Each check is Pass (1), Partial (0.5) or Fail (0) times its weight (1–3). Not-verified checks are excluded. Area score = weighted share passed. Overall = area scores weighted by revenue impact (product page 18, checkout 16, listings 12, delivery/returns/payments 12, navigation 10, homepage 8, search 8, trust 8, content 8, UI & design system 8).

Bands: Critical 0–29 · Poor 30–49 · Fair 50–69 · Good 70–84 · Excellent 85–100 (Pixilated's mapping; Baymard does not publish one).

## Before this goes to the client

Capture phone screens (Arabic + English) and test Apple Pay in Safari to close the 8 "Not verified" checks and the "Verify live" findings; measure contrast on gold and grey text.
