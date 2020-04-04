def power(x, n):
   def helper(x, n):
      if n == 0:
         return 1.0
      temp = power(x, n // 2)
      if n % 2 == 0:
         return temp * temp
      else:
         return temp * temp * x

   if n < 0:
      return 1.0 / helper(x, -n)  #make sure to use 1.0 otherwise this will fail
   else:
      return helper(x, n)

# Driver Code
x, y = 2, -3
print('%f' %(power(x, y)))
