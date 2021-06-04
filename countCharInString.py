def countCharAlt(S):
   result = {i:S.count(i) for i in set(S)}
   return result

def charOccurance(S):
   res = {}
   for k in S:
      if k in res:
         res[k] += 1
      else:
         res[k] = 1
   return res

def maxCharOccurance(S):
   resDict = charOccurance(S)
   maxChar, maxCount = '', 0
   for k, v  in resDict.items():
      if v > maxCount:
         maxChar, maxCount = k, v
   return maxChar, maxCount

def repeatedChars(S):
    resDict = charOccurance(S)
    repeatChars = ''
    for k, v in resDict.items():
        if v > 1:
            repeatChars += k
    if len(repeatChars) > 0:
        return repeatChars
    else:
        return 'No repeated characters found.'

myStr = "anthony gonzalvis"
resDict = charOccurance(myStr)
print "All characters occurance: \n"+str(resDict)
resTuple = "Highest occurred character: \n"+str(maxCharOccurance(myStr))
print resTuple
