"""
Floor in a Sorted Array
Given a sorted array and a value x, the floor of x is the largest element in array smaller than or equal to x. Write efficient functions to find floor of x.

Examples:

Input : arr[] = {1, 2, 8, 10, 10, 12, 19}, x = 5
Output : 2

Explanation : 2 is the largest element in
arr[] smaller than 5.

Input : arr[] = {1, 2, 8, 10, 10, 12, 19}, x = 20
Output : 19
Explanation :19 is the largest element in
arr[] smaller than 20.

Input : arr[] = {1, 2, 8, 10, 10, 12, 19}, x = 0
Output : -1
Explanation :Since floor doesn't exist,
output is -1.
"""

class Solution(object):
   def getFloorAndCeiling(self, arr, x):
      """
      type: arr: list
      type: x: int
      rtype: int
      """

      def getFloor(arr, low, high, x):
         # if x is greater than high, high is floor
         if x >= arr[high]:
            return high
         # if low is greater than high, return -1
         if low > high:
            return -1
         # get the mid value
         mid = low + (high - low) // 2
         # check if mid is x,  mid is floor
         if arr[mid] == x:
            return mid
         # check if x is between mid - 1 and mid
         if mid > 0 and  arr[mid - 1] < x < arr[mid]:
            return mid - 1
         # if x is less than mid, check on left half
         if x < arr[mid]:
            return getFloor(arr, low, mid - 1, x)
         if arr[mid] < x < arr[high]:
            return getFloor(arr, mid + 1, high, x)


      def getCeiling(arr, low, high, x):
         # if x is lower than low, ceiling is low
         if x <= arr[low]:
            return low
         # if x is high, ceiling is high
         if x == arr[high]:
            return high
         # if x is greater than high, return -1
         if x > arr[high] or low > high:
            return -1
         # get the mid value
         mid = low + (high - low) // 2
         # check if mid value is x
         if arr[mid] == x:
            return mid
         # check if x is between mid and mid + 1
         if mid > 0 and arr[mid] < x <= arr[mid + 1]:
            return mid + 1
         # if x is greater than mid + 1 value, recurse right
         if arr[mid] < x < arr[high]:
            return getCeiling(arr, mid, high, x)
         # if x is less than mid, recurse left
         if arr[low] < x < arr[mid]:
            return getCeiling(arr, low, mid - 1, x)

      ceiling = getCeiling(arr, 0, len(arr) - 1, x)
      floor = getFloor(arr, 0, len(arr) - 1, x)

      return arr[floor], arr[ceiling]

I = [1, 2, 8, 10, 10, 12, 19]
s = Solution()

print s.getFloorAndCeiling(I, 3)
