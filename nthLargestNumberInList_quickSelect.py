"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

def nthLargestElement(L, n):
   k = len(L) - n
   if k == 0:
      return quickSortHelper(L, 0, len(L)-1, len(L)-1)
   else:
      return quickSortHelper(L, 0, len(L)-1, k)

def quickSortHelper(L, first, last, k):
   print "============="
   if first <= last:
      splitpoint = partition(L, first, last)
      print "splitpoint " + str(splitpoint)
      if splitpoint == k:
         print "matched smallest k to splitpoint " + str(splitpoint)
         return L[k]
      elif splitpoint > k:
         print str(splitpoint) + " is greater than " + str(k)
         print "recurse from %d to %d"%(first, splitpoint-1)
         return quickSortHelper(L, first, splitpoint-1, k)
      else:
         print str(splitpoint) + " is less than " + str(k)
         print "recurse from %d to %d"%(splitpoint+1, last)
         return quickSortHelper(L, splitpoint+1, last, k)

def partition(L, first, last):
   pivot = L[first]
   leftmark = first + 1
   rightmark = last
   done = False

   while not done:
      while leftmark <= rightmark and L[first] > L[leftmark]:
         leftmark += 1
      while leftmark <= rightmark and L[first] < L[rightmark]:
         rightmark -= 1
      if leftmark > rightmark:
         done = True
      else:
         L[leftmark], L[rightmark] = L[rightmark], L[leftmark]
   L[first], L[rightmark] = L[rightmark], L[first]
   return rightmark


input =  [3,2,1,5,6,4]
print nthLargestElement(input, 6)
