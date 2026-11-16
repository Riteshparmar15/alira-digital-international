from pathlib import Path
import re

path = Path(__file__).resolve().parents[1] / "pricing" / "index.html"
text = path.read_text(encoding="utf-8")

text = re.sub(r"<title>.*?</title>", "<title>Website Development Pricing | Alira Digital</title>", text, count=1, flags=re.S)
text = re.sub(
    r'<meta name="description" content="[^"]*">',
    '<meta name="description" content="Transparent website development packages from Alira Digital. Starter $249, Business $449 and Premium $699 starting prices in USD. Hosting and domain billed separately.">',
    text,
    count=1,
)
text = text.replace('href="/faq"', 'href="/pricing"')
text = text.replace("content=\"/faq\"", 'content="/pricing"')
text = re.sub(
    r'<meta property="og:title" content="[^"]*">',
    '<meta property="og:title" content="Website Development Pricing | Alira Digital">',
    text,
    count=1,
)
text = re.sub(
    r'<meta property="og:description" content="[^"]*">',
    '<meta property="og:description" content="Transparent website development packages starting at $249 USD. Clear deliverables, no unlimited revision promises.">',
    text,
    count=1,
)

if "home-agency.css" not in text:
    text = text.replace(
        '<link rel="stylesheet" href="/assets/css/brand-system.css">',
        '<link rel="stylesheet" href="/assets/css/brand-system.css">\n'
        '<link rel="stylesheet" href="/assets/css/home-agency.css">',
    )

# Fix current nav item for pricing
text = text.replace('<li><a href="/pricing">Pricing</a></li>', '<li><a href="/pricing" aria-current="page">Pricing</a></li>', 1)
text = text.replace('<li><a href="/" aria-current="page">Home</a></li>', '<li><a href="/">Home</a></li>')

MAIN = '''<main>
<section class="page-hero">
  <div class="orb" style="width:480px;height:480px;right:-140px;top:-80px" data-float="40"></div>
  <div class="wrap">
    <div class="crumbs" data-hero><a href="/">Home</a> · Pricing</div>
    <div class="page-hero-row">
      <h1 class="display" data-hero-split>Clear starting prices. <span class="green">Custom quotes when needed.</span></h1>
      <p class="lead" data-hero>These are proposed starting prices in USD, subject to project scope. Hosting and domain costs are billed separately. Unlimited revisions or unlimited support are never promised.</p>
    </div>
  </div>
</section>

<section class="pad" style="padding-top:0">
  <div class="wrap">
    <div class="price-preview">
      <article class="price-card" data-reveal>
        <span class="plan">Starter — $249</span>
        <p class="amount">$249 <small>starting</small></p>
        <ul>
          <li>Up to 3 pages</li>
          <li>Responsive design</li>
          <li>Contact form</li>
          <li>Basic on-page SEO</li>
          <li>Social media links</li>
          <li>Basic deployment support</li>
        </ul>
        <a class="btn btn--soft" href="/contact" data-magnetic>Request this package</a>
      </article>
      <article class="price-card is-featured" data-reveal>
        <span class="plan">Business — $449</span>
        <p class="amount">$449 <small>starting</small></p>
        <ul>
          <li>Up to 7 pages</li>
          <li>Custom website design</li>
          <li>Responsive layouts</li>
          <li>Enquiry forms</li>
          <li>SEO-friendly structure</li>
          <li>Performance optimization</li>
          <li>Deployment support</li>
        </ul>
        <a class="btn btn--green" href="/contact" data-magnetic>Get a Free Quote</a>
      </article>
      <article class="price-card" data-reveal>
        <span class="plan">Premium — $699</span>
        <p class="amount">$699 <small>starting</small></p>
        <ul>
          <li>Up to 12 pages</li>
          <li>Advanced custom design</li>
          <li>Advanced functionality</li>
          <li>Multiple enquiry forms</li>
          <li>Enhanced SEO implementation</li>
          <li>Performance optimization</li>
          <li>Priority project support</li>
        </ul>
        <a class="btn btn--soft" href="/contact" data-magnetic>Request this package</a>
      </article>
    </div>

    <div class="sec-head" style="margin-top:72px">
      <span class="eyebrow">Notes</span>
      <h2 class="h2" data-split>What to expect before you book.</h2>
    </div>
    <div class="agency-grid">
      <article class="agency-card" data-reveal>
        <span class="n">01</span>
        <h3>Starting estimates</h3>
        <p>Final pricing depends on page count, content readiness, design complexity and required functionality.</p>
      </article>
      <article class="agency-card" data-reveal>
        <span class="n">02</span>
        <h3>Hosting &amp; domains</h3>
        <p>Hosting and domain registration are billed separately unless agreed otherwise in writing.</p>
      </article>
      <article class="agency-card" data-reveal>
        <span class="n">03</span>
        <h3>Custom quotations</h3>
        <p>Need e-commerce, booking systems or a larger site? Request a custom quotation with your brief.</p>
      </article>
    </div>

    <div class="cta" data-scale-in style="margin-top:72px">
      <div class="cta-orb" data-float="40"></div>
      <div class="dark-dots"></div>
      <div class="cta-row">
        <div style="display:grid;gap:26px">
          <span class="eyebrow">Next step</span>
          <h2 data-split>Tell us about your website project.</h2>
          <div class="btn-row">
            <a class="btn btn--green" href="/contact" data-magnetic>Get a Free Quote</a>
            <a class="btn btn--light" href="https://wa.me/919313512434" target="_blank" rel="noopener" data-magnetic>WhatsApp Now</a>
          </div>
        </div>
        <div class="contact-lines">
          <span>+91 9313512434</span>
          <span>info.aliradigital@gmail.com</span>
        </div>
      </div>
    </div>
  </div>
</section>
</main>'''

text = re.sub(r"<main>[\s\S]*?</main>", MAIN, text, count=1)
path.write_text(text, encoding="utf-8")
print("pricing page ready")
