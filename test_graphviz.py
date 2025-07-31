# test_graphviz.py

from app.extractor import extract_pptx_content
from app.cleaner import refine_bullets
from app.mindmap_graphviz import generate_graphviz_code

pptx_path = "uploads/Unit 1.pptx"
slides = extract_pptx_content(pptx_path)
cleaned = refine_bullets(slides)

dot_code = generate_graphviz_code(cleaned)

print("\n🧠 MindMap DOT Code:")
print("-" * 40)
print(dot_code)
