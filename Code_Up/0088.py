a, d, n = input().split()
a = int(a)
d = int(d)
n = int(n)
i = 0
while i < (n-1):
    a += d
    i += 1
print(a)