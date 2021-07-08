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

def validpar(s):
    keep = { "(": ")",
             "[": "]",
             "{": "}" }

    mystack = []

    for i in range(len(s)):
        if s[i] in keep:
            mystack.append(s[i])
            print (mystack)
        else:
            if s[i] in keep.values():
                print("val:", s[i])
                print("compare:",mystack[-1])
                if keep[mystack[-1]] is not s[i]:
                    return False
                else:
                    mystack.pop()

    return True

print (validpar("{[]}"))

print (validpar("([)])"))
