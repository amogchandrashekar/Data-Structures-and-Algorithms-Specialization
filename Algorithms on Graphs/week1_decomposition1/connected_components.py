#Uses python3

import sys


def dfs(x, visited):
    """
    Helper function, sets all connected components in a run to True
    :param x: node index
    :param visited: true if already path has been seen, else false
    :return: updates visited on each call
    """
    visited[x] = True
    for node in adj[x]:
        if not visited[node]:
            dfs(node, visited)
    return visited


def number_of_components(adj):
    """
    Main function to count number of connected components in a graph
    :param adj: adjacency list
    :return: number of connected components
    """
    counter = 0
    visited = [False] * len(adj)
    for index in range(len(adj)):
        if not visited[index]:
            visited = dfs(index, visited)
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
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
