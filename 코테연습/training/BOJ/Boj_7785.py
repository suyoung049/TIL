import sys

sys.stdin = open("7785_input.txt", "r")
input = sys.stdin.readline
N = int(input())
logs = dict()
status_enter = []
for i in range(N):
    K, V = input().split()
    logs[K] = V
print(logs)
for key in logs:
    if logs[key] == 'enter':
        status_enter.append(key)
so_ = status_enter.sort(reverse = True)
for name in status_enter:
    print(name)
