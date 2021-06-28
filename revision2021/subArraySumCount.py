"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

def subArraySum(A, sum):
    if len(A) in range(1, 20001):
        tmpSum = 0
        count = 0
        i = j = 0

        while i < len(A) and j < len(A) and i <= j:
            tmpSum += A[i]

            if tmpSum == sum:
                count += 1
                tmpSum -= A[i]
                i += 1
            else:
                tmpSum += A[j]
                j += 1
        return count
    else:
        return -1

nums = [1,1,1]
k = 2
print subArraySum(nums, k)
