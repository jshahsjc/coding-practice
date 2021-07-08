"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

from collections import defaultdict

def subArraySumK(A, k):
    currSum = 0
    count = 0
    keep = defaultdict(lambda: 0)

    for i in range(len(A)):
        currSum += A[i]
        if currSum == k:
            count += 1
        if (currSum - k) in keep:
            count += keep[(currSum - k)]
        else:
            keep[currSum] += 1

    return count

nums = [1,1,1]
k = 2
print subArraySumK(nums, k)
