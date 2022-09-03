import sys
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

start = {}
end = {}

for i in range(n):
    car_num = input().strip()
    start[i] = car_num


for i in range(n):
    car_num = input().strip()
    end[car_num] = i


count = 0

for i in range(1, n):
    for j in range(0, i):
        if end[start[j]] > end[start[i]]:
            count += 1
            break

print(count)