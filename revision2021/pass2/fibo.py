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
