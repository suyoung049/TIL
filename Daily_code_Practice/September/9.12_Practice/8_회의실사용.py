import sys
sys.stdin = open('8_input.txt')
input = sys.stdin.readline

n = int(input())
table = []

for _ in range(n):
    x, y = map(int, input().split())

    table.append([x,y])


table.sort(key = lambda x: (x[1], x[0]))
# sr_table = sorted(table, key=lambda x: x[0])
# sr_table = sorted(sr_table, key=lambda x: x[1])
print(table)

coun = 1

end = table[0][1]

for i in range(1,n):
    if table[i][0] >= end:
        coun += 1
        end = table[i][1]

print(coun)
    
    