# -*- coding:utf-8 -*-
from __future__ import print_function
import networkx as nx
import time
import community
import sys
from load_graph import load_graph

def louvain():
    filename = sys.argv[1]
    graph = load_graph(filename)

    partition_start = time.time()
    partition = community.best_partition(g)
    partition_end = time.time()

    community_start = time.time()
    result = community.modularity(partition, graph)
    community_end = time.time()

    print('# partition time ', partition_end - partition_start)
    print('# community time ', community_end - community_start)


if __name__ == '__main__':
    louvain()
