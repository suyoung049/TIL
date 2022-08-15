import sys

sys.stdin = open("11651_input.txt", "r")

T = int(input())
code_list = []
for _ in range(T):
    a, b = map(int, input().split())
    code_list.append((b,a))
sr_code_list = sorted(code_list)

for a, b in sr_code_list:
    print(b,a)
