# app/mindmap_graphviz.py
import os

# Explicitly set Graphviz bin path for Python subprocess
os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"


from graphviz import Digraph

def generate_graphviz_code(slide_data):
    """
    Converts slide structure into Graphviz DOT code.
    Returns a string for use in st.graphviz_chart().
    """
    dot = Digraph()
    dot.attr(rankdir="LR")  # Change to TB for vertical tree
    dot.node("Root", "MindMap")

    for i, slide in enumerate(slide_data):
        slide_title = slide.get("slide_title", f"Slide {i+1}").strip()
        slide_id = f"slide_{i}"
        dot.node(slide_id, slide_title)
        dot.edge("Root", slide_id)

        for j, bullet in enumerate(slide.get("bullets", [])):
            bullet_id = f"{slide_id}_{j}"
            dot.node(bullet_id, bullet.strip())
            dot.edge(slide_id, bullet_id)

    return dot.source
