def fibo(N):
    fib = [0, 1]
    prevVal = 0
    currVal = 1
    for i in range(N - 2):
        nextVal = currVal + prevVal
        fib.append(nextVal)
        prevVal = currVal
        currVal = nextVal
    return fib

print fibo(5)



def fibo(n):
    keep = defaultdict()
    if n == 0:
        return 0
    if n == 1  or n == 2:
        return 1
    if n > 2:
        if n in keep:
            return keep[n]
        res = fibo(n - 1) + fibo(n - 2)
        keep[n] = res
        return res



def fibo(n):
    keep = defaultdict()
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    if n > 2:
        if n in keep:
            return keep[n]
        res = fibo(n - 1) + fibo(n - 2)
        keep[n] = res
        return res
