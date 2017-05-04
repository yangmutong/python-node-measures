# -*- coding:utf-8 -*-

import networkx as nx
import time
import community
import sys
from __future__ import print_function

def louvain():
    filename = sys.argv[1]
    input = open(filename, 'r')
    g = nx.DiGraph()
    load_start = time.time()
    for line in input:
      arr = line.split('\t')
      g.add_weighted_edges_from([(arr[0], arr[1], arr[3])])

    load_end = time.time()

    partition_start = time.time()
    partition = community.best_partition(g)
    partition_end = time.time()

    community_start = time.time()
    result = community.modularity(partition, g)
    community_end = time.time()

    print('# load time ', load_end - load_start)
    print('# partition time ', partition_end - partition_start)
    print('# community time ', community_end - community_start)


if __name__ == '__main__':
    louvain()
