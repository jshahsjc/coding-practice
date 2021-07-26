"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""

def validParenth(input_str):
    v_par = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    temp = []
    for i in input_str:
        if i in v_par:
            temp.append(i)
        if i in v_par.values():
            if v_par[temp[-1]] != i:
                return False
            else:
                temp.pop()
    return True
