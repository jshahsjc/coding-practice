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

def commonPrefix(strs):
    strs = sorted(strs, key = lambda x: len(x))
    base_len = len(strs[0])
    res = strs[0]

    for str in strs[1:]:
        if str[:base_len] != res:
            res = res.strip[res[-1]]
        if len(res) == 0:
            return ""

    return res
