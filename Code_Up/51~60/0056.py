a, b = input().split()
a = int(a)
b = int(b)
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or (not(c) and d))