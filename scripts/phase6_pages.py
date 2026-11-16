from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]

# --- local-demo.js: allow WhatsApp/email handoff forms ---
demo = root / "local-demo.js"
demo_text = demo.read_text(encoding="utf-8")
new_submit = '''document.addEventListener('submit', function (event) {
  var form = event.target;
  if (!(form instanceof HTMLFormElement)) return;
  // Allow intentional WhatsApp / mailto handoff forms
  if (form.id === 'enquiry' || form.getAttribute('data-handoff') === 'whatsapp' || form.getAttribute('data-handoff') === 'local') {
    return;
  }
  event.preventDefault();
  event.stopImmediatePropagation();
  let message = form.querySelector('[data-demo-result]');
  if (!message) {
    message = document.createElement('p');
    message.dataset.demoResult = '';
    message.setAttribute('role', 'status');
    form.append(message);
  }
  message.textContent = 'Demo only: your enquiry has not been sent. Connect your own contact service before publishing.';
}, true);'''
demo_text = re.sub(
    r"document\.addEventListener\('submit', function \(event\) \{[\s\S]*?\}, true\);",
    new_submit,
    demo_text,
    count=1,
)
# Soften the enquiry note — clarify handoff, not fake send
demo_text = demo_text.replace(
    "Local demonstration — this form does not send enquiries.",
    "This form prepares your message for WhatsApp or email. Nothing is posted to a server.",
)
demo.write_text(demo_text, encoding="utf-8", newline="\n")
print("local-demo.js updated")

PRICING_MAIN = r'''<main>
<section class="page-hero">
  <div class="orb" style="width:480px;height:480px;right:-140px;top:-80px" data-float="40"></div>
  <div class="wrap">
    <div class="crumbs" data-hero><a href="/">Home</a> · Pricing</div>
    <div class="page-hero-row">
      <h1 class="display" data-hero-split>Website packages with <span class="green">clear starting prices.</span></h1>
      <p class="lead" data-hero>Proposed starting prices in USD for small business websites. Final quotes depend on scope. Hosting and domain are billed separately. Unlimited revisions or unlimited support are never promised.</p>
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
          <li>Contact / quote form</li>
          <li>Basic on-page SEO</li>
          <li>Social media links</li>
          <li>Basic deployment support</li>
        </ul>
        <a class="btn btn--soft" href="/contact?package=starter" data-magnetic>Request Starter</a>
      </article>
      <article class="price-card is-featured" data-reveal>
        <span class="plan">Business — $449</span>
        <p class="amount">$449 <small>starting</small></p>
        <ul>
          <li>Up to 7 pages</li>
          <li>Custom website design</li>
          <li>Responsive layouts</li>
          <li>Enquiry / quote forms</li>
          <li>SEO-friendly structure</li>
          <li>Performance optimization</li>
          <li>Deployment support</li>
        </ul>
        <a class="btn btn--green" href="/contact?package=business" data-magnetic>Get a Free Quote</a>
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
        <a class="btn btn--soft" href="/contact?package=premium" data-magnetic>Request Premium</a>
      </article>
    </div>

    <div class="sec-head" style="margin-top:72px">
      <span class="eyebrow">Compare</span>
      <h2 class="h2" data-split>What each package typically includes.</h2>
      <p class="muted">Use this as a planning guide. Your quotation will confirm exact pages and features.</p>
    </div>
    <div class="price-compare" data-reveal>
      <table>
        <thead>
          <tr>
            <th>Item</th>
            <th>Starter</th>
            <th>Business</th>
            <th>Premium</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>Page count</td><td>Up to 3</td><td>Up to 7</td><td>Up to 12</td></tr>
          <tr><td>Custom design</td><td>Template-led</td><td class="yes">Yes</td><td class="yes">Advanced</td></tr>
          <tr><td>Mobile responsive</td><td class="yes">Yes</td><td class="yes">Yes</td><td class="yes">Yes</td></tr>
          <tr><td>Enquiry / quote forms</td><td>1</td><td class="yes">Yes</td><td class="yes">Multiple</td></tr>
          <tr><td>On-page SEO</td><td>Basic</td><td class="yes">Structured</td><td class="yes">Enhanced</td></tr>
          <tr><td>Performance polish</td><td>—</td><td class="yes">Yes</td><td class="yes">Yes</td></tr>
          <tr><td>Deployment support</td><td>Basic</td><td class="yes">Yes</td><td class="yes">Priority</td></tr>
        </tbody>
      </table>
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
        <p>Need booking tools, e-commerce or a larger site? Request a custom quotation with your brief.</p>
      </article>
    </div>

    <div class="sec-head" style="margin-top:72px">
      <span class="eyebrow">Pricing FAQ</span>
      <h2 class="h2" data-split>Common questions about cost.</h2>
    </div>
    <div class="price-faq" data-reveal>
      <details open>
        <summary>Are these final fixed prices?</summary>
        <div class="ans">No. They are starting estimates in USD. We confirm a written quotation after reviewing your pages, content and features.</div>
      </details>
      <details>
        <summary>Do packages include hosting or a domain?</summary>
        <div class="ans">No. Hosting and domain costs are separate unless we agree otherwise in writing.</div>
      </details>
      <details>
        <summary>Can I start with Starter and upgrade later?</summary>
        <div class="ans">Yes. Many businesses launch with a smaller site, then add pages or features as they grow.</div>
      </details>
      <details>
        <summary>How do I get a quote?</summary>
        <div class="ans">Use the contact form, WhatsApp or email. Mention the package you are considering and a short description of your business.</div>
      </details>
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
            <a class="btn btn--light" href="https://wa.me/919313512434?text=Hi%20Alira%20Digital%2C%20I%27d%20like%20a%20website%20quote." target="_blank" rel="noopener" data-magnetic>WhatsApp Now</a>
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

CONTACT_MAIN = r'''<main>

