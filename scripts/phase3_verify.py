from pathlib import Path

root = Path(__file__).resolve().parents[1]
idx = (root / "index.html").read_text(encoding="utf-8")
print("homepage Get a Free Quote:", idx.count("Get a Free Quote"))
print("homepage hero--agency:", "hero--agency" in idx)
print("homepage home-agency.css:", "home-agency.css" in idx)
print("extra close before main:", "</div>\n  </div>\n  <main>" in idx.replace("\r\n", "\n"))
print("pricing exists:", (root / "pricing" / "index.html").exists())
pricing = (root / "pricing" / "index.html").read_text(encoding="utf-8")
print("pricing title ok:", "Website Development Pricing" in pricing)
print("pricing packages:", pricing.count("$249") + pricing.count("$449") + pricing.count("$699"))

# detect possible double mobile-menu close across pages
bad = []
for p in root.rglob("*.html"):
    t = p.read_text(encoding="utf-8").replace("\r\n", "\n")
    if "</div>\n  </div>\n  <main>" in t:
        bad.append(str(p.relative_to(root)))
print("pages with extra close before main:", bad or "none")
