"""
Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.

Example 1:

Input: A = [4,7,9,10], K = 1
Output: 5
Explanation:
The first missing number is 5.
Example 2:

Input: A = [4,7,9,10], K = 3
Output: 8
Explanation:
The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 3:

Input: A = [1,2,4], K = 3
Output: 6
Explanation:
The missing numbers are [3,5,6,7,...], hence the third missing number is 6.


Note:

1 <= A.length <= 50000
1 <= A[i] <= 1e7
1 <= K <= 1e8
"""

def missing(A, idx):
   return A[idx] - A[0] - idx

def kthMissingElement(A, k):
   n = len(A) - 1
   if k > missing(A, n):
      return A[n] + k - missing(A, n)

   idx = 1
   while missing(A, idx) < k:
      idx += 1

   return A[idx - 1] - missing(A, idx - 1) + k

def kthMissingElementBinarySearch(A, k):
   if missing(A, len(A)-1) < k:
      return A[len(A) - 1] + k - missing(A, len(A) - 1)

   left = 0
   right = len(A) - 1
   while left != right:
      pivot = left + (right - left) // 2
      if missing(A, pivot) < k:
         left = pivot + 1
      else:
         right = pivot

   return A[left - 1] + k - missing(A, left - 1)

A = [1, 2, 4]
K = 3
print str(kthMissingElement(A, K)) + " - using iterative method"
print str(kthMissingElementBinarySearch(A, K)) + " - using binary search method"

B = [4,7,9,10]
J = 3
print str(kthMissingElement(B, J)) + " - using iterative method"
print str(kthMissingElementBinarySearch(B, J)) + " - using binary search method"
