from pathlib import Path

root = Path(__file__).resolve().parents[1]
old = """        <li><a href=\"/services\">All Services</a></li>
        <li><a href=\"/custom-erp-system\">Business &amp; ERP System</a></li>
        <li><a href=\"/online-platform-development\">Online Platform</a></li>
        <li><a href=\"/mobile-app-development\">Mobile Application</a></li>
        <li><a href=\"/website-design\">Website Design</a></li>
        <li><a href=\"/ai-agents-automation\">AI Agents &amp; Automation</a></li>"""
new = """        <li><a href=\"/services\">All Services</a></li>
        <li><a href=\"/services\">Business Websites</a></li>
        <li><a href=\"/services\">Website Redesign</a></li>
        <li><a href=\"/services\">Landing Pages</a></li>
        <li><a href=\"/website-design\">Website Design</a></li>
        <li><a href=\"/pricing\">Pricing</a></li>"""

targets = [
    "contact/index.html",
    "pricing/index.html",
    "services/index.html",
    "about-us/index.html",
    "industries/index.html",
    "projects/index.html",
    "faq/index.html",
    "areas-we-serve/index.html",
]

for rel in targets:
    path = root / rel
    if not path.exists():
        print("missing", rel)
        continue
    text = path.read_text(encoding="utf-8")
    if old not in text:
        print("no-match", rel)
        continue
    path.write_text(text.replace(old, new), encoding="utf-8")
    print("updated", rel)
