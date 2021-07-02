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

def longestSubStrNoRepeat(S):
    i = 0
    j = 1
    count = 0
    print (len(S))
    if len(S) == 0:
        return 0
    if len(S) == 1:
        return 1
    while j < len(S):
        if S[i] == S[j]:
            count = j - i + 1
            print(count)
            i += 1
            j += 1
        else:
            j += 1

    return count

print longestSubStrNoRepeat("pwwkew")
