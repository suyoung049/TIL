import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

n = int(input())

i = 2
while True:
    if n == 1:
        break

    if n % i == 0:
        print(i)
        n = n//i
    else:
        i += 1
    

    
