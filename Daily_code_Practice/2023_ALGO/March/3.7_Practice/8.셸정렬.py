import sys
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

n = int(input())   


num_li = []

for _ in range(n):
    num_li.append(int(input()))


def shell_sort():
    h = 1

    while h < n//9:
        h = (h * 3) + 1
    
    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = num_li[i]
            while j >= 0 and num_li[j] > tmp:
                num_li[j + h] = num_li[j]
                j -= h
            num_li[j + h] = tmp
        
        h //=3

shell_sort()

for i in num_li:
    print(i)