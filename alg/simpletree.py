class Tree:
    """
    simple tree implemented as an array
    cond 1.1 non-overlapping: no two nodes share the same cell in the array
        left child = 2n+1, right child = 2n+2
        for n in C, no n exists such that 2n+1=2n+2
    cond 1.2 no holes: there are no wasted cells
        at depth d, there are 2**d nodes
        a full tree at this depth has 2**d + 2**(d-1) + ... + 2**0 nodes
         = 2**(d+1) - 1 and the last element is at 2**(d+1) - 2
        this is also given by the recursive formula n'=2n+2. expanded d times,
        this also equals 2**(d+1) - 2
        As there are no overlaps, there is exactly 1 cell for every node
    """
    def __init__(self, arr=None):
        if arr is not None:
            self.arr = arr
        else:
            self.arr = [None] * 10

    def root(self):
        return self.arr[0]

    def find(self, value):
        i = 0
        for x in self.arr:
            if x == value:
                return i
            i += 1
        return 0

    def left_of_index(self, index):
        return 2*index + 1

    def right_of_index(self, index):
        return 2*index + 2

    def insert(self, value, root=None):
        'insert value into tree, reorganising if required'
        if root is None:
            self.arr[0] = value
            return
        root_index = self.find(root)
        root_value = self.arr[root_index]
        dest = 0
        if root_value >= value:
            dest = 2*root_index + 2
            if self.arr[dest] is None:
                self.arr[dest] = value
        else:
            dest = 2*root_index + 1
            if self.arr[dest] is None:
                self.arr[dest] = value
        return dest

    def __repr__(self):
        return str(self.arr)


if __name__ == '__main__':
    t = Tree()
    t.insert(5)
    t.insert(7, 5)
    t.insert(1, 5)
    print(t)
