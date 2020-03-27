#Uses python3

"""
Task.
    Given an undirected graph with n vertices and m edges, check whether it is bipartite.
Input Format.
    A graph is given in the standard format.
Constraints.
    1 ≤ n ≤ 10 5 , 0 ≤ m ≤ 10 5 .
Output Format.
    Output 1 if the graph is bipartite and 0 otherwise.

Example:
Input:
>>> 4 4 1 2 4 1 2 3 3 1
Output:
>>> 0
"""
import sys


def bipartite(adj):
    """
    Function to find if the graph is bipartite or not
    :param adj: adjacency list
    :return:
    1 if the graph is bipartite, else return 0
    Idea : While calculating distance from source vertex, (considered 0 as the source), assign colors to each node
    either 1 or 0, depending on the color of the source vertex. If we find disparity in this while assigning color
    to any node of graph (if color doesnt match to already given color) return 0 else return 1
    """
    source_vertex = 0
    dist = {vertex: -1 for vertex in range(len(adj))}
    color = {vertex: -1 for vertex in range(len(adj))}
    dist[source_vertex] = 0
    color[source_vertex] = 0
    vertex_queue = list()
    vertex_queue.append(source_vertex)

    while vertex_queue:
        vertex = vertex_queue.pop(0)
        for adj_vertex in adj[vertex]:
            if dist[adj_vertex] == -1 and color[adj_vertex] == -1:
                vertex_queue.append(adj_vertex)
                dist[adj_vertex] = dist[vertex] + 1
                color[adj_vertex] = 1 - color[vertex]
            elif color[adj_vertex] != 1 - color[vertex]:
                return 0
    return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    # input= "11 12 1 3 1 2 2 4 3 4 4 8 8 11 4 5 5 6 6 7 7 10 4 9 9 10"
    # input = "5 5 1 2 2 4 4 5 5 3 3 1"
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))