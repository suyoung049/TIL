import sys
sys.stdin = open('11_input.txt', 'r')

max_ = 0

for i in range(9):
    num_ = int(input())

    if num_ > max_:
        max_ = num_
        count = i+1
print(max_)
print(count)
