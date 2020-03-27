class Tree:
   def __init__(self, node, left=None, right=None):
      self.val = node
      self.left = left
      self.right = right

   def insert(self,data):
      if self.val == data:
         return False  # duplicate value
      elif self.val > data:
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

   def find(self,data):
      if self.val == data:
         return data
      elif self.val > data:
         if self.left is None:
            return False
         else:
            return self.left.find(data)
      else:
         if self.right is None:
            return False
         else:
            return self.right.find(data)

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
            return  1 + self.left.getheight()
         elif self.right:
            return 1 + self.right.getheight()
         else:
            return 1
      else:
         return 0

   def preorder(self):
      if self is not None:
         print self.val
         if self.left:
            self.left.preorder()
         if self.right:
            self.right.preorder()

   def inorder(self):
      if self is not None:
         if self.left:
            self.left.inorder()
         print self.val
         if self.right:
            self.right.inorder()

class Solution(Tree):
   def getdiameter(self, root):
      """
      root: Tree node
      rtype: integer - longer of root path or suboptimal path
      """
      left_height = 0
      right_height = 0
      if root is not None:
         if root.left:
            left_height = root.left.getheight()
         if root.right:
            right_height = root.right.getheight()
         root_path = 1 + left_height + right_height
         sub_path =                                               max(self.getdiameter(root.left),                                        self.getdiameter(root.right))
         return max(root_path, sub_path)
      else:
         return 0

   def binaryTreePaths(self, root):
      """
      root: Tree Node
      rtype: List[str]
      """
      self.paths = []   # we'll return this

      def constructPaths(root, path = ''):
         if root is not None:
            path += str(root.val) #start with root
            if root.left is None and root.right is None:
               self.paths.append(path)  #leaf node found, add path to puths
            else:
               path += '-->'  # extend current path to left and right
               constructPaths(root.left, path)
               constructPaths(root.right, path)

      constructPaths(root)
      return self.paths

   def rangeSumBST(self, root, L, R):
      """
      :type root: TreeNode
      :type L: int
      :type R: int
      :rtype: int
      """
      self.ans = 0
      def dfs(root):
         if root is not None:
            if L <= root.val <= R:
               self.ans += root.val
            if L < root.val:
               dfs(root.left)
            if root.val < R:
               dfs(root.right)
      dfs(root)
      return self.ans

t = Tree(100)
L = [20, 1, 5, 144, 566, 1, 35, 50, 1004, 2402, 596]
for k in L:
   t.insert(k)

res = []
for j in range(50, 1000):
   if t.find(j):
      res.append(t.find(j))

print "From 50 to 1000, these data found in the tree" + str(res)
print "size of the tree is: " +str(t.getsize())
print "Height of the tree is: " + str(t.getheight())
print "Preorder Tree:"
t.preorder()
print "Inorder Tree:"
t.inorder()

s = Solution(object)
print "Diameter of the tree is: " + str(s.getdiameter(t))
print "Paths of this tree are: " + str(s.binaryTreePaths(t))
print "Sum between 20 and 50 is: " + str(s.rangeSumBST(t, 20, 50))
