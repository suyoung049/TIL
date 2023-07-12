import sys

sys.stdin = open("10546_input.txt", "r")

mara = dict()
N = int(input())
for _ in range(N):
    k = input()
    if k in mara:
        mara[k] += 1
    else:
        mara[k] = 1
for _ in range(N-1):
    k = input()
    mara[k] -= 1

for k in mara:
    if mara[k] == 1:
        print(k)


