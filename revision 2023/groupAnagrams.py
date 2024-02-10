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

from collections import defaultdict

def groupAnagrams(inList):
    keep = defaultdict(list)
    for i in range(len(inList)):
        keep[tuple(sorted(inList[i]))].append(inList[i])
    return keep.values()
