import sys

sys.stdin = open("10798_input.txt", "r")
data = [[0]*15 for i in range(5)]

for i in range(5):
    text = list(input())
    for j in range(len(text)):
        data[i][j] = text[j]
print(data)

for i in range(15):
    for j in range(5):
        if data[j][i] != 0:
            print(data[j][i], end = '')
        else:
            continue 