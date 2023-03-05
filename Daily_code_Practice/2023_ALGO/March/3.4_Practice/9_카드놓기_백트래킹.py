import sys
sys.stdin = open('9_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
m = int(input())

card_list = []
for _ in range(n):
    card = int(input())
    card_list.append(card)

check = [False for _ in range(n)]
rs = set()
str_ = ''

def select(num_):
    global str_

    if num_ == m:
        rs.add(str_)
        return

    for i in range(n):
        if check[i] == False:
            check[i] = True
            
            str_ += str(card_list[i])
            select(num_ + 1)
            
            check[i] = False
            str_ = str(str_[:-len(str(card_list[i]))])

select(0)
print(len(rs))