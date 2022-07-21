a = input()
n = int(a)
sum = 0
for i in range(0, n+1):
    sum += i
    i += 1
    if sum >= n:
        break
print(sum)