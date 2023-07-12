import sys

sys.stdin = open("2857_input.txt", "r")
agent = []
fbi = []
for _ in range(5):
    agent.append(input())
for i in range(len(agent)):
    if 'FBI' in agent[i]:
        fbi.append(i+1)

if not fbi:
    print('HE GOT AWAY!')
else:
    for i in fbi:
        print(i, end = ' ')
        