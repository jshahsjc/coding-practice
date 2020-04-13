"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2

Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
Input: [0,1,0]
Output: 2

Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.
"""
from collections import defaultdict
def longestBalancedBinarySubArray(nums):
   max_len = 0
   balance = defaultdict(int)
   curr_bal = 0

   for i, val in enumerate(nums):
      if val == 1:
         curr_bal += 1
      else:
         curr_bal -= 1

      if curr_bal == 0:
         max_len = i + 1

      comp = 0 - curr_bal
      # print comp
      if balance[comp] is not None:
         print max_len
         max_len = max(max_len, i - balance[comp])
      else:
         balance[curr_bal] = i

   return max_len


input = [0,1,0,0,0,1,1,0,1]
print len(input)
# -1 +1 (max_len 2) -1 -1 -1 +1 +1 -1 + 1
print longestBalancedBinarySubArray(input)
