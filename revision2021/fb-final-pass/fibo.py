def fibo(n):
    def fibo_mem(num, fib_cache):
        if num in fib_cache:
            return fib_cache[num]
        val = fibo_mem(num - 1, fib_cache) + fibo_mem(num - 2, fib_cache)
        fib_cache[num] = val
        return val
    fib_cache = { 1:1, 2:1 }
    return fibo_mem(n, fib_cache)
