import sys
sys.stdin = open('13_input.txt', 'r')
input = sys.stdin.readline

T = int(input())
    

for test_case in range(T):
    num_list = list(map(int, input().split()))
    num_list.pop(0)

    aver = sum(num_list)/len(num_list)
    print(aver)
    people = 0

    for score in num_list:
        if score > aver:
            people += 1
        answer = (people/len(num_list)) * 100
        answer = round(answer, 3)
    a = "{:.3f}%".format(answer)
    print(a)
   
    
    

