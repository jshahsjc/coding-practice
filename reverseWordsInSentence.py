"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""

def reverseWordsInSentense(s):

   stack = []
   p = len(s) - 1
   res = ''
   final = ''

   while p >= 0:
      if s[p] != ' ':
         stack.append(s[p])
         p -= 1
      else:
         stack.append(' ')
         p -= 1
   print stack

   for i in range(len(stack)):
      if stack[i] is not ' ':
         res += stack[i]
      else:
         final = res + stack[i] + final
         res = ''
   # This will leave last word in res
   return res + ' ' + final

input = "Let's take LeetCode contest"
print input
print reverseWordsInSentense(input)
