import sys
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

num_list = list(map(int, input().split()))

time = sum(num_list)
sr_time = sorted(num_list)
for _ in range(n-1):
    sr_time.pop()
    a = sum(sr_time)

    time += a

print(time)    
