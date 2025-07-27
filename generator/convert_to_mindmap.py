# generator/convert_to_mindmap.py

import json
import os

# Load extracted slide data
with open("../extracted/unit1_l1.json", "r", encoding="utf-8") as f:
    slide_data = json.load(f)

mindmap_nodes = []
mindmap_edges = []

node_id = 1
parent_id = None

def add_node(text, parent=None):
    global node_id
    current_id = str(node_id)
    mindmap_nodes.append({
        "id": current_id,
        "data": {"label": text},
        "position": {"x": 0, "y": 0}
    })
    if parent:
        mindmap_edges.append({
            "id": f"e{parent}-{current_id}",
            "source": parent,
            "target": current_id
        })
    node_id += 1
    return current_id

# Use slide titles as major nodes, bullets as sub-nodes
for slide in slide_data:
    title = slide.get("slide_title", f"Slide {node_id}").strip()
    bullets = slide.get("bullets", [])
    print(f"Converting slide: {title}")

    if title:
        parent_id = add_node(title)
        for b in bullets:
            text = b.strip()
            if text and len(text) > 2:
                add_node(text, parent=parent_id)

# Save mind map JSON
os.makedirs("../public", exist_ok=True)
with open("../public/mindmap.json", "w", encoding="utf-8") as f:
    json.dump({"nodes": mindmap_nodes, "edges": mindmap_edges}, f, indent=2)

print("✅ Mind map structure saved to public/mindmap.json")
