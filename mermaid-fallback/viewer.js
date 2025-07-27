import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';

mermaid.initialize({ startOnLoad: false });

function sanitizeLabel(text) {
  return text
    .replace(/\n/g, ' ')             // Remove newlines
    .replace(/["<>]/g, '')           // Remove double quotes, angle brackets
    .replace(/\s+/g, ' ')            // Collapse whitespace
    .trim()
    .slice(0, 50);                   // Limit to 50 chars
}

async function renderMindMap() {
  try {
    const res = await fetch('../public/mindmap.json');
    const data = await res.json();

    let diagram = 'graph TD;\n';

    for (const edge of data.edges) {
      const sourceNode = data.nodes.find(n => n.id === edge.source);
      const targetNode = data.nodes.find(n => n.id === edge.target);

      if (sourceNode && targetNode) {
        const sourceLabel = sanitizeLabel(sourceNode.data.label);
        const targetLabel = sanitizeLabel(targetNode.data.label);

        diagram += `"${edge.source}"["${sourceLabel}"] --> "${edge.target}"["${targetLabel}"]\n`;
      }
    }

    document.querySelector('#mermaid').textContent = diagram;
    mermaid.init(undefined, '#mermaid');
  } catch (err) {
    console.error("⚠️ Error loading mind map:", err);
    document.querySelector('#mermaid').textContent = 'graph TD;\nA["Error loading data"]';
    mermaid.init(undefined, '#mermaid');
  }
}

window.onload = renderMindMap;
