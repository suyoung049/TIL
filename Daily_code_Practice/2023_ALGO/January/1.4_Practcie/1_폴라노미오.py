import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

bord = input()
answer = ""
stack = ""
fola = False

def check(j):
    global fola
    global answer
    global stack

    if j % 2 != 0:
        fola = True

    else:
        while True:
            if j >= 4:
                answer += "AAAA"
                j = j - 4
                if j == 0:
                    break
            else:
                answer += "BB"
                break
        stack = ''
                
for i in range(len(bord)):
    if bord[i] == ".":
        if stack:
            x = len(stack)
            check(x)
            answer += "."

        else:
            answer += "."

    else:
        stack += bord[i]

if stack:
    x = len(stack)
    check(x)

if fola:
    print(-1)
else:
    print(answer)