import sys
sys.stdin = open('10_input.txt', 'r')

minus = input().split('-')
num_ = []

for i in minus:
    sum_ = 0
    plus = i.split('+')

    for j in plus:
        sum_ += int(j)
    num_.append(sum_)

first = num_[0]

for k in range(1,len(num_)):
    first -= num_[k]

print(first)