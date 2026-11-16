from pathlib import Path

p = Path(__file__).resolve().parents[1] / "pricing" / "index.html"
t = p.read_text(encoding="utf-8")
t = t.replace(
    "<p>Web &amp; System Solutions. We build custom ERP systems, AI agents &amp; automation, online platforms, mobile apps and corporate websites for businesses across India and worldwide.</p>",
    "<p>Website Design &amp; Development. We create professional, modern websites that help small businesses build trust, attract customers and grow online.</p>",
    1,
)
old = """          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about-us">About Us</a></li>
            <li><a href="/services">Services</a></li>
            <li><a href="/industries">Who we serve</a></li>
            <li><a href="/projects">Projects</a></li>
            <li><a href="/blog">Blog</a></li>
            <li><a href="/contact">Contact</a></li>
          </ul>"""
new = """          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/services">Services</a></li>
            <li><a href="/industries">Industries</a></li>
            <li><a href="/projects">Work</a></li>
            <li><a href="/pricing">Pricing</a></li>
            <li><a href="/about-us">About</a></li>
            <li><a href="/contact">Contact</a></li>
          </ul>"""
if old in t:
    t = t.replace(old, new, 1)
    print("footer pages updated")
else:
    print("footer pages pattern not found")
p.write_text(t, encoding="utf-8")
print("done")
