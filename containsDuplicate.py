"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

def containsDuplicate(nums):
   """
   :type nums: List[int]
   :rtype: bool
   """
#   return len(nums) != len(set(nums))
   count = {}
   for n in nums:
      if n not in count:
         count[n] = 1
      else:
         count[n] += 1

   for value in count.values():
      return value != 1

input = [1,2,3]

print containsDuplicate(input)
