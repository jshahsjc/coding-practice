"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.


Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

Follow up: Could you minimize the total number of operations done?
"""



def moveZero(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] is not 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums














def moveZero(nums):
    i = 0
    j = 1
    if len(nums) <= 1:
        return nums
    while j < len(nums):
        if nums[i] is 0:
            if nums[j] is 0:
                j += 1
            else:
                nums[i], nums[j] =  nums[j], nums[i]
                i +=  1
        else:
            i += 1
            j += 1

    return nums

nums = [0,1,0,3,12]
print(moveZero(nums))

def moveZero(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums
