"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""
# from collections import defaultdict

class Solution(object):
   def subarraySum(self, nums, k):
      """
      :type nums: List[int]
      :type k: int
      :rtype: int
      """
      count = 0 # we'll return this
      curr_sum = 0
      prev_sum = {}

      for i in range(len(nums)):
         curr_sum += nums[i]
         print curr_sum

         if curr_sum == k:
            count += 1

         if (curr_sum - k) in prev_sum:
            count += prev_sum[curr_sum - k]
         else:
            if curr_sum in prev_sum:
               prev_sum[curr_sum] += 1
            else:
               prev_sum[curr_sum] = 1

      return count

nums = [1,1,1,-4,6,8,-6,1,1]; k = -1

s = Solution()
print s.subarraySum(nums, k)
