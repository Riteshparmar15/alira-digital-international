from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
checks = []

def ok(label, cond):
    checks.append((label, bool(cond)))

# robots / sitemap
ok("robots.txt exists", (root / "robots.txt").exists())
ok("robots disallow", "Disallow: /" in (root / "robots.txt").read_text(encoding="utf-8"))
ok("sitemap draft exists", (root / "sitemap.xml").exists())
ok("robots does not advertise sitemap", "Sitemap:" not in (root / "robots.txt").read_text(encoding="utf-8"))

pages = {
    "index.html": ["skip-link", 'id="main"', "map-data-BIkaf5qX"],
    "pricing/index.html": ["skip-link", "pages-CCS7nnQc", "faq.jpg", "alira-pro-1-dark.svg"],
    "services/index.html": ["Website Design & Development Services", "ERP, AI Agents"],
    "industries/index.html": ["Industries We Serve", "Custom Systems"],
    "projects/index.html": ["Website Portfolio & Demo Projects"],
    "contact/index.html": ["Contact & Free Website Quote", "Malaysia", "fieldset"],
    "about-us/index.html": ["ritesh-cutout.webp", 'width="720"'],
}

for rel, needles in pages.items():
    t = (root / rel).read_text(encoding="utf-8")
    if rel == "index.html":
        ok("home skip", "skip-link" in t and 'id="main"' in t)
        ok("home no map-data", "map-data-BIkaf5qX" not in t)
        ok("home robots once", t.count('name="robots"') == 1)
        ok("home org not Custom ERP WebPage name", "Custom ERP, Web & App Development" not in t)
    if rel == "pricing/index.html":
        ok("pricing no pages.js", "pages-CCS7nnQc" not in t)
        ok("pricing no faq.jpg", "faq.jpg" not in t)
        ok("pricing og svg", "alira-pro-1-dark.svg" in t)
        ok("pricing skip", "skip-link" in t)
    if rel == "services/index.html":
        ok("services twitter agency", "Website Design & Development Services" in t)
        ok("services no old twitter ERP title", "ERP, AI Agents, Platform, App" not in t)
    if rel == "industries/index.html":
        ok("industries twitter", "Industries We Serve" in t)
        ok("industries no pages.js", "pages-CCS7nnQc" not in t)
    if rel == "projects/index.html":
        ok("projects twitter/og portfolio", "Website Portfolio & Demo Projects" in t)
    if rel == "contact/index.html":
        ok("contact twitter quote", "Contact & Free Website Quote" in t)
        ok("contact no Malaysia", "Malaysia" not in t)
        ok("contact package fieldset", "<fieldset class=\"field\"" in t and 'aria-label="Package interest"' in t)
        # nested fieldset balance rough check
        ok("contact fieldset balance", t.count("<fieldset") == t.count("</fieldset>"))
    if rel == "about-us/index.html":
        ok("about founder dims", 'width="720"' in t and "ritesh-cutout.webp" in t)

# facebook sameAs on services
st = (root / "services" / "index.html").read_text(encoding="utf-8")
ok("facebook no space sameAs", "facebook.com/Alira Digital" not in st)
ok("facebook fixed sameAs", "facebook.com/AliraDigital" in st or "facebook.com/Alira" in st)

# skip CSS
ok("skip CSS", ".skip-link" in (root / "assets" / "css" / "brand-system.css").read_text(encoding="utf-8"))

failed = [l for l, c in checks if not c]
for l, c in checks:
    print(("OK  " if c else "FAIL"), l)
print("---")
print(f"{len(checks)-len(failed)}/{len(checks)} passed")
if failed:
    raise SystemExit(1)
