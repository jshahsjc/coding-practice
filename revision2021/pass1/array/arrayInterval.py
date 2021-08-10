"""
349. Intersection of Two Arrays
Easy

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""

def twoArrayIntersect(nums1, nums2):
    if len(nums1) > len(nums2):
        twoArrayIntersect(nums2, nums1)
    res = []
    for n in set(nums1):
        if n in set(nums2):
            res.append(n)
    return res

# Alternte method
from collections import defaultdict
def twoArrayIntersect(nums1, nums2):
    nums1.sort()
    nums2.sort()
    nums = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j] and nums1[i] not in nums:
            nums.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return nums
