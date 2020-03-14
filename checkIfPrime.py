def checkIfPrime(Num):
   prime = False
   if Num > 1:
      for i in range(2, Num):
         if Num % i == 0:
            print '%d Not a prime, divisible by %d'%(Num,i)
            break
      else:
         print '%d is a prime'%Num
         prime = True
   else:
      print '%d is not a prime, not greater than 1'%Num

   return prime

def findPrime(A):
   primeList = []
   for k in A:
      check = checkIfPrime(k)
      if check:
         primeList.append(k)

   return primeList


#InputNum = int(raw_input("enter a number:"))

#checkIfPrime(InputNum)

T = [1, 20 , 21, 107, 407, 510, 555, 1024, 13, 0, -2]

primes = findPrime(T)
print primes
