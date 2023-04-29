import sys
from collections import deque
sys.stdin = open("1_input.txt","r")

n = int(input())
rope = []

for _ in range(n):
    rope.append(int(input()))

rope.sort()

rope = deque(rope)

max_kg = 0
while True:
    if len(rope) == 0:
        break
    len_rope = len(rope)
    one_rope = rope.popleft()
    max_kg = max(max_kg, one_rope * len_rope)

print(max_kg)



    