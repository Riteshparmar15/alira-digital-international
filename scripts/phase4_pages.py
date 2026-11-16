from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]

CSS_LINK = (
    '<link rel="stylesheet" href="/assets/css/brand-system.css">\n'
    '<link rel="stylesheet" href="/assets/css/home-agency.css">\n'
    '<link rel="stylesheet" href="/assets/css/services-industries.css">'
)

FOOTER_BRAND = (
    "<p>Website Design &amp; Development. We create professional, modern websites "
    "that help small businesses build trust, attract customers and grow online.</p>"
)

FOOTER_PAGES = """          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/services">Services</a></li>
            <li><a href="/industries">Industries</a></li>
            <li><a href="/projects">Work</a></li>
            <li><a href="/pricing">Pricing</a></li>
            <li><a href="/about-us">About</a></li>
            <li><a href="/contact">Contact</a></li>
          </ul>"""

FOOTER_SERVICES = """          <ul>
            <li><a href="/services">All Services</a></li>
            <li><a href="/services#business-website">Business Websites</a></li>
            <li><a href="/services#redesign">Website Redesign</a></li>
            <li><a href="/services#landing-page">Landing Pages</a></li>
            <li><a href="/services#seo">SEO-Friendly Websites</a></li>
            <li><a href="/pricing">Pricing</a></li>
          </ul>"""


def ensure_css(text: str) -> str:
    if "services-industries.css" in text:
        return text
    if 'href="/assets/css/brand-system.css">' in text:
        return text.replace(
            '<link rel="stylesheet" href="/assets/css/brand-system.css">',
            CSS_LINK,
            1,
        )
    return text


def fix_mobile_extra(text: str) -> str:
    text = text.replace("\r\n", "\n")
    # remove one or more orphan closes before main after mobile menu
    text = re.sub(
        r'(id="mobileMenu"[\s\S]*?</div>\n)</div>\n(?:</div>\n)*(<main>)',
        r"\1\2",
        text,
        count=1,
    )
    return text


def patch_footer(text: str) -> str:
    text = re.sub(
        r"<p>Web &amp; System Solutions\.[^<]*</p>",
        FOOTER_BRAND,
        text,
        count=1,
    )
    text = re.sub(
        r"(<div><h4>Pages</h4>)([\s\S]*?)(</div>\s*<div><h4>Resources</h4>)",
        r"\1" + FOOTER_PAGES + r"\3",
        text,
        count=1,
    )
    # alternate footer format with newlines
    text = re.sub(
        r"(<div>\s*<h4>Pages</h4>\s*)<ul>[\s\S]*?</ul>(\s*</div>)",
        r"\1" + FOOTER_PAGES + r"\2",
        text,
        count=1,
    )
    text = re.sub(
        r"(<div><h4>Services</h4>)([\s\S]*?)(</div>\s*<div><h4>Contact</h4>)",
        r"\1" + FOOTER_SERVICES + r"\3",
        text,
        count=1,
    )
    text = re.sub(
        r"(<div>\s*<h4>Services</h4>\s*)<ul>[\s\S]*?</ul>(\s*</div>)",
        r"\1" + FOOTER_SERVICES + r"\2",
        text,
        count=1,
    )
    return text


