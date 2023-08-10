import sys
sys.stdin = open('1_input.txt', "r")
input = sys.stdin.readline

n = int(input())

box_li = []
max_high = 0

for _ in range(n):
    idx, high = map(int, input().split())
    if high > max_high:
        max_high = high
    
    box_li.append((idx,high))

box_li.sort()

anser = max_high
temp_high = 0
temp_idx = 0
for i in range(n):
    if i == 0:
        temp_high = box_li[i][1]
        temp_idx = box_li[i][0]
        if temp_high == max_high:
            break

    else:
        if temp_high < box_li[i][1]:
            anser += (box_li[i][0] - temp_idx) * temp_high
            temp_idx = box_li[i][0] 
            temp_high = box_li[i][1]

            if temp_high == max_high:
                break

temp_high = 0
temp_idx = 0
for j in range(n-1, -1, -1):
    if j == n-1:
        temp_high = box_li[j][1]
        temp_idx = box_li[j][0]
        if temp_high == max_high: 
            break
    
    else:
        if temp_high < box_li[j][1]:
            anser += (temp_idx - box_li[j][0]) * temp_high
            temp_high = box_li[j][1]
            temp_idx = box_li[j][0]

            if temp_high == max_high:
                break
        
    


print(anser)