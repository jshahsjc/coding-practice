'''
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > Null, where Null is defined as the blank character which is less than any other character (More info).

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
'''

def alienDictCheck(words, order):
    # result bool
    isSorted = True
    # Build order dictionary
    orderDict = {}
    i = 1
    for char in order:
        if char not in orderDict:
            orderDict[char] = i
        i += 1
    # Start comparing word
    for num in len(words) - 1:
        w1 = words[num]
        w2 = words[num + 1]
        tLen = min(len(w1), len(w2))
        if w1[:tLen] == w2[:tLen] and  len(w1) > len(w2):
            return False
        else:
            for t in range(tLen):
                if orderDict[w1[t]] > orderDict[w2[t]]:
                    return False
    return isSorted

#Test
words = ["apple", "app"]
order = "abcdefghijklmnopqrstuvwxyz"

if alienDictCheck:
    print words, "are sorted based on:", order
else:
    print "Not sorted."
