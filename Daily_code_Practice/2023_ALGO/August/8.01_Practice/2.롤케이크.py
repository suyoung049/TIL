import sys
sys.stdin = open("2_input.txt", "r")
input = sys.stdin.readline

cake = int(input())
people = int(input())

cake_li = [0] * (cake + 1)

ex_result = 0
real_result = 0
ex_idx = 0
real_idx = 0

for i in range(1, people+1):
    start, end = map(int, input().split())
    result = end - start
    if result > ex_result:
        ex_result = result
        ex_idx = i


    cnt = 0
    for k in range(start, end+1):
        if cake_li[k] != 0:
            continue
        cake_li[k] = i
        cnt += 1
    
    if real_result < cnt:
        real_result = cnt
        real_idx = i

print(ex_idx)
print(real_idx)