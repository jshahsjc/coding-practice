"""
Given a string s containing only lower case English letters and the '?' character, convert all the '?' characters into lower case letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.

It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.

Example 1:

Input: s = "?zs"
Output: "azs"
Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".
Example 2:

Input: s = "ubv?w"
Output: "ubvaw"
Explanation: There are 24 solutions for this problem. Only "v" and "w" are invalid modifications as the strings will consist of consecutive repeating characters in "ubvvw" and "ubvww".
Example 3:

Input: s = "j?qg??b"
Output: "jaqgacb"
Example 4:

Input: s = "??yw?ipkj?"
Output: "acywaipkja"

Constraints:

1 <= s.length <= 100
s contains only lower case English letters and '?'.
"""

def removeQ(instr):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    inlist = list(instr)
    while inlist.count('?') > 0:
        qindx = inlist.index('?')
        prev = inlist[qindx - 1] if qindx > 0 else ''
        next = inlist[qindx + 1] if qindx < len(inlist) - 1 else ''
        for char in alphabet:
            if char is not prev and char is not next:
                inlist[qindx] = char
                break
    return "".join(inlist)








#####  Worst solution below #####

def removeQ(in_str):
    res = ""
    alphabet = 'abcdefghijklmnopqrstuvwxyz?'
    if len(in_str) == 1 and in_str[0] == "?":
        return 'a'
    if len(in_str) == 0:
        return ""
    for i in range(len(in_str)):
        if in_str[i] != '?':
            res += in_str[i]
        elif i == len(in_str) - 1 and in_str[i] == '?':
            for char in alphabet:
                if char != res[-1]:
                    res += char
                    break
        elif in_str[i] == '?' and res != "":
            for char in alphabet:
                if char != res[-1] and char != in_str[i + 1]:
                    res += char
                    break
        elif in_str[i] == '?' and res == "":
            for char in alphabet:
                if char != in_str[i + 1]:
                    res += char
                    break
    return res
























print (replaceQmark("?zs"))
print(replaceQmark("ubv?w"))
print(replaceQmark("j?qg??b"))
print(replaceQmark("??yw?ipkj?"))
