a, b = input().split()
a = int(a)
b = int(b)
c = bool(int(a))
d = bool(int(b))
print(not(c) and not(d)) # Not(c or d)