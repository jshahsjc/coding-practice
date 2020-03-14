def OddEven(N):
   if N % 2 == 0:
      return "Entered number %d is Even"%N
   else:
      return "Entered number %d is Odd"%N

print OddEven(10)
print OddEven(int(raw_input("Enter a number:")))
