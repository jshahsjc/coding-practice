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
    """
    s: given str
    k: max distinct chars
    maxlen: return int
    """
    if len(s) * k == 0:
        return 0
    #max length of string with k distinct
    maxlen = 1
    # sliding window pointers
    i = j = 0
    currWindow = defaultdict(int)
    while j < len(s):
        currWindow[s[j]] = j
        j += 1
        if len(currWindow) is k + 1:
            delIndx = min(currWindow.values())
            del currWindow[s[delIndx]]
            i += 1
            print((i, j))
        maxlen = max(maxlen, (j - i))
    return maxlen



from collecitons import defaultdict
def longestSubStrWithKdist(strs, k):
    keep = defaultdict()
    i = 0
    max_len = 0
    for j in range(len(strs)):
        keep[strs[j]] = j
        if len(keep) > k:
            d_indx = min(keep.values())
            del keep[strs[d_indx]]
            i += 1
        max_len = max(max_len, j - i)
    return max_len
