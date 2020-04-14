"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
"""

def reverseStr(s, k):
      """
      :type s: str
      :type k: int
      :rtype: str
      """
      l = list(s)
      for i in range(0, len(l), 2*k):
         l[i: i + k] = l[i:i+k][::-1]

      return ''.join(l)

print reverseStr('abcdefg', 2)
