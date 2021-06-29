"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

def subArraySum(A, k):
    currSum = 0
    count == 0
    priorSums = {}
    for i in range(len(A)):
        currSum += A[i]
        if currSum == k:
            count += 1
        elif (currSum - k) in priorSums:
            count += priorSums[currSum - k]
        elif currSum in priorSums:
            priorSums[currSum] += 1
        else:
            priorSums[currSum] = 1


    return count


#test
nums = [1,1,1]
k = 2
print subArraySum(nums, k)
