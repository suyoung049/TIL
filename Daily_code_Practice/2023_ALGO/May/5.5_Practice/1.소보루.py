import sys
sys.stdin = open("1_input.txt", 'r')
input = sys.stdin.readline

total, eat = map(int, input().split())
people = int(input())
people_li = []

for _ in range(people):
    eat_time = int(input())
    people_li.append(eat_time)

eat_bread = total-eat

cur_bread = 0
check = True
for cur_time in range(1000001):
    for idx in range(people):
        if cur_time % people_li[idx] == 0:
            cur_bread += 1
        
        if cur_bread >= eat_bread:
            check = False
            print(idx+1)
            break
    
    if check == False:
        break

            
    

