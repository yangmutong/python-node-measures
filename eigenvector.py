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
    print('Eigenvector centrality time: %.5f' % (time.time() - eigenvector_start))

    eigenvector_start = time.time()
    eigenvector = nx.eigenvector_centrality_numpy(graph)
    print('Eigenvector centrality with Numpy time: %.5f' % (time.time() - eigenvector_start))

if __name__ == '__main__':
    main()
