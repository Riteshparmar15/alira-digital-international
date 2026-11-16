"""
Phase 8 static + structural audit (no browser).
Checks key routes HTML for functional/responsive risk patterns.
"""
from pathlib import Path
import re
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

root = Path(__file__).resolve().parents[1]
BASE = "http://127.0.0.1:8010"
pages = [
    "/",
    "/services/",
    "/industries/",
    "/projects/",
    "/pricing/",
    "/contact/",
    "/about-us/",
    "/demos/bright-home-cleaning/",
]

results = []

def check(label, cond, detail=""):
    results.append((bool(cond), label, detail))


def fetch(path):
    req = Request(BASE + path, headers={"User-Agent": "phase8-audit"})
    with urlopen(req, timeout=12) as r:
        return r.status, r.read().decode("utf-8", errors="replace")


# --- HTTP + content checks ---
htmls = {}
for p in pages:
    try:
        status, body = fetch(p)
        htmls[p] = body
        check(f"HTTP {p}", status == 200, str(status))
    except Exception as e:
        htmls[p] = ""
        check(f"HTTP {p}", False, str(e))

# Homepage
h = htmls.get("/", "")
check("home has skip link", "skip-link" in h)
check("home has main#main", 'id="main"' in h)
check("home CTA contact", "/contact" in h)
check("home CTA WhatsApp", "wa.me/919313512434" in h)
check("home work demo link", "/demos/bright-home-cleaning/" in h)
check("home pricing packages", "$249" in h and "$449" in h and "$699" in h)
check("home no map-data", "map-data-BIkaf5qX" not in h)
check("home nav Work / Pricing", 'href="/projects"' in h and 'href="/pricing"' in h)

# Services / industries
check("services website focus", "Business Website" in htmls.get("/services/", "") or "website" in htmls.get("/services/", "").lower())
check("industries cleaning", "Cleaning" in htmls.get("/industries/", ""))

# Projects honesty
p = htmls.get("/projects/", "")
check("projects honesty notice", "How to read this portfolio" in p)
check("projects demo label", "Demo Project" in p)
check("projects concept label", "Concept Design" in p)
check("projects demo href", "/demos/bright-home-cleaning/" in p)

# Pricing
pr = htmls.get("/pricing/", "")
check("pricing compare table", "price-compare" in pr)
check("pricing FAQ", "Pricing FAQ" in pr or "Are these final fixed prices" in pr)
check("pricing package query links", "package=starter" in pr and "package=business" in pr)
check("pricing no pages.js", "pages-CCS7nnQc" not in pr)
check("pricing no faq.jpg OG", "faq.jpg" not in pr)

# Contact
c = htmls.get("/contact/", "")
check("contact website hero", "plan your" in c.lower() or "website" in c.lower())
check("contact handoff attr", 'data-handoff="whatsapp"' in c)
check("contact no fake send claim in ready text", "sent successfully" not in c.lower() or "do not show a fake" in c.lower())
check("contact WhatsApp CTA", "wa.me/919313512434" in c)
check("contact mailto", "mailto:info.aliradigital@gmail.com" in c)
check("contact handoff js", "contact-handoff.js" in c)
check("contact fieldset balance", c.count("<fieldset") == c.count("</fieldset>"))

# Demo
d = htmls.get("/demos/bright-home-cleaning/", "")
check("demo banner", "Demo Project" in d)
check("demo local form", "demo-quote" in d)
check("demo no fake thank you alert", "alert(" not in d)
check("demo agency handoff", "wa.me/919313512434" in d and "mailto:info.aliradigital@gmail.com" in d)

# About
a = htmls.get("/about-us/", "")
check("about founder dims", 'ritesh-cutout.webp' in a and 'width="720"' in a)

# Internal link crawl from homepage (same-origin path links)
link_re = re.compile(r'href="(/[^"#?]*)')
internal = set(link_re.findall(h))
for body in htmls.values():
    internal |= set(link_re.findall(body))
internal = sorted(p for p in internal if not p.startswith("/build/") and not p.startswith("/assets/img/"))

broken = []
for path in internal:
    # normalize directory indexes
    try:
        status, _ = fetch(path if path.endswith(("/", ".html", ".css", ".js", ".svg", ".webp", ".png", ".jpg", ".ico", ".xml", ".txt")) or "." in path.split("/")[-1] else path)
        # try with trailing slash if 404-ish — urlopen raises
        if status >= 400:
            broken.append((path, status))
    except HTTPError as e:
        # retry with trailing slash for extensionless
        if not path.endswith("/"):
            try:
                status, _ = fetch(path + "/")
                if status >= 400:
                    broken.append((path, status))
            except Exception as e2:
                broken.append((path, str(e2)))
        else:
            broken.append((path, e.code))
    except Exception as e:
        broken.append((path, str(e)))

check("no broken internal links from key pages", len(broken) == 0, str(broken[:12]))

# Structural HTML issues on key pages
for path, body in htmls.items():
    if not body:
        continue
    # extra closing mobile-menu pattern historically
    check(f"{path} has header", "site-header" in body or path.startswith("/demos/"))
    # duplicate robots ok as long as noindex present on agency pages
    if path != "/demos/bright-home-cleaning/":
        check(f"{path} noindex", "noindex" in body)

# Responsive CSS presence
css_files = [
    root / "assets/css/brand-system.css",
    root / "assets/css/home-agency.css",
    root / "assets/css/portfolio.css",
    root / "assets/css/pricing-contact.css",
    root / "demos/bright-home-cleaning/styles.css",
]
for f in css_files:
    t = f.read_text(encoding="utf-8") if f.exists() else ""
    check(f"{f.name} has mobile media query", "@media" in t and "max-width" in t)

# Report
failed = [r for r in results if not r[0]]
for ok, label, detail in results:
    mark = "OK  " if ok else "FAIL"
    print(f"{mark} {label}" + (f" — {detail}" if detail and not ok else ""))
print("---")
print(f"{len(results)-len(failed)}/{len(results)} passed")
if failed:
    raise SystemExit(1)
