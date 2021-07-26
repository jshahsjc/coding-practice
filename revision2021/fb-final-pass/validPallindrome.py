"""
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""

def validPalindrome(s):
    test_str = ""
    for char in s:
        if char.isalnum():
            test_str += char.lower()
    i = 0
    j = len(test_str) - 1
    while i < j:
        if test_str[i] == test_str[j]:
            i += 1
            j -= 1
        else:
            return False
    return True
