#Uses python3

"""
Task.
    Given n points on a plane, connect them with segments of minimum total length such that there is a
    path between any two points.
Input Format.
    The first line contains the number n of points. Each of the following n lines defines a point (x i , y i ).
Constraints.
    1 ≤ n ≤ 200; −10 3 ≤ x i , y i ≤ 10 3 are integers. All points are pairwise different, no three points lie on the same line.
Output Format.
    Output the minimum total length of segments. The absolute value of the difference
    between the answer of your program and the optimal value should be at most 10 −6 . To ensure this,
    output your answer with at least seven digits after the decimal point (otherwise your answer, while
    being computed correctly, can turn out to be wrong because of rounding issues).

Example:
Input:
>>> 4 0 0 0 1 1 0 1 1
Output:
>>> 3.0000000
"""
import sys
import math
import heapq


def distance(x1, y1, x2, y2):
    """
    Find distance between two co ordinates
    :return: Distance
    """
    return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))


def get_meta(x, y):
    """
    Get adjacency list and cost by taking input as points
    :param x: x co ordinates of points in a list
    :param y: y co ordinates of points in a list
    :return: adjacency list and cost (distances here)
    """
    cost = [[] for _ in range(len(x))]
    adj = [[] for _ in range(len(x))]
    for i, vertex in enumerate(x):
        for j, adj_vertex in enumerate(y):
            if i == j: continue
            dist = distance(x[i], y[i], x[j], y[j])
            adj[i].append(j)
            cost[i].append(dist)
    return adj, cost


def get_queue(adj, weight):
    """
    Create queue with distances and ends of the edge
    :param adj: adjacency list
    :param weight: distances
    :return: minimum priority queue
    """
    min_queue = list()
    for vertex, adj_list in enumerate(adj):
        for adj_vertex in adj_list:
            v_index = adj[vertex].index(adj_vertex)
            heapq.heappush(min_queue, [weight[vertex][v_index], [vertex, adj_vertex]])
    heapq.heappush(min_queue, [0, [0, 0]])
    return min_queue


def make_set(adj):
    """
    Create a set with all points as a independent set
    :param adj: adjacency list
    :return:
    """
    discovered = list()
    for vertex in range(len(adj)):
        new_set = set()
        new_set.add(vertex)
        discovered.append(new_set)
    return discovered


def minimum_distance(x, y):
    """
    Main function.
    idea: Implementation of kruskals algorithm. Create a queue with distances.
    use disjoint sets to find the distance
    :param x: x co ords of points
    :param y: y co ords of points
    :return:
    """
    adj, weight = get_meta(x, y)
    min_queue = get_queue(adj, weight)
    result = 0
    discovered = make_set(adj)

    def union(node_a, node_b):
        """
        Merge two sets
        """
        new_set = set()
        remove_value = list()
        for index, node_set in enumerate(discovered):
            if node_a in node_set or node_b in node_set:
                new_set = new_set | node_set
                if node_set not in remove_value:
                    remove_value.append(node_set)
        for i in remove_value:
            discovered.remove(i)
        discovered.append(new_set)

    def find(node_vertex):
        """
        Find which set the node vertex belongs to
        """
        for index, node_set in enumerate(discovered):
            if node_vertex in node_set:
                return index

    while min_queue:
        dis, nodes = heapq.heappop(min_queue)
        node_a, node_b = nodes
        if find(node_a) != find(node_b):
            union(node_a, node_b)
            result += dis

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
