"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23


Constraints:

1 <= nums.length <= 3 * 104
-105 <= nums[i] <= 105

"""

def maxSubArraySum(nums):
    curr_sum = 0
    max_sum = 0
    for i in range(len(nums)):
        curr_sum = max(curr_sum + nums[i], nums[i])
        max_sum = max(max_sum, curr_sum)
    return max_sum










import math

def maxSubArraySum(nums):
    max_sum = -(10**5)
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            max_sum = max(max_sum, curr_sum)

    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [5,4,-1,7,8]
print(maxSubArraySum(nums))


def maxSubArray(nums):
    curr_sum = max_sum = nums[0]
    for j in range(1, len(nums)):
        curr_sum = max(nums[j], curr_sum + nums[j])
        max_sum = max(max_sum, curr_sum)
    return max_sum
