"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
class Solution(object):
   def moveZeroes(self, nums):
      """
      :type nums: List[int]
      :rtype: None Do not return anything, modify nums in-place instead.
      """
      nzp = 0
      for p in range(len(nums)):
         if nums[p] != 0:
            nums[p], nums[nzp] = nums[nzp], nums[p]
            nzp += 1

      return nums

s = Solution()
I = [0,1,0,3,12]

print "original: " + str(I)
print "zero moved: " + str(s.moveZeroes(I))
