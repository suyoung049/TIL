import sys
sys.stdin = open("2_input.txt", "r")
input = sys.stdin.readline

n = int(input())

def divide(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    
    elif i % 2 == 0:
        return divide(i//2)
    else:
        return 1 - divide(i//2)


print(divide(n-1))