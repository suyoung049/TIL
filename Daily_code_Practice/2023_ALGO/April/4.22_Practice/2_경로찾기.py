import sys
sys.stdin = open("2_input.txt", "r")

def pprint(list_):
    for row in list_:
        print(row)

n, k = map(int, input().split())

binary = []
hamming = [[0] * n for _ in range(n)]


for _ in range(n):
    binary.append(input())

start, end = map(int, input().split())

for j in range(n-1):
    for i in range(j, n):
        count_ = 0
        for x in range(k):
            if binary[j][x] != binary[i][x]:
                count_ += 1

        hamming[j][i] = count_
        hamming[i][j] = count_

pprint(hamming)

# answer = []
# def search(y):
#     global answer
#     print(y)
#     if y == start:
#         return y

#     for i in range(n):
#         if hamming[y][i] == 1:
#             search(i)


# for i in range(n):
#     if hamming[end][i] == 1:
#         search(i)