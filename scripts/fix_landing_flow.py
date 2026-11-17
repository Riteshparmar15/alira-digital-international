from pathlib import Path

p = Path(__file__).resolve().parents[1] / "index.html"
html = p.read_text(encoding="utf-8")

about_start = html.find(
    '    <section class="pad on-dark" data-glow style="overflow:hidden" id="about">'
)
about_end = html.find('    <section class="pad" id="industries"', about_start)
if about_start == -1 or about_end == -1:
    raise SystemExit(f"about block not found: {about_start=} {about_end=}")

about = html[about_start:about_end]
html = html[:about_start] + html[about_end:]

faq_marker = '    <section class="pad" id="faq" aria-labelledby="faq-title">'
faq_idx = html.find(faq_marker)
if faq_idx == -1:
    raise SystemExit("faq marker not found")

html = html[:faq_idx] + about + "\n" + html[faq_idx:]
p.write_text(html, encoding="utf-8")
print("Moved #about to sit after pricing and before FAQ.")
