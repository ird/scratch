class Tree:
    """
    simple tree implemented as an array
    """
    def __init__(self, arr=None):
        if arr is not None:
            self.arr = arr
        else:
            self.arr = [None] * 10

    def get(self, index):
        return self.arr[index]

    def find(self, value):
        i = 0
        for x in self.arr:
            if x == value:
                return i
            i += 1
        return 0

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

    def prnt(self):
        print(self.arr)


if __name__ == '__main__':
    t = Tree()
    t.insert(5)
    t.insert(7, 5)
    t.insert(1, 5)
    t.prnt()
