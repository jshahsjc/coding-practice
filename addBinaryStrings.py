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
take two binary strings: b1 and b2
for the length of maximum lengh of b1 or b2

function1: compute a binary sum of two given bits, return (sum, carry)
do a binary addtion on the bits:
   1 + 1 = 0, carry 1 (decimal 2, 2%2 = 0 (sum), 2/2 = 1 (carry))
   1 + 0 = 1, carry 0 (decimal 1, 1%2 = 1 (sum), 1/2 = 0 (carry))
   0 + 0 = 0, carry 0 (decimal 0, 0%2 = 0 (sum), 0/2 = 0 (carry))

function 2:
start with last bit in both binary strings and go left, until reach 0th index
do this until 0th index of both strings

It's possible that 2 strings are of different length
so, may be try something like merge sort.

if index of b1 and b2 >=0:
   sum = int(b1[index]) + int(b2[index]) + carry
   index -= 1
if b1 index >=0:
   sum = sum + int(b1[index]) + carry
if b2 index >= 0:
   sum = sum + int(b2[index]) + carry

"""

def binary_bit_add(b1, b2, carry = 0): # This is very naive/can be more complex
   if (b1 + b2 ) == 2:
      return (0, 1)
   elif (b1 + b2) == 1:
      return (1, 0)
   else:
      return (0, 0)

def binary_string_add(s1, s2):
   i = len(s1) - 1
   j = len(s2) - 1
   grand_sum = ""
   carry = 0
   sum = 0

   while i >= 0 and j >= 0:
      bit_sum, bit_carry = binary_bit_add(int(s1[i]), int(s2[j]))
      if carry:
         bit_sum, carry = binary_bit_add(bit_sum, carry)
      grand_sum = str(bit_sum) + grand_sum
      carry = carry + bit_carry
      i -= 1
      j -= 1

   while i >= 0:
      bit_sum, bit_carry = binary_bit_add(int(s1[i]), carry)
      grand_sum = str(bit_sum) + grand_sum
      carry = bit_carry
      i -= 1

   while j >= 0:
      bit_sum, bit_carry = binary_bit_add(int(s2[j]), carry)
      grand_sum = str(bit_sum) + grand_sum
      carry = bit_carry
      j -= 1

   if carry:
      grand_sum = str(carry) + grand_sum

   return grand_sum

s1 = '1011'
s2 = '111'
print "%s + %s = "%(s1, s2) + binary_string_add(s1, s2)
