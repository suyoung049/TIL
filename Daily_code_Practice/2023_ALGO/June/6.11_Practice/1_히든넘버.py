import sys
sys.stdin = open("1_input.txt", "r")

n = int(input())

word = input()

hidden = ''
result = 0

for i in range(n):
    if word[i].isdigit():
        hidden += word[i]
    
    else:
        if hidden:
            if len(hidden) <= 6:
                result += int(hidden)
                hidden = ''
            else:
                hidden = ''
if hidden:
    result += int(hidden)

print(result)

