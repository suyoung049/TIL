import sys
sys.stdin = open('1_input.txt', "r")
input = sys.stdin.readline

n, m = map(int, input().split())

num_li = list(map(int, input().split()))

right_point, left_point = 0, 0
min_length = sys.maxsize
sum_num = 0

while True:
    if sum_num >= m:
        min_length = min(min_length, right_point-left_point)
        sum_num = sum_num - num_li[left_point]
        left_point += 1
    
    elif right_point == n:
        break

    else:
        sum_num += num_li[right_point]
        right_point += 1

if min_length == sys.maxsize:
    print(0)

else:
    print(min_length)