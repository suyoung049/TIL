import sys
sys.stdin = open("1_input.txt")


n = int(input())

book_dic = dict()

for _ in range(n):
    book = input()

    if book in book_dic:
        book_dic[book] += 1

    else:
        book_dic[book] = 1

max = 0
sbook = dict(sorted(book_dic.items(), key = lambda x : (-x[1], x[0])))

for i in sbook:
    if sbook[i] > max:
        max = sbook[i]
        answer = i

print(answer) 
