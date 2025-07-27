import os
import json
from extractor import extract_pptx_content

# Path to your PPT file
ppt_file = "ppt_files/Unit 1.1.pptx"

# Run the extractor
slides = extract_pptx_content(ppt_file)

# Print to console (optional)
for i, slide in enumerate(slides, 1):
    print(f"\nSlide {i}: {slide['slide_title']}")
    for b in slide["bullets"]:
        print(f"  - {b}")

# Save output
output_path = "extracted/unit1_l1.json"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(slides, f, indent=2, ensure_ascii=False)

print(f"\n✅ Extracted data saved to {output_path}")
