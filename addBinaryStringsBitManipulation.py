"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

"""
bit manipulation
"""

def add_binary_strings(a, b):
   # convert binary strings a and b into integers with base 2
   x, y = int(a, 2), int(b, 2)
   while y:
      sum = x ^ y  # this computes sum without carry
      carry = (x & y) << 1 # compute carry separately
      x, y = sum, carry

   return bin(x)[2:]

a = '1010'
b = '1011'
print add_binary_strings(a, b)
