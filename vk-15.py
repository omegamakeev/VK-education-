cache = {}

def fib(n):
    if n in cache:
        return cache[n]
    elif n <= 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    cache[n] = result
    return result

n = int(input())
print(fib(n))