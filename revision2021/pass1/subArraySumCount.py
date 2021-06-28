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
        count = 0
        i = 0
        j = 0
        currSum = A[i]
        while i < len(A) and j < len(A) and i <= j:
            # exapand the window by incrementing j and adding element at j to currSum
            if currSum < sum and j < (len(A)-1):
                j += 1
                currSum += A[j]
                continue
            # sum is achieved, increment count
            if currSum == sum:
                count += 1
            # if sum achieved OR currSum > sum, remove i element from window and shrink window  by incrementing i
            currSum -= A[i]
            i += 1
        return count
    else:
        return -1

nums = [-1,1,1]
k = 0
print subArraySum(nums, k)
