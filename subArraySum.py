"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""
from collections import defaultdict

class Solution(object):
   def subarraySum(self, nums, k):
      """
      :type nums: List[int]
      :type k: int
      :rtype: int
      """
      res = 0
      curr_sum = 0
      prev_sums = defaultdict(lambda : 0)

      for i in range(len(nums)):
         curr_sum += nums[i]
         if curr_sum == k:
            res += 1

         if curr_sum - k in prev_sums:
            res += prev_sums[curr_sum - k]

         else:
            prev_sums[curr_sum] += 1
         print prev_sums

      return res


nums = [1,1,1,-4,6,8,-6]; k = 2
s = Solution()
print s.subarraySum(nums, k)
