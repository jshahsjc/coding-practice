def sumElements(L):
   sum = 0
   for k in L:
      sum = sum + k
   return sum

t = [1, 2, 5, 8]
tsum = sumElements(t)
print "sum of elements: " + str(tsum)
