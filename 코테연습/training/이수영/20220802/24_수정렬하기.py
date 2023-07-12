import sys

sys.stdin = open("24_input.txt", "r")
input = sys.stdin.readline

N = int(input())
list_ = []
for _ in range(N):
    list_.append(int(input()))
sor_list = sorted(list_)

for i in sor_list:
    print(i)

