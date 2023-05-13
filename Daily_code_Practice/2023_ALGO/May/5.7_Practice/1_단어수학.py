import sys
sys.stdin = open("1_input.txt", 'r')

n = int(input())

word_dic = {}


for _ in range(n):
    word_num = input()
    count_ = len(word_num) - 1
    for i in range(len(word_num)):
        if word_num[i] not in word_dic:
            word_dic[word_num[i]] = 1 * (10**(count_ - i))
            
        else:
            word_dic[word_num[i]] += 1 * (10 ** (count_ - i))
        
word_dic = sorted(word_dic.items(), key = lambda x : (-x[1], x[0]))

sum_ = 0
idx = 0

len_word = len(word_dic)

while True:
    sum_ += word_dic[idx][1] *(9 - idx)
    idx += 1

    if idx == len_word:
        break

print(sum_)


