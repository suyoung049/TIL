import sys
sys.stdin = open("4_input.txt", "r")
input = sys.stdin.readline

num_list = list(map(int, input().split()))

for i in range(1, len(num_list)):

    for j in range(i, 0, -1):
        if num_list[j] < num_list[j-1]:
            temp = num_list[j]
            num_list[j] = num_list[j-1]
            num_list[j-1] = temp

print(num_list)