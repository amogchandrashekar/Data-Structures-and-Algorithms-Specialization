#Uses python3

"""
Task.
    Construct a trie from a collection of patterns.
Input Format.
    An integer n and a collection of strings Patterns = {p 1 , . . . , p n } (each string is given on a
    separate line).
Constraints.
    1 ≤ n ≤ 100; 1 ≤ |p i | ≤ 100 for all 1 ≤ i ≤ n; p i ’s contain only symbols A, C, G, T; no p i is
    a prefix of p j for all 1 ≤ i ̸ = j ≤ n.
Output Format.
    The adjacency list corresponding to Trie(Patterns), in the following format. If
    Trie(Patterns) has n nodes, first label the root with 0 and then label the remaining nodes with the
    integers 1 through n − 1 in any order you like. Each edge of the adjacency list of Trie(Patterns) will be
    encoded by a triple: the first two members of the triple must be the integers i, j labeling the initial and
    terminal nodes of the edge, respectively; the third member of the triple must be the symbol c labeling
    the edge; output each such triple in the format u->v:c (with no spaces) on a separate line.

Sample 1.

Input:
1
ATA

Output:
0->1:A
2->3:A
1->2:T

Explanation:
0
| A
1
| T
2
| A
3
"""
import sys
from collections import defaultdict

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.


def build_trie(patterns):
    tree = defaultdict(dict)
    counter = 0
    for pattern in patterns:
        current_node = 0
        for letter in pattern:
            if letter in tree[current_node]:
                current_node = tree[current_node][letter]
            else:
                counter += 1
                tree[current_node][letter] = counter
                current_node = counter
    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    # patterns = ["ATAGA", "ATC", "GAT"]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
