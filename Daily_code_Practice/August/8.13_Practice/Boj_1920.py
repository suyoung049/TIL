import sys

sys.stdin = open("1920_input.txt", "r")

def binary_search(a, x):
    start = 0
    end = len(a) -1

    while start <= end:
        mid = (start + end) // 2
        if x == a[mid]:
            return 1
        elif x > a[mid]:
            start = mid +1
        else:
            end = mid -1
    return 0

N = int(input())

num_list = list(map(int, input().split()))
a = sorted(num_list)

M = int(input())

surch = list(map(int, input().split()))

for i in range(M):
    print(binary_search(a, surch[i]))