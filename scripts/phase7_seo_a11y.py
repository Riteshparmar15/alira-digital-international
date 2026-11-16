from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]

SKIP = (
    '<a class="skip-link" href="#main">Skip to main content</a>\n'
)

SKIP_CSS = """
/* Skip link */
.skip-link {
  position: absolute;
  left: 12px;
  top: 12px;
  z-index: 10000;
  transform: translateY(-160%);
  padding: 10px 14px;
  border-radius: 999px;
  background: var(--color-text);
  color: #fff;
  font-weight: 700;
  text-decoration: none;
  box-shadow: var(--shadow-md);
}
.skip-link:focus,
.skip-link:focus-visible {
  transform: translateY(0);
  outline: 2px solid var(--color-primary);
  outline-offset: 3px;
}
"""

# --- brand-system skip CSS ---
brand = root / "assets" / "css" / "brand-system.css"
bt = brand.read_text(encoding="utf-8")
if ".skip-link" not in bt:
    bt = bt.replace(
        "/* ---------- Focus & accessibility ---------- */",
        "/* ---------- Focus & accessibility ---------- */\n" + SKIP_CSS,
        1,
    )
    brand.write_text(bt, encoding="utf-8", newline="\n")
    print("brand-system: skip-link CSS")

META = {
    "index.html": {
        "og_image_alt": "Alira Digital website design and development agency",
        "webpage_name": "Website Design & Development Agency | Alira Digital",
        "webpage_desc": "Alira Digital creates professional websites for cleaning companies, home-service businesses and SMBs across India and internationally.",
        "org_desc": "Alira Digital is a website design and development agency based in Vadodara, Gujarat, India. We build professional websites for small businesses nationally and internationally.",
    },
    "services/index.html": {
        "twitter_title": "Website Design & Development Services | Alira Digital",
        "twitter_desc": "Business websites, landing pages, redesigns, SEO pages and conversion-focused builds for home-service and SMB clients.",
        "webpage_name": "Website Design & Development Services | Alira Digital",
        "webpage_desc": "Website design and development services from Alira Digital: business sites, landing pages, redesigns and SEO-focused pages.",
    },
    "industries/index.html": {
        "twitter_title": "Industries We Serve | Alira Digital",
        "twitter_desc": "Website design for cleaning companies, plumbers, landscapers, consultants and other home-service businesses.",
        "webpage_name": "Industries We Serve | Alira Digital",
        "webpage_desc": "Alira Digital builds websites for cleaning, plumbing, landscaping, consulting and other home-service businesses.",
    },
    "projects/index.html": {
        "og_title": "Website Portfolio & Demo Projects | Alira Digital",
        "og_desc": "Explore Alira Digital website work and clearly labelled demo projects, including a cleaning company demo site.",
        "twitter_title": "Website Portfolio & Demo Projects | Alira Digital",
        "twitter_desc": "Website portfolio and concept designs with honest Demo Project and Concept Design labels.",
        "webpage_name": "Website Portfolio & Demo Projects | Alira Digital",
        "webpage_desc": "Website portfolio and concept designs from Alira Digital, with clearly labelled demo projects.",
    },
    "contact/index.html": {
        "twitter_title": "Contact & Free Website Quote | Alira Digital",
        "twitter_desc": "Contact Alira Digital for a website quote via WhatsApp or email. Prepare a brief and send it yourself — no fake form success.",
        "og_desc": "Contact Alira Digital for a website quote. WhatsApp +91 9313512434 or email info.aliradigital@gmail.com.",
        "webpage_name": "Contact & Free Website Quote | Alira Digital",
        "webpage_desc": "Contact Alira Digital for a website quote. Reach us on WhatsApp or email from Vadodara, Gujarat, India, serving clients nationally and internationally.",
    },
    "pricing/index.html": {
        "og_image": "/assets/img/alira-pro-1-dark.svg",
        "og_image_type": "image/svg+xml",
        "og_image_alt": "Alira Digital website development pricing packages",
        "twitter_image": "/assets/img/alira-pro-1-dark.svg",
        "twitter_image_alt": "Alira Digital website development pricing packages",
    },
    "website-design/index.html": {
        "webpage_name": "Website Design & Development | Alira Digital",
    },
    "about-us/index.html": {
        "meta_desc": "Meet Alira Digital — a website design and development agency in Vadodara, Gujarat, led by Ritesh Parmar. We build professional websites for small businesses.",
        "og_desc": "About Alira Digital: website design and development for small businesses, based in Vadodara, Gujarat.",
        "twitter_desc": "About Alira Digital: website design and development for small businesses, based in Vadodara, Gujarat.",
    },
}


