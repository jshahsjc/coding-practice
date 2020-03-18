"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.


Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""

"""
function1: check if given string is a pallindrome
function2: remove a character from given string
function3:
   for each character, remove it by function2,
   and check if the remaining string is a pallindrome by passing it into function1. return the character without which remaining string is a pallindrome. If no such character, return False.
"""

def check_if_pallindrome(S):
   pal = False
   i, j = 0, len(S)-1
   while i <= j:
      if S[i] == S[j]:
         i += 1
         j -= 1
         pal = True
      else:
         break
   return pal

# print check_if_pallindrome("wowatsiraristawo")

def pallindrome_after_char_removed(S):
   res = { k : v for k, v in enumerate(S) }
   for k, v in res.items():
      temp_str = ''
      for num in range(len(res)):
         if num is not k:
            temp_str = temp_str + res[num]
            print temp_str
      if check_if_pallindrome(temp_str):
         print "%s is pallindrome, after removing %s from %s." %(temp_str, v, S)
         return True
         # return pallindrome string and the removed character
         break
   else:
      print "%s cannot be a pallindrome with 1 char removed."%S
      return False


t = 'assaa'
print pallindrome_after_char_removed(t)
