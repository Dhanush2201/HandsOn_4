def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
def debug_fib():
    n = int(input("Enter the value of n: "))  
    print(f"Calling fib({n})")
    result = fib(n)
    print(f"fib({n}) = {result}")
    return result
debug_fib()