def nFactorial(n):
    while n > 0:
        res = n * nFactorial(n - 1)
    return res

print nFactorial(5)
