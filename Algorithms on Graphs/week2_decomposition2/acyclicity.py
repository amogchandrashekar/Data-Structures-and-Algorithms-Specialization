#Uses python3

"""
Task. Check whether a given directed graph with n vertices and m edges contains a cycle.
Input Format. A graph is given in the standard format.
Constraints. 1 ≤ n ≤ 10 3 , 0 ≤ m ≤ 10 3 .
Output Format. Output 1 if the graph contains a cycle and 0 otherwise.

Input:
>>> 4 4 1 2 4 1 2 3 3 1
Output:
>>> 1
as 1 --> 2 --> 3 --> 1
"""

import sys


def acyclic(adj):
    """
    Main function to find if a graph contains cycle or not
    :param adj: adjacency list
    :return:
    1 : if a cycle is present in the graph
    0 : if no cycle is present in the graph
    """
    visited_adj = [False] * len(adj)

    def dfs(vertex, cyclic=False):
        visited_adj[vertex], rec_visited[vertex] = True, True
        for adj_node in adj[vertex]:
            if not visited_adj[adj_node]:
                cyclic = dfs(adj_node, cyclic)
            elif rec_visited[adj_node]: # condition to find the cycle
                cyclic = True
        rec_visited[vertex] = False # remove recursively set vertex to false
        return cyclic

    for index in range(len(visited_adj)):
        if not visited_adj[index]:
            rec_visited = [False] * len(visited_adj) # change visited recursively to find the cycle in graph
            if dfs(index): # If any cycle is found, return 1
                return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
