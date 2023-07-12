import sys

sys.stdin = open("1764_input.txt", "r")
N, M = map(int, input().split())
no_listen = dict()

for i in range(N):
    people = input()
    no_listen[people] = 'nolisten'

no_listen_see = []
for j in range(M):
    people = input()
    if people in no_listen:
        no_listen_see.append(people)
so_ = no_listen_see.sort

print(len(no_listen_see))
for k in range(len(no_listen_see)):
    print(no_listen_see[k])

