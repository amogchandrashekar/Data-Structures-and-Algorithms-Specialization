#Uses python3

"""
Task.
    Given an undirected graph with n vertices and m edges and two vertices u and v, compute the length
    of a shortest path between u and v (that is, the minimum number of edges in a path from u to v).
Input Format.
    A graph is given in the standard format. The next line contains two vertices u and v.
Constraints.
    2 ≤ n ≤ 10 5 , 0 ≤ m ≤ 10 5 , u ̸ = v, 1 ≤ u, v ≤ n.
Output Format.
    Output the minimum number of edges in a path from u to v, or −1 if there is no path.

example:
input:
>>> 4 4 1 2 4 1 2 3 3 1 2 4
output:
>>> 2
"""

import sys


def distance(adj, s, t):
    """
    Function to find shortest distance between root and end node
    :param adj: adjacency list
    :param s: root node
    :param t: end node
    :return: distance between s and t -1, if they are not connected
    """
    dist = {vertex: -1 for vertex in range(len(adj))}
    dist[s] = 0
    vertex_queue = list()
    vertex_queue.append(s)

    while vertex_queue:
        vertex = vertex_queue.pop(0)
        for adj_vertex in adj[vertex]:
            if dist[adj_vertex] == -1:
                vertex_queue.append(adj_vertex)
                dist[adj_vertex] = dist[vertex] + 1
    return dist[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
