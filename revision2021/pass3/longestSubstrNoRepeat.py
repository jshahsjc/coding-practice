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
from collections import defaultdict

def longestSubStrNoRepeat(s):
    #temp = defaultdict()
    i = 0
    j = 1
    maxlen = 1
    if len(s) == 1:
        return 1
    if len(s) == 0:
        return 0

    while j < len(s):
        temp = ""
        temp += s[i]
        #temp[s[i]] = i
        if s[j] not in temp:
        #    temp[s[j]] = j
            temp += s[j]
            maxlen = max(maxlen, len(temp))
            print (temp, maxlen)
            j += 1

        else:
            #del temp[s[min(temp.values())]]
            i += 1
            j = i + 1
    return maxlen
    
s = "pwwkew"
print  (longestSubStrNoRepeat(s))
