from pathlib import Path

root = Path(__file__).resolve().parents[1]
index = root / "index.html"
text = index.read_text(encoding="utf-8")

# --- Nav desktop ---
old_nav = """      <ul class="nav-links">
        <li><a href="/" aria-current="page">Home</a></li>
        <li><a href="/services">Services</a></li>
        <li><a href="/industries">Industries</a></li>
        <li><a href="/projects">Work</a></li>
        <li><a href="/pricing">Pricing</a></li>
        <li><a href="/about-us">About</a></li>
        <li><a href="/contact">Contact</a></li>
      </ul>
      <a class="btn btn--green" href="/contact" data-magnetic>Get a Free Quote <span class="btn-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg></span></a>"""

new_nav = """      <ul class="nav-links">
        <li><a href="#top">Home</a></li>
        <li><a href="#services">Services</a></li>
        <li><a href="#industries">Industries</a></li>
        <li><a href="#work">Work</a></li>
        <li><a href="#pricing">Pricing</a></li>
        <li><a href="#about">About</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <a class="btn btn--green" href="#contact" data-magnetic>Get a Free Quote <span class="btn-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg></span></a>"""

if old_nav not in text:
    raise SystemExit("desktop nav block not found")
text = text.replace(old_nav, new_nav)

# --- Mobile nav ---
old_mm = """    <ul>
      <li><a class="mm-link" href="/"><small>01</small>Home</a></li>
      <li><a class="mm-link" href="/services"><small>02</small>Services</a></li>
      <li><a class="mm-link" href="/industries"><small>03</small>Industries</a></li>
      <li><a class="mm-link" href="/projects"><small>04</small>Work</a></li>
      <li><a class="mm-link" href="/pricing"><small>05</small>Pricing</a></li>
      <li><a class="mm-link" href="/about-us"><small>06</small>About</a></li>
      <li><a class="mm-link" href="/contact"><small>07</small>Contact</a></li>
    </ul>"""

new_mm = """    <ul>
      <li><a class="mm-link" href="#top"><small>01</small>Home</a></li>
      <li><a class="mm-link" href="#services"><small>02</small>Services</a></li>
      <li><a class="mm-link" href="#industries"><small>03</small>Industries</a></li>
      <li><a class="mm-link" href="#work"><small>04</small>Work</a></li>
      <li><a class="mm-link" href="#pricing"><small>05</small>Pricing</a></li>
      <li><a class="mm-link" href="#about"><small>06</small>About</a></li>
      <li><a class="mm-link" href="#contact"><small>07</small>Contact</a></li>
    </ul>"""

if old_mm not in text:
    raise SystemExit("mobile nav block not found")
text = text.replace(old_mm, new_mm)

# Logo home -> #top
text = text.replace(
    'href="/" aria-label="Alira Digital home"',
    'href="#top" aria-label="Alira Digital home"',
)

# Section ids
replacements = [
    ('id="services-overview"', 'id="services"'),
    ('id="why-alira"', 'id="about"'),
    ('id="industries-preview"', 'id="industries"'),
    ('id="work-preview"', 'id="work"'),
    ('id="pricing-preview"', 'id="pricing"'),
]

for a, b in replacements:
    if a not in text:
        raise SystemExit(f"missing {a}")
    text = text.replace(a, b)

# Hero CTAs
text = text.replace('href="/contact" data-magnetic>Get a Free Quote', 'href="#contact" data-magnetic>Get a Free Quote')
text = text.replace('href="/projects" data-magnetic>Explore Our Work', 'href="#work" data-magnetic>Explore Our Work')

# Statement link
text = text.replace(
    'href="/about-us">More about Alira Digital',
    'href="#about">More about Alira Digital',
)

# Service card links -> stay on section / remove dead deep links
for href in [
    "/services#business-website",
    "/services#redesign",
    "/services#landing-page",
    "/services#responsive",
    "/services#maintenance",
    "/services#seo",
]:
    text = text.replace(f'href="{href}"', 'href="#contact"')

text = text.replace('href="/services" data-magnetic>View all services', 'href="#contact" data-magnetic>Request a quote')

# Industry pills
for slug in ["cleaning", "plumbing", "landscaping", "home-services", "consulting"]:
    text = text.replace(f'href="/industries#{slug}"', 'href="#contact"')

# Work cards - keep demo external, point concepts to #work/#contact
text = text.replace('href="/projects/corporate-websites"', 'href="#work"')
text = text.replace('href="/projects" data-cursor="View"', 'href="#work" data-cursor="View"')
text = text.replace('href="/projects" data-magnetic>Explore Our Work', 'href="#contact" data-magnetic>Get a Free Quote')

# Pricing CTAs
text = text.replace('href="/pricing" data-magnetic>View package', 'href="#contact" data-magnetic>Get a Free Quote')
text = text.replace('href="/contact?package=business"', 'href="#contact"')
text = text.replace('href="/contact">Request a tailored quotation', 'href="#contact">Request a tailored quotation')

# FAQ side CTAs already partly replaced via Get a Free Quote replace
text = text.replace(
    'href="/contact" data-magnetic>Get a Free Quote <span class="btn-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17 17 7M8 7h9v9" /></svg></span></a><a class="btn btn--soft" href="https://wa.me/919313512434"',
    'href="#contact" data-magnetic>Get a Free Quote <span class="btn-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17 17 7M8 7h9v9" /></svg></span></a><a class="btn btn--soft" href="https://wa.me/919313512434"',
)

