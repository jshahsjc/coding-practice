"""
Given a nested list,
input: [1, [2], [3]]
output: [1, 2, 3]
"""

# Solution is to use dfs
def flatNested(inList):
    res = []
    def dfs(l):
        for n in l:
            if isinstance(n, list):
                dfs(n)
            else:
                res.append(n)
    dfs(inList)
    return res
s = [1, [2], [3]]

print(flatNested(s))
