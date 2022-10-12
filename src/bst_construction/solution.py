# Time complexity - average O(logN), worst O(N)
# Space complexity - average O(logN), worst O(N)
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        def _insert_helper(node):
            if value < node.value:
                if node.left is None:
                    node.left = BST(value)
                else:
                    _insert_helper(node.left)
            else:
                if node.right is None:
                    node.right = BST(value)
                else:
                    _insert_helper(node.right)
                
        
        _insert_helper(self)
        return self

    def contains(self, value):
        def _contains(node):
            if node is None:
                return False
            if node.value == value:
                return True
            elif node.value > value:
                return _contains(node.left)
            else:
                return _contains(node.right)
        return _contains(self)

    def remove(self, value, parent=None):
        if value < self.value and self.left is not None:
            self.left.remove(value, self)
        elif value > self.value and self.right is not None:
            self.right.remove(value, self)
        else:
            if self.left is not None and self.right is not None:
                self.value = self.right.minValue()
                self.right.remove(self.value, self)
            elif parent is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
            elif parent.left is self:
                parent.left = self.left if self.left is not None else self.right
            elif parent.right is self:
                parent.right = self.left if self.left is not None else self.right
        return self
        
    def minValue(self):
        if self.left is None:
            return self.value
        return self.left.minValue()
