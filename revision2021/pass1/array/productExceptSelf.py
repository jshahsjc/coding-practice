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

def productExceptSelf(A):
    left_prods = [1] * len(A)
    right_prods = [1] * len(A)
    mul = 1
    res = [0] * len(A)
    for i in range(1, len(A)):
        left_prod[i] = A[i - 1] * left_prod[i - 1]

    for i in reversed(range(len(A) - 1)):
        right_prods[i] = right_prods[i + 1] * A[i + 1]

    for i in range(len(res)):
        res[i] = left_prod[i] * right_prod[i]

    return res
