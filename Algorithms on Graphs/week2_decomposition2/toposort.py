#Uses python3

"""
Task.
    Compute a topological ordering of a given directed acyclic graph (DAG) with n vertices and m edges.
Input Format.
    A graph is given in the standard format.
Constraints.
    1 ≤ n ≤ 10 5 , 0 ≤ m ≤ 10 5 . The given graph is guaranteed to be acyclic.
Output Format.
    Output any topological ordering of its vertices. (Many DAGs have more than just one
    topological ordering. You may output any of them.)

Example:
Input:
>>> 4 3 1 2 4 1 3 1
Output:
>>> 4 3 1 2
"""

import sys


def toposort(adj):
    """
    Main function to find order for linear ordering.
    Idea: Do dfs and while returning from recursion stack store the order and reverse it.
    This would basically be ordering in reverse post order
    :param adj: adjacency list
    :return: linear order
    """
    visited = [False] * len(adj)
    order = list()

    def dfs(vertex):
        visited[vertex] = True
        for adj_vertex in adj[vertex]:
            if not visited[adj_vertex]:
                dfs(adj_vertex)
        order.append(vertex)

    for node in range(len(visited)):
        if not visited[node]:
            dfs(node)

    order.reverse()
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')