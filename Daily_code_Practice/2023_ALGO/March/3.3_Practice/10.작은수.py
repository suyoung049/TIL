import sys
sys.stdin = open('10_input.txt','r')

a, b = map(int, input().split())

num_list = list(map(int, input().split())) 

for num_ in num_list:
    if num_ < b:
        print(num_)