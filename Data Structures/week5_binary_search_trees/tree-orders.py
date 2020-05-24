# python3

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c
        self.postorder = list()
        self.inorder = list()
        self.preorder = list()

    def in_order(self, index=0):
        if self.left[index] != -1:
            self.in_order(self.left[index])
        self.inorder.append(self.key[index])
        if self.right[index] != -1:
            self.in_order(self.right[index])
        return

        # Finish the implementation
        # You may need to add a new recursive method to do that

    def pre_order(self, index=0):
        self.preorder.append(self.key[index])
        if self.left[index] != -1:
            self.pre_order(self.left[index])
        if self.right[index] != -1:
            self.pre_order(self.right[index])
        return

    def post_order(self, index=0):
        if self.left[index] != -1:
            self.post_order(self.left[index])
        if self.right[index] != -1:
            self.post_order(self.right[index])
        self.postorder.append(self.key[index])
        return


def main():
    tree = TreeOrders()
    tree.read()
    tree.in_order()
    tree.pre_order()
    tree.post_order()
    print(" ".join(str(x) for x in tree.inorder))
    print(" ".join(str(x) for x in tree.preorder))
    print(" ".join(str(x) for x in tree.postorder))


threading.Thread(target=main).start()
