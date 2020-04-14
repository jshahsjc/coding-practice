"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""

def lengthOfLastWord(s):
   if s[-1] is not ' ':
      l = s.split()
      return len(l[-1])
   else:
      return 0

def lengthOfLastWordAlt(s):
   p = len(s) - 1
   if s[p] == ' ':
      return 0

   while p >= 0 and s[p] == ' ':
      p -= 1

   res = 0
   while p >= 0 and s[p] != ' ':
      p -= 1
      res += 1

   return res

print lengthOfLastWordAlt("Hello World")
