class TreeNode:
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

    def is_leaf(self):
        return not (self.left or self.right)

    def has_left_child(self):
        return self.left

    def has_right_child(self):
        return self.right

    def is_left_child(self):
        return self.parent and self.parent.left == self

    def is_right_child(self):
        return self.parent and self.parent.right == self


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def put(self, key):
        if self.root:
            self._put(key, self.root)
        else:
            self.root = TreeNode(key)
        self.size += 1

    def _put(self, key, c_node):
        if key < c_node.key:
            if c_node.has_left_child():
                self._put(key, c_node.left)
            else:
                c_node.left = TreeNode(key, parent=c_node)
        else:
            if c_node.has_right_child():
                self._put(key, c_node.right)
            else:
                c_node.right = TreeNode(key, parent=c_node)

    def get(self, key):
        if key == self.root.key:
            return key
        else:
            res = self._get(key, self.root)
            if res:
                return res.key
            else:
                None

    def _get(self, key, c_node):
        if c_node is None:
            return None
        elif key == c_node.key:
            return c_node
        elif key < c_node.key:
            return self._get(key, c_node.left)
        else:
            return self._get(key, c_node.right)

    def find_max(self, c_node):
        if c_node is None:
            return None
        elif c_node.has_right_child():
            return self.find_max(c_node.right)
        else:
            return c_node.key

    def find_min(self, c_node):
        if c_node is None:
            return None
        elif c_node.has_left_child():
            return self.find_min(c_node.left)
        else:
            return c_node.key

    def find_height(self, c_node):
        l_height = r_height = 0
        if c_node.is_leaf():
            return 0
        if c_node.has_left_child():
            l_height = self.find_height(c_node.left)
        if c_node.has_right_child():
            r_height = self.find_height(c_node.right)
        return max(l_height, r_height) + 1


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.put(15)
    bst.put(20)
    bst.put(1)
    bst.put(2)
    bst.put(3)
    bst.put(4)
    bst.put(5)
    bst.put(6)
    bst.put(7)
    bst.put(9)
    bst.put(8)
    l_max = bst.find_max(bst.root)
    print(l_max)
    l_min = bst.find_min(bst.root)
    print(l_min)
    h = bst.find_height(bst.root)
    print(h)
