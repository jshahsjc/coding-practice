def fibo(n):
    fib = [ 0, 1 ]
    if n == 2:
        return fib
    if n <= 1:
        return 0
    for i in range(2, n):
        val = fib[i - 1] + fib[i - 2]
        fib.append(val)

    return fib
