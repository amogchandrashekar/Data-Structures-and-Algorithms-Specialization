#Uses python3

"""
Task.
    Given an directed graph with possibly negative edge weights and with n vertices and m edges, check
    whether it contains a cycle of negative weight.
Input Format.
    A graph is given in the standard format.
Constraints.
    1 ≤ n ≤ 10 3 , 0 ≤ m ≤ 10 4 , edge weights are integers of absolute value at most 10 3 .
Output Format.
    Output 1 if the graph contains a cycle of negative weight and 0 otherwise.

Example:
Input:
>>> 4 4 1 2 -5 4 1 2 2 3 2 3 1 1
Output:
>>> 1
"""

import sys
import numpy as np

def negative_cycle(adj, cost):
    """
    Find if graph contains negative cycle or not.
    Idea: The distances get updated on nth cycle (length of nodes in graph), if negative cycle is there
    ie, the values stop updating after certain cycles, if the graph has negative cycle, only then the distance values
    tend to infinity.
    :param adj: adjacency list
    :param cost: cost distances
    :return:
    1 if graph contains a cycle with negative weights
    0  otherwise
    """
    dist = {vertex: np.inf for vertex in range(len(adj))}
    neg_cycle = 0

    for index in range(len(adj)):
        for vertex in range(len(adj)):
            for adj_vertex in adj[vertex]:
                v_index = adj[vertex].index(adj_vertex)
                if dist[vertex] == np.inf:
                    dist[vertex] = 0
                updated_distance = dist[vertex] + cost[vertex][v_index]
                if updated_distance < dist[adj_vertex]:
                    dist[adj_vertex] = updated_distance
                    if index == len(adj) - 1:
                        neg_cycle = 1
    return neg_cycle


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
