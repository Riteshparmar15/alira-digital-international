"""
Flip the site from preview/noindex to crawlable production SEO.

Run ONLY when the production domain is live and content is approved:
  python scripts/go_live_seo.py

This will:
  - Replace robots.txt with Allow + Sitemap
  - Remove noindex/nofollow from public marketing pages
  - Keep noindex on 404, brand-preview, and /demos/
"""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
ORIGIN = "https://aliradigital.com"

KEEP_NOINDEX = {
    "404.html",
    "brand-preview.html",
}
KEEP_NOINDEX_PREFIXES = ("demos/",)

robots = f"""# Production crawl rules
User-agent: *
Allow: /

# Keep demo sandbox out of search
Disallow: /demos/
Disallow: /brand-preview.html

Sitemap: {ORIGIN}/sitemap.xml
"""
(root / "robots.txt").write_text(robots, encoding="utf-8", newline="\n")
print("robots.txt: allow + sitemap")

changed = 0
for html in root.rglob("*.html"):
    rel = html.relative_to(root).as_posix()
    if rel in KEEP_NOINDEX or rel.startswith(KEEP_NOINDEX_PREFIXES):
        continue
    text = html.read_text(encoding="utf-8")
    new = re.sub(
        r'\s*<meta name="robots" content="noindex,? ?nofollow">\s*',
        "\n",
        text,
    )
    if new != text:
        html.write_text(new, encoding="utf-8", newline="\n")
        changed += 1
        print("indexable:", rel)

print(f"done — removed noindex from {changed} pages")
print("Verify Search Console + sitemap after deploy.")
