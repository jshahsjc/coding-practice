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

def double_sum(nums, t):
    keep = {}
    for n in range(len(nums)):
        comp = t - nums[n]
        if comp not in keep:
            keep[nums[n]] = n
        else:
            return [nums[keep[comp]], nums[n]]
    return []

def triplet_sum(nums):
    res = []
    if len(nums) < 3:
        return []

    for n in len(nums):
        triplet = []
        triplet.append(nums[n])
        temp = nums[:n] + nums[n:]
        target = 0 - nums[n]
        triplet += double_sum(temp, target)
        if len(triplet) == 3 and sorted(triplet) not in res:
            res.append(sorted(triplet))

    return res
