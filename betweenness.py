from __future__ import print_function
import networkx as nx
import time
import sys
from load_graph import load_graph
def main():
    filename = sys.argv[1]
    graph = load_graph(filename)

    betweenness_start = time.time()
    betweenness = nx.betweenness_centrality(graph)
    betweenness_end = time.time()
    print('calculate time ', (betweenness_end - betweenness_start))

if __name__ == '__main__':
    main()
