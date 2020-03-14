def dupInList(A):
   uniqList = []
   dupList = []
   for x in A:
      if x not in uniqList:
         uniqList.append(x)
      elif x not in dupList:
         dupList.append(x)
   return [uniqList, dupList]

t = 'hey I am a rockstar , rockstar am I not'
LT = t.split()
print "Uniq words in given sentence:" +str(dupInList(LT)[0])
print "Repeated words in given sentence:" +str(dupInList(LT)[1])
