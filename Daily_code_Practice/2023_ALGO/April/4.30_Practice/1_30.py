import sys

# 30의 배수의 자리수의 모든 합은 3의 배수

thirty = list(input())
thirty.sort(reverse=True)
sum_thirty = 0

if "0" not in thirty:
    print(-1)

else:
    for i in range(len(thirty)):
        sum_thirty += int(thirty[i])
    
    if sum_thirty % 3 == 0:
        print("".join(thirty))
    else:
        print(-1)