# Bottom CTA
text = text.replace(
    """                <a class="btn btn--green" href="/contact" data-magnetic>Get a Free Quote <span class="btn-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9" /></svg></span></a>
                <a class="btn btn--light" href="https://wa.me/919313512434" target="_blank" rel="noopener" data-magnetic>WhatsApp Now""",
    """                <a class="btn btn--green" href="#contact" data-magnetic>Get a Free Quote <span class="btn-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9" /></svg></span></a>
                <a class="btn btn--light" href="https://wa.me/919313512434" target="_blank" rel="noopener" data-magnetic>WhatsApp Now""",
)

# Footer pages
old_foot_pages = """          <h4>Pages</h4>
          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/services">Services</a></li>
            <li><a href="/industries">Industries</a></li>
            <li><a href="/projects">Work</a></li>
            <li><a href="/pricing">Pricing</a></li>
            <li><a href="/about-us">About</a></li>
            <li><a href="/contact">Contact</a></li>
          </ul>"""

new_foot_pages = """          <h4>Pages</h4>
          <ul>
            <li><a href="#top">Home</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#industries">Industries</a></li>
            <li><a href="#work">Work</a></li>
            <li><a href="#pricing">Pricing</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#contact">Contact</a></li>
          </ul>"""

if old_foot_pages not in text:
    raise SystemExit("footer pages not found")
text = text.replace(old_foot_pages, new_foot_pages)

old_foot_res = """          <h4>Resources</h4>
          <ul>
            <li><a href="/areas-we-serve">Areas we serve</a></li>
            <li><a href="/faq">FAQ</a></li>
            <li><a href="/custom-erp-guide">Custom ERP guide</a></li>
            <li><a href="/blog">Blog</a></li>
          </ul>"""

new_foot_res = """          <h4>Resources</h4>
          <ul>
            <li><a href="#industries">Areas we serve</a></li>
            <li><a href="#faq">FAQ</a></li>
            <li><a href="#process">Process</a></li>
            <li><a href="#work">Selected work</a></li>
          </ul>"""

text = text.replace(old_foot_res, new_foot_res)

old_foot_svc = """          <h4>Services</h4>
          <ul>
            <li><a href="/services">All Services</a></li>
            <li><a href="/services">Business Websites</a></li>
            <li><a href="/services">Website Redesign</a></li>
            <li><a href="/services">Landing Pages</a></li>
            <li><a href="/website-design">Website Design</a></li>
            <li><a href="/pricing">Pricing</a></li>
          </ul>"""

new_foot_svc = """          <h4>Services</h4>
          <ul>
            <li><a href="#services">All Services</a></li>
            <li><a href="#services">Business Websites</a></li>
            <li><a href="#services">Website Redesign</a></li>
            <li><a href="#services">Landing Pages</a></li>
            <li><a href="#pricing">Pricing</a></li>
            <li><a href="#contact">Get a Quote</a></li>
          </ul>"""

text = text.replace(old_foot_svc, new_foot_svc)

# Insert contact section before final CTA pad-sm
contact_section = """
    <section class="pad" id="contact" aria-labelledby="contact-title">
      <div class="wrap">
        <div class="sec-head">
          <span class="eyebrow">Contact</span>
          <h2 class="h2" id="contact-title" data-split>Let's plan your website.</h2>
          <p class="muted">Send a short brief by WhatsApp or email. We reply with next steps — nothing is auto-posted to a fake inbox.</p>
        </div>
        <div class="landing-contact" data-reveal>
          <div class="landing-contact-card">
            <h3>WhatsApp</h3>
            <p>Fastest way to share your business details and goals.</p>
            <a class="btn btn--green" href="https://wa.me/919313512434?text=Hi%20Alira%20Digital%2C%20I%27d%20like%20a%20website%20quote." target="_blank" rel="noopener" data-magnetic>Chat on WhatsApp <span class="btn-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg></span></a>
          </div>
          <div class="landing-contact-card">
            <h3>Email</h3>
            <p>Prefer a written brief? Include your services, city and page needs.</p>
            <a class="btn btn--soft" href="mailto:info.aliradigital@gmail.com?subject=Website%20quote%20request" data-magnetic>Email a brief <span class="btn-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg></span></a>
          </div>
          <div class="landing-contact-meta">
            <div><span>Phone</span><a href="https://wa.me/919313512434" target="_blank" rel="noopener">+91 9313512434</a></div>
            <div><span>Email</span><a href="mailto:info.aliradigital@gmail.com">info.aliradigital@gmail.com</a></div>
            <div><span>Based in</span><span>Vadodara, Gujarat, India · Serving US, UK, Canada &amp; Australia</span></div>
          </div>
        </div>
      </div>
    </section>

"""

marker = '    <section class="pad-sm">'
if marker not in text:
    raise SystemExit("CTA marker not found")
if 'id="contact"' not in text.split(marker)[0]:
    text = text.replace(marker, contact_section + marker, 1)

# CSS version bump
text = text.replace("home-agency.css?v=11", "home-agency.css?v=12")

# Landing script helpers: close mobile menu on hash nav + active section
landing_js = """
<script>
(function () {
  document.querySelectorAll('.mm-link[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function () {
      var menu = document.getElementById('mobileMenu');
      var burger = document.querySelector('.burger');
      if (menu) menu.classList.remove('open');
      if (burger) {
        burger.setAttribute('aria-expanded', 'false');
        burger.classList.remove('is-open');
      }
      document.documentElement.classList.remove('menu-open');
      document.body.classList.remove('menu-open');
    });
  });
})();
</script>
"""

if "mm-link[href^=\"#\"]" not in text:
    text = text.replace("</body>", landing_js + "\n</body>")

index.write_text(text, encoding="utf-8")
print("updated index.html")
