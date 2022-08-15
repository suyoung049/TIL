a,b,c = input().split(' ')
d = int(a)
e = int(b)
f = int(c)
if d > e :
    if d > f:
        print(d)
    else :
        print(f)
elif e < f:
    print(f)
else :
    print(e)