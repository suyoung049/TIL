import sys

sys.stdin = open("2495_input.txt", "r")

for _ in range(3):
    num_list = list(input())
    coun = 0
    
    for i in range(len(num_list)-1):
        start = num_list[i]

        num_coun = 1
        for j in range(i+1,len(num_list)):
            if start != num_list[j]:
                break
            if start == num_list[j]:
                num_coun += 1

        coun = max(coun, num_coun)
    print(coun)
        
