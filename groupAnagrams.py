"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

"""
func. to check if 2 words are anagrams
res list  = []
iterate through input list:
   temp = []
   for current value, find anagrams and append to a temp list
   append temp to res list
"""

class Solution(object):
   def groupAnagrams(self, strs):
      """
      :type strs: List[str]
      :rtype: List[List[str]]
      """

      def isAnagrams(str1, str2):
         if len(str1) != len(str2):
            return False
         count = 0
         for c in str1:
            if c in str2:
               count += 1
         if count == len(str1) and count == len(str2):
            return True

      def isAnagramsAlt(str1, str2):
         return sorted(str1) == sorted(str2)

      print 'input' + str(strs)
      group_anagrams = []
      for i in range(len(strs)):
         anagrams = []
         anagrams.append(strs[i])

         temp = strs[:i] + strs[i + 1:]
         print 'temp' + str(temp)
         for j in range(len(temp)):
            print strs[i], temp[j]
            if isAnagramsAlt(strs[i], temp[j]):
               anagrams.append(temp[j])
         anagrams.sort()
         print 'sorted' + str(anagrams)
         if anagrams not in group_anagrams:
            group_anagrams.append(anagrams)

      return group_anagrams

s = Solution()
input = ["eat", "tea", "tan", "ate", "nat", "bat"]

print s.groupAnagrams(input)
