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

def search_in_rotated_list(L, x):
   start = 0
   end = len(L) - 1

   while start <= end:
      mid = start + (end - start) // 2
      if L[mid] == x:
         return mid

      elif L[mid] >= L[start]:
         if x < L[mid] and x >= L[start]:
            end = mid - 1
         else:
            start = mid + 1

      else:
         if x <= L[end] and x > L[mid]:
            start = start + 1
         else:
            end = mid - 1

   return -1

L = [6,7,0,1,2,3,4,5]
for i in L:
   print search_in_rotated_list(L, i)
