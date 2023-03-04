import sys
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline

width, higth = map(int, input().split())

n = int(input())

width_li = [0]
higth_li = [0]

width_li.append(higth)
higth_li.append(width)



for _ in range(n):
    a, b = map(int, input().split())

    if a == 0:
        width_li.append(b)
    else:
        higth_li.append(b)

width_li.sort()
higth_li.sort()

max_with = 0
max_hight = 0

for i in range(len(width_li) -1 ):
    max_with = max(max_with, (width_li[i+1] - width_li[i]))

for j in range(len(higth_li)-1):
    max_hight = max(max_hight, (higth_li[j+1]-higth_li[j]))

print(max_hight * max_with)