# Bubble sort uses two for loops
# O(n**2)


def bubbleSort(A):
   print "Sorting intput List:"
   print A
   swapped = False
   for i in range(0,len(A)-1):
      for j in range(0,len(A)-1-i):
         print "i is %d, j is %d"%(i,j)
         if A[j] > A[j+1]:
            A[j],A[j+1] = A[j+1],A[j]
            swapped = True
            print "Swapping A[j] with A[j+1]"
            print A
         if swapped:
            break
   return A

L = [7,8,5,4,9,2]
bubbleSort(L)
print "Sorted List: "
print L
