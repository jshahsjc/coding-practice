"""
Given a dictionary, swap the keys and values.
"""
from collections import defaultdict
def swapDictKeyVal(my_dict):
    res = defaultdict(list)
    for k, v in my_dict.items():
        try:
            res[v].append(k)
        except TypeError as e:
            return str(e)
    return res
