"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""

def longestCommonPrefix(strs):
    if len(strs) <= 1:
        return strs

    strs = sorted(strs, key = lambda x: len(x))
    res = strs[0]
    i = 1
    while i < len(strs) and len(res) > 0:
        if res != strs[i][:len(res)]:
            res = res[:len(res)-1]
        else:
            i += 1
    return res

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))

strs = ["dog","racecar","car"]
print(longestCommonPrefix(strs))
