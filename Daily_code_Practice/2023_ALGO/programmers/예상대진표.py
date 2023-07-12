(n, a, b) = (8, 4, 7)

answer = 0
while True:
    if abs(a-b) == 1 and min(a,b) %2 != 0:
        answer += 1
        break
    
    else:
        if a % 2 != 0:
            a = a + 1
        
        if b % 2 != 0:
            b = b + 1

        a = a//2
        b = b//2

        answer += 1

print(answer)

