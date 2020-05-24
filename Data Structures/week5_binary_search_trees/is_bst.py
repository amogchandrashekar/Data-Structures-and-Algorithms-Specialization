#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def IsBinarySearchTree(tree):
    if not tree:
        return True
    queue = list()
    lower_limit, upper_limit = float("-inf"), float("inf")
    node_val, left_index, right_index = tree[0]
    queue.append([node_val, left_index, right_index, lower_limit, upper_limit])
    while queue:
        node_val, left_index, right_index, lower_limit, upper_limit = queue.pop(0)
        if lower_limit <= node_val <= upper_limit:
            if 0 <= left_index < len(tree):
                val, l, r = tree[left_index]
                queue.append([val, l, r, lower_limit, node_val])
            if 0 <= right_index < len(tree):
                val, l, r = tree[right_index]
                queue.append([val, l, r, node_val, upper_limit])
        else:
            return False
    return True


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
