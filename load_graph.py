from __future__ import print_function
import networkx as nx
import time

def load_graph(filename, type='directed'):
    input = open(filename, 'r')
    g = nx.Graph()
    if type == 'directed':
        g = nx.DiGraph()
    load_start = time.time()
    for line in input:
        arr = line.split('\t')
        g.add_weighted_edges_from([(arr[0], arr[1], 1)])

    load_end = time.time()
    print('load time ', (load_end - load_start))
    return g