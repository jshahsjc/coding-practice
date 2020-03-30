"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution(object):
   def threeSum(self, nums):
      """
      :type nums: List[int]
      :rtype: List[List[int]]
      """
      def twoSum(arr, target):
         vault = {}
         for i, num in enumerate(arr):
            comp = target - num
            if comp not in vault:
               vault[num] = i
            else:
               s1, s2 = vault[comp], i
               return arr[s1], arr[s2]
         return None

      res = []
      for j, num in enumerate(nums):
         target = 0 - num
         temp = nums[:j] + nums[j + 1:]
         triplet = []
         two_sum = twoSum(temp, target)
         print two_sum

         if two_sum:
            triplet.append(num)
            triplet += list(two_sum)
            triplet.sort()

         if triplet not in res and triplet:
            res.append(triplet)

      return res

s = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print s.threeSum(nums)
