def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        a,b = 0,1
        for _ in range (2,n+1):
            a,b = b,a+b
        return b
n = 10
print(fibonacci(n))

#
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Example usage:
n = 10  # Change this value for more or fewer numbers
print(f"The first {n} Fibonacci numbers are: {fibonacci(n)}")