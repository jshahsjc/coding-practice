"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""

class Solution(object):
   def rob(self, nums):
      """
      :type nums: List[int]
      :rtype: int
      """
      odd_houses = 0
      odd_path = []
      even_houses = 0
      even_path = []
      for number, house in enumerate(nums):
         if number % 2 == 0:
            even_houses += house
            even_path.append(number)
         else:
            odd_houses += house
            odd_path.append(number)

      if odd_houses >= even_houses:
         return odd_houses, odd_path
      else:
         return even_houses, even_path

nums1 = [1,2,3,1,10,20]
nums2 = [2,7,9,3,1]

s = Solution()
print s.rob(nums1)
print s.rob(nums2)
