numbers = [1,2,3,4,6,7,8,0]

check = list(range(0,10))

answer = 0


for i in check:
    if i not in numbers:
        answer += i
print(answer)