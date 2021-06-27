def nFactorial(n):
    while n > 1:
        return n * nFactorial(n - 1)
    else:
        if n == 1 or n == 0:
            return 1

print nFactorial(5)