SERVICES_MAIN = r'''<main>

<section class="page-hero">
  <div class="orb" style="width:560px;height:560px;right:-160px;top:-120px" data-float="40"></div>
  <div class="wrap">
    <div class="crumbs" data-hero><a href="/">Home</a> · Services</div>
    <div class="page-hero-row">
      <h1 class="h1" data-hero-split>Website services that turn visitors into customers.</h1>
      <p class="lead" data-hero>From first builds to redesigns and ongoing care — clear deliverables, conversion-focused structure and transparent starting prices in USD.</p>
    </div>
    <nav class="svc-jump" aria-label="Services" data-hero>
      <a href="#business-website"><b>01</b>Business Website</a>
      <a href="#redesign"><b>02</b>Redesign</a>
      <a href="#landing-page"><b>03</b>Landing Page</a>
      <a href="#responsive"><b>04</b>Responsive</a>
      <a href="#maintenance"><b>05</b>Maintenance</a>
      <a href="#seo"><b>06</b>SEO-Friendly</a>
    </nav>
  </div>
</section>

<section class="pad-sm">
  <div class="wrap svc-detail">

    <article class="svc-block" id="business-website">
      <div class="svc-block-copy">
        <span class="idx">01 / 06</span>
        <h2>Business Website Development</h2>
        <p class="lead-sm">A multi-page website that explains what you do, builds trust quickly and makes it easy for customers to request a quote.</p>
        <div class="svc-meta">
          <div>
            <h3>What it includes</h3>
            <ul>
              <li>Custom homepage and core service pages</li>
              <li>About and contact/enquiry sections</li>
              <li>Mobile-responsive layouts</li>
              <li>Basic on-page SEO foundations</li>
            </ul>
          </div>
          <div>
            <h3>Who needs it</h3>
            <ul>
              <li>Businesses with no website or a weak online presence</li>
              <li>Service companies that need clear service explanations</li>
              <li>Owners who want more inbound enquiries</li>
            </ul>
          </div>
          <div>
            <h3>Business benefits</h3>
            <ul>
              <li>Look professional when customers search online</li>
              <li>Reduce repetitive “what do you offer?” questions</li>
              <li>Create a reliable path to contact and quotes</li>
            </ul>
          </div>
          <div>
            <h3>Deliverables</h3>
            <ul>
              <li>Designed and developed website pages</li>
              <li>Enquiry form setup</li>
              <li>Deployment support</li>
            </ul>
          </div>
        </div>
        <div class="btn-row"><a class="btn btn--green" href="/contact" data-magnetic>Get a Free Quote</a><a class="btn btn--soft" href="/pricing" data-magnetic>View pricing</a></div>
      </div>
      <aside class="svc-aside">
        <h3>Best starting point</h3>
        <p>Most cleaning, plumbing, landscaping and consulting businesses begin here — a clear site that presents services and captures enquiries.</p>
      </aside>
    </article>

    <article class="svc-block" id="redesign">
      <div class="svc-block-copy">
        <span class="idx">02 / 06</span>
        <h2>Website Redesign</h2>
        <p class="lead-sm">Modernise an outdated site with stronger design, clearer messaging and better conversion paths — without inventing a new brand from scratch.</p>
        <div class="svc-meta">
          <div>
            <h3>What it includes</h3>
            <ul>
              <li>Content and structure review</li>
              <li>Updated visual design system</li>
              <li>Improved page hierarchy and CTAs</li>
              <li>Responsive rebuild where needed</li>
            </ul>
          </div>
          <div>
            <h3>Who needs it</h3>
            <ul>
              <li>Businesses embarrassed by an old website</li>
              <li>Sites that look fine on desktop but fail on mobile</li>
              <li>Pages that get traffic but few enquiries</li>
            </ul>
          </div>
          <div>
            <h3>Business benefits</h3>
            <ul>
              <li>Restore credibility with first-time visitors</li>
              <li>Make services easier to understand</li>
              <li>Guide more visitors toward contact actions</li>
            </ul>
          </div>
          <div>
            <h3>Deliverables</h3>
            <ul>
              <li>Redesigned key pages</li>
              <li>Updated enquiry paths</li>
              <li>Launch support</li>
            </ul>
          </div>
        </div>
        <div class="btn-row"><a class="btn btn--green" href="/contact" data-magnetic>Request a redesign quote</a></div>
      </div>
      <aside class="svc-aside">
        <h3>Common trigger</h3>
        <p>If your site was built years ago and no longer matches the quality of your real-world work, a redesign is usually faster than starting over blindly.</p>
      </aside>
    </article>

    <article class="svc-block" id="landing-page">
      <div class="svc-block-copy">
        <span class="idx">03 / 06</span>
        <h2>Landing Page Development</h2>
        <p class="lead-sm">A focused page built around one offer and one action — ideal for ads, seasonal campaigns and lead generation.</p>
        <div class="svc-meta">
          <div>
            <h3>What it includes</h3>
            <ul>
              <li>Single-page conversion layout</li>
              <li>Offer-focused messaging sections</li>
              <li>Quote or lead form</li>
              <li>Mobile-first design</li>
            </ul>
          </div>
          <div>
            <h3>Who needs it</h3>
            <ul>
              <li>Businesses running ads or promotions</li>
              <li>Companies launching a new service package</li>
              <li>Teams that need a clean campaign destination</li>
            </ul>
          </div>
          <div>
            <h3>Business benefits</h3>
            <ul>
              <li>Fewer distractions than a full website</li>
              <li>Clearer tracking of campaign response</li>
              <li>Faster path from interest to enquiry</li>
            </ul>
          </div>
          <div>
            <h3>Deliverables</h3>
            <ul>
              <li>Designed landing page</li>
              <li>Form integration</li>
              <li>Deployment support</li>
            </ul>
          </div>
        </div>
        <div class="btn-row"><a class="btn btn--green" href="/contact" data-magnetic>Get a landing page quote</a></div>
      </div>
      <aside class="svc-aside">
        <h3>Use it for</h3>
        <p>Spring cleaning packages, emergency plumbing offers, landscaping seasonals or consulting lead magnets.</p>
      </aside>
    </article>

    <article class="svc-block" id="responsive">
      <div class="svc-block-copy">
        <span class="idx">04 / 06</span>
        <h2>Responsive Website Development</h2>
        <p class="lead-sm">Websites that work properly on phones, tablets and desktops — because most customers will check you on a mobile device first.</p>
        <div class="svc-meta">
          <div>
            <h3>What it includes</h3>
            <ul>
              <li>Mobile-first layout planning</li>
              <li>Touch-friendly navigation and buttons</li>
              <li>Readable typography across devices</li>
              <li>Responsive images and forms</li>
            </ul>
          </div>
          <div>
            <h3>Who needs it</h3>
            <ul>
              <li>Businesses whose current site breaks on phones</li>
              <li>Owners getting complaints about hard-to-use pages</li>
              <li>Teams preparing for international visitors</li>
            </ul>
          </div>
          <div>
            <h3>Business benefits</h3>
            <ul>
              <li>Better first impressions on mobile search</li>
              <li>Fewer abandoned visits due to usability issues</li>
              <li>Consistent brand experience on every screen</li>
            </ul>
          </div>
          <div>
            <h3>Deliverables</h3>
            <ul>
              <li>Responsive page builds</li>
              <li>Device checks for key breakpoints</li>
              <li>Launch support</li>
            </ul>
          </div>
        </div>
        <div class="btn-row"><a class="btn btn--green" href="/contact" data-magnetic>Talk about responsive design</a></div>
      </div>
      <aside class="svc-aside">
        <h3>Practical standard</h3>
        <p>Every Alira Digital website project is responsive by default. This service is ideal when the priority is fixing mobile experience first.</p>
      </aside>
    </article>

    <article class="svc-block" id="maintenance">
      <div class="svc-block-copy">
        <span class="idx">05 / 06</span>
        <h2>Website Maintenance &amp; Support</h2>
        <p class="lead-sm">Keep your website reliable after launch with updates, fixes and content changes — scoped clearly, never as unlimited support.</p>
        <div class="svc-meta">
          <div>
            <h3>What it includes</h3>
            <ul>
              <li>Content updates and page edits</li>
              <li>Bug fixes and minor improvements</li>
              <li>Security and dependency checks where applicable</li>
              <li>Agreed response expectations</li>
            </ul>
          </div>
          <div>
            <h3>Who needs it</h3>
            <ul>
              <li>Businesses without an in-house web person</li>
              <li>Owners who change services or pricing often</li>
              <li>Teams that need a reliable update channel</li>
            </ul>
          </div>
          <div>
            <h3>Business benefits</h3>
            <ul>
              <li>Keep information accurate for customers</li>
              <li>Avoid a neglected site after launch</li>
              <li>Plan updates without emergency scrambling</li>
            </ul>
          </div>
          <div>
            <h3>Deliverables</h3>
            <ul>
              <li>Defined support scope</li>
              <li>Update turnaround agreement</li>
              <li>Change log for completed work</li>
            </ul>
          </div>
        </div>
        <div class="btn-row"><a class="btn btn--green" href="/contact" data-magnetic>Ask about maintenance</a></div>
      </div>
      <aside class="svc-aside">
        <h3>Important note</h3>
        <p>We do not promise unlimited revisions or unlimited support. Maintenance is scoped so both sides know what is included.</p>
      </aside>
    </article>

    <article class="svc-block" id="seo">
      <div class="svc-block-copy">
        <span class="idx">06 / 06</span>
        <h2>SEO-Friendly Website Development</h2>
        <p class="lead-sm">Build websites with clean structure, metadata and performance foundations that help search engines understand your business.</p>
        <div class="svc-meta">
          <div>
            <h3>What it includes</h3>
            <ul>
              <li>Logical heading hierarchy</li>
              <li>Unique page titles and meta descriptions</li>
              <li>Clean URLs and internal linking</li>
              <li>Image alt text and technical SEO basics</li>
            </ul>
          </div>
          <div>
            <h3>Who needs it</h3>
            <ul>
              <li>Businesses that rely on Google search for leads</li>
              <li>Local and international service providers</li>
              <li>Owners rebuilding a poorly structured site</li>
            </ul>
          </div>
          <div>
            <h3>Business benefits</h3>
            <ul>
              <li>Stronger foundation for organic visibility</li>
              <li>Clearer pages for both users and search engines</li>
              <li>Fewer technical SEO cleanup projects later</li>
            </ul>
          </div>
          <div>
            <h3>Deliverables</h3>
            <ul>
              <li>SEO-ready page structure</li>
              <li>On-page metadata setup</li>
              <li>Sitemap and robots guidance</li>
            </ul>
          </div>
        </div>
        <div class="btn-row"><a class="btn btn--green" href="/contact" data-magnetic>Get an SEO-ready website quote</a></div>
      </div>
      <aside class="svc-aside">
        <h3>Honest expectation</h3>
        <p>SEO foundations help your site compete. Ranking still depends on competition, content quality and ongoing effort — we do not invent traffic guarantees.</p>
      </aside>
    </article>

    <div class="soft-archive" data-reveal>
      <h3>Other capabilities</h3>
      <p>Alira Digital also has experience with broader digital systems. These remain available on request, but our primary focus for international clients is website design and development.</p>
      <div class="cluster">
        <a href="/website-design">Website design deep-dive</a>
        <a href="/custom-erp-system">Custom ERP</a>
        <a href="/online-platform-development">Online platforms</a>
        <a href="/mobile-app-development">Mobile apps</a>
        <a href="/ai-agents-automation">AI agents</a>
      </div>
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
          <span class="eyebrow">Next step</span>
          <h2 data-split>Tell us which service you need.</h2>
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

INDUSTRIES_MAIN = r'''<main>

