from __future__ import print_function
import networkx as nx
import time
import sys
from load_graph import load_graph
def main():
    filename = sys.argv[1]
    graph = load_graph(filename)
    eigenvector_start = time.time()
    eigenvector = nx.eigenvector_centrality(graph)
    eigenvector_end = time.time()
    print('calculate time ', (eigenvector_end - eigenvector_start))

if __name__ == '__main__':
    main()
