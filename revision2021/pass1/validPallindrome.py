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

def validPalindrome(S):
    """
    S: sentence
    return bool
    """
    temp = ""
    for s in S:
        if s.isalnum():
            temp += s

    i, j = 0, len(temp) - 1
    while i < j:
        if temp[i].lower() == temp[j].lower():
            i += 1
            j -= 1
        else:
            return False

    return True

S = "A man, a plan, a canal: Panama"
S = "race9 9e car"
if validPalindrome(S):
    print("yes !!")
else:
    print("No !!")
