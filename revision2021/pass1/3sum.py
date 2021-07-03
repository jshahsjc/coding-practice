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
    A: List of int
    return two indices whose
    sum would equal to a target t
    """
    compdict = {}
    i = 0
    while i < len(A):
        comp = t - A[i]
        if comp not in compdict:
            compdict[comp] = i
            i += 1
        else:
            return (A[i], A[compdict[comp]])
    return ()

def threeSum(nums):
    res = []
    for i in range(len(nums)):
        triplet = []
        triplet.append(nums[i])
        target = 0 - nums[i]
        print("target:", target)
        alist = nums[:i] + nums[(i + 1):]
        print ("alist:", alist)
        cmp = twoSum(alist, target)
        print ("cmp:", cmp)
        if len(cmp) == 2:
            triplet.append(cmp[0])
            triplet.append(cmp[1])
        if len(triplet) == 3:
            res.append(triplet)
    return res

nums = [-1,0,1,2,-1,-4]
test = threeSum(nums)
print (test)
