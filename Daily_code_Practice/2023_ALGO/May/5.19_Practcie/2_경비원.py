import sys
sys.stdin = open("2_input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())

store_li = []

store_count = int(input())

for _ in range(store_count):
    y, x = map(int, input().split())
    store_li.append((y,x))

me = list(map(int, input().split()))
result = 0

for store in store_li:
    if store[0] == 1:
        if me[0] == store[0]:
            result += abs(me[1] - store[1])

        if me[0] == 3:
            result += (me[1] + store[1])
        
        if me[0] == 4:
            result += (me[1] + n-store[1])
        
        if me[0] == 2:
            temp = min((me[1] + store[1]), (n-me[1] + n-store[1]))
            result += (temp + m)
    
    if store[0] == 2:
        
        if me[0] == store[0]:
            result += abs(me[1] - store[1])
        
        if me[0] == 3:
            result += (me[1] + m-store[1])
        
        if me[0] == 4:
            result += (n-me[1] + m- store[1])
        
        if me[0] == 1:
            temp = min((me[1] + store[1]), (n-me[1] + n-store[1]))
            result += (temp + m)
    
    if store[0] == 3:
        if me[0] == store[0]:
            result += abs(me[1] - store[1])
        
        if me[0] == 1:
            result += (me[1] + store[1])
        
        if me[0] == 2:
            result += (me[1] + m-store[1])
        
        if me[0] == 4:
            temp = min((me[1] + store[1]),(m-me[1] + m-store[1]))
            result += temp + n
    
    if store[0] == 4:
        if me[0] == store[0]:
            result += abs(me[1] - store[1])
        
        if me[0] == 1:
            result += (me[1] + n-store[1])
        
        if me[0] == 2:
            result += (n-store[1] + m - me[1])
        
        if me[0] == 3:
            temp = min((me[1] + store[1]), (n-me[1] + n-store[1]))
            result += (temp + m)

print(result)





