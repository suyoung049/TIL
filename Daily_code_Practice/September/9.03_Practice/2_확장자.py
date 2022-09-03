import sys
sys.stdin = open('2_input.txt', 'r')


n = int(input())

list_ = []  # 파일명.확장자
dict_ = {}  # 확장자 

for _ in range(n):
    list_.append(input())

for file in list_:
    a, b = file.split('.')
    print(a, b)

    if b in dict_:
        dict_[b] += 1

    else:
        dict_[b] = 1

sr_dict_ = sorted(dict_.items())

for i in sr_dict_:
    print(*i)


# from collections import Counter
# n=int(input())
# name=[]
# for _ in range(n):
#     name.append(list(input().split('.'))[1])

# name=Counter(name)
# name=sorted(name.items(), key=lambda x: x[0])

# for i,j in name :
#     print(i,j)

    