def nFactorial(n):
    if n > 1:
        return n * nFactorial(n - 1)
    elif n == 1 or n == 0::
        return 1
    else:
        return -1
print nFactorial(5)
