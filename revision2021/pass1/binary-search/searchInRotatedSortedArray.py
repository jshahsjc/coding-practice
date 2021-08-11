"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

def searchInRotatedSortedArray(nums, k):
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = lo + hi // 2
        if nums[mid] == k:
            return mid
        if nums[mid] >= nums[lo]:
            # rotation point is to the right of mid
            if nums[mid] > k >= nums[lo]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            # rotation point is to the left of mid
            if nums[mid] < k <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