<section class="page-hero">
  <div class="orb" style="width:540px;height:540px;right:-180px;top:-140px" data-float="40"></div>
  <div class="wrap">
    <div class="crumbs" data-hero><a href="/">Home</a> · Industries</div>
    <div class="page-hero-row">
      <h1 class="h1" data-hero-split>Websites for service businesses that need more enquiries.</h1>
      <p class="lead" data-hero>We help cleaning, plumbing, landscaping, home service and consulting businesses look credible online and convert visitors into customers.</p>
    </div>
  </div>
</section>

<section class="pad-sm">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Who we help</span>
      <h2 class="h2" data-split>Industry problems websites can actually solve.</h2>
      <p class="muted">If customers compare you online before they call, your website should answer their questions and make the next step obvious.</p>
    </div>
    <div class="industry-pills" data-reveal>
      <a href="#cleaning">Cleaning companies</a>
      <a href="#plumbing">Plumbing businesses</a>
      <a href="#landscaping">Landscaping companies</a>
      <a href="#home-services">Home service providers</a>
      <a href="#consulting">Consulting businesses</a>
    </div>
  </div>
</section>

<section class="pad-sm">
  <div class="wrap">

    <article class="industry-story" id="cleaning">
      <div class="industry-story-copy">
        <span class="idx">01 / 05</span>
        <h2>Cleaning companies</h2>
        <p class="lead-sm">Homeowners and facility managers look for trust signals fast: services, areas covered, pricing clarity and an easy quote request.</p>
        <div class="btn-row"><a class="btn btn--green" href="/contact" data-magnetic>Get a cleaning website quote</a><a class="btn btn--soft" href="/projects" data-magnetic>See related work</a></div>
      </div>
      <div class="stack">
        <div class="problem-box">
          <h3>Common website problems</h3>
          <ul>
            <li>Services are unclear, so visitors leave for a competitor</li>
            <li>No mobile-friendly quote form</li>
            <li>Missing service-area and trust information</li>
          </ul>
        </div>
        <div class="solution-box">
          <h3>How Alira Digital helps</h3>
          <ul>
            <li>Clear residential and commercial service pages</li>
            <li>Quote request forms that work on phones</li>
            <li>Professional layout that builds confidence quickly</li>
          </ul>
        </div>
      </div>
    </article>

    <article class="industry-story" id="plumbing">
      <div class="industry-story-copy">
        <span class="idx">02 / 05</span>
        <h2>Plumbing businesses</h2>
        <p class="lead-sm">When someone has a plumbing issue, they need fast answers: what you fix, whether you cover their area and how to contact you now.</p>
        <div class="btn-row"><a class="btn btn--green" href="/contact" data-magnetic>Get a plumbing website quote</a></div>
      </div>
      <div class="stack">
        <div class="problem-box">
          <h3>Common website problems</h3>
          <ul>
            <li>Emergency and standard services are mixed together</li>
            <li>Contact options are hard to find on mobile</li>
            <li>Weak proof of professionalism and reliability</li>
          </ul>
        </div>
        <div class="solution-box">
          <h3>How Alira Digital helps</h3>
          <ul>
            <li>Service pages organised by job type</li>
            <li>Prominent call, WhatsApp and quote actions</li>
            <li>Clean, trustworthy design for urgent decision-making</li>
          </ul>
        </div>
      </div>
    </article>

    <article class="industry-story" id="landscaping">
      <div class="industry-story-copy">
        <span class="idx">03 / 05</span>
        <h2>Landscaping companies</h2>
        <p class="lead-sm">Landscaping buyers want to see capability and process — then request an estimate without friction.</p>
        <div class="btn-row"><a class="btn btn--green" href="/contact" data-magnetic>Get a landscaping website quote</a></div>
      </div>
      <div class="stack">
        <div class="problem-box">
          <h3>Common website problems</h3>
          <ul>
            <li>Services and project types are hard to scan</li>
            <li>Seasonal offers are buried or missing</li>
            <li>Estimate requests rely only on phone calls</li>
          </ul>
        </div>
        <div class="solution-box">
          <h3>How Alira Digital helps</h3>
          <ul>
            <li>Visual service storytelling with clear next steps</li>
            <li>Estimate forms for residential and commercial work</li>
            <li>Pages that support seasonal campaigns and landing offers</li>
          </ul>
        </div>
      </div>
    </article>

    <article class="industry-story" id="home-services">
      <div class="industry-story-copy">
        <span class="idx">04 / 05</span>
        <h2>Home service providers</h2>
        <p class="lead-sm">Electricians, HVAC, handymen and similar trades need websites that explain services simply and convert local search interest into booked jobs.</p>
        <div class="btn-row"><a class="btn btn--green" href="/contact" data-magnetic>Get a home services website quote</a></div>
      </div>
      <div class="stack">
        <div class="problem-box">
          <h3>Common website problems</h3>
          <ul>
            <li>Generic template sites that look like every competitor</li>
            <li>Unclear service packages and coverage</li>
            <li>No structured path from visit to enquiry</li>
          </ul>
        </div>
        <div class="solution-box">
          <h3>How Alira Digital helps</h3>
          <ul>
            <li>Service-first information architecture</li>
            <li>Conversion-focused contact sections</li>
            <li>Responsive design for on-the-go customers</li>
          </ul>
        </div>
      </div>
    </article>

    <article class="industry-story" id="consulting">
      <div class="industry-story-copy">
        <span class="idx">05 / 05</span>
        <h2>Consulting businesses</h2>
        <p class="lead-sm">Independent consultants and professional firms need a polished site that communicates expertise, process and how to start a conversation.</p>
        <div class="btn-row"><a class="btn btn--green" href="/contact" data-magnetic>Get a consulting website quote</a></div>
      </div>
      <div class="stack">
        <div class="problem-box">
          <h3>Common website problems</h3>
          <ul>
            <li>Expertise is buried in long, unclear copy</li>
            <li>No clear engagement or discovery process</li>
            <li>Contact feels impersonal or incomplete</li>
          </ul>
        </div>
        <div class="solution-box">
          <h3>How Alira Digital helps</h3>
          <ul>
            <li>Positioning-led homepage and service pages</li>
            <li>Simple process explanation that builds trust</li>
            <li>Professional enquiry experience for serious prospects</li>
          </ul>
        </div>
      </div>
    </article>

  </div>
