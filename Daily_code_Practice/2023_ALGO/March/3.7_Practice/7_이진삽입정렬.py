import sys
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

n = int(input())   

num_li = []

for _ in range(n):
    num_li.append(int(input()))


def binary_insert():
    for i in range(1, n):
        key = num_li[i]
        pl = 0
        pr = i -1

        while True:
            pc = (pl+pr)//2

            if num_li[pc] == key:
                break
            elif num_li[pc] < key:
                pl = pc + 1
            elif num_li[pc] > key:
                pr = pc - 1
            
            if pl > pr:
                break
        
        pd = pc + 1 if pl <= pr else pr + 1

        for j in range(i, pd, -1):
            num_li[j] = num_li[j-1]
        num_li[pd] = key
binary_insert()
for i in num_li:
    print(i)