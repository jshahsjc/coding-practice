def nFactorial(n, res = 0):
    while n > 1:
        res = n * nFactorial(n - 1)
    else:
        if n == 1 or n == 0:
            res = 1
    return res

print nFactorial(5)
