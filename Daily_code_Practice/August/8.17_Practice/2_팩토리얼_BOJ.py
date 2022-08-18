N = int(input()) # 10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 ....

def factorial(N):
    if N == 0 or N== 1:
        return 1
    return N * factorial(N-1)
print(factorial(N))