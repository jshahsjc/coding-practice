# This is selection sort
# 1. Start with assuming the first element in the list is smallest
# 2. Now, compare current smallest element to rest of the list and
# 3. if there is a smaller than the current smallest value, swap them.
# 4. move the pointer to the next element, and consider it smallest.
# Repeat steps 1 to 3 with new smallest value
# This method uses 2 for loops, so O(N**2)
# Due to expensive time complexity, it's not recommended for very large lists 
def selection_sort(A):
   for i in range(0,(len(A)-1)):
      minIndex = i
      for j in range(i+1,len(A)):
         if A[j] < A[minIndex]:
            minIndex = j
      if minIndex != i:
         A[i],A[minIndex] = A[minIndex],A[i]

L = [7,8,5,4,9,2]
selection_sort(L)
print L
