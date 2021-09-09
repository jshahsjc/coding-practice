"""
Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.

Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "", t = ""
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:

Input: s = "a", t = ""
Output: true
Example 4:

Input: s = "", t = "A"
Output: true
"""

def oneEditDist(s, t):
    if len(s) > len(t):
        return oneEditDist(t, s)
    if len(t) - len(s) > 1:
        return False
    if s == t:
        return False
    if len(s) == len(t) and s != t:
        for i in range(len(s)):
            if s[i] != t[i] and s[i + 1:] != t[i + 1]:
                return False
    if len(t) - len(s) == 1:
        for i in range(len(s)):
            if s[i] != t[i] and s[i:] != t[i + 1:]:
                return False
    return True

















def oneEditDist(s, t):
    """
    s, t: input strings
    rtype: bool
    """

    if len(s) > len(t):
        return oneEditDist(t, s)

    elif (len(t) - len(s)) > 1:
        return False

    elif (len(t) - len(s)) == 1:
        for i in range(len(s)):
            if s[i] is not t[i]:
                if s[i:] is not t[(i + 1):]:
                    return False
    elif (len(t) - len(s)) == 0:
        if s  == t:
            return False
        for i in range(len(s)):
            if s[i] is not t[i]:
                if s[(i + 1):] is not t[(i + 1):]:
                    return False
    else:
        return None
    return True

s = "ab"
t = "acb"
print oneEditDist(s, t)

s = "a"
t = ""
print oneEditDist(s, t)

s = ""
t = ""
print oneEditDist(s, t)
