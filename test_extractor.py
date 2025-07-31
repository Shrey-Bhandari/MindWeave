# test_extractor.py

import os
from app.extractor import extract_pptx_content

from app.extractor import extract_pptx_content
from app.cleaner import refine_bullets



# Load slides
slides = extract_pptx_content("uploads/Unit 1.pptx")

# Clean bullets
refined = refine_bullets(slides)

# Print preview
for idx, slide in enumerate(refined, 1):
    print(f"\n🔹 Slide {idx}: {slide['slide_title']}")
    for bullet in slide["bullets"]:
        print(f"   • {bullet}")


def main():
    pptx_path = "uploads/Unit 1.pptx"

    if not os.path.exists(pptx_path):
        print(f"❌ File not found: {pptx_path}")
        return

    print(f"📂 Extracting from: {pptx_path}")
    slides = extract_pptx_content(pptx_path)

    if not slides:
        print("⚠️ No slide content found.")
        return

    print("\n📑 Extracted Slide Content:\n" + "-" * 40)
    for idx, slide in enumerate(slides, 1):
        title = slide.get("slide_title", "Untitled Slide")
        bullets = slide.get("bullets", [])
        print(f"\n🔹 Slide {idx}: {title}")
        if bullets:
            for bullet in bullets:
                print(f"   • {bullet}")
        else:
            print("   (No bullet points found)")

if __name__ == "__main__":
    main()
