def findFactors(N):
   return [x for x in range(1,N+1) if N % x == 0]

print findFactors(20)
print findFactors(100)
