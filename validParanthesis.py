"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

"""
from collections import defaultdict
def validParanthesis(s):
   count = defaultdict(str)
   for i in s:
      if i not in count:
         count[i] = 1
      else:
         count[i] += 1

   if count['('] != count[')']:
      return False

   if count['['] != count[']']:
      return False

   if count['{'] != count['}']:
      return False

   return True


def validParantesisAlt(s):
   stack = []
   parathesis = {')':'(', ']':'[', '}':'{'}

   for c in s:
      if c in parathesis:
         top_element = stack.pop() if stack else '#'
         if top_element != parathesis[c]:
            return False
      else:
         stack.append(c)

   return not stack

print "()[]{}"
print validParantesisAlt("()[]{}")

print "()["
print validParantesisAlt("()[")
