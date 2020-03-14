def intersectLists(L1, L2):
   L3 = [value for value in L1 if value in L2]
   L1uniq = [ _ for _ in L1 if _ not in L3 ]
   L2uniq = [ _ for _ in L2 if _ not in L3 ]
   return [L3, L1uniq, L2uniq]

List1 = [1, 2, 3, 4, 5]
List2 = [4, 5, 6, 7, 8, 0, 9, 1]
res = intersectLists(List1, List2)[0]
List1uniq = intersectLists(List1, List2)[1]
List2uniq = intersectLists(List1, List2)[2]

print "shared elements in lists are:"+str(res)
print "uniq elements in List1 are:"+str(List1uniq)
print "uniq elements in List2 are:"+str(List2uniq)
