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

def goatLatin(S):
    # convert the sentence into the list
    L = S.split()
    # create empty list to store values
    # This is important since the word 
    # or a string is an immutable object
    # Hence, we cannot update the word in place
    goatL = []
    print "L:", L
    # check for each word if it begins with a vowel
    V = "aeiouAEIOU"
    for n, word in enumerate(L):
        print "word0:", word[0]
        if word[0] in V:
            print "It's a vowel"
            goatWord = word + "ma" + (n+1)*"a"
        else:
            print "It's not a vowel"
            goatWord = word[1:] + word[0] + "ma" + (n+1)*"a"

    	goatL.append(goatWord)

    return " ".join(goatL)

#test
inA = "I speak Goat Latin"
expectedGoatA = "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
actualGoatA = goatLatin(inA)
print "Expected:", expectedGoatA
print "Received:", actualGoatA
if expectedGoatA == actualGoatA:
    print "Success!"
else:
    print  "Awww !!"
