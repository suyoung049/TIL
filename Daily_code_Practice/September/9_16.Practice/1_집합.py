import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
S = set()
for _ in range(n):
    command = input().split()
    if command[0] == 'add':
        if command[1] in S:
            continue
        else:
            S.add(command[1])

    if command[0] == 'check':
        if command[1] in S:
            print('1')
        else:
            print('0')
    
    if command[0] == 'remove':
        if command[1] in S:
            S.remove(command[1])
        else:
            continue
    
    if command[0] == 'toggle':
        if command[1] in S:
            S.remove(command[1])
        
        else:
            S.add(command[1])

    if command[0] == 'all':
        S = {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'}

    if command[0] == 'empty':
        S = set()


