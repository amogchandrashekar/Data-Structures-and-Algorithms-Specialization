# python3

import sys, threading
from collections import defaultdict
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def compute_height(self):
                height, queue, h = defaultdict(list), list(), 0
                for index, value in enumerate(self.parent):
                    height[value].append(index)

                queue += height[-1]
                while(True):
                    nodecount = len(queue)
                    if nodecount == 0:
                        return h
                    h += 1
                    while nodecount > 0:
                        node = queue.pop(0)
                        if node in height:
                            queue += height[node]
                        nodecount -= 1




def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
