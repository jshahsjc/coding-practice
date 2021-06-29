"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

def twoSum(A, t):
    compDict = {}
    for i in range(len(A)):
        comp = t - A[i]
        if comp in compDict:
            return (i, compDict[comp])
        else:
            compDict[A[i]] = i
    return ()

given_nums = [2, 7, 11, 15]
target = 9

print twoSum(given_nums, target)
