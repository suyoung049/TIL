import sys
sys.stdin = open('3_input.txt', 'r')
from collections import deque
from itertools import combinations
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n = int(input())

school = [list(input().split()) for _ in range(n)]

def watch(y, x, direction):
    
    if direction == 0:
        while y >= 0:
            if school[y][x] == 'S':
                return True
            if school[y][x] == 'O':
                return False
            y -= 1
    
    if direction == 1:
        while y < n:
            if school[y][x] == 'S':
                return True
            if school[y][x] == 'O':
                return False
            y += 1
    
    if direction == 2:
        while x >= 0:
            if school[y][x] == 'S':
                return True
            if school[y][x] == 'O':
                return False
            
            x -= 1

    if direction == 3:
        while x < n:
            if school[y][x] == 'S':
                return True
            if school[y][x] == 'O':
                return False
            
            x += 1
    
    return False
    
    
def process():
    for y, x in teach_li:
        for i in range(4):
            if watch(y, x, i):
                return True
    return False


empty_li = []
teach_li = []
for j in range(n):
    for i in range(n):
        if school[j][i] == 'X':
            empty_li.append((j,i))
        elif school[j][i] == 'T':
            teach_li.append((j,i))
   

answer = False
for wall in combinations(empty_li, 3):
    for w in wall:
        school[w[0]][w[1]] = 'O'
    
    result = process()

    if not result:
        answer = True
        break

    for w in wall:
        school[w[0]][w[1]] = 'X'

if answer:
    print('YES')
else:
    print('NO')





    