def set_attr_meta(text: str, attr: str, name: str, content: str) -> str:
    """Replace content of <meta {attr}="{name}" content="...">"""
    pat = rf'(<meta {attr}="{re.escape(name)}" content=")[^"]*(">)'
    if re.search(pat, text):
        return re.sub(pat, rf"\g<1>{content}\g<2>", text, count=1)
    return text


def replace_json_field(text: str, key: str, value: str, count: int = 0) -> str:
    """Replace "key":"..." JSON string values (non-greedy until next unescaped quote is hard; use simple pattern)."""
    pat = rf'("{re.escape(key)}":")((?:\\.|[^"\\])*)(")'
    def repl(m):
        return m.group(1) + value.replace("\\", "\\\\").replace('"', '\\"') + m.group(3)
    return re.sub(pat, repl, text, count=count)


def dedupe_robots(text: str) -> str:
    matches = list(re.finditer(r'<meta name="robots" content="[^"]*">\s*', text))
    if len(matches) <= 1:
        return text
    # keep first, remove later ones
    for m in reversed(matches[1:]):
        text = text[: m.start()] + text[m.end() :]
    return text


def ensure_skip_and_main(text: str) -> str:
    if 'class="skip-link"' not in text:
        # after <body>
        text = re.sub(r"(<body[^>]*>)", r"\1\n" + SKIP, text, count=1)
    # id on main
    if re.search(r"<main(\s[^>]*)?>", text) and 'id="main"' not in text:
        text = re.sub(r"<main\b", '<main id="main"', text, count=1)
    return text


def drop_pages_js(text: str) -> str:
    text = text.replace(
        '<link rel="modulepreload" as="script" href="/build/assets/pages-CCS7nnQc.js" />',
        "",
    )
    text = text.replace(
        '<script type="module" src="/build/assets/pages-CCS7nnQc.js"></script>',
        "",
    )
    # compact double spaces from removals in link lines
    text = re.sub(r"(/>)\s+(<link)", r"\1\n\2", text)
    return text


def drop_map_data(text: str) -> str:
    text = text.replace(
        '<link rel="modulepreload" as="script" href="/build/assets/map-data-BIkaf5qX.js" />',
        "",
    )
    text = text.replace(
        '<script type="module" src="/build/assets/map-data-BIkaf5qX.js"></script>',
        "",
    )
    return text


def fix_facebook_sameas(text: str) -> str:
    return text.replace(
        "https://www.facebook.com/Alira Digital",
        "https://www.facebook.com/AliraDigital",
    )


def fix_schema_assets(text: str) -> str:
    text = text.replace(
        "https://aliradigital.com/assets/img/logo.png",
        "https://aliradigital.com/assets/img/alira-pro-1-dark.svg",
    )
    text = text.replace(
        "https://aliradigital.com/assets/img/og-image.jpg",
        "https://aliradigital.com/assets/img/alira-pro-1-dark.svg",
    )
    return text


def soft_org_description(text: str) -> str:
    # Soften ERP-first org description on agency pages without inventing claims
    old = "Alira Digital is a software house in Vadodara, Gujarat that builds custom ERP systems, AI agents & automation, online platforms, mobile apps and corporate websites for businesses across India and worldwide."
    new = "Alira Digital is a website design and development agency in Vadodara, Gujarat that builds professional websites for small businesses across India and internationally. Custom systems remain available on request."
    return text.replace(old, new)


KEY_PAGES = [
    "index.html",
    "services/index.html",
    "industries/index.html",
    "projects/index.html",
    "pricing/index.html",
    "contact/index.html",
    "about-us/index.html",
    "website-design/index.html",
    "privacy-policy/index.html",
]

