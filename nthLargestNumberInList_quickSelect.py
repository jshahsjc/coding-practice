class Solution(object):
   def nthLargestElement(self, L, n):

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

      k = len(L) - n
      if k == 0:
         return quickSortHelper(L, 0, len(L)-1, len(L)-1)
      else:
         return quickSortHelper(L, 0, len(L)-1, k)

s = Solution()
input =  [3,2,1,5,6,4]
print s.nthLargestElement(input, 6)
