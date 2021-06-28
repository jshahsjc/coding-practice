"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

def twoSum(nums, target):
    seen = {}
    for i in range(len(nums)):
        comp = target - num[i]
        if comp not in seen:
            seen[nums[i]] = i
        else:
            return (seen[comp], i)

nums = [2, 7, 11, 15]
target = 9
print twoSum(nums, target)
