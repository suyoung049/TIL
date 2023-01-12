import sys
sys.stdin = open('4_input.txt', 'r')
from itertools import combinations
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

n, m = map(int, input().split())
bag = [[0,0]]
value = [[0] * (m+1) for _ in range(n+1)]
print(value)

for _ in range(n):
    a, b = map(int, input().split())
    bag.append([a,b])

for j in range(n+1):
    for i in range(m+1):
        w = bag[j][0]
        v = bag[j][1]

        if i < w:
            value[j][i] = value[j-1][i]

        else:
            value[j][i] = max(v + value[j-1][i-w], value[j-1][i])

pprint(value)

# bag = []

# for _ in range(n):
#     a, b = map(int, input().split())
#     bag.append((a,b))

# result = 0
# for i in range(1, n+1):
#     for j in combinations(bag, i):

#         po = 0
#         value = 0

#         for k in j:
#             po += k[0]

#             if po <= m:
#                 value += k[1]
#                 result = max(result, value)

# print(result)

       

        