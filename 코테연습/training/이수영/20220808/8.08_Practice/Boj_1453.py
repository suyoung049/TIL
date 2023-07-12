comp = [0]*101
N = int(input())
n = list(map(int, input().split()))
coun = 0
for i in n:
    if comp[i-1] == 0:
        comp[i-1] = 1
    else:
        coun += 1
print(coun)

