# -*- coding:utf-8 -*-

import networkx as nx
from heapq import heappop, heappush
from itertools import count
import random
from math import sqrt
from networkx.utils import not_implemented_for


g = nx.DiGraph()
g.add_weighted_edges_from([ (1, 2, 7.0), (1, 4, 5.0), (2, 3, 8.0), (2, 4, 9.0), (2,5,7.0), (3, 5, 5.0), (4, 5, 15.0), (4,6, 6.0), (5, 6, 8.0), (5, 7, 9.0), (6, 7, 11.0)])



def _single_source_dijkstra_path_basic(G, s, weight='weight'):
    # modified from Eppstein
    # 可以到达的节点
    accessNodes = []
    P = {}
    # 初始化P
    for v in G:
        P[v] = []
    # 初始化sigma
    sigma = dict.fromkeys(G, 0.0)    # sigma[v]=0 for v in G
    alreadySearched = {}
    sigma[s] = 1.0
    push = heappush
    pop = heappop
    seen = {s: 0}
    c = count()
    Q = []   # use Q as heap with (distance,node id) tuples
    push(Q, (0, next(c), s, s))
    while Q:
        (dist, _, pred, v) = pop(Q)
        if v in alreadySearched:
            continue  # already searched this node.
        sigma[v] += sigma[pred]  # count paths
        accessNodes.append(v)
        alreadySearched[v] = dist
        for w, edgedata in G[v].items():
            vw_dist = dist + edgedata.get(weight, 1)
            if w not in alreadySearched and (w not in seen or vw_dist < seen[w]):
                seen[w] = vw_dist
                push(Q, (vw_dist, next(c), v, w))
                sigma[w] = 0.0
                P[w] = [v]
            elif vw_dist == seen[w]:  # handle equal paths
                sigma[w] += sigma[v]
                P[w].append(v)
    return accessNodes, P, sigma

def _accumulate_basic(betweenness, S, P, sigma, s):
    delta = dict.fromkeys(S, 0)
    while S:
        w = S.pop()
        coeff = (1.0 + delta[w]) / sigma[w]
        for v in P[w]:
            delta[v] += sigma[v] * coeff
        if w != s:
            betweenness[w] += delta[w]
    return betweenness

# accessNodes, P, sigma = _single_source_dijkstra_path_basic(g, 1)
# betweenness = dict.fromkeys(g, 0.0)
# print accessNodes
# print P
# print sigma
# print betweenness
# print _accumulate_basic(betweenness, accessNodes, P, sigma, 1)

def eigenvector_centrality(G, max_iter=100, tol=1.0e-6, nstart=None,
                           weight='weight'):
    if len(G) == 0:
        raise nx.NetworkXPointlessConcept('cannot compute centrality for the'
                                          ' null graph')
    # If no initial vector is provided, start with the all-ones vector.
    if nstart is None:
        # 将所有节点的值赋值为1
        nstart = {v: 1.0 for v in G}
    if all(v == 0 for v in nstart.values()):
        raise nx.NetworkXError('initial vector cannot have all zero values')
    # Normalize the initial vector so that each entry is in [0, 1]. This is
    # guaranteed to never have a divide-by-zero error by the previous line.
    # 对节点中的每一个节点赋值，将值改为节点中的值除以初始化节点的总数, k为键，v为对应的键值,x 为初始值
    x = {k: v / sum(nstart.values()) for k, v in nstart.items()}
    # 图中节点的总数
    nnodes = G.number_of_nodes()
    # make up to max_iter iterations
    # 在最大迭代次数内进行循环迭代计算
    for i in range(max_iter):
        xlast = x
        x = xlast.copy()  # Start with xlast times I to iterate with (A+I)
        # do the multiplication y^T = x^T A (left eigenvector)
        # 对于每一个节点
        for n in x:
            # 中的每一个邻接节点
            for nbr in G[n]:
                # 更新邻接节点的中心性的值为此节点的中心性的值乘以与邻接节点相连的边的权重，如无权重则乘以1
                x[nbr] += xlast[n] * G[n][nbr].get(weight, 1)
        # Normalize the vector. The normalization denominator `norm`
        # should never be zero by the Perron--Frobenius
        # theorem. However, in case it is due to numerical error, we
        # assume the norm to be one instead.
        # 将上述获得的节点的中心性值的列表中的每个中心性值平方后整体求和，并开方
        norm = sqrt(sum(z ** 2 for z in x.values())) or 1
        print('norm ')
        print(norm)
        # 将x重新赋值，赋值为原有的值除以norm，用以归一化
        x = {k: v / norm for k, v in x.items()}
        # Check for convergence (in the L_1 norm).
        # 用于检查收敛
        print('condition ')
        print(sum(abs(x[n] - xlast[n]) for n in x))
        if sum(abs(x[n] - xlast[n]) for n in x) < nnodes * tol:
            return x
    return x
    #raise nx.PowerIterationFailedConvergence(max_iter)

input = open('soc-Slashdot0811.txt', 'r')
graph = nx.DiGraph()
for line in input:
    arr = line.split('\t')
    graph.add_weighted_edges_from([(arr[0], arr[1], 1)])


tmp = eigenvector_centrality(g)


