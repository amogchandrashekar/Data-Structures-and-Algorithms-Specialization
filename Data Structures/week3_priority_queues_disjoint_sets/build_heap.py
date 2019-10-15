# python3

class Heap:

    def __init__(self):
        self.data = list()
        self.swaps = list()

    def write_swaps(self):
        """
        Write indices that are swapped on console
        """
        print(len(self.swaps))
        for i, j in self.swaps:
            print(i, j)

    @property
    def size(self):
        """
        Return length of data
        """
        return len(self.data)

    def read_data(self):
        """
        Take input from the user
        """
        n = int(input())
        self.data = [int(s) for s in input().split()]
        assert n == self.size

    def l_child_index(self, parent_index):
        """
        Return the left child's index taking parents index
        return -1 if left child does not exist
        """
        l_index = (2 * parent_index) + 1
        if l_index >= self.size:
            return -1
        return l_index

    def r_child_index(self, parent_index):
        """
        Return the right child's index taking parents index
        return -1 if right child does not exist
        """
        r_index = (2 * parent_index) + 2
        if r_index >= self.size:
            return -1
        return r_index

    def swap_index_values(self, index_1, index_2):
        """
        Swap values in two indices
        """
        self.data[index_1], self.data[index_2] = self.data[index_2], self.data[index_1]

    def sift_down(self, index):
        """
        Sift down procedure to build binary min heap
        """
        min_index = index
        l_index = self.l_child_index(index)
        r_index = self.r_child_index(index)

        if (l_index != -1) and self.data[l_index] < self.data[min_index]:
            min_index = l_index
        if (r_index != -1) and self.data[r_index] < self.data[min_index]:
            min_index = r_index

        if index != min_index:
            self.swaps.append((index, min_index))
            self.swap_index_values(index, min_index)
            self.sift_down(min_index)

    def build_heap(self):
        """
        Iterate from half of size of data and store swap indices
        """
        for i in range(self.size // 2, -1, -1):
            self.sift_down(i)
        return self.write_swaps()


def main():
    heap = Heap()
    heap.read_data()
    heap.build_heap()


if __name__ == "__main__":
    main()
