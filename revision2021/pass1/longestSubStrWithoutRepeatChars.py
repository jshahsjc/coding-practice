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
        print("first if")
        return 0
    if len(S) == 1:
        print("2nd if")
        return 1
    while j < len(S):
        print("in while")
        if S[i] == S[j]:
            print("3rd if")
            print ("i", i)
            print ("j", j)
            print(count)
            j += 1
        else:
            print("in else")
            print (S[i:j+1])
            count = j - i + 1
            i += 1
            j += 1

    return count

print longestSubStrNoRepeat("pwwkew")
