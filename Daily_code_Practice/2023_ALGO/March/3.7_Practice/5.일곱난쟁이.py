import sys
sys.stidn = open('5_input.txt', 'r')
input = sys.stdin.readline

small_li = []

for _ in range(9):
    small_li.append(int(input()))


small_li.sort()
tall_sum = sum(small_li)


for i in range(8):
    for j in range(i+1, 9):
        if tall_sum - small_li[i] - small_li[j] == 100:
            not_small = [small_li[i], small_li[j]]
        

for i in small_li:
    if i not in not_small:
        print(i)