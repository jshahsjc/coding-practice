"""
884. Uncommon Words from Two Sentences

A sentence is a string of single-space separated words where each word consists only of lowercase letters.
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]

Constraints:

1 <= s1.length, s2.length <= 200
s1 and s2 consist of lowercase English letters and spaces.
s1 and s2 do not have leading or trailing spaces.
All the words in s1 and s2 are separated by a single space.
"""
from collections import defaultdict
def uncommonWords(s1, s2):
    s1 = s1.split()
    s2 = s2.split()
    if len(s1) > len(s2):
        return uncommonWords(s2, s1)
    s1_dict = defaultdict()
    s2_dict = defaultdict()
    res = []
    for s in s1:
        if s not in s1_dict:
            s1_dict[s] = 1
        else:
            s1_dict[s] += 1
    for s in s2:
        if s not in s2_dict:
            s2_dict[s] = 1
        else:
            s2_dict[s] += 1
    for k in s1_dict:
        if s1_dict[k] == 1 and k not in s2:
            res.append(k)
    for k in s2_dict:
        if s2_dict[k] == 1 and k not in s1:
            res.append(k)
    return res
    #return [ k for k in s1 if s1[k] == 1 and k not in s2 ]