</section>

<section class="pad on-dark" style="overflow:hidden">
  <div class="dark-dots"></div>
  <div class="wrap" style="position:relative;display:grid;gap:28px">
    <span class="eyebrow">International focus</span>
    <p class="statement" data-highlight>Built for service businesses in the <em>United States</em>, <em>United Kingdom</em>, <em>Canada</em> and <em>Australia</em> — with clear English, USD starting prices and remote delivery.</p>
  </div>
</section>

<section class="pad-sm">
  <div class="wrap">
    <div class="cta" data-scale-in>
      <div class="cta-orb" data-float="40"></div>
      <div class="dark-dots"></div>
      <div class="cta-row">
        <div style="display:grid;gap:26px">
          <span class="eyebrow">Ready to grow</span>
          <h2 data-split>Recognise your business here?</h2>
          <div class="btn-row">
            <a class="btn btn--green" href="/contact" data-magnetic>Get a Free Quote</a>
            <a class="btn btn--light" href="/services" data-magnetic>View services</a>
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


def update_services():
    path = root / "services" / "index.html"
    text = path.read_text(encoding="utf-8")
    text = ensure_css(text)
    text = fix_mobile_extra(text)
    text = re.sub(
        r"<title>.*?</title>",
        "<title>Website Design &amp; Development Services | Alira Digital</title>",
        text,
        count=1,
        flags=re.S,
    )
    text = re.sub(
        r'<meta name="description" content="[^"]*">',
        '<meta name="description" content="Website design and development services from Alira Digital: business websites, redesigns, landing pages, responsive builds, maintenance and SEO-friendly development for international small businesses.">',
        text,
        count=1,
    )
    text = re.sub(
        r'<meta property="og:title" content="[^"]*">',
        '<meta property="og:title" content="Website Design &amp; Development Services | Alira Digital">',
        text,
        count=1,
    )
    text = re.sub(
        r'<meta property="og:description" content="[^"]*">',
        '<meta property="og:description" content="Professional website services for cleaning, plumbing, landscaping, home service and consulting businesses.">',
        text,
        count=1,
    )
    text = re.sub(r"<main>[\s\S]*?</main>", SERVICES_MAIN, text, count=1)
    text = patch_footer(text)
    text = text.replace(
        '<div class="ld-top"><span>Alira Digital</span><span>Web &amp; System Solutions</span><span class="ld-hide-s">Vadodara, Gujarat · India</span></div>',
        '<div class="ld-top"><span>Alira Digital</span><span>Website Design &amp; Development</span><span class="ld-hide-s">International clients</span></div>',
        1,
    )
    path.write_text(text, encoding="utf-8", newline="\n")
    print("services updated")


