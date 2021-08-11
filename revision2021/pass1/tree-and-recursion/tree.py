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


class Solution:
    def getHeight(self, root):
        """
        Suppose getheight method is not included in the Tree class
        Use this function to achieve desired outcome
        """
        if root is not None:
            if root.left is not None and root.right is not None:
                return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
            elif root.left:
                return 1 + self.getHeight(root.left)
            elif root.right:
                return 1 + self.getHeight(root.right)
            else:
                return 1
        else:
            return 0

    def getDiameter(self, root):
        """
        root: Tree Node
        return: int
        """
        if root is not None:
            left_height = self.getHeight(root.left)
            right_height = self.getHeight(root.right)
            root_path_dia = 1 + left_height + right_height
            max_sub_path_dia = max(self.getDiameter(root.left), self.getDiameter(root.right))
            return max(root_path, max_sub_path)
        else:
            return 0

    def iterativePreorder(self, root):
        """
        use stack
        1. push root
        while stack is not empty:
        2. pop from stack and print element
        3. push children of popped element

        """
        if root is None:
            return

        mystack = []
        mystack.append(root)

        while len(mystack) > 0:
            current = mystack.pop()
            print(current.val, end = ' ')

            if current.right is not None:
                mystack.append(current.right)

            if current.left is not None:
                mystack.append(current.left)

    def iterativeInorder(self, root):
        mystack = []
        current = root
        while True:
            if current is not None:
                mystack.append(current)
                current = current.left

            elif len(mystack) > 0:
                current = mystack.pop()
                print(current.val, end = ' ')
                current = current.right
            else:
                break
