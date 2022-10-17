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
        return (self.left or self.right)

    def has_both_children(self):
        return (self.left and self.right)

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

    def _put(self, key, val, current_node):
        if key < current_node.key: 
            if current_node.has_left_child():
                self._put(key, val, current_node.left)
            else:
                current_node.left = TreeNode(key, val, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.right)
            else:
                current_node.right = TreeNode(key, val, parent=current_node)
    
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
    
    def _get(self, key, current_node):
        if current_node is None:
            return None
        elif key == current_node.key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left)
        else:
            return self._get(key, current_node.right)
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False
    
    def delete(self, key):
        if self.key > 1:
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

    def remove(self, current_node):
        if current_node.is_leaf():
            if current_node == current_node.parent.left:
                current_node.parent.left = None
            else:
                current_node.parent.right = None
        elif current_node.has_both_children():
            pass
        else: # only one chlid
            if current_node.has_left_child():
                if current_node.is_left_child():
                    current_node.left.parent = current_node.parent
                    current_node.parent.left = current_node.left
                elif current_node.is_right_child():
                    current_node.left.parent = current_node.parent
                    current_node.parent.right = current_node.left
            else: # right child
                if current_node.is_left_child():
                    current_node.right.parent = current_node.parent
                    current_node.parent.left = current_node.right
                elif current_node.is_right_child():
                    current_node.right.parent = current_node.parent
                    current_node.parent.right = current_node.right
        

    def __delitem__(self, key):
        self.delete(key)

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.put(15, 1)
    bst.put(20, 2)
    bst.put(7, 0)

    print(bst.get(15))
    # print(bst.get(15))
    # print(bst.get(220))