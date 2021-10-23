def factorial(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return factorial(n - 1) + factorial(n - 2)

n = int(input())
print(factorial(n))
