def factorial(N):
    if  N == 0:
        return 1
    return N * factorial(N-1)

n , k = map(int, input().split())

print(factorial(n)//(factorial(k) * factorial(n-k)))