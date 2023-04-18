import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

time = int(input())

button_li = [300, 60, 10]
push_li = []

for button in button_li:
    if time < button:
        push_li.append(0)
    
    else:
        push_li.append(time//button)
        time = time%button
    
if time != 0:
    print(-1)
else:
    print(*push_li)