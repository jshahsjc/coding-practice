class Tree:
    def __init__(self, node, left = None, right = None):
        self.val = node
        self.left = left
        self.right = right

    def insert(self, data):
        if self.val == data:
            return False
        if self.val > data:
            if self.left is not None:
                return self.left.insert(data)
            else:
                self.left = Tree(data)
                return True
        else:
            if self.right is not None:
                return self.right.insert(data)
            else:
                self.right = Tree(data)
                return True

    def find(self, data):
        if self.val == data:
            return data
        elif self.val > data:
            if self.left is not None:
                return self.left.find(data)
            else:
                return False
        elif self.val < data:
            if self.right is not None:
                return self.right.find(data)
            else:
                return False
        else:
            return False

    def getsize(self):
        if self is not None:
            if self.left is not None and self.right is not None:
                return 1 + self.left.getsize() + self.right.getsize()
            elif self.left:
                return 1 + self.left.getsize()
            elif self.right:
                return 1 + self.right.getsize()
            else:
                return 1
        else:
            return 0

    def getheight(self):
        if self is not None:
            if self.left is not None and self.right is not None:
                return 1 + max(self.left.getheight(), self.right.getheight())
            elif self.left:
                return 1 + self.left.getheight()
            elif self.right:
                return 1 + self.right.getheight()
            else:
                return 1
        else:
            return 0

    def preorder(self):
        res = []
        if self is not None:
            res.append(self.val)
            if self.left:
                res.append(self.left.preorder())
            if self.right:
                res.append(self.right.preorder())
        return res

    def inorder(self):
        res = []
        if self is  not None:
            if self.left:
                res.append(self.left.inorder())
            res.append(self.val)
            if self.right:
                res.append(self.right.inorder())
        return res
