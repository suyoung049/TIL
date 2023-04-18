import sys
sys.stdin = open("3_input.txt", 'r')


n = int(input())

first = list(input())

len_ = len(first)

for _ in range(n-1):
    second = list(input())

    for i in range(len_):
        if first[i] != second[i]:
            first[i] = '?'

print("".join(first))