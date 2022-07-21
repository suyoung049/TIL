a, m, d, n = input().split()
a = int(a)
m = int(m)
d = int(d)
n = int(n)
i = 0
while i < (n-1):
    a = (a*m) + d
    i += 1
print(a)