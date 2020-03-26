"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
"""

"""
intersection = [ value for value in nums1 if value in nums2 ]
"""
def getIntersection(N1, N2):
   result = []
   for value in N1:
      if value in N2 and value not in result:
         result.append(value)
   return result

nums1 = [1,2,2,1]
nums2 = [2,2]

print getIntersection(nums1, nums2)
