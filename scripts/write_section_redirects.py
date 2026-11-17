from pathlib import Path

root = Path(__file__).resolve().parents[1]

redirects = {
    "services/index.html": "#services",
    "industries/index.html": "#industries",
    "projects/index.html": "#work",
    "pricing/index.html": "#pricing",
    "about-us/index.html": "#about",
    "contact/index.html": "#contact",
    "faq/index.html": "#faq",
    "areas-we-serve/index.html": "#industries",
    "website-design/index.html": "#services",
    "custom-erp-system/index.html": "#services",
    "custom-erp-guide/index.html": "#services",
    "online-platform-development/index.html": "#services",
    "mobile-app-development/index.html": "#services",
    "ai-agents-automation/index.html": "#services",
    "blog/index.html": "#top",
}

for rel, section in redirects.items():
    target = "/" + section  # "/#services"
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="robots" content="noindex, nofollow">
  <meta http-equiv="refresh" content="0;url={target}">
  <title>Redirecting… | Alira Digital</title>
  <script>location.replace('{target}');</script>
</head>
<body>
  <p><a href="{target}">Continue to Alira Digital</a></p>
</body>
</html>
"""
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    print("wrote", rel, "->", target)
