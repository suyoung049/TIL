import sys
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

n, level_up = map(int, input().split())

character_level = []

for _ in range(n):
    level = int(input())
    character_level.append(level)

start = 1
end = max(character_level) + (level_up//n)

max_level = 0
while True:

    if start > end:
        break
        
    up = 0
    mid = (start + end)//2

    for character in character_level:
        if mid > character:
            up += (mid - character)
    
    if up > level_up:
        end = mid -1
    
    else:
        start = mid + 1
        max_level = mid

print(max_level)