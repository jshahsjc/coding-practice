def nFactorial(n, res = 0):
    while n > 0:
        res = n * nFactorial(n - 1)
    return res

print nFactorial(5)
