# Written by Ovi
# Date: 2025-02-24
# This script generates and saves a hierarchical tree structure representing process creation using fork().

import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Define nodes
nodes = {
    "P": "(Parent) P",
    "C1": "(Child #1)\npid = fork()",
    "C1R": "(returns > 0)",
    "C2": "(Child #2)\npid2 = fork()",
    "C2R": "(returns > 0)",
    "C3": "(Child #3)\npid3 = fork()",
    "C3R": "(returns > 0)"
}

# Add nodes to the graph
for key, label in nodes.items():
    G.add_node(key, label=label)

# Define edges to represent fork process and returns
edges = [
    ("P", "C1"),  # Parent forks Child #1
    ("C1", "C1R"),  # Return from fork (Parent continues)
    ("C1", "C2"),  # Child #1 forks Child #2
    ("C2", "C2R"),  # Return from fork (Child #1 continues)
    ("C2", "C3"),  # Child #2 forks Child #3
    ("C3", "C3R")   # Return from fork (Child #2 continues)
]

# Add edges to the graph
G.add_edges_from(edges)

# Define positions for a tree-like visualization
pos = {
    "P": (0, 4),
    "C1": (-1, 3),
    "C1R": (1, 3),
    "C2": (-1.5, 2),
    "C2R": (-0.5, 2),
    "C3": (-2, 1),
    "C3R": (-1, 1)
}

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(
    G, pos, with_labels=True,
    labels=nx.get_node_attributes(G, 'label'),
    node_size=3500, node_color="lightblue",
    font_size=9, font_weight="bold", edge_color="black",
    linewidths=1.5, arrows=True
)

# Save as high-quality image
plt.savefig("hierarchy_tree.png", dpi=300, bbox_inches='tight')