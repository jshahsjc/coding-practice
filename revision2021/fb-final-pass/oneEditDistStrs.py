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

def oneEditDist(str_a, str_b):
    if len(str_a) > len(str_b):
        return oneEditDist(str_b,  str_a)

    if len(str_b) - len(str_a) > 1:
        return False

    if str_a == str_b:
        return False

    if str_b[:len(str_a)] == str_a:
        return True
    else:
        for i in range(len(str_a)):
            if str_a[i] != str_b[i] and str_a[i:] != str_b[i+1:]:
                return False

    return True
