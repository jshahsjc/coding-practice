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

def equalSumSubarray(nums):
    sum = 0
    match_sum = 0
    for n in nums:
        sum += n

    for i in range(len(nums)):
        match_sum += nums[i]
        sum -= nums[i]
        if match_sum == sum:
            return [ nums[:i + 1], nums[i + 1:] ]

A = [1, 2, 3, 4, 5, 5]
print(equalSumSubarray(A))
