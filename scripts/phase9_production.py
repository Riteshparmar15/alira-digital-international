from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
ORIGIN = "https://aliradigital.com"

KEY = [
    "index.html",
    "services/index.html",
    "industries/index.html",
    "projects/index.html",
    "pricing/index.html",
    "contact/index.html",
    "about-us/index.html",
    "website-design/index.html",
]

# --- 404: remove GitHub Pages slash redirect ---
p404 = root / "404.html"
t404 = p404.read_text(encoding="utf-8")
t404 = re.sub(
    r"\s*<script>\s*// GitHub Pages Smart Redirect[\s\S]*?</script>\s*",
    "\n",
    t404,
    count=1,
)
if 'class="skip-link"' not in t404:
    t404 = t404.replace("<body", '<body', 1)
p404.write_text(t404, encoding="utf-8", newline="\n")
print("404: removed GHP redirect")

# --- brand-preview noindex ---
bp = root / "brand-preview.html"
if bp.exists():
    bt = bp.read_text(encoding="utf-8")
    if "noindex" not in bt:
        bt = bt.replace("<head>", '<head>\n<meta name="robots" content="noindex,nofollow">', 1)
        bp.write_text(bt, encoding="utf-8", newline="\n")
        print("brand-preview: noindex added")
    else:
        print("brand-preview: already noindex")

# --- absolute canonical + og:url on key pages ---
def abs_url(path: str) -> str:
    if path == "/" or path == "":
        return ORIGIN + "/"
    return ORIGIN + path


for rel in KEY:
    path = root / rel
    if not path.exists():
        continue
    text = path.read_text(encoding="utf-8")
    # canonical
    m = re.search(r'<link rel="canonical" href="([^"]*)">', text)
    if m:
        href = m.group(1)
        if href.startswith("/"):
            text = text.replace(
                f'<link rel="canonical" href="{href}">',
                f'<link rel="canonical" href="{abs_url(href)}">',
                1,
            )
    # hreflang
    text = re.sub(
        r'(<link rel="alternate" hreflang="(?:en|x-default)" href=")(/[^"]*)(">)',
        lambda m: m.group(1) + abs_url(m.group(2)) + m.group(3),
        text,
    )
    # og:url
    m = re.search(r'<meta property="og:url" content="([^"]*)">', text)
    if m and m.group(1).startswith("/"):
        text = text.replace(
            f'<meta property="og:url" content="{m.group(1)}">',
            f'<meta property="og:url" content="{abs_url(m.group(1))}">',
            1,
        )
    # og:image relative → absolute
    text = text.replace(
        'content="/assets/img/alira-pro-1-dark.svg"',
        f'content="{ORIGIN}/assets/img/alira-pro-1-dark.svg"',
    )
    text = text.replace(
        'content="/assets/img/alira-pro-1-dark.svg"',  # already done
        f'content="{ORIGIN}/assets/img/alira-pro-1-dark.svg"',
    )
    # twitter:image relative
    text = re.sub(
        r'(<meta name="twitter:image" content=")(/assets/[^"]+)(">)',
        rf'\1{ORIGIN}\2\3',
        text,
    )
    # bump local-demo cache
    text = text.replace("/local-demo.js?v=6", "/local-demo.js?v=9")
    text = text.replace('src="/local-demo.js"', 'src="/local-demo.js?v=9"')
    path.write_text(text, encoding="utf-8", newline="\n")
    print("canonicals:", rel)

# Ensure all HTML still pointing at local-demo get v=9
for html in root.rglob("*.html"):
    t = html.read_text(encoding="utf-8")
    n = t.replace("/local-demo.js?v=6", "/local-demo.js?v=9").replace(
        'src="/local-demo.js"', 'src="/local-demo.js?v=9"'
    )
    if n != t:
        html.write_text(n, encoding="utf-8", newline="\n")

# --- expand sitemap (still draft; robots remains Disallow until go-live) ---
urls = [
    "/",
    "/services",
    "/industries",
    "/projects",
    "/projects/corporate-websites",
    "/pricing",
    "/about-us",
    "/contact",
    "/website-design",
    "/faq",
    "/areas-we-serve",
    "/demos/bright-home-cleaning/",
]
lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    "<!-- Draft sitemap. Linked from robots.txt only after running scripts/go_live_seo.py -->",
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
]
for u in urls:
    loc = ORIGIN + (u if u != "/" else "/")
    if u == "/":
        loc = ORIGIN + "/"
    lines.append(f"  <url><loc>{loc}</loc></url>")
lines.append("</urlset>")
(root / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
print("sitemap expanded")

# --- .gitignore ---
gi = root / ".gitignore"
git = gi.read_text(encoding="utf-8") if gi.exists() else ""
extras = ["", "# Vercel", ".vercel/", "node_modules/"]
for line in extras:
    if line and line not in git:
        git = git.rstrip() + "\n" + line + "\n"
    elif line == "" and not git.endswith("\n"):
        git += "\n"
gi.write_text(git if git.endswith("\n") else git + "\n", encoding="utf-8", newline="\n")
print("gitignore updated")

print("phase9 production prep done")
