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

def validParn(tstStr):
    tmpStack = []
    reference = { "}": "{", "]": "[", ")": "(" }
    for par in tstStr:
        if par in reference:
            if tmpStack and reference[par] != tmpStack.pop():
                    return False
            else:
                tmpStack.append(par)
    return not tmpStack
