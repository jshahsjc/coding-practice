"""
Given a dictionary, swap the keys and values.
"""
from collections import defaultdict

def swapKv(testDict):
    outDict = defaultdict(list)
    for k,v in swapKv.items():
        try:
            outDict[v].append(k)
        except typeError as e:
            return str(e)
    return outDict
