lines = [[0, 4], [2, 5], [2, 8]]

fir = set(list(range(lines[0][0], lines[0][1] + 1 )))
sec = set(list(range(lines[1][0], lines[1][1] + 1 )))
thr = set(list(range(lines[2][0], lines[2][1] + 1 )))

a = len(fir & sec)
b = len(fir & thr)
c = len(sec & thr)
d = len(sec & fir & thr)



if a != 0:
    a -= 1
if b != 0:
    b -= 1
if c !=0:
    c -= 1
if d != 0:
    d -= 1

print(a,b,c,d)


answer = a + b + c - 2*d

print(answer)

