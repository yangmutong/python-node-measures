import networkx as nx
import time
from __future__ import print_function
import sys

def main():
    filename = sys.argv[1]
    input = open(filename, 'r')
    g = nx.DiGraph()
    load_start = time.time()
    for line in input:
      arr = line.split('\t')
      g.add_weighted_edges_from([(arr[0], arr[1], 1)])

    load_end = time.time()

    print('load time ', (load_end - load_start))

    betweenness_start = time.time()
    betweenness = nx.betweenness_centrality(g)
    betweenness_end = time.time()
    print('calculate time ', (betweenness_end - betweenness_start))


if __name__ == '__main__':
    main()