<section class="page-hero">
  <div class="orb" style="width:520px;height:520px;right:-180px;top:-140px" data-float="40"></div>
  <div class="orb orb--ring" style="width:200px;height:200px;right:30%;top:40%" data-float="-30"></div>
  <div class="wrap">
    <div class="crumbs" data-hero><a href="/">Home</a> · Contact</div>
    <div class="page-hero-row">
      <h1 class="display" data-hero-split>Let's plan your <span class="green">website.</span></h1>
      <p class="lead" data-hero>Share a short brief and we will reply with next steps. Prefer a direct chat? Use WhatsApp or email — nothing is auto-sent to a fake inbox.</p>
    </div>
  </div>
</section>

<section class="pad-sm" style="padding-top:0">
  <div class="wrap contact-grid">
    <div style="display:grid;gap:28px">
      <div class="contact-cards">
        <a class="c-card" href="https://wa.me/919313512434?text=Hi%20Alira%20Digital%2C%20I%27d%20like%20a%20website%20quote." target="_blank" rel="noopener" data-reveal><span class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 5a2 2 0 0 1 2-2z"/></svg></span><span class="c-txt"><small>Phone / WhatsApp</small><span class="val">+91 9313512434</span></span><span class="c-arr"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg></span></a>
        <a class="c-card" href="mailto:info.aliradigital@gmail.com?subject=Website%20enquiry" data-reveal><span class="ico ico--teal"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg></span><span class="c-txt"><small>Email</small><span class="val">info.aliradigital@gmail.com</span></span><span class="c-arr"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg></span></a>
        <a class="c-card" href="https://www.facebook.com/Alira Digital" target="_blank" rel="noopener" data-reveal><span class="ico ico--fb"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M14 8.5V6.8c0-.8.2-1.3 1.4-1.3H17V2.2C16.7 2.1 15.6 2 14.4 2 11.9 2 10.2 3.5 10.2 6.3v2.2H7.5v3.7h2.7V22H14v-9.8h2.8l.4-3.7z"/></svg></span><span class="c-txt"><small>Facebook</small><span class="val">facebook.com/Alira Digital</span></span><span class="c-arr"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg></span></a>
        <a class="c-card" href="https://maps.google.com/?q=Vadodara,+Gujarat,+India" target="_blank" rel="noopener" data-reveal><span class="ico ico--brown"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s7-6.2 7-11.5A7 7 0 0 0 5 9.5C5 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg></span><span class="c-txt"><small>HQ · serving India &amp; worldwide</small><span class="val val--addr">Vadodara, Gujarat, 390007, India</span></span><span class="c-arr"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg></span></a>
      </div>
      <p class="muted" data-reveal style="margin:0">We work with cleaning companies, plumbers, landscapers, consultants and other home-service and local businesses across India and internationally (UK, US, Canada, AU and more). <a class="text-link" href="/areas-we-serve">See areas we serve</a>.</p>
      <div class="contact-direct" data-reveal>
        <a class="btn btn--green" href="https://wa.me/919313512434?text=Hi%20Alira%20Digital%2C%20I%27d%20like%20a%20website%20quote." target="_blank" rel="noopener" data-magnetic>Chat on WhatsApp</a>
        <a class="btn btn--soft" href="mailto:info.aliradigital@gmail.com?subject=Website%20enquiry" data-magnetic>Email a brief</a>
        <a class="btn btn--soft" href="/pricing" data-magnetic>View pricing packages</a>
      </div>
    </div>
    <form class="form form--steps" id="enquiry" novalidate data-handoff="whatsapp" data-reveal data-err-svc="Pick at least one option, or 'Not sure yet'." data-err-msg="Choose what sounds familiar, or tell us a little about your business and website goals." data-err-name="Please add your name so we know who to reply to." data-err-biz="Tell us what your company does, so we understand your business before we reply." data-ready="Your message is ready. Open it in WhatsApp to send it, or email it to" data-wa="Open in WhatsApp" data-email="Send by email" data-edit="Edit my answers">
      <p class="handoff-note">After you prepare your message, you choose WhatsApp or email. We do not show a fake “sent successfully” state.</p>
      <div class="fs-head">
        <h2>Request a website quote</h2>
        <ol class="fs-steps"><li class="is-on"><b>1</b><span>What you need</span></li><li><b>2</b><span>Your business</span></li><li><b>3</b><span>Your details</span></li></ol>
        <div class="fs-bar" aria-hidden="true"><i></i></div>
      </div>
      <fieldset class="fs-step is-on">
        <legend>What do you need? <small>Pick one or more</small></legend>
        <div class="pick-grid">
          <input type="checkbox" id="svc-3" name="svc" value="Business website"><label for="svc-3"><span class="pk-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 3.5 5.7 3.5 9s-1 6.3-3.5 9c-2.5-2.7-3.5-5.7-3.5-9s1-6.3 3.5-9z"/></svg></span><b>Business website</b><small>Multi-page site for your company</small></label>
          <input type="checkbox" id="svc-lp" name="svc" value="Landing page"><label for="svc-lp"><span class="pk-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M8 14h8"/></svg></span><b>Landing page</b><small>One-page campaign or offer site</small></label>
          <input type="checkbox" id="svc-redesign" name="svc" value="Website redesign"><label for="svc-redesign"><span class="pk-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 7h10M18 7h2M4 17h4M12 17h8"/><circle cx="16" cy="7" r="2"/><circle cx="10" cy="17" r="2"/></svg></span><b>Website redesign</b><small>Refresh an existing site</small></label>
          <input type="checkbox" id="svc-seo" name="svc" value="SEO &amp; content pages"><label for="svc-seo"><span class="pk-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3-3"/></svg></span><b>SEO pages</b><small>Service / location pages</small></label>
          <input type="checkbox" id="svc-0" name="svc" value="Custom system / ERP (optional)"><label for="svc-0"><span class="pk-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="13" rx="2"/><path d="M8 21h8M12 17v4M7 13v-3M11 13V8M15 13v-5"/></svg></span><b>Custom system</b><small>Optional — ERP / operations</small></label>
          <input type="checkbox" id="svc-4" name="svc" value="Not sure yet"><label for="svc-4"><span class="pk-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.7.3-1 .8-1 1.5V14M12 17h.01"/></svg></span><b>Not sure yet</b><small>We'll help you figure it out</small></label>
        </div>
        <div class="field" style="margin-top:18px">
          <label>Package interest <small style="font-weight:500;color:var(--color-text-muted)">(optional)</small></label>
          <div class="package-chips">
            <label><input type="checkbox" name="today" id="pkg-starter" value="Interested in Starter ($249)"> Starter $249</label>
            <label><input type="checkbox" name="today" id="pkg-business" value="Interested in Business ($449)"> Business $449</label>
            <label><input type="checkbox" name="today" id="pkg-premium" value="Interested in Premium ($699)"> Premium $699</label>
            <label><input type="checkbox" name="today" id="pkg-custom" value="Need a custom quotation"> Custom quote</label>
          </div>
        </div>
      </fieldset>
      <fieldset class="fs-step">
        <legend>About your business <small>Choose what sounds familiar</small></legend>
        <div class="opt-chips">
          <input type="checkbox" id="today-0" name="today" value="No website yet"><label for="today-0">No website yet</label>
          <input type="checkbox" id="today-1" name="today" value="Outdated website"><label for="today-1">Outdated website</label>
          <input type="checkbox" id="today-2" name="today" value="Need more enquiries"><label for="today-2">Need more enquiries</label>
          <input type="checkbox" id="today-3" name="today" value="Expanding service areas"><label for="today-3">Expanding service areas</label>
          <input type="checkbox" id="today-4" name="today" value="Running ads / campaigns"><label for="today-4">Running ads / campaigns</label>
        </div>
        <div class="field"><label for="f-msg">Anything else we should know?</label><textarea id="f-msg" name="message" placeholder="e.g. Cleaning company in Austin, need a 7-page site with quote form and service area pages."></textarea></div>
      </fieldset>
      <fieldset class="fs-step">
        <legend>Your details <small>So we can reply</small></legend>
        <div class="two">
          <div class="field"><label for="f-name">Your name</label><input id="f-name" name="name" autocomplete="name" placeholder="Alex Morgan"></div>
          <div class="field"><label for="f-company">Company</label><input id="f-company" name="company" autocomplete="organization" placeholder="Bright Home Cleaning"></div>
        </div>
        <div class="field"><label for="f-biz">What does your company do?</label><input id="f-biz" name="business" placeholder="e.g. Residential cleaning, plumbing, landscaping"></div>
        <div class="field"><label for="f-phone">Phone or email</label><input id="f-phone" name="contact" placeholder="+1 … or you@email.com"></div>
      </fieldset>
      <div class="fs-nav">
        <button class="btn btn--soft fs-back" type="button" hidden><span class="btn-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M17 7 7 17M16 16H7V7"/></svg></span> Back</button>
        <button class="btn btn--green fs-next" type="button" data-magnetic>Next <span class="btn-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg></span></button>
        <button class="btn btn--green fs-send" type="submit" data-magnetic hidden>Prepare my message <span class="btn-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg></span></button>
      </div>
      <div class="form-out" role="status" aria-live="polite"></div>
    </form>
  </div>
