def merge(L1, L2, A = []):
   i = j = 0
   while i < len(L1) and j < len(L2):
      if L1[i] <= L2[j]:
         A.append(L1[i])
         i += 1
      else:
         A.append(L2[j])
         j += 1

   while i < len(L1):
      A.append(L1[i])
      i += 1

   while j < len(L2):
      A.append(L2[j])
      j += 1

   return A

l1 = [10, 12, 15, 21, 29]
l2 = [13, 16, 22, 23, 24, 11]

mergedList = merge(l1, l2)
print mergedList
