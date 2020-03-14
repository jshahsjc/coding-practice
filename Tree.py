class Tree:
   def __init__(self, data, left=None, right=None):
      self.data = data
      self.left = left
      self.right = right

   def insert(self,data):
      if self.data == data:
         return False  # duplicate value
      elif self.data > data:
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
      if self.data == data:
         return data
      elif self.data > data:
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
      if self.left is not None and self.right is not None:
         return 1 + self.left.getsize() + self.right.getsize()
      elif self.left:
         return 1 + self.left.getsize()
      elif self.right:
         return 1 + self.right.getsize()
      else:
         return 1

   def preorder(self):
      if self is not None:
         print self.data
         if self.left:
            self.left.preorder()
         if self.right:
            self.right.preorder()

   def inorder(self):
      if self is not None:
         if self.left:
            self.left.inorder()
         print self.data
         if self.right:
            self.right.inorder()

t = Tree(100)
L = [20, 1, 5, 144, 566, 1, 35, 50, 1004, 2402, 596]
for k in L:
   t.insert(k)

res = []
for j in range(50, 1000):
   if t.find(j) is not False:
      res.append(t.find(j))
print "From 50 to 1000, these data found in the tree" + str(res)

print "size of the tree is: " +str(t.getsize())

print "Preorder Tree:"
t.preorder()
print "Inorder Tree:"
t.inorder()
