import sys

sys.stdin = open("12_덩치.txt")

people_number = int(input())
people_list = []
for i in range(people_number):
    x, y = map(int, input().split())
    people_list.append((x, y))

print(people_list)

for j in people_list:
    rank = 1
    for k in people_list:
        if j[0] < k[0] and j[1] < k[1]:
            rank += 1
    print(rank, end = ' ')


    
