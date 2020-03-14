def mergeSort(A):
   if len(A) > 1:
      m = len(A) // 2  # Find mid index
      L = A[:m]   # Create left sub-array
      R = A[m:]   # Create right sub-array

      mergeSort(L)   # Recursive call on left array
      mergeSort(R)   # Recursive call on right array
      merge(A, L, R) # Merge the Left and Right arrays

def merge(A, L, R):
      i = j = k = 0   # Initialize indexes for L, R and A
      while i < len(L) and j < len(R):  # Merge sub-arrays
         if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
         else:
            A[k] = R[j]
            j += 1
         k += 1

      while i < len(L):   # Add any remaining elements from L
         A[k] = L[i]
         i += 1
         k += 1

      while j < len(R):   # Add any remaining elements from R
         A[k] = R[j]
         j += 1
         k += 1

if __name__ == '__main__':
   l1 = [10, 12, 15, 21, 29]
   l2 = [13, 16, 22, 23, 24, 27]
   L = []

   mergedList = merge(L, l1, l2)
#   T = [12, 14, 99, 38, 24, 10, 1]
   print "Input Test:"
   print l1
   print l2
#   mergeSort(T)
   print "Sorted Test"
   print mergedList
