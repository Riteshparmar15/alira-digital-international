from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
pattern = re.compile(r"(</div>\n)(  </div>\n)(  <main>)")
fixed = 0
for path in root.rglob("*.html"):
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    new, n = pattern.subn(r"\1\3", text, count=1)
    # Only fix when mobile-menu is immediately above
    if n and 'id="mobileMenu"' in text[max(0, text.find("<main>") - 800) : text.find("<main>")]:
        path.write_text(new, encoding="utf-8", newline="\n")
        fixed += 1
        print("fixed", path.relative_to(root))
print("fixed count", fixed)
