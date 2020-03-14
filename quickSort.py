def quickSort(A):
   print "input array:"
   print A
   quickSortHelper(A, 0, len(A)-1)

def quickSortHelper(A, first, last):
   print "\nRunning quickSortHelper from index %d to index %d"%(first, last)
   print A
   if first < last:
      print "\n Running partition from %d to %d"%(A[first], A[last])
      splitpoint = partition(A, first, last)
      print "\n Splitpoint is %d at index %d:"%(A[splitpoint], splitpoint)
      quickSortHelper(A, first, splitpoint -1)
      quickSortHelper(A, splitpoint + 1, last)

def partition(A, first, last):
   pivot = A[first]
   leftmark = first + 1
   rightmark = last
   done = False

   while not done:
      while leftmark <= rightmark and A[first] > A[leftmark]:
         leftmark += 1
      while leftmark <= rightmark and A[first] < A[rightmark]:
         rightmark -= 1

      if leftmark > rightmark:
         done = True
      else:
         A[leftmark], A[rightmark] = A[rightmark], A[leftmark]

   A[first], A[rightmark] = A[rightmark], A[first]
   return rightmark

T = [20, 1, 25, 6, 100, 30, 35, 56, 7, 9, 80]
quickSort(T)
print "\nThe sorted array T:"
print T
