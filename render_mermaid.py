# render_mermaid.py
from pathlib import Path
md_path = Path("outputs/diagram.md")
html_path = Path("outputs/diagram.html")
content = md_path.read_text(encoding="utf-8") if md_path.exists() else "No diagram.md found."
# strip triple backticks if present
if content.startswith("```mermaid"):
    content = content.replace("```mermaid", "").replace("```", "").strip()
html = f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8"/>
  <script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
    mermaid.initialize({{ startOnLoad: true }});
  </script>
  <style> body {{ font-family: Arial, sans-serif; padding: 20px; }} </style>
</head>
<body>
<h1>Mermaid Diagram</h1>
<div class="mermaid">
{content}
</div>
</body>
</html>"""
html_path.write_text(html, encoding="utf-8")
print("Wrote", html_path)
