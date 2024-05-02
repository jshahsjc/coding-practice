"""
Given a string of numbers, with length between 4 and 12, find all possible valid ip addresses.
IN: "1111", OUT: ["1.1.1.1"]
IN: "100100100100", OUT: ["100.100.100.100",... other possible valid Ips]
"""
import ipaddress

def getIpCombinations(numStr):
    result = []
    for i in range(1, len(numStr) - 2):
        for j in range(i + 1, len(numStr) - 1):
            for k in range(j + 1, len(numStr)):
                temp = numStr[:k] + "." + numStr[k:]
                temp = temp[:j] + "." + temp[j:]
                temp = temp[:i] + "." + temp[i:]
                if ipaddress.ip_address(temp): # calling another function
                    result.append(temp)
                temp = numStr
    return numStr

def isValidIp(ipStr):
    ipCand = ipStr.split(".")
    if len(ipCand) != 4:
        return False
    for octet in ipCand:
        if 0 < int(octet) <= 255 and int(octet[0]) != 0:
            continue
        else:
            return False
    return True
