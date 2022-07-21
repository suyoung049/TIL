d = []
for i in range(20):
    d.append([])
    for j in range(20):  # 리스트 안에 다른 리스트 추가해 넣기
        d[i].append(0)     #리스트 안에 들어있는 리스트에 0추가해 넣기

n = int(input())
for i in range(n):
    x, y = input().split()
    d[int(x)][int(y)] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end = ' ')
    print() 

d = []
for i in range(20):   
    d.append([])
    for j in range(20):    #[0 for j in range(20)]
        d[i].append(0)

 # d = [0 for j in range(20)] for i in range(20)]