from __future__ import print_function
import networkx as nx
import time
import sys
from load_graph import load_graph

def main():
    filename = sys.argv[1]
    graph = load_graph(filename)

    in_degree_start = time.time()
    in_degree = nx.in_degree_centrality(graph)
    in_degree_end = time.time()
    print('in degree calculate time ', (in_degree_end - in_degree_start))

    out_degree_start = time.time()
    out_degree = nx.out_degree_centrality(graph)
    out_degree_end = time.time()
    print('out degree calculate time ', (out_degree_end - out_degree_start))

    degree_start = time.time()
    degree = nx.degree_centrality(graph)
    degree_end = time.time()
    print('degree calculate time ', (degree_end - degree_start))

if __name__ == '__main__':
    main()
