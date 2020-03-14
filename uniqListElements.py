def uniqListElements(L):
   uniqL = []

   for k in L:
      if k not in uniqL:
         uniqL.append(k)
   return uniqL

t = [1, 2, 3, 3, 6, 6, 100, 100, 41]
print uniqListElements(t)
