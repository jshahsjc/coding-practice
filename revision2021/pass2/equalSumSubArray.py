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

def equalSumArrays(A):
    sum  =  0
    currSum = 0
    for i in A:
        sum  += i

    for i in range(len(A)):
        currSum += A[i]
        sum -= A[i]
        if currSum == sum:
            return (A[:i+1], A[i+1:])
    return "Not Possible"

Arr = [ 1 , 2 , 3 , 4 , 5 , 5  ]
print (equalSumArrays(Arr))
