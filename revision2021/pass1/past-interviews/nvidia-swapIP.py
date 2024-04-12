"""
str1 = '''
My PC1 Primary IP is 1.1.1.1 and Secondary IP is 2.2.2.2
My PC2 Primary IP is 3.1.1.1 and Secondary IP is 4.2.2.2
My PC3 Primary IP is 5.1.1.1 Secondary IP is 6.2.2.2
'''
"""

import re

def swapIps(inStr):
    p = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    tempStr = inStr.split('\n') # list of lines
    res = ""
   # print(tempStr)
    for line in tempStr:
        if line:
            # print(line)
            x = re.findall(p, line) # two ip addresses in a list
            # print(x)
            tempLine = line.split() # list of strings
            tempLine[tempLine.index(x[1])] = x[0]
            tempLine[tempLine.index(x[0])] = x[1]
            innerTempStr = " ".join(tempLine)
            res += innerTempStr + '\n'
    return res

print(swapIps(str1))
