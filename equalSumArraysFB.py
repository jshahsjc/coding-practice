"""
https://www.geeksforgeeks.org/split-array-two-equal-sum-subarrays/

Split an array into two equal Sum subarrays
Given an array of integers greater than zero, find if it is possible to split it in two subarrays (without reordering the elements), such that the sum of the two subarrays is the same. Print the two subarrays.

Examples :

Input : Arr[] = { 1 , 2 , 3 , 4 , 5 , 5  }
Output :  { 1 2 3 4 }
          { 5 , 5 }

Input : Arr[] = { 4, 1, 2, 3 }
Output : {4 1}
         {2 3}

Input : Arr[] = { 4, 3, 2, 1}
Output : Not Possible
Asked In : Facebook interview

"""

def equiSumArray(A):
   sum = 0
   for i in A:
      sum += i

   left_sum = 0
   for i, val in enumerate(A):
      left_sum += val
      sum -= val
      if left_sum == sum:
         print str(A[0: i + 1])
         print str(A[i + 1: len(A)])
         return True

   return False


A = [1 , 2 , 3 , 4 , 5 , 5]

print equiSumArray(A)
