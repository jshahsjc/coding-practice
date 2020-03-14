# Find n! with recursion and integration
def recursion_factorial(n):
   if n < 0:
      return -1
   elif n == 0 or n == 1:
      return 1
   else:
      return n * recursion_factorial(n-1)

def iteration_factorial(n):
   if n < 0:
      return -1
   elif n == 0 or n == 1:
      return 1
   else:
      k =1
      for i in range(1,n+1):
         k = k * i
      return k

number = int(raw_input("what is the number ?"))
print ('recursive method: %d'%recursion_factorial(number))
print ('iterative method: %d'%iteration_factorial(number))
