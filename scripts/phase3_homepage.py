from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
index = root / "index.html"
text = index.read_text(encoding="utf-8")

if "home-agency.css" not in text:
    text = text.replace(
        '<link rel="stylesheet" href="/assets/css/brand-system.css">',
        '<link rel="stylesheet" href="/assets/css/brand-system.css">\n'
        '<link rel="stylesheet" href="/assets/css/home-agency.css">',
    )

text = re.sub(
    r"<title>.*?</title>",
    "<title>Website Design &amp; Development Agency | Alira Digital</title>",
    text,
    count=1,
    flags=re.S,
)
text = re.sub(
    r'<meta name="description"\s+content="[^"]*">',
    '<meta name="description" content="Alira Digital designs and develops modern, high-performing websites that help small businesses build trust, attract customers and grow online. Serving clients in the US, UK, Canada and Australia.">',
    text,
    count=1,
)
text = re.sub(
    r'<meta property="og:title" content="[^"]*">',
    '<meta property="og:title" content="Website Design &amp; Development Agency | Alira Digital">',
    text,
    count=1,
)
text = re.sub(
    r'<meta property="og:description"\s+content="[^"]*">',
    '<meta property="og:description" content="Websites that turn visitors into customers. Professional website design and development for home service and professional businesses.">',
    text,
    count=1,
)
text = re.sub(
    r'<meta name="twitter:title" content="[^"]*">',
    '<meta name="twitter:title" content="Website Design &amp; Development Agency | Alira Digital">',
    text,
    count=1,
)
text = re.sub(
    r'<meta name="twitter:description"\s+content="[^"]*">',
    '<meta name="twitter:description" content="Websites that turn visitors into customers. Professional website design and development for home service and professional businesses.">',
    text,
    count=1,
)

# Loader: only first occurrence in loader UI
text = text.replace(
    '<div class="ld-top"><span>Alira Digital</span><span>Web &amp; System Solutions</span><span\n'
    '          class="ld-hide-s">Vadodara, Gujarat · India</span></div>',
    '<div class="ld-top"><span>Alira Digital</span><span>Website Design &amp; Development</span><span\n'
    '          class="ld-hide-s">India · International</span></div>',
    1,
)
text = text.replace(
    '<span class="ld-msg">Collecting scattered data</span>',
    '<span class="ld-msg">Preparing your experience</span>',
    1,
)

NAV = '''<ul class="nav-links">
        <li><a href="/" aria-current="page">Home</a></li>
        <li><a href="/services">Services</a></li>
        <li><a href="/industries">Industries</a></li>
        <li><a href="/projects">Work</a></li>
        <li><a href="/pricing">Pricing</a></li>
        <li><a href="/about-us">About</a></li>
        <li><a href="/contact">Contact</a></li>
      </ul>
      <a class="btn btn--green" href="/contact" data-magnetic>Get a Free Quote <span class="btn-ico"><svg
            viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"
            stroke-linejoin="round" aria-hidden="true">
            <path d="M7 17 17 7M8 7h9v9" />
          </svg></span></a>'''

# Replace desktop nav block on homepage (from nav-links through header CTA)
text = re.sub(
    r'<ul class="nav-links">[\s\S]*?</ul>\s*<a class="btn btn--green" href="/contact"[\s\S]*?</a>',
    NAV,
    text,
    count=1,
)

MOBILE = '''<div class="mobile-menu" id="mobileMenu" data-lenis-prevent>
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
      <div class="foot-social"><a class="fs-wa" href="https://wa.me/919313512434" target="_blank" rel="noopener"
          aria-label="WhatsApp"><svg viewBox="0 0 24 24" aria-hidden="true">
            <path
              d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.2 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .1-3.3-.8-2.8-1.1-4.5-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.9s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.9 2.1c.1.2.1.3 0 .5l-.3.5-.4.5c-.1.1-.3.3-.1.6.2.3.7 1.2 1.6 2 1.1 1 2 1.3 2.3 1.4.3.1.5.1.6-.1l.9-1c.2-.3.4-.2.6-.1l2 1c.3.1.5.2.5.3.1.2.1.7-.1 1.3z" />
          </svg></a></div>
    </div>
  </div>'''

text = re.sub(
    r'<div class="mobile-menu" id="mobileMenu"[\s\S]*?</div>\s*<main>',
    MOBILE + "\n  <main>",
    text,
    count=1,
)

