"""
A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.

If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".

Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin.



Example 1:

Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
Example 2:

Input: "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
"""

"""
1. break the sentense into an enumerate list
2. for each word, check the first letter
   if the first letter is a vowel, + 'ma'
   elif it's a constant, word = word[1:] + word[:1] + 'ma' + 'a'* (index of word)
3. join the list back with a single space
"""

def goat_latin(S):
   words = S.split()
   for index, value in enumerate(words, start=1):
      if value[0] not in 'aeiou':
         words[index-1] = value[1:] + value[0] + 'ma' + 'a'*index
      else:
         words[index-1] = value + 'ma' + 'a'*index

   return " ".join(words)

S1 = 'I speak Goat Latin'
S2 = 'The quick brown fox jumped over the lazy dog'
print goat_latin(S2)
if goat_latin(S2) == 'heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa':
   print 'pass'
