"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""

def productExceptSelf(nums):
    left_product = [1]
#    right_product = []
#    res = []
    left_mul = 1
    right_mul = 1
    for i in range(1, len(nums)):
        left_mul *= nums[i - 1]
        left_product.append(left_mul)
    for j in reversed(range(len(nums) - 1)):
        right_mul *= nums[ j + 1 ]
        left_product[j] *= right_mul
    return left_product
