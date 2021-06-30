"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""
from collections import  defaultdict

def anagram_buckets(words):
    buckets = defaultdict(list)
    for word in words:
            buckets[tuple(sorted(word))].append(word)

    return buckets.values()

test = ["star", "rats", "car", "arc", "arts", "stars"]
print anagram_buckets(test)
