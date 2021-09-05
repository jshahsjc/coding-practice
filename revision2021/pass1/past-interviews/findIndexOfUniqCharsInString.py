"""
Asked in Aviatrix first coding screen:
Given a string i.e.: 'statistics',
return list of indices of uniq characters with 1 based index: [3, 9] for a and c
if no uniq chars in the string, return -1
"""

def findUniqChars(input_str):
    res = []
    keep = {}
    for s in input_str:
        if s not in keep:
            keep[s] = 1
        else:
            keep[s] += 1
    for i, s in enumerate(input_str):
        if keep[s] == 1:
            res.append(i + 1)
    if not res:
        return -1
    return res
