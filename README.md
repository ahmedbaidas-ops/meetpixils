# MeetPixils — Design System

A creative-ecosystem design system serving designers across MENA. Built from a 3-tier W3C DTCG token architecture, four sub-brand themes (Academy / Battle / Experience / Brands), and a hand-built component library.

**Design lead:** Pixilated Studio · Amman
**Version:** v1.0 · April 2026
**Languages:** English + Arabic (RTL day-one)

---

## Pages

| Path | Purpose |
|---|---|
| [`/`](./index.html) | Marketing site — hero, services, work, team, contact |
| [`/system/`](./system/index.html) | The full design system reference — tokens, components, patterns, theming, a11y, voice, lockups |
| [`/claude-demo/`](./claude-demo/index.html) | The same system re-skinned with Anthropic's palette — proof that the discipline transfers |

## Run locally

```bash
python3 -m http.server 4173
# then open http://localhost:4173
```

## Folder layout

```
meetpixils/
├── index.html              ← Marketing
├── styles.css
├── script.js
├── system/
│   ├── index.html          ← Design system reference (16 cards · 7 type tiers · 4 themes)
│   ├── tokens.css          ← 3-tier W3C DTCG tokens (drop-in)
│   ├── system.css
│   └── system.js
├── claude-demo/
│   ├── index.html          ← Claude.ai-style chat re-skin
│   └── claude.css
└── assets/
    ├── meetpixils-logo.png
    ├── meetacademy-logo.png
    ├── meetbattle-logo.png
    └── meetexperience-logo.png
```

## What's inside the system

- **Tokens** — 3-tier (global palette → semantic role → component alias), W3C DTCG 2025.10
- **Mixed radius** — tiles 0px · buttons 14px · images 16px · cards 24px · pills 999px
- **Typography** — Poppins SemiBold for display · IBM Plex Mono for metadata · Noto Sans Arabic for RTL
- **Plum-tinted shadows** — never black; warmth carried into every elevation
- **Per-arm theming** — `data-theme="academy|battle|experience"` swaps brand variables without changing components
- **16 card variants** — course, live battle, event, case study, profile, mentor, stat, quote, pricing, achievement, resource, sponsor, feature, CTA, empty state, loading skeleton
- **WCAG 2.2 AA** — 3px coral focus ring at 25% alpha · `prefers-reduced-motion` honoured throughout
- **Bilingual** — RTL is first-class (logical properties everywhere)

## Re-skinning

The Claude demo demonstrates how the system extends. Same architecture (3 tiers, mixed radius, tinted shadows, mono metadata, icon-led footers, soft squircle cards) — palette swapped from `Orange/Cream/Plum` to `Coral/Cream/Ink`. Components don't change; tokens do.

---

*If the codebase contradicts this brief, the brief wins until updated.*
