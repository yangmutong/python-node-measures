from __future__ import print_function
import networkx as nx
import time
import sys
from load_graph import load_graph

def main():
    filename = sys.argv[1]
    graph = load_graph(filename)

    closeness_start = time.time()
    closeness = nx.closeness_centrality(graph)
    closeness_end = time.time()
    print('calculate time ', (closeness_end -closeness_start))

if __name__ == '__main__':
    main()