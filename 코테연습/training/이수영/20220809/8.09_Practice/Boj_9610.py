import sys

sys.stdin = open("9610_input.txt", "r")

N = int(input())
dict_ = {'Q1':0, 'Q2':0, 'Q3':0, 'Q4':0, 'AXIS': 0}
for _ in range(N):
    x, y = map(int, input().split())

    if x > 0 and y > 0:
        dict_['Q1'] += 1
    elif x > 0 and y < 0:
        dict_['Q4'] += 1
    elif x < 0 and y > 0:
        dict_['Q2'] += 1
    elif x <0 and y < 0:
        dict_['Q3'] += 1
    else:
        dict_['AXIS'] += 1
for i in dict_:
    print(f'{i}: {dict_[i]}')