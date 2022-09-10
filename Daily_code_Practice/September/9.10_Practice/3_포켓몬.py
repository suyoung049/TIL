import sys
sys.stdin = open('3_input.txt', 'r')


input = sys.stdin.readline

n, m = map(int, input().split())

poketmon = {}

for i in range(1,n+1):
    x = input().strip()

    poketmon[i] = x
    poketmon[x] = i

for _ in range(m):
    command = input().strip()

    if command.isdigit() == True:
        print(poketmon[int(command)])

    else:
        print(poketmon[command])