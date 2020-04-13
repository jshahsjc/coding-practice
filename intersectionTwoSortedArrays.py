def intersectTwoSortedArrays(arr1, arr2):
   i, j = 0, 0
   res = []
   while i < len(arr1) and j < len(arr2):
      print arr1[i], arr2[j]
      if arr1[i] == arr2[j] and arr1[i] not in res:
         res.append(arr1[i])
         i += 1
         j += 1
      elif arr1[i] < arr2[j]:
         i += 1
      else:
         j += 1

   return res

nums1 = [-1, 0, 1, 1, 2, 2]
nums2 = [-4, -1, 0, 1, 1, 2, 2]

print intersectTwoSortedArrays(nums1, nums2)
