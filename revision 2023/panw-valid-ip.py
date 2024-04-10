def validIp(inStr):
     """
     IN: "100.100.100.100"
     """
     testList = inStr.split(".")
     if len(testList) != 4:
             return False
     for val in testList:
             if 0 <= int(val) <= 255 and val[0] != "0":
                     continue
             else:
                     return False
     return True

def getIpCombinations(inStr):
	"""
    IN: "1111"
    IN: "100.100.100.100"
	"""
	outList = []
	for i in range(1, len(inStr) - 2):
		for j in range(i + 1, len(inStr) - 1):
			for k in range(j + 1, len(inStr)):
				outStr = inStr[:k] + "." + inStr[k:]
				outStr = outStr[:j] + "." + outStr[j:]
				outStr = outStr[:i] + "." + outStr[i:]
				if validIp(outStr):
					outList.append(outStr)
				outStr = inStr
	return outList
