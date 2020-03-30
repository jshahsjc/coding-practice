"""
Given two strings s and t, determine if they are both one edit distance apart.

Note:

There are 3 possiblities to satisify one edit distance apart:

Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t
Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:

Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace '0' with '1' to get t.
"""

class Solution(object):
   def isOneEditDistance(self, s, t):
      """
      :type s: str
      :type t: str
      :rtype: bool
      """
      len_s = len(s)
      len_t = len(t)
      if len_s > len_t:
         self.isOneEditDistance(t, s)

      if len_t - len_s > 1:
         return False

      if len_t > len_s:
         if s == t[:len_s]:
            return True

         for i in range(len_s):
            if s[i] != t[i]:
               return s[i:] == t[(i+1):]

      if len_t == len_s:
         for i in range(len_s):
            if s[i] != t[i]:
               return s[(i+1):] == t[(i+1):]

      return False

s = Solution()
print "one edit distant ?: " + str(s.isOneEditDistance("ab", "abc"))
