#Uses python3

import sys


def reach(adj, x, y):
    """
    Main function to find if a node in graph is reachable to another node
    :param adj: adjacency list
    :param x: node in the graph (starting point)
    :param y: node in the graph (ending point)
    :return: 1 if a path exists between nodes, else return 0
    """
    visited = [False] * len(adj)

    def dfs(x):
        visited[x] = True
        for node in adj[x]:
            if not visited[node]:
                dfs(node)
        return 1 if visited[y] is True else 0

    return dfs(x)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
