from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
path = root / "projects" / "index.html"
text = path.read_text(encoding="utf-8")

if "portfolio.css" not in text:
    text = text.replace(
        '<link rel="stylesheet" href="/assets/css/brand-system.css">',
        '<link rel="stylesheet" href="/assets/css/brand-system.css">\n'
        '<link rel="stylesheet" href="/assets/css/home-agency.css">\n'
        '<link rel="stylesheet" href="/assets/css/portfolio.css">',
        1,
    )

text = re.sub(
    r"<title>.*?</title>",
    "<title>Website Portfolio &amp; Demo Projects | Alira Digital</title>",
    text,
    count=1,
    flags=re.S,
)
text = re.sub(
    r'<meta name="description" content="[^"]*">',
    '<meta name="description" content="Explore Alira Digital website work and clearly labelled demo projects, including a cleaning company demo site for prospective home-service clients.">',
    text,
    count=1,
)
text = re.sub(
    r'<meta property="og:title" content="[^"]*">',
    '<meta property="og:title" content="Website Portfolio &amp; Demo Projects | Alira Digital">',
    text,
    count=1,
)

MAIN = r'''<main>

<section class="page-hero">
  <div class="orb" style="width:480px;height:480px;right:-120px;top:-60px" data-float="40"></div>
  <div class="wrap">
    <div class="crumbs" data-hero><a href="/">Home</a> · Work</div>
    <div class="page-hero-row">
      <h1 class="h1" data-hero-split>Website work and concept designs.</h1>
      <p class="lead" data-hero>We showcase website directions for service businesses and clearly label self-created demos. No invented client results or revenue claims.</p>
    </div>
  </div>
</section>

<section class="pad-sm" style="padding-top:0">
  <div class="wrap">
    <div class="notice-panel" data-reveal>
      <h2>How to read this portfolio</h2>
      <p><strong>Demo Project</strong> and <strong>Concept Design</strong> labels mean the work was created by Alira Digital for demonstration. They are not presented as completed client engagements unless separately confirmed.</p>
    </div>

    <div class="portfolio-grid">
      <a class="portfolio-card" href="/demos/bright-home-cleaning/" data-reveal>
        <div class="media"><img src="/assets/img/web-eco-fresh.webp" alt="Bright Home Cleaning demo website preview" loading="lazy" width="1276" height="800"></div>
        <div class="body">
          <div class="meta-row">
            <span class="badge-demo">Demo Project</span>
            <span class="tech">Cleaning · Website</span>
          </div>
          <h3>Bright Home Cleaning</h3>
          <p>A fictional cleaning company website with residential and commercial services, service areas, sample testimonials and a quote request form.</p>
          <span class="tech">HTML · CSS · Responsive · Conversion-focused</span>
        </div>
      </a>

      <a class="portfolio-card" href="/projects/corporate-websites" data-reveal>
        <div class="media"><img src="/assets/img/web-collage.webp" alt="Professional business website design showcase" loading="lazy" width="1600" height="1000"></div>
        <div class="body">
          <div class="meta-row">
            <span class="badge-demo">Concept Design</span>
            <span class="tech">Professional websites</span>
          </div>
          <h3>Professional business website concepts</h3>
          <p>Design directions for professional and service-business websites, including homepage structure, trust-building layout and enquiry paths.</p>
          <span class="tech">UI design · Responsive layouts · SEO structure</span>
        </div>
      </a>

      <a class="portfolio-card" href="/industries#home-services" data-reveal>
        <div class="media"><img src="/assets/img/web-pro-eco-health.webp" alt="Home services website concept preview" loading="lazy" width="1200" height="800"></div>
        <div class="body">
          <div class="meta-row">
            <span class="badge-demo">Concept Design</span>
            <span class="tech">Home services</span>
          </div>
          <h3>Home services website direction</h3>
          <p>Concept direction for trades and home-service providers that need clear service pages and mobile-friendly quote actions.</p>
          <span class="tech">Service pages · Mobile-first · Lead capture</span>
        </div>
      </a>

      <a class="portfolio-card" href="/services#landing-page" data-reveal>
        <div class="media"><img src="/assets/img/web-luvera.webp" alt="Landing page concept preview" loading="lazy" width="1200" height="800"></div>
        <div class="body">
          <div class="meta-row">
            <span class="badge-demo">Concept Design</span>
            <span class="tech">Landing pages</span>
          </div>
          <h3>Campaign landing page concepts</h3>
          <p>Focused one-page layouts for promotions and paid campaigns, built around a single offer and clear call to action.</p>
          <span class="tech">Landing pages · Forms · Conversion layout</span>
        </div>
      </a>
    </div>

    <div class="soft-archive" style="margin-top:56px" data-reveal>
      <h3>Additional system concepts</h3>
      <p>Earlier ERP, platform and app case pages remain available for reference. Until verified as completed client engagements, treat them as concept or demo material.</p>
      <div class="cluster">
        <a href="/projects/fitcom-gym-app">Fitcom concept</a>
        <a href="/projects/waste-management-erp">Industrial ERP concept</a>
        <a href="/projects/travel-agency-erp">Travel ERP concept</a>
        <a href="/projects/aurora-car-rental">Fleet booking concept</a>
        <a href="/projects/ai-operations-copilot">AI operations concept</a>
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
          <span class="eyebrow">Want something similar?</span>
          <h2 data-split>Let's plan a website for your business.</h2>
          <div class="btn-row">
            <a class="btn btn--green" href="/contact" data-magnetic>Get a Free Quote</a>
            <a class="btn btn--light" href="/demos/bright-home-cleaning/" data-magnetic>Open cleaning demo</a>
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

# Soft-label corporate websites page intro for honesty
corp = root / "projects" / "corporate-websites" / "index.html"
if corp.exists():
    c = corp.read_text(encoding="utf-8")
    c2 = c.replace(
        "Alira Digital designs and builds corporate websites for Indian and global businesses, including content creation, responsive design and search engine optimisation. This page shows a selection of them: industrial and cleanroom suppliers in Penang, a steel fabricator, a kuey teow manufacturer, two law firms in Kuala Lumpur, a housing project, brands for home appliances, personal care and health food, a carbon fibre parts specialist and a video studio.",
        "This page gathers website concept designs and visual directions for professional businesses. Treat featured examples as Concept Design material unless a project is separately confirmed as a completed Alira Digital client engagement.",
    )
    if 'badge-demo' not in c2 and "Concept Design" not in c2[:5000]:
        c2 = c2.replace(
            '<span class="eyebrow">In short</span>',
            '<span class="eyebrow">Concept Design</span>',
            1,
        )
    corp.write_text(c2, encoding="utf-8", newline="\n")
    print("corporate websites page soft-labelled")

# Update homepage featured work to lead with cleaning demo
home = root / "index.html"
h = home.read_text(encoding="utf-8")
old_work = '''        <div class="work-grid">
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
        </div>'''
new_work = '''        <div class="work-grid">
          <a class="work-card" href="/demos/bright-home-cleaning/" data-cursor="View" data-reveal>
            <div class="frame" data-clip data-tilt style="aspect-ratio:1600/1000"><span class="chip"><i></i>Demo Project</span><img src="/assets/img/web-eco-fresh.webp" alt="Bright Home Cleaning demo website" loading="lazy" width="1276" height="800"></div>
            <div class="work-meta">
              <h3>Bright Home Cleaning</h3>
              <p><span class="badge-demo">Demo Project</span> Fictional cleaning company website demo</p>
            </div>
          </a>
          <a class="work-card" href="/projects/corporate-websites" data-cursor="View" data-reveal>
            <div class="frame" data-clip data-tilt style="aspect-ratio:1600/1000"><span class="chip"><i></i>Concept Design</span><img src="/assets/img/web-collage.webp" alt="Professional business website concepts" loading="lazy" width="1600" height="1000"></div>
            <div class="work-meta">
              <h3>Professional business websites</h3>
              <p><span class="badge-demo">Concept Design</span> Service-business website directions</p>
            </div>
          </a>
          <a class="work-card" href="/projects" data-cursor="View" data-reveal>
            <div class="frame" data-clip data-tilt style="aspect-ratio:1600/1000"><span class="chip"><i></i>Landing Page</span><img src="/assets/img/web-pro-eco-health.webp" alt="Landing page concept design" loading="lazy" width="1200" height="800"></div>
            <div class="work-meta">
              <h3>Campaign landing pages</h3>
              <p><span class="badge-demo">Concept Design</span> Lead-focused layouts for promotions</p>
            </div>
          </a>
        </div>'''
if old_work in h:
    h = h.replace(old_work, new_work, 1)
    home.write_text(h, encoding="utf-8", newline="\n")
    print("homepage work cards updated")
else:
    print("homepage work cards pattern not found")

path.write_text(text, encoding="utf-8", newline="\n")
print("projects portfolio updated")