</section>

<section class="pad-sm" style="padding-top:0">
  <div class="wrap">
    <div class="map-card" data-reveal>
      <div class="map-view" data-map data-lat="22.3072" data-lng="73.1812" data-mark="/assets/img/alira-mark.svg?v=4" data-name="Alira Digital" data-addr="Vadodara, Gujarat, 390007, India" data-waze="https://wa.me/919313512434" data-whatsapp="https://wa.me/919313512434" data-gmaps="https://maps.google.com/?q=Vadodara,+Gujarat,+India" data-hint="Click to explore the map" role="region" aria-label="Map of the Alira Digital office in Vadodara, Gujarat"></div>
      <div class="map-info">
        <small>Visit us</small>
        <b>Alira Digital</b>
        <span>Vadodara, Gujarat, 390007, India</span>
        <div class="map-btns">
          <a class="btn btn--green" href="https://wa.me/919313512434?text=Hi%20Alira%20Digital%2C%20I%27d%20like%20a%20website%20quote." target="_blank" rel="noopener" data-magnetic>WhatsApp <span class="btn-ico"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.2 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .1-3.3-.8-2.8-1.1-4.5-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.9s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.9 2.1c.1.2.1.3 0 .5l-.3.5-.4.5c-.1.1-.3.3-.1.6.2.3.7 1.2 1.6 2 1.1 1 2 1.3 2.3 1.4.3.1.5.1.6-.1l.9-1c.2-.3.4-.2.6-.1l2 1c.3.1.5.2.5.3.1.2.1.7-.1 1.3z"/></svg></span></a>
          <a class="btn btn--soft" href="https://maps.google.com/?q=Vadodara,+Gujarat,+India" target="_blank" rel="noopener" data-magnetic>Google Maps <span class="btn-ico"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7zm0 9.6a2.6 2.6 0 1 1 0-5.2 2.6 2.6 0 0 1 0 5.2z"/></svg></span></a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="pad on-dark" id="refer" style="overflow:hidden">
  <div class="dark-dots"></div>
  <div class="wrap" style="position:relative">
    <div class="sec-head">
      <span class="eyebrow">Work with us</span>
      <h2 class="h2" data-split>Know a business that needs a better website?</h2>
      <p class="muted">Good introductions help the right companies get found online. Here's who we help and how to connect us.</p>
    </div>
    <div class="refer-tabs" role="tablist" aria-label="Referral guide">
      <button type="button" role="tab" id="t-refer" aria-controls="p-refer" aria-selected="true">Ideal referral</button>
      <button type="button" role="tab" id="t-collab" aria-controls="p-collab" aria-selected="false">Collaboration partners</button>
      <button type="button" role="tab" id="t-intro" aria-controls="p-intro" aria-selected="false">How to introduce us</button>
    </div>
    <div class="refer-panel" id="p-refer" role="tabpanel" aria-labelledby="t-refer"><ul class="refer-list"><li><span class="rf-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 21V10l5 3v-3l5 3V9l5 3V4h3v17z"/></svg></span><b>Home-service owners</b><span>Cleaning, plumbing, landscaping and similar local service businesses.</span></li><li><span class="rf-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M3 14h18M9 4v16M15 4v16"/></svg></span><b>No site or an outdated site</b><span>Businesses that still rely on social posts or an old brochure site.</span></li><li><span class="rf-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></span><b>Need more quote requests</b><span>Owners who want clearer service pages and a stronger enquiry path.</span></li><li><span class="rf-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 15c-1.5 1.5-2 5-2 5s3.5-.5 5-2M9 15l-3-3c1-4 4-8 11-9-1 7-5 10-9 11zM14.5 9.5h.01"/></svg></span><b>Expanding into new areas</b><span>Teams launching in new cities or service zones who need a credible site.</span></li></ul></div>
    <div class="refer-panel" id="p-collab" role="tabpanel" aria-labelledby="t-collab" hidden><ul class="refer-list"><li><span class="rf-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M8 9v11"/></svg></span><b>Marketing freelancers</b><span>Bring us in when a client needs the website behind your campaigns.</span></li><li><span class="rf-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7l9-4 9 4v10l-9 4-9-4z"/><path d="M3 7l9 4 9-4M12 11v10"/></svg></span><b>Local consultants</b><span>Refer owners who need a professional web presence for their brand.</span></li><li><span class="rf-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m12 19 7-7 3 3-7 7-3-3z"/><path d="m18 13-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"/><path d="m2 2 7.586 7.586"/><circle cx="11" cy="11" r="2"/></svg></span><b>Graphic designers</b><span>Partner when designs need to become a live, conversion-focused site.</span></li><li><span class="rf-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l2.4 5.6L20 11l-5.6 2.4L12 19l-2.4-5.6L4 11l5.6-2.4z"/><path d="M19 3v4M17 5h4"/></svg></span><b>Branding studios</b><span>Refer clients who need their new brand carried into a website.</span></li></ul></div>
    <div class="refer-panel" id="p-intro" role="tabpanel" aria-labelledby="t-intro" hidden><ul class="refer-list"><li><span class="rf-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m8 8-4 4 4 4M16 8l4 4-4 4M14 5l-4 14"/></svg></span><b>Website design &amp; development agency</b><span>We build professional sites for small and mid-sized service businesses.</span></li><li><span class="rf-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="6" height="6" rx="1.5"/><rect x="15" y="15" width="6" height="6" rx="1.5"/><path d="M9 6h4a2 2 0 0 1 2 2v7"/></svg></span><b>Clear packages and custom quotes</b><span>Starting prices in USD, with written scope before work begins.</span></li><li><span class="rf-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 7h10M18 7h2M4 17h4M12 17h8"/><circle cx="16" cy="7" r="2"/><circle cx="10" cy="17" r="2"/></svg></span><b>Easy first conversation</b><span>Introduce us on WhatsApp or email — we take it from there.</span></li></ul></div>
  </div>
