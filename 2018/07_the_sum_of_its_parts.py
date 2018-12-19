
'''
ADVENT OF CODE: 2018
Day 7: The Sum of Its Parts
'''
from parse import parse
import networkx as nx
from string import ascii_uppercase

in_file = open('inputs/07.input','r').readlines()
inst = [tuple(parse('Step {} must be finished before step {} can begin.',l)) for l in in_file]

# part 1
step_types = set(x for sl in inst for x in sl)
G = nx.DiGraph()
map(G.add_node, step_types)
G.add_edges_from(inst)
ltsorted = ''.join(nx.lexicographical_topological_sort(G))
print(ltsorted)

# part 2
durations = {letter:ord(letter)-ord('A')+61 for letter in ascii_uppercase}
p = nx.dag_longest_path(G)
print(p)
print(sum(durations[n] for n in p))



