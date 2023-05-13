import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

n = int(input())

load_li = list(map(int, input().split()))
oil_li = list(map(int, input().split()))

i = 0
cost = 0

while True:
    if oil_li[i] > oil_li[i+1]:
        cost += load_li[i]*oil_li[i]
        i += 1
    
    elif oil_li[i] <= oil_li[i+1]:
        temp = oil_li[i]
        while True:
            cost += temp*load_li[i]
            i += 1
            
            if temp > oil_li[i]:
                break
            
            if i == n-1:
                break
    
    if i == n-1:
        break

print(cost)