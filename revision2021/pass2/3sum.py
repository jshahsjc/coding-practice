"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []


Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

def twoSum(A, t):
    """
    find two numbers from A that would sum equals t
    """
    comps = {}
    for i in range(len(A)):
        comp = t - A[i]
        if comp not in comps:
            comps[A[i]] = i
        else:
            return [A[i], A[comps[comp]]]
    return []

def threeSum(nums):
    i = 0
    res = []
    while i < len(nums):
        triplets = []
        triplets.append(nums[i])
        templist = nums[:i] + nums[(i + 1):]
        target = 0 - nums[i]
        triplets += twoSum(templist, target)
        if len(triplets) == 3 and sorted(triplets) not in res:
            res.append(triplets)
        i += 1
    return res
