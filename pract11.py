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
--------------

Asked in Aviatrix first coding screen:
Given a string i.e.: 'statistics',
return list of indices of uniq characters with 1 based index: [3, 9] for a and c
if no uniq chars in the string, return -1

"""
import re

class Playstr:
    def __init__(self, inStr):
        self.inStr = inStr

    def __str__(self):
        return f"input string: {self.inStr}"

    def isPal(self):
        t = re.findall(r'[a-z0-9]', self.inStr.lower())
        print(t)
        print(len(t))
        i = 0
        j = len(t) - 1
        print(i,j)
        while i <= j:
            if t[i] != t[j]:
                return False
            i += 1
            j -= 1
            print(f"After: {i,j}")
        return True

    def uniqStr(self):
        res = []
        for c in self.inStr:
            if self.inStr.count(c) == 1:
                res.append(self.inStr.index(c)+1) # 1 based index
        if res:
            return res
        return -1

s = Playstr("A man, a plan, a canal: Panama")
if s.isPal():
    print('Pass')

u = Playstr("statistics")
print('s:',s.uniqStr())
