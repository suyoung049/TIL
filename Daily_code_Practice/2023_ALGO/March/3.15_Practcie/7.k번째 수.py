import sys
sys.stdin = open('7_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
k = int(input())

num_list = []

for i in range(1,n+1):
    for j in range(1,n+1):
        num_list.append(i * j)

num_list.sort()
print(num_list[k])