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
    A: list
    t: int
    """
    comps = {}
    for i in range(len(A)):
        comp = t - A[i]
        if comp not in comps:
            comps[A[i]] = i
        else:
            return [A[i], A[comps[comp]]

    return []

def threeSum(nums):
    """
    nums: list
    """
    i = 0
    res = []
    while i < len(nums):
        triplet = []
        triplet.append(nums[i])
        target = 0 - nums[i]
        templist = nums[:i] + nums[(i + 1):]
        triplet += twoSum(templist, target)
        if len(triplet) == 3 and sorted(triplet) not in res:
            res.append(sorted(triplet))
        i += 1
    return res


nums = [-1,0,1,2,-1,-4]
test = threeSum(nums)
print (test)
