"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""
from  collections import defaultdict
def longestSubStrNoRepeat(s):
    maxlen = 0
    i = 0
    keep =  defaultdict()
    for j in range(len(s)):
        if s[j] in keep:
            i = keep[s[j]]
        maxlen = max(maxlen, j - i + 1)
        keep[s[j]] = j + 1

    return maxlen

print longestSubStrNoRepeat("pwwkew")



def longestSubStrNoRepeat(strs):
    i = 0
    max_len = 0
    keep = defaultdict()
    for j in range(len(strs)):
        if strs[j] in keep:
            i = strs[j]
        max_len = max(max_len, j - i + 1)
        keep[strs[j]] = j + 1
    return max_len
