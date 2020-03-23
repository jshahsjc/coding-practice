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
   length = len(nums)
   output = [0]*length
   L = [0]*length
   R = [0]*length

   # L is a list where each element is multiplication of all the elements to the left of element's index in main input list nums.
   L[0] = 1
   for i in range(1, length):
      L[i] = L[i-1]*nums[i-1]

   # R is a list where each element is a multiplication of all elements to the right of elements' index in the main input list nums.
   R[length-1] = 1
   for i in reversed(range(length-1)):
      R[i] = R[i+1]*nums[i+1]

   # output is a list with multiplicaion of elemnents from L and R at a given index.
   # This is the multiplication of all indexes in the list excetp self.
   # achieved without using division.
   for i in range(length):
      output[i] = L[i]*R[i]

   return output

nums = [1,2,3,4]
print productExceptSelf(nums)
