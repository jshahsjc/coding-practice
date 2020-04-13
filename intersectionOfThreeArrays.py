class Solution(object):
   def arraysIntersectionAlt(self, arr1, arr2, arr3):
      """
      :type arr1: List[int]
      :type arr2: List[int]
      :type arr3: List[int]
      :rtype: List[int]
      """
      def getIntersection(arr1, arr2):
         return [ k for k in arr1 if k in arr2 ]

      return getIntersection(getIntersection(arr1, arr2), arr3)

   def arraysIntersection(self, arr1, arr2, arr3):
      i, j, k = 0, 0, 0
      res = []
      while i < len(arr1) and j < len(arr2) and k < len(arr3):
         if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
            res.append(arr1[i])
            i += 1
            j += 1
            k += 1
         elif arr1[i] < arr2[j]:
            i += 1
         elif arr2[j] < arr3[k]:
            j += 1
         else:
            k += 1
      return res

arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]

s = Solution()
print s.arraysIntersection(arr1, arr2, arr3)
