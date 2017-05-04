import networkx as nx
import time

input = open('slashdot0811.txt', 'r')
g = nx.DiGraph()
load_start = time.time()
for line in input:
  arr = line.split('\t')
  g.add_weighted_edges_from([(arr[0], arr[1], 1)])

load_end = time.time()

# print 'load time ' + (load_end - load_start)

# betweenness_start = time.time()
# betweenness = nx.betweenness_centrality(g)
# betweenness_end = time.time()
# print 'calculate time ' + (betweenness_end - betweenness_start)
eigenvector = nx.eigenvector_centrality(g)

