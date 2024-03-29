"""
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1.
Example 2:

Input: [1,[4,[6]]]
Output: 27
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.
"""
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """




class Solution(object):
   def depthSum(self, nestedList):
      """
      :type nestedList: List[NestedInteger]
      :rtype: int
      """
      def getDepthSum(nested_list, depth):
         if nested_list is None:
            return 0
         else:
            for nested_int in nested_list:
               if nested_int.isInteger():
                  self.ans += depth * nested_int.getInteger()
               else:
                  getDepthSum(nested_int.getList(), (depth + 1))
            return self.ans

      self.ans = 0
      return getDepthSum(nestedList, 1)

nList = [[1,1],2,[1,1]]

"""
Alternate solution with simple native python constructs.
"""

def nestedListDepthSum(n_list):
    if not n_list:
        return -1
    def dfs(n_list, d):
        res = 0
        for n in n_list:
            if isinstance(n, list):
                res += dfs(n, d + 1)
            if isinstance(n, int):
                res += (n * d)
        return res
    return dfs(n_list, 1)
