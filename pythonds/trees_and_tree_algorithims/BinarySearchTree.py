class TreeNode:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None
    

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def _insert(self, key, c_node):
        if key < c_node.key:
            if c_node.left:
                self._insert(key, c_node.left)
            else:
                c_node.left = TreeNode(key)
        else:
            if c_node.right:
                self._insert(key, c_node.right)
            else:
                c_node.right = TreeNode(key)

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(key, self.root)

    def _get(self, key, c_node):
        if c_node is None:
            return None
        elif key == c_node.key:
            return c_node
        elif key < c_node.key:
            return self._get(key, c_node.left)
        else:
            return self._get(key, c_node.right)

    def get(self, key):
        if key == self.root.key:
            return key
        else:
            res = self._get(key, self.root)
            if res:
                return res.key
            else:
                return None

    def height(self, c_node):
        if c_node is None:
            return -1

        left_subtree = self.height(c_node.left)
        right_subtree = self.height(c_node.right)
        return max(left_subtree, right_subtree) + 1
    
    

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(15)
    bst.insert(10)
    bst.insert(20)
    bst.insert(3)
    bst.insert(16)
    bst.insert(1)
    print(bst.get(0))
    print(bst.height(bst.root))
