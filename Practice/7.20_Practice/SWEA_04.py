a = input()
n = int(a)
1 <= n <= 1000
i = 1
for i in range(1, n+1):
    if n % i == 0:
        print(i, end =' ')