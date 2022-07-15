a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a < b and a < c:
    print(a)
else:
    if b < c:
        print(b)
    else:
        print(c)