"""
Greatest contiguous sub-array of size K
Given an array arr[] of integers and an integer K, the task is to find the greatest contiguous sub-array of size K. Sub-array X is said to be greater than sub-array Y if the first non-matching element in both the sub-arrays has a greater value in X than in Y

Examples:

Input: arr = [1, 4, 3, 2, 5], K = 4
Output: 4 3 2 5
Two subarrays are [1, 4, 3, 2] and [4, 3, 2, 5].
Hence, the greater one is [4, 3, 2, 5]
"""

def largestContiguousSubArray(A, k):
   sub_arr = []
   for ind in range(len(A) - k + 1):
      sub_arr.append(A[ind : ind + k])
   print sub_arr
   return sorted(sub_arr)[-1]

arr = [ 1, 4, 3, 2, 5, 10, 8, 9 ]
K = 4
print largestContiguousSubArray(arr, K)
