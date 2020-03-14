 a,b,fib = 0,1,[0,1]
#fib.append(a)
#fib.append(b)
def fibonacci(n):
   if n == 2:
      return
   else:
      global a,b #If we need to assign a new value to a global variable then we can do that by declaring the variable as global inside a function.
      a,b = b,a+b
      fib.append(b)
      fibonacci(n-1)
fib_len = int(raw_input("length of fib series ?"))
fibonacci(fib_len)
print fib
