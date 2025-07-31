# app/cleaner.py

import re

def refine_bullets(slide_data):
    """
    Refines slide bullet content by:
    - Splitting compound sentences into atomic ideas
    - Removing duplicates
    - Cleaning up whitespace and empty lines
    """
    cleaned = []

    for slide in slide_data:
        title = slide.get("slide_title", "").strip()
        raw_bullets = slide.get("bullets", [])
        refined_bullets = []

        for bullet in raw_bullets:
            # Split on newline and sentence-ending punctuation (., ;)
            parts = re.split(r'[\n;.]+', bullet)

            for part in parts:
                text = part.strip()
                if len(text) > 3 and text.lower() not in [b.lower() for b in refined_bullets]:
                    refined_bullets.append(text)

        cleaned.append({
            "slide_title": title,
            "bullets": refined_bullets
        })

    return cleaned
