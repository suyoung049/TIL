n = 3848844
result = 0

n = n -1

for i in range(2, n+1):
    if n % i == 0:
        result = i
        break

print(result)