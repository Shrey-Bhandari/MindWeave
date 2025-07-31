from graphviz import Digraph

dot = Digraph(comment='MindMap')
dot.attr(rankdir='LR')

dot.node('Root', 'MindMap')
dot.node('slide_0', 'Unit 1: Introduction to AI')
dot.edge('Root', 'slide_0')

dot.node('slide_1', 'What is AI?')
dot.edge('Root', 'slide_1')

dot.node('slide_1_0', 'Definition: Simulation of human intelligence in machines')
dot.edge('slide_1', 'slide_1_0')

# Add other nodes and edges similarly, following your DOT structure

# Render the graph to a PNG file
dot.render('mindmap_output', format='png', cleanup=True)

print("MindMap image generated as mindmap_output.png")
