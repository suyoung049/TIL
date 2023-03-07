import sys
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

n = int(input())   


num_li = []

for _ in range(n):
    num_li.append(int(input()))



def select_sort():
    for i in range(n-1):
        min = i

        for j in range(i+1, n):
            if num_li[j] < num_li[min]:
                min = j
        num_li[i], num_li[min] = num_li[min], num_li[i]

select_sort()

for i in num_li:
    print(i)