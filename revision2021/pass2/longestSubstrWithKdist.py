"""
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.


Constraints:

1 <= s.length <= 5 * 104
0 <= k <= 50
"""
from collections import defaultdict

def longestSubStrWithKdist(s, k):
    i = 0
    keep = defaultdict()
    maxlen = 0

    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1

    for j in range(len(s)):
        keep[s[j]] = j
        if len(keep) > k:
            i += 1
            delIndx = min(keep.values())
            del keep[s[delIndx]]
        maxlen = max(maxlen, j - i + 1)
        
    return maxlen
s = "eceba"
k = 2

print longestSubStrWithKdist(s, k)
