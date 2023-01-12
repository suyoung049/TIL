import sys
sys.stdin = open('8_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

line = []

for _ in range(n):
    a = int(input())
    line.append(a)

start, end = 0, max(line)

while True:
    if start > end:
        break
    
    else:
        count = 0
        mid = (start + end)//2

        for i in line:
            if i >= mid:
                count += i//mid

        if count >= m:
            start = mid +1
        
        else:
            end = mid - 1

print(end)