import sys

sys.stdin = open("02_input.txt", "r")
T = int(input())
n = 0
for test_case in range(1, T +1):
    numbers = list(map(int, input().split()))
    sum = 0
    count = 0
    n += 1
    for i in numbers:
        sum += i
        count += 1
        result = round(sum/count)
        
    print(f"#{n} {result} ")