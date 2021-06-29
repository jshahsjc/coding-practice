"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""

# First simple o(n^2) solution:
def productXself(A):
    tmpA = []
    answer = []
    for i in range(len(A)):
        p = 1
        tmpA = A[:i] + A[i + 1:]
        print tmpA
        for val in tmpA:
            p *=  val
        print p
        answer.append(p)
    return answer

print (productXself([1,2,3,4]))

# O(n) solution:

def productExceptSelf(A):
    L = []*len(A)
    R = []*len(A)
    
