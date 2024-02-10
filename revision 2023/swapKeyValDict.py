"""
Given a dictionary, swap the keys and values.
"""
from collections import defaultdict

def swapKeyVal(testDict):
    res = defaultdict(list)
    for k,v in testDict.items():
        try:
            res[v].append(k)
        except typeError as e:
            return str(e)
    return res
