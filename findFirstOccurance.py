def findFirstOccurance(A, n):
   for k in range(len(A)):
      if A[k] == n:
         return k
         break
   else:
      return None


L = [100, 5, 86, 10, 50, 50, 5, 10]
if findFirstOccurance(L, 101) is not None:
   resIndex = findFirstOccurance(L, 101)
   print "first occurance is at index %d: "%resIndex
else:
   print "Not in the list"
