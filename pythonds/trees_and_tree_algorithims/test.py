class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def has_left_child(self):
        return self.left

    def has_right_child(self):
        return self.right

    def is_left_child(self):
        return self.parent and self.parent.left == self

    def is_right_child(self):
        return self.parent and self.parent.right == self

    def has_left_child(self):
        return self.left

    def has_right_child(self):
        return self.right

    def has_both_children(self):
        return self.left and self.right

    def has_any_children(self):
        return self.left or self.right

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.left or self.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, c_node):
        if key < c_node.key:
            if c_node.has_left_child():
                self._put(key, val, c_node.left)
            else:
                c_node.left = TreeNode(key, val)
        else:
            if c_node.has_right_child():
                self._put(key, val, c_node.right)
            else:
                c_node.right = TreeNode(key, val)

    def __setitem__(self, key, val):
        self.put(key, val)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.val
            else:
                return None
        else:
            return None

    def _get(self, key, c_node):
        if not c_node:
            return None
        elif key == c_node.key:
            return c_node
        elif key < c_node.key:
            return self._get(key, c_node.left)
        else:
            return self._get(key, c_node.right)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.put(10, 8)
    bst.put(5, 6)
    bst.put(15, 11)
    print(bst.get(15))
    print(bst.get(5))
