from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]

NAV_TEMPLATE = '''<ul class="nav-links">
        <li><a href="/"{home_current}>Home</a></li>
        <li><a href="/services"{services_current}>Services</a></li>
        <li><a href="/industries"{industries_current}>Industries</a></li>
        <li><a href="/projects"{projects_current}>Work</a></li>
        <li><a href="/pricing"{pricing_current}>Pricing</a></li>
        <li><a href="/about-us"{about_current}>About</a></li>
        <li><a href="/contact"{contact_current}>Contact</a></li>
      </ul>
      <a class="btn btn--green" href="/contact" data-magnetic>Get a Free Quote <span class="btn-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg></span></a>'''

MOBILE_TEMPLATE = '''<div class="mobile-menu" id="mobileMenu" data-lenis-prevent>
    <ul>
      <li><a class="mm-link" href="/"><small>01</small>Home</a></li>
      <li><a class="mm-link" href="/services"><small>02</small>Services</a></li>
      <li><a class="mm-link" href="/industries"><small>03</small>Industries</a></li>
      <li><a class="mm-link" href="/projects"><small>04</small>Work</a></li>
      <li><a class="mm-link" href="/pricing"><small>05</small>Pricing</a></li>
      <li><a class="mm-link" href="/about-us"><small>06</small>About</a></li>
      <li><a class="mm-link" href="/contact"><small>07</small>Contact</a></li>
    </ul>
    <div class="mm-foot">
      <span>Website Design &amp; Development · International clients</span>
      <a href="https://wa.me/919313512434" target="_blank" rel="noopener">+91 9313512434</a>
      <span>info.aliradigital@gmail.com</span>
      <div class="foot-social"><a class="fs-wa" href="https://wa.me/919313512434" target="_blank" rel="noopener" aria-label="WhatsApp"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.2 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .1-3.3-.8-2.8-1.1-4.5-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.9s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.9 2.1c.1.2.1.3 0 .5l-.3.5-.4.5c-.1.1-.3.3-.1.6.2.3.7 1.2 1.6 2 1.1 1 2 1.3 2.3 1.4.3.1.5.1.6-.1l.9-1c.2-.3.4-.2.6-.1l2 1c.3.1.5.2.5.3.1.2.1.7-.1 1.3z"/></svg></a></div>
    </div>
  </div>'''

NAV_RE = re.compile(
    r'<ul class="nav-links">[\s\S]*?</ul>\s*<a class="btn btn--green" href="/contact"[\s\S]*?</a>',
    re.M,
)
MOBILE_RE = re.compile(
    r'<div class="mobile-menu" id="mobileMenu"[\s\S]*?</div>\s*(?=<main|</body>)',
    re.M,
)

# Also catch mobile menus that end before main with different whitespace
MOBILE_RE2 = re.compile(
    r'<div class="mobile-menu" id="mobileMenu"[\s\S]*?<div class="mm-foot">[\s\S]*?</div>\s*</div>',
    re.M,
)


def currents_for(path: Path):
    rel = path.relative_to(root).as_posix()
    flags = {
        "home_current": "",
        "services_current": "",
        "industries_current": "",
        "projects_current": "",
        "pricing_current": "",
        "about_current": "",
        "contact_current": "",
    }
    if rel == "index.html":
        flags["home_current"] = ' aria-current="page"'
    elif rel.startswith("services/") or rel == "website-design/index.html":
        flags["services_current"] = ' aria-current="page"'
    elif rel.startswith("industries/"):
        flags["industries_current"] = ' aria-current="page"'
    elif rel.startswith("projects/"):
        flags["projects_current"] = ' aria-current="page"'
    elif rel.startswith("pricing/"):
        flags["pricing_current"] = ' aria-current="page"'
    elif rel.startswith("about-us/"):
        flags["about_current"] = ' aria-current="page"'
    elif rel.startswith("contact/"):
        flags["contact_current"] = ' aria-current="page"'
    return flags


updated = 0
for path in root.rglob("*.html"):
    if path.name in {"brand-preview.html", "404.html"}:
        continue
    # skip nested blog assets already handled as html pages - include them
    raw = path.read_text(encoding="utf-8")
    if 'class="nav-links"' not in raw:
        continue
    flags = currents_for(path)
    nav = NAV_TEMPLATE.format(**flags)
    new = NAV_RE.sub(nav, raw, count=1)
    if MOBILE_RE2.search(new):
        new = MOBILE_RE2.sub(MOBILE_TEMPLATE, new, count=1)
    if new != raw:
        path.write_text(new, encoding="utf-8")
        updated += 1
        print("updated", path.relative_to(root))

print(f"Done. Updated {updated} pages.")
