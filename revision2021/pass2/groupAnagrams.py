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


def anagram_buckets(words):
    buckets = {}
    for word in words:
        if sorted(word) not in buckets:
            buckets[sorted(word)] = [word]
        else:
            buckets[sorted(word)].append(word)

    return buckets

test = ["star", "rats", "car", "arc", "arts", "stars"]
print anagram_buckets(test)
