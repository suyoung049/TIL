import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())

sin_li = [(0, 0, 1)]

for _ in range(n):
    y, x, z = map(int, input().split())
    sin_li.append((y, x, z))

sin_li.append((m, 0, 1))

cnt = 0

for i in range(1, len(sin_li)):
    (d, r, g) = sin_li[i]

    cnt += d - sin_li[i-1][0]

    time = 0

    if r - (cnt % (r + g)) < 0 :
        time = 0

    else:
        time = r - (cnt %(r+g))
    
    cnt += time
    

print(cnt)