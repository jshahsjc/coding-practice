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

def groupAnagrams(strs):
    keep = defaultdict(list)
    for str in strs:
        keep[sorted(str)].append(str)

    return keep.values()
