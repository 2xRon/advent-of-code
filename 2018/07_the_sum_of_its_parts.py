"""
ADVENT OF CODE: 2018
Day 7: The Sum of Its Parts
"""
from parse import parse
import networkx as nx
from string import ascii_uppercase
import matplotlib.pyplot as plt

in_file = open("inputs/07.input", "r").readlines()

inst = [
    tuple(parse("Step {} must be finished before step {} can begin.", l))
    for l in in_file
]

# part 1
step_types = set(x for sl in inst for x in sl)
G = nx.DiGraph()
map(G.add_node, step_types)
G.add_edges_from(inst)
print("".join(nx.lexicographical_topological_sort(G)))


# part 2
durations = {letter: ord(letter) - ord("A") + 61 for letter in ascii_uppercase}
path = nx.dag_longest_path(G)
path_edges = list(zip(path, path[1:]))
print(sum(durations[n] for n in path))

pos = nx.spring_layout(G, k=5)
nx.draw(G, pos, node_color="k")
nx.draw_networkx_nodes(G, pos, nodelist=path, node_color="r")
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="r", width=3)
plt.axis("equal")
plt.savefig("graph.png", bbox_inches="tight")
