import sys
sys.stdin = open("2_input.txt", "r")


word = input()

word_dic = {}

for chr in word:
    if chr not in word_dic:
        word_dic[chr] = 1
    else:
        word_dic[chr] += 1

odd_check = False
word_check = False
for chr in word_dic:
    
    if word_dic[chr] %2 != 0:
        if odd_check == False:
            odd_check = True
        else:
            print("I'm Sorry Hansoo")
            word_check = True
            break
        
if word_check == False:
    temp = ''
    answer = ''
    sort_word = dict(sorted(word_dic.items(), key = lambda x : x[0]))
    for chr in word_dic:
        if word_dic[chr] == 1:
            temp = chr
        
        else:
            word_1 = chr * (word_dic[chr]//2)
            answer += word_1
    
    word_2 = answer[::-1]
    if temp != '':
        answer += temp
    answer += word_2

print(answer)
            
        

    