MAIN = r'''<main>

    <section class="hero hero--agency" id="top">
      <canvas class="hero-canvas" id="heroDots" aria-hidden="true" data-cursor="Click"></canvas>
      <div class="wrap">
        <div class="hero-grid">
          <div class="hero-copy">
            <div class="brand-lockup" data-hero>Alira Digital</div>
            <span class="eyebrow" data-hero>Website Design &amp; Development Agency</span>
            <h1 class="display" data-hero-split>Your Business Deserves a <span class="accent">Better Website.</span></h1>
            <p class="lead" data-hero>Alira Digital creates professional, modern and responsive websites that help businesses attract customers, build credibility and grow online.</p>
            <div class="hero-slot" aria-hidden="true"></div>
            <div class="btn-row" data-hero>
              <a class="btn btn--green" href="/contact" data-magnetic>Get a Free Quote <span class="btn-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9" /></svg></span></a>
              <a class="btn btn--soft" href="/projects" data-magnetic>Explore Our Work <span class="btn-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9" /></svg></span></a>
            </div>
            <div class="hero-tags" data-hero>
              <span class="tag"><i></i>Home service businesses</span>
              <span class="tag"><i></i>US · UK · Canada · Australia</span>
            </div>
          </div>
          <div class="hero-visual" aria-hidden="true">
            <div class="hero-visual-frame">
              <div class="hv-bar"><i></i><i></i><i></i><span>yourbusiness.com</span></div>
              <h2 class="hv-title">Websites that turn <em>visitors</em> into customers.</h2>
              <span class="hv-cta">Request a quote</span>
            </div>
          </div>
        </div>
      </div>
      <div class="hero-hint"><b></b>Scroll</div>
    </section>

    <section class="pad">
      <div class="wrap" style="position:relative;display:grid;gap:28px">
        <span class="eyebrow" data-reveal>What we do</span>
        <p class="statement" data-highlight>We design and develop modern, high-performing websites that help small businesses <em>build trust</em>, attract customers and <em>grow online</em>.</p>
        <div data-reveal><a class="link-arrow" href="/about-us">More about Alira Digital <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a></div>
      </div>
    </section>

    <section class="pad" id="services-overview" aria-labelledby="services-title">
      <div class="wrap">
        <div class="sec-head">
          <span class="eyebrow">Services</span>
          <h2 class="h2" id="services-title" data-split>Website services built for growth.</h2>
          <p class="muted">Clear packages for businesses that need a professional online presence — not a complicated software project.</p>
        </div>
        <div class="agency-grid">
          <article class="agency-card" data-reveal>
            <span class="n">01</span>
            <h3>Business Website Development</h3>
            <p>Multi-page websites that explain your services, build trust and make it easy to enquire.</p>
            <a href="/services">Learn more</a>
          </article>
          <article class="agency-card" data-reveal>
            <span class="n">02</span>
            <h3>Website Redesign</h3>
            <p>Modernise an outdated site with clearer structure, stronger design and better conversion paths.</p>
            <a href="/services">Learn more</a>
          </article>
          <article class="agency-card" data-reveal>
            <span class="n">03</span>
            <h3>Landing Page Development</h3>
            <p>Focused pages for campaigns and lead generation, built around one clear call to action.</p>
            <a href="/services">Learn more</a>
          </article>
          <article class="agency-card" data-reveal>
            <span class="n">04</span>
            <h3>Responsive Website Development</h3>
            <p>Sites that look and work well on phones, tablets and desktops — where most customers start.</p>
            <a href="/services">Learn more</a>
          </article>
          <article class="agency-card" data-reveal>
            <span class="n">05</span>
            <h3>Website Maintenance &amp; Support</h3>
            <p>Ongoing updates, fixes and content changes so your website stays reliable after launch.</p>
            <a href="/services">Learn more</a>
          </article>
          <article class="agency-card" data-reveal>
            <span class="n">06</span>
            <h3>SEO-Friendly Website Development</h3>
            <p>Clean structure, metadata and performance foundations that help search engines understand your business.</p>
            <a href="/services">Learn more</a>
          </article>
        </div>
        <p style="margin-top:40px;text-align:center" data-reveal><a class="btn btn--soft" href="/services" data-magnetic>View all services <span class="btn-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9" /></svg></span></a></p>
      </div>
    </section>

    <section class="pad on-dark" data-glow style="overflow:hidden" id="why-alira">
      <div class="dark-dots"></div>
      <div class="wrap" style="position:relative">
        <div class="sec-head">
          <span class="eyebrow">Why Alira Digital</span>
          <h2 class="h2" data-split>A website partner focused on enquiries.</h2>
          <p class="muted">Premium design, clear communication and conversion-minded structure — without invented claims or cookie-cutter templates.</p>
        </div>
        <div class="on-dark-rings">
          <div class="rings">
            <div class="rings-line" data-draw><i></i></div>
            <div class="ring-item" data-reveal>
              <div class="ring-num"><b>01</b></div>
              <h3>Built for small businesses</h3>
              <p>Messaging and layouts designed for cleaning, plumbing, landscaping, home services and professional firms.</p>
            </div>
            <div class="ring-item" data-reveal>
              <div class="ring-num"><b>02</b></div>
              <h3>Conversion-first structure</h3>
              <p>Every page is organised to guide visitors toward a quote request, call or WhatsApp message.</p>
            </div>
            <div class="ring-item" data-reveal>
              <div class="ring-num"><b>03</b></div>
              <h3>Clear delivery process</h3>
              <p>Transparent scopes, starting prices and regular updates from brief to launch.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="pad" id="industries-preview" aria-labelledby="industries-title">
      <div class="wrap">
        <div class="sec-head">
          <span class="eyebrow">Industries</span>
          <h2 class="h2" id="industries-title" data-split>Built for service businesses that need more enquiries.</h2>
          <p class="muted">If customers search online before they call, your website should do the hard work of building trust.</p>
        </div>
        <div class="industry-pills" data-reveal>
          <a href="/industries">Cleaning companies</a>
          <a href="/industries">Plumbing businesses</a>
          <a href="/industries">Landscaping companies</a>
          <a href="/industries">Home service providers</a>
          <a href="/industries">Consulting businesses</a>
        </div>
      </div>
    </section>

    <section class="pad" id="work-preview" aria-labelledby="work-title">
      <div class="wrap">
        <div class="sec-head">
          <span class="eyebrow">Selected work</span>
          <h2 class="h2" id="work-title" data-split>Website projects and concept designs.</h2>
          <p class="muted">We showcase completed website work and clearly labelled concept designs. No invented client results.</p>
        </div>
        <div class="work-grid">
          <a class="work-card" href="/projects/corporate-websites" data-cursor="View" data-reveal>
            <div class="frame" data-clip data-tilt style="aspect-ratio:1600/1000"><span class="chip"><i></i>Website Design</span><img src="/assets/img/web-collage.webp" alt="Website design examples by Alira Digital" loading="lazy" width="1600" height="1000"></div>
            <div class="work-meta">
              <h3>Professional business websites</h3>
              <p>Corporate and service-business website design showcase</p>
            </div>
          </a>
          <a class="work-card" href="/projects" data-cursor="View" data-reveal>
            <div class="frame" data-clip data-tilt style="aspect-ratio:1600/1000"><span class="chip"><i></i>Demo Project</span><img src="/assets/img/web-eco-fresh.webp" alt="Demo concept website design" loading="lazy" width="1276" height="800"></div>
            <div class="work-meta">
              <h3>Home services concept</h3>
              <p><span class="badge-demo">Concept Design</span> Example direction for service businesses</p>
            </div>
          </a>
          <a class="work-card" href="/projects" data-cursor="View" data-reveal>
            <div class="frame" data-clip data-tilt style="aspect-ratio:1600/1000"><span class="chip"><i></i>Landing Page</span><img src="/assets/img/web-pro-eco-health.webp" alt="Landing page concept design" loading="lazy" width="1200" height="800"></div>
            <div class="work-meta">
              <h3>Campaign landing pages</h3>
              <p><span class="badge-demo">Concept Design</span> Lead-focused layouts for promotions</p>
            </div>
          </a>
        </div>
        <p style="margin-top:48px;text-align:center" data-reveal><a class="btn btn--soft" href="/projects" data-magnetic>Explore Our Work <span class="btn-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9" /></svg></span></a></p>
      </div>
    </section>

    <section class="pad" id="process" aria-labelledby="process-title">
      <div class="wrap">
        <div class="sec-head">
          <span class="eyebrow">Process</span>
          <h2 class="h2" id="process-title" data-split>A clear path from brief to launch.</h2>
          <p class="muted">Simple stages, visible progress and no surprises on scope.</p>
        </div>
        <div class="process-steps">
          <article data-reveal>
            <span class="step-n">01 · Discover</span>
            <h3>Understand your business</h3>
            <p>We learn your services, customers and goals before recommending a structure.</p>
          </article>
          <article data-reveal>
            <span class="step-n">02 · Design</span>
            <h3>Shape the experience</h3>
            <p>Wireframes and visual direction focused on clarity, trust and conversion.</p>
          </article>
          <article data-reveal>
            <span class="step-n">03 · Build</span>
            <h3>Develop and refine</h3>
            <p>Responsive development, forms, SEO foundations and content placement.</p>
          </article>
          <article data-reveal>
            <span class="step-n">04 · Launch</span>
            <h3>Go live with support</h3>
            <p>Deployment help, final checks and a clear next step for ongoing care.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="pad" id="pricing-preview" aria-labelledby="pricing-title">
      <div class="wrap">
        <div class="sec-head">
          <span class="eyebrow">Pricing</span>
          <h2 class="h2" id="pricing-title" data-split>Transparent starting packages in USD.</h2>
          <p class="muted">Starting estimates only. Final pricing depends on project scope. Hosting and domain are billed separately.</p>
        </div>
        <div class="price-preview">
          <article class="price-card" data-reveal>
            <span class="plan">Starter</span>
            <p class="amount">$249 <small>starting</small></p>
            <ul>
              <li>Up to 3 pages</li>
              <li>Responsive design</li>
              <li>Contact form</li>
              <li>Basic on-page SEO</li>
            </ul>
            <a class="btn btn--soft" href="/pricing" data-magnetic>View package</a>
          </article>
          <article class="price-card is-featured" data-reveal>
            <span class="plan">Business</span>
            <p class="amount">$449 <small>starting</small></p>
            <ul>
              <li>Up to 7 pages</li>
              <li>Custom website design</li>
              <li>Enquiry forms</li>
              <li>SEO-friendly structure</li>
            </ul>
            <a class="btn btn--green" href="/contact" data-magnetic>Get a Free Quote</a>
          </article>
          <article class="price-card" data-reveal>
            <span class="plan">Premium</span>
            <p class="amount">$699 <small>starting</small></p>
            <ul>
              <li>Up to 12 pages</li>
              <li>Advanced custom design</li>
              <li>Enhanced SEO setup</li>
              <li>Priority project support</li>
            </ul>
            <a class="btn btn--soft" href="/pricing" data-magnetic>View package</a>
          </article>
        </div>
        <p class="muted" style="margin-top:28px;text-align:center" data-reveal>Need something custom? <a class="text-link" href="/contact">Request a tailored quotation</a>.</p>
      </div>
    </section>

    <section class="pad" id="faq" aria-labelledby="faq-title">
      <div class="wrap faq-grid">
        <div class="faq-side">
          <span class="eyebrow">FAQ</span>
          <h2 class="h2" id="faq-title" data-split>Straight answers before you enquire.</h2>
          <p class="muted" style="margin:0">Still deciding? Send a short brief and we will reply with next steps.</p>
          <div class="btn-row"><a class="btn btn--green" href="/contact" data-magnetic>Get a Free Quote <span class="btn-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17 17 7M8 7h9v9" /></svg></span></a><a class="btn btn--soft" href="https://wa.me/919313512434" target="_blank" rel="noopener" data-magnetic>WhatsApp <span class="btn-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17 17 7M8 7h9v9" /></svg></span></a></div>
        </div>
        <div class="faq">
          <details open>
            <summary>What does Alira Digital do?<span class="pm" aria-hidden="true"></span></summary>
            <div class="ans"><p>Alira Digital is a website design and development agency. We create professional, modern and responsive websites that help small businesses attract customers and generate enquiries.</p></div>
          </details>
          <details>
            <summary>Who do you typically work with?<span class="pm" aria-hidden="true"></span></summary>
            <div class="ans"><p>We focus on cleaning companies, plumbing businesses, landscaping companies, home service providers, consultants and other small to medium-sized businesses looking for international-quality websites.</p></div>
          </details>
          <details>
            <summary>Do you work with clients outside India?<span class="pm" aria-hidden="true"></span></summary>
            <div class="ans"><p>Yes. We work with clients in the United States, United Kingdom, Canada and Australia. Communication is handled online via email and WhatsApp.</p></div>
          </details>
          <details>
            <summary>How does pricing work?<span class="pm" aria-hidden="true"></span></summary>
            <div class="ans"><p>We publish starting packages in USD. Final pricing depends on page count, design complexity and functionality. Hosting and domain costs are billed separately.</p></div>
          </details>
          <details>
            <summary>How do I request a quote?<span class="pm" aria-hidden="true"></span></summary>
            <div class="ans"><p>Use the contact form, email info.aliradigital@gmail.com, or WhatsApp +91 9313512434 with a short description of your business and goals.</p></div>
          </details>
        </div>
      </div>
    </section>

    <section class="pad-sm">
      <div class="wrap">
        <div class="cta" data-scale-in>
          <div class="cta-orb" data-float="40"></div>
          <div class="dark-dots"></div>
          <div class="cta-row">
            <div style="display:grid;gap:26px">
              <span class="eyebrow">Ready to start</span>
              <h2 data-split>Let's build a website that wins customers.</h2>
              <div class="btn-row">
                <a class="btn btn--green" href="/contact" data-magnetic>Get a Free Quote <span class="btn-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9" /></svg></span></a>
                <a class="btn btn--light" href="https://wa.me/919313512434" target="_blank" rel="noopener" data-magnetic>WhatsApp Now <span class="btn-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9" /></svg></span></a>
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

# Footer brand + pages + services refresh (homepage)
text = text.replace(
    "<p>Web &amp; System Solutions. We build custom ERP systems, AI agents &amp; automation, online platforms, mobile apps and corporate websites for businesses across India and worldwide.</p>",
    "<p>Website Design &amp; Development. We create professional, modern websites that help small businesses build trust, attract customers and grow online.</p>",
    1,
)
text = text.replace(
    """          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about-us">About Us</a></li>
            <li><a href="/services">Services</a></li>
            <li><a href="/industries">Who we serve</a></li>
            <li><a href="/projects">Projects</a></li>
            <li><a href="/blog">Blog</a></li>
            <li><a href="/contact">Contact</a></li>
          </ul>""",
    """          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/services">Services</a></li>
            <li><a href="/industries">Industries</a></li>
            <li><a href="/projects">Work</a></li>
            <li><a href="/pricing">Pricing</a></li>
            <li><a href="/about-us">About</a></li>
            <li><a href="/contact">Contact</a></li>
          </ul>""",
    1,
)
text = text.replace(
    """          <ul>
            <li><a href="/services">All Services</a></li>
            <li><a href="/custom-erp-system">Business &amp; ERP System</a></li>
            <li><a href="/online-platform-development">Online Platform</a></li>
            <li><a href="/mobile-app-development">Mobile Application</a></li>
            <li><a href="/website-design">Website Design</a></li>
        <li><a href="/ai-agents-automation">AI Agents &amp; Automation</a></li>
          </ul>""",
    """          <ul>
            <li><a href="/services">All Services</a></li>
            <li><a href="/services">Business Websites</a></li>
            <li><a href="/services">Website Redesign</a></li>
            <li><a href="/services">Landing Pages</a></li>
            <li><a href="/website-design">Website Design</a></li>
            <li><a href="/pricing">Pricing</a></li>
          </ul>""",
    1,
)
text = text.replace(
    '<span class="eyebrow">Pure Creative Light · Vadodara, Gujarat, India</span>\n'
    '        <p class="foot-sign-line" data-split>Your digital transformation <span class="accent">partner.</span></p>',
    '<span class="eyebrow">Alira Digital · Website Design &amp; Development</span>\n'
    '        <p class="foot-sign-line" data-split>Websites that turn visitors into <span class="accent">customers.</span></p>',
    1,
)
text = text.replace(
    "<small>Alira Digital Solutions · Custom Software &amp; Digital Engineering</small>",
    "<small>Alira Digital · Website Design &amp; Development Agency</small>",
    1,
)
text = text.replace(
    "<span>Software House in Vadodara, Gujarat, India</span>",
    "<span>Based in India · Serving US, UK, Canada &amp; Australia</span>",
    1,
)

index.write_text(text, encoding="utf-8")
print("Homepage rewritten")
print("has home-agency:", "home-agency.css" in text)
print("has Get a Free Quote:", text.count("Get a Free Quote"))
print("has hero--agency:", "hero--agency" in text)
