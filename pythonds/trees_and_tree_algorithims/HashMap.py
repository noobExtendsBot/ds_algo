from calendar import c


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

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.left or self.right)

    def has_any_children(self):
        return self.left or self.right

    def has_both_children(self):
        return self.left and self.right

    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.value = value
        self.left = lc
        self.right = rc
        if self.has_left_child():
            self.left.parent = self
        if self.has_right_child():
            self.right.parent = self


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
                c_node.left = TreeNode(key, val, parent=c_node)
        else:
            if c_node.has_right_child():
                self._put(key, val, c_node.right)
            else:
                c_node.right = TreeNode(key, val, parent=c_node)

    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self, key):
        if self.root.key == key:
            return self.root.val
        else:
            res = self._get(key, self.root)
            if res:
                return res.val
            else:
                return None

    def _get(self, key, c_node):
        if c_node is None:
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

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError("Error, key not in the tree")
        elif self.size == 1 and key == self.root.key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("Error, key not in the tree")

    def find_min(self, c_node):
        if c_node is None:
            return
        elif c_node.left:
            return self.find_min(c_node.left)
        else:
            return c_node

    def remove(self, c_node):
        if c_node.is_leaf():
            if c_node == c_node.parent.left:
                c_node.parent.left = None
            else:
                c_node.parent.right = None
        elif c_node.has_both_children():
            temp_node = self.find_min(c_node.right)
            key, val = temp_node.key, temp_node.val
            self.remove(temp_node)
            c_node.key = key
            c_node.val = val
        else:  # only one chlid
            if c_node.is_left_child():
                if c_node.has_left_child():
                    c_node.left.parent = c_node.parent
                    c_node.parent.left = c_node.left
                elif c_node.has_right_child():
                    c_node.right.parent = c_node.parent
                    c_node.parent.left = c_node.right
            elif c_node.is_right_child():
                if c_node.has_left_child():
                    c_node.left.parent = c_node.parent
                    c_node.parent.right = c_node.left
                elif c_node.has_right_child():
                    c_node.right.parent = c_node.parent
                    c_node.parent.right = c_node.right

    def in_order_traversal(self, c_node):
        if c_node is None:
            return

        self.in_order_traversal(c_node.left)
        print(c_node.key)
        self.in_order_traversal(c_node.right)

    def __delitem__(self, key):
        self.delete(key)


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.put(17, 0)
    bst.put(25, 0)
    bst.put(5, 0)
    bst.put(2, 0)
    bst.put(11, 0)
    bst.put(35, 0)
    bst.put(9, 0)
    bst.put(16, 0)
    bst.put(29, 0)
    bst.put(38, 0)
    bst.put(7, 0)

    bst.delete(25)
    print(bst.get(25))
    print(bst.get(35))
    print(bst.get(29))
    print(bst.get(38))
    bst.in_order_traversal(bst.root)
    print(" ")
    bst.delete(17)
    bst.in_order_traversal(bst.root)
    print(" ")
    bst.delete(29)
    bst.delete(35)
    bst.delete(38)
    bst.in_order_traversal(bst.root)
    print(" ")
    bst.delete(38)
    bst.in_order_traversal(bst.root)
    # bst.in_order_traversal(bst.root)
    # print(bst.find_min(bst.root))