for rel in KEY_PAGES:
    path = root / rel
    if not path.exists():
        print("skip missing", rel)
        continue
    text = path.read_text(encoding="utf-8")
    orig = text

    text = dedupe_robots(text)
    text = ensure_skip_and_main(text)
    text = fix_facebook_sameas(text)
    text = fix_schema_assets(text)
    text = soft_org_description(text)

    if rel in ("pricing/index.html", "industries/index.html", "privacy-policy/index.html"):
        text = drop_pages_js(text)
    if rel == "index.html":
        text = drop_map_data(text)

    cfg = META.get(rel, {})
    if "twitter_title" in cfg:
        text = set_attr_meta(text, "name", "twitter:title", cfg["twitter_title"])
    if "twitter_desc" in cfg:
        text = set_attr_meta(text, "name", "twitter:description", cfg["twitter_desc"])
    if "og_title" in cfg:
        text = set_attr_meta(text, "property", "og:title", cfg["og_title"])
    if "og_desc" in cfg:
        text = set_attr_meta(text, "property", "og:description", cfg["og_desc"])
    if "og_image" in cfg:
        text = set_attr_meta(text, "property", "og:image", cfg["og_image"])
    if "og_image_type" in cfg:
        text = set_attr_meta(text, "property", "og:image:type", cfg["og_image_type"])
    if "og_image_alt" in cfg:
        text = set_attr_meta(text, "property", "og:image:alt", cfg["og_image_alt"])
    if "twitter_image" in cfg:
        text = set_attr_meta(text, "name", "twitter:image", cfg["twitter_image"])
    if "twitter_image_alt" in cfg:
        text = set_attr_meta(text, "name", "twitter:image:alt", cfg["twitter_image_alt"])
    if "meta_desc" in cfg:
        text = set_attr_meta(text, "name", "description", cfg["meta_desc"])

    # WebPage name/description — prefer first WebPage occurrence via targeted replacements
    if "webpage_name" in cfg:
        # Replace WebPage "name" after "@type":"WebPage"
        text = re.sub(
            r'("@type":"WebPage"[^}]*?"name":")((?:\\.|[^"\\])*)(")',
            lambda m: m.group(1) + cfg["webpage_name"].replace('"', '\\"') + m.group(3),
            text,
            count=1,
        )
    if "webpage_desc" in cfg:
        text = re.sub(
            r'("@type":"WebPage"[^}]*?"description":")((?:\\.|[^"\\])*)(")',
            lambda m: m.group(1) + cfg["webpage_desc"].replace('"', '\\"') + m.group(3),
            text,
            count=1,
        )
    if "org_desc" in cfg:
        text = re.sub(
            r'("@type":\["Organization","ProfessionalService"\][^}]*?"description":")((?:\\.|[^"\\])*)(")',
            lambda m: m.group(1) + cfg["org_desc"].replace('"', '\\"') + m.group(3),
            text,
            count=1,
        )
        # also plain Organization without array
        if cfg["org_desc"] not in text:
            text = re.sub(
                r'("description":")(Alira Digital is a software house based in Vadodara[^"]*)(")',
                lambda m: m.group(1) + cfg["org_desc"] + m.group(3),
                text,
                count=1,
            )

    # Malaysia leftovers in contact/website-design WebPage
    text = text.replace("across Malaysia", "internationally")
    text = text.replace("Website Design Malaysia:", "Website Design:")
    text = text.replace("Website Design Malaysia", "Website Design")

    if text != orig:
        path.write_text(text, encoding="utf-8", newline="\n")
        print("updated", rel)
    else:
        print("unchanged", rel)

# About founder image dimensions
about = root / "about-us" / "index.html"
at = about.read_text(encoding="utf-8")
old_img = '<img src="/assets/img/ritesh-cutout.webp" alt="Ritesh Parmar, Founder &amp; Software Solution Architect of Alira Digital" loading="lazy">'
new_img = '<img src="/assets/img/ritesh-cutout.webp" alt="Ritesh Parmar, Founder &amp; Software Solution Architect of Alira Digital" width="720" height="900" loading="lazy">'
if old_img in at:
    about.write_text(at.replace(old_img, new_img, 1), encoding="utf-8", newline="\n")
    print("about-us: founder image dimensions")

# Contact package interest fieldset
contact = root / "contact" / "index.html"
ct = contact.read_text(encoding="utf-8")
old_pkg = '''        <div class="field" style="margin-top:18px">
          <label>Package interest <small style="font-weight:500;color:var(--color-text-muted)">(optional)</small></label>
          <div class="package-chips">'''
new_pkg = '''        <fieldset class="field" style="margin-top:18px;border:0;padding:0;min-inline-size:0">
          <legend>Package interest <small style="font-weight:500;color:var(--color-text-muted)">(optional)</small></legend>
          <div class="package-chips" role="group" aria-label="Package interest">'''
if old_pkg in ct:
    ct = ct.replace(old_pkg, new_pkg, 1)
    ct = ct.replace(
        '''          </div>
        </div>
      </fieldset>
      <fieldset class="fs-step">
        <legend>About your business''',
        '''          </div>
        </fieldset>
      </fieldset>
      <fieldset class="fs-step">
        <legend>About your business''',
        1,
    )
    contact.write_text(ct, encoding="utf-8", newline="\n")
    print("contact: package interest fieldset")
else:
    print("contact package pattern miss")

# Prefetch fonts CSS is already linked; add preload for fonts.css on homepage if missing
home = root / "index.html"
ht = home.read_text(encoding="utf-8")
if 'rel="preload" as="style" href="/assets/fonts/fonts.css"' not in ht:
    ht = ht.replace(
        '<link rel="stylesheet" href="/assets/fonts/fonts.css">',
        '<link rel="preload" as="style" href="/assets/fonts/fonts.css">\n  <link rel="stylesheet" href="/assets/fonts/fonts.css">',
        1,
    )
    home.write_text(ht, encoding="utf-8", newline="\n")
    print("index: fonts.css preload")

print("phase7 done")
