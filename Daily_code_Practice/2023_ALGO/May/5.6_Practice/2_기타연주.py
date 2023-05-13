import sys
sys.stdin = open("2_input.txt", "r")
input = sys.stdin.readline

n, p = map(int, input().split())

finger = [[] for _ in range(7)]

result = 0
for _ in range(n):
    line, flat = map(int, input().split())

    if len(finger[line]) == 0:
        finger[line].append(flat)
        result += 1
    
    else:
        while True:
            if len(finger[line]) == 0:
                finger[line].append(flat)
                result += 1
                break
            
            if finger[line][-1] < flat: 
                finger[line].append(flat)
                result += 1
                break
            
            elif finger[line][-1] == flat:
                break
            
            else:
                finger[line].pop()
                result += 1

print(result)