def update_industries():
    path = root / "industries" / "index.html"
    text = path.read_text(encoding="utf-8")
    text = ensure_css(text)
    text = fix_mobile_extra(text)
    text = re.sub(
        r"<title>.*?</title>",
        "<title>Industries We Serve | Alira Digital</title>",
        text,
        count=1,
        flags=re.S,
    )
    text = re.sub(
        r'<meta name="description" content="[^"]*">',
        '<meta name="description" content="Alira Digital builds websites for cleaning companies, plumbing businesses, landscaping companies, home service providers and consulting firms seeking more online enquiries.">',
        text,
        count=1,
    )
    text = re.sub(
        r'<meta property="og:title" content="[^"]*">',
        '<meta property="og:title" content="Industries We Serve | Alira Digital">',
        text,
        count=1,
    )
    text = re.sub(
        r'<meta property="og:description" content="[^"]*">',
        '<meta property="og:description" content="Website solutions for cleaning, plumbing, landscaping, home services and consulting businesses.">',
        text,
        count=1,
    )
    text = re.sub(r"<main>[\s\S]*?</main>", INDUSTRIES_MAIN, text, count=1)
    text = patch_footer(text)
    text = text.replace(
        '<div class="ld-top"><span>Alira Digital</span><span>Web &amp; System Solutions</span><span class="ld-hide-s">Vadodara, Gujarat · India</span></div>',
        '<div class="ld-top"><span>Alira Digital</span><span>Website Design &amp; Development</span><span class="ld-hide-s">International clients</span></div>',
        1,
    )
    path.write_text(text, encoding="utf-8", newline="\n")
    print("industries updated")


if __name__ == "__main__":
    update_services()
    update_industries()
    print("phase 4 complete")
