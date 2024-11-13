import sys
sys.stdin = open('1_input.txt', 'r')

# 입력
n = int(input())
arr = []
for _ in range(n):
    arr.append(input().strip())

max_size = 0
l = n
r = n

for i in range(n):
    for j in range(i+1, n):
        if arr[i] == arr[j]:
            continue
        length = min(len(arr[i]), len(arr[j]))
        temp = 0
        for k in range(length):
            if arr[i][k] != arr[j][k]:
                break
            temp += 1
        if temp > max_size:
            max_size = temp
            l = i
            r = j
        elif temp == max_size:
            if i < l or (i == l and j < r):
                l = i
                r = j

small = min(l, r)
big = max(l, r)
print(arr[small])
print(arr[big])