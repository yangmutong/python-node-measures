from __future__ import print_function
import networkx as nx
import time
import sys
from load_graph import load_graph

## clustering API in NetworkX has not been implemented for directed graph
def main():
    filename = sys.argv[1]
    graph = load_graph(filename, type='undirected')

    cc_start = time.time()
    cc = nx.clustering(graph, weight='weight')
    cc_end = time.time()

    print('calculate time ', (cc_end - cc_start))

if __name__ == '__main__':
    main()