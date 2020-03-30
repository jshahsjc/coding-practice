"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

class Solution(object):
   def lengthOfLongestSubstring(self, s):
      """
      :type s: str
      :rtype: int
      """
      start = 0
      max_len = 0
      used = {}

      for i, c in enumerate(s):
         if c in used and start <= used[c]:
            start = used[c] + 1
         else:
            max_len = max(max_len, i - start + 1)
         used[c] = i
      return max_len

s = Solution()
TL = ["bbbbb", "pwwkew", "abcabcbb"]
for t in TL:
   print "Length of longest substring in " + t + ": " + str(s.lengthOfLongestSubstring(t))
