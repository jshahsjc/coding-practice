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
def longestSubStrKdistinct(s, k):
    """
    s: given string
    k: max distinct chars
    return maxlen: int representing longest substring with k max distinct chars
    """

    i = j = 0
    maxlen = 1
    temp = defaultdict()
    if len(s) <= 1:
        return maxlen

    while j < len(s):
        temp[s[j]] = j
        j += 1
        if len(temp) == k + 1:
            delIndx = min(temp.values())
            del temp[s[delIndx]]
            i += 1

        maxlen = max(maxlen, (j - i))
    return maxlen

s = "eceba"
k = 2
print (longestSubStrKdistinct(s, k))
