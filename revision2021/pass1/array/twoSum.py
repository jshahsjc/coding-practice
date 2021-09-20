"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

from collections import defaultdict
def twoSum(nums, t):
    keep = defaultdict()
    for i in range(len(nums)):
        comp = t - nums[i]
        if comp in keep:
            return [keep[comp], i]
        else:
            keep[nums[i]] = i
    return []





























def twoSum(nums, target):
    i = 0
    while i < len(nums):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
        else:
            i += 1

nums = [2, 7, 11, 15]
target = 9