</section>

</main>'''


def wire_css(text: str, extra: str) -> str:
    if extra in text:
        return text
    needle = '<link rel="stylesheet" href="/assets/css/brand-system.css">'
    if needle in text:
        return text.replace(
            needle,
            needle + f'\n<link rel="stylesheet" href="{extra}">',
            1,
        )
    return text


def fix_pricing(path: Path):
    text = path.read_text(encoding="utf-8")
    text = wire_css(text, "/assets/css/pricing-contact.css")
    if "home-agency.css" not in text:
        text = wire_css(text, "/assets/css/home-agency.css")
    # Fix FAQ leftover twitter tags
    text = text.replace(
        '<meta name="twitter:title" content="FAQ: Custom ERP, Apps &amp; Websites | Alira Digital">',
        '<meta name="twitter:title" content="Website Development Pricing | Alira Digital">',
    )
    text = text.replace(
        '<meta name="twitter:description" content="Answers to common questions about Alira Digital: custom ERP systems, AI agents, mobile apps and websites, cost and timelines, clients across India and worldwide and support after launch.">',
        '<meta name="twitter:description" content="Transparent website development packages starting at $249 USD. Clear deliverables, no unlimited revision promises.">',
    )
    # Strip FAQPage schema block by replacing with slim Offer catalog — keep org only via simple breadcrumb fix
    text = re.sub(
        r'\{"@type":"BreadcrumbList","itemListElement":\[\{"@type":"ListItem","position":1,"name":"Home","item":"/"\},\{"@type":"ListItem","position":2,"name":"FAQ","item":"/faq"\}\]\}',
        '{"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"/"},{"@type":"ListItem","position":2,"name":"Pricing","item":"/pricing"}]}',
        text,
        count=1,
    )
    # Remove FAQPage entity from JSON-LD if present
    text = re.sub(
        r',\{"@type":"FAQPage","mainEntity":\[[\s\S]*?\]\}\]\}</script>',
        "]}</script>",
        text,
        count=1,
    )
    text = re.sub(r"<main>[\s\S]*?</main>", PRICING_MAIN, text, count=1)
    # Fix footer FAQ link + extra closing div under mobile menu
    text = text.replace('<li><a href="/pricing">FAQ</a></li>', '<li><a href="/faq">FAQ</a></li>')
    # Remove duplicate stray </div> after mobile menu if present (mm-foot closes then extra)
    text = text.replace(
        """    </div>
  </div>
</div>
<main>""",
        """    </div>
</div>
<main>""",
        1,
    )
    path.write_text(text, encoding="utf-8", newline="\n")
    print("pricing updated")


def fix_contact(path: Path):
    text = path.read_text(encoding="utf-8")
    text = wire_css(text, "/assets/css/home-agency.css")
    text = wire_css(text, "/assets/css/pricing-contact.css")
    if "contact-handoff.js" not in text:
        text = text.replace(
            '<script src="/local-demo.js"></script>',
            '<script src="/local-demo.js"></script>\n<script src="/assets/js/contact-handoff.js" defer></script>',
            1,
        )
    text = re.sub(
        r"<title>.*?</title>",
        "<title>Contact &amp; Free Website Quote | Alira Digital</title>",
        text,
        count=1,
        flags=re.S,
    )
    text = re.sub(
        r'<meta name="description" content="[^"]*">',
        '<meta name="description" content="Contact Alira Digital for a website quote. WhatsApp +91 9313512434 or email info.aliradigital@gmail.com. Prepare a brief and send via WhatsApp or email.">',
        text,
        count=1,
    )
    text = re.sub(
        r'<meta property="og:title" content="[^"]*">',
        '<meta property="og:title" content="Contact &amp; Free Website Quote | Alira Digital">',
        text,
        count=1,
    )
    text = re.sub(r"<main>[\s\S]*?</main>", CONTACT_MAIN, text, count=1)
    # Package query preselect helper
    if "package-preselect" not in text:
        text = text.replace(
            "</body>",
            """<script>
(function(){
  var p = new URLSearchParams(location.search).get('package');
  if (!p) return;
  var map = {starter:'pkg-starter', business:'pkg-business', premium:'pkg-premium'};
  var id = map[String(p).toLowerCase()];
  if (!id) return;
  var el = document.getElementById(id);
  if (el) el.checked = true;
  var svc = document.getElementById('svc-3');
  if (svc) svc.checked = true;
})();
</script>
</body>""",
            1,
        )
    path.write_text(text, encoding="utf-8", newline="\n")
    print("contact updated")


fix_pricing(root / "pricing" / "index.html")
fix_contact(root / "contact" / "index.html")

# Sync homepage package CTAs to contact package params where useful
home = root / "index.html"
h = home.read_text(encoding="utf-8")
h2 = h.replace(
    '<a class="btn btn--soft" href="/pricing" data-magnetic>View package</a>',
    '<a class="btn btn--soft" href="/pricing" data-magnetic>View package</a>',
    1,
)
# Featured Business already goes to contact — add package param
h2 = h2.replace(
    '''            <a class="btn btn--green" href="/contact" data-magnetic>Get a Free Quote</a>
          </article>
          <article class="price-card" data-reveal>
            <span class="plan">Premium</span>''',
    '''            <a class="btn btn--green" href="/contact?package=business" data-magnetic>Get a Free Quote</a>
          </article>
          <article class="price-card" data-reveal>
            <span class="plan">Premium</span>''',
    1,
)
if h2 != h:
    home.write_text(h2, encoding="utf-8", newline="\n")
    print("homepage pricing CTA synced")
else:
    print("homepage unchanged or pattern missed")
