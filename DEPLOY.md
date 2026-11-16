# Alira Digital — Deploy checklist (Vercel)

Static HTML site. No build step. Repo root is the site root.

## 1. Before first deploy

- [x] `vercel.json` — clean URLs, no trailing slash, security/cache headers
- [x] `local-demo.js` — production-safe (no refresh→home, no form blocking)
- [x] `404.html` — Vercel-ready (GitHub Pages slash redirect removed)
- [x] Draft `sitemap.xml` (not linked while `robots.txt` disallows crawl)
- [ ] Confirm Facebook page URL (`facebook.com/AliraDigital`)
- [ ] Optional: disable `.github/workflows/deploy.yml` if Vercel is the only host

## 2. Deploy to Vercel

1. Import the Git repo in Vercel (or `npx vercel` from this folder).
2. **Framework Preset:** Other  
3. **Root Directory:** `.` (repo root)  
4. **Build Command:** leave empty  
5. **Output Directory:** leave empty  
6. Assign domain `aliradigital.com` / `www` and set redirects as needed.

Preview URLs stay safe: sitewide `noindex` + `robots.txt` `Disallow: /` until go-live.

## 3. Go-live SEO flip (when content is approved)

```bash
python scripts/go_live_seo.py
```

Then commit, redeploy, and:

- [ ] Confirm `https://aliradigital.com/robots.txt` allows crawl and lists the sitemap
- [ ] Confirm homepage meta is no longer `noindex`
- [ ] Submit sitemap in Google Search Console
- [ ] Spot-check `/contact` WhatsApp + email handoff on production
- [ ] Spot-check `/demos/bright-home-cleaning/` still `noindex` (header + meta)

## 4. Keep noindex forever

- `404.html`
- `brand-preview.html`
- `/demos/**`

## 5. Known content debt (not deploy blockers)

- Malaysia-framed blog posts / Aurora locale leftovers
- Footer still lists some legacy ERP service links (soft-demoted, routes remain)
- Prefer a dedicated JPEG/PNG OG image later (SVG works but social crawlers vary)
