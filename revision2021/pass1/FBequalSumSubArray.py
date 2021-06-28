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

# Approach1:
# sum = 0
# start adding elements from the left to the sum;
# each time calculate  the sum of rest of the array -- say rightSum;
# if sum == rightSum, we have  the answer
# Problem with this is that each time we have to iterate through whole right side

# Approach2:
# sum  = 0
# fullSum = whole sum of all array elements
# iterate values from left,
# sum += value and fullSum -= value;
# compare sum and fullSum

def equalSumSubArray(A):
    sum = 0
    leftSum = 0
    for i in A:
        sum += i
    for k, val in enumerate(A):
        leftSum += val
        sum -= val
        if leftSum == sum:
            return [A[:k+1], A[k+1:]]

# Test
testA =  [ 1 , 2 , 3 , 4 , 5 , 5 ]
print "equiSum left:", equalSumSubArray(testA)[0]
print "equiSum right:", equalSumSubArray(testA)[1]
