#Uses python3

"""
Task.
    Compute the number of strongly connected components of a given directed graph with n vertices and m edges.
Input Format.
    A graph is given in the standard format.
Constraints.
    1 ≤ n ≤ 10 4 , 0 ≤ m ≤ 10 4 .
Output Format.
    Output the number of strongly connected components.

Example:
Input:
>>> 4 4 1 2 4 1 2 3 3 1
Output:
>>> 2
"""

import sys

sys.setrecursionlimit(200000)


def reverse_graph(adj_list):
    """
    Find reverse adjacency list
    :param adj_list: adjacency list
    :return: reverse adjacency list
    """
    rev_adj_list = [[] for _ in range(len(adj_list))]
    for index in range(len(adj_list)):
        for vertex in adj_list[index]:
            rev_adj_list[vertex].append(index)
    return rev_adj_list


def number_of_strongly_connected_components(adj):
    """
    Find number of connected components in a graph
    :param adj: adjacency list
    :return: number of connected components in a graph
    """
    rev_adj = reverse_graph(adj)
    visited = [False] * len(adj)
    order = list()

    def dfs(vertex):
        visited[vertex] = True
        for adj_vertex in adj[vertex]:
            if not visited[adj_vertex]:
                dfs(adj_vertex)
        order.append(vertex)

    def reverse_dfs(vertex):
        visited[vertex] = True
        for adj_vertex in rev_adj[vertex]:
            if not visited[adj_vertex]:
                reverse_dfs(adj_vertex)

    for node in range(len(visited)):
        if not visited[node]:
            dfs(node)

    # make visited to false again
    visited = [False] * len(adj)
    counter = 0
    for vertex in order:
        if not visited[vertex]:
            reverse_dfs(vertex)
            # increment counter for every found connected component
            counter += 1

    return counter

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
