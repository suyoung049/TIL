import sys
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

a = int(input())
b = input()

for i in range(2,-1,-1):
    answer = a * int(b[i])
    print(answer)

print(a*int(b))
    



    
    