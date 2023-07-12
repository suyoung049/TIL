import sys

sys.stdin = open("1302_input.txt")

n = int(input())
book_list = {}
for _ in range(n):
    name = input()
    if name in book_list:
        book_list[name] += 1
    else:
        book_list[name] = 1
max = 0
sbook = dict(sorted(book_list.items()))
for i in sbook:
    if(sbook[i]) > max:
        max = sbook[i]
        maxi = i
print(maxi)
print(sbook)

# sorted(result.items(), key = lambda x : (-x[1], x[0])) 
# # -x[1] 은 벨류값을 내림차순 # x[0] 은 키값을 오름차순

#  sorted(a.key(), reverse=True)
#  sorted(a.key())
#  key만 정렬된 값 반환  ['a', 'c', 'e']

# sorted(a.items())                                                                                                                           
# key와 value를 튜플로 묶어서 정렬된 값 반환  [('a',2), ('c',4), ('e'.2)] 

# sorted(a.items(), key=lambda x: x[0])
# x[0]은 key값을 기준으로 정렬하는 것을 의미함

# sorted(a.items(), key=lambda x: x[1]
# x[1]은 value값을 기준으로 정렬하는 것을 의미함


