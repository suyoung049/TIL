import sys
sys.stdin = open("1_input.txt","r")


while True:
    try:

        sentence = input()

        check_li = [0, 0, 0, 0]

        for chr in sentence:
            if chr.islower() == True:
                check_li[0] += 1
            
            if chr.islower() == False and chr != " ":
                if chr.isdigit() == False:
                    check_li[1] += 1
            
            if chr.isdigit() == True:
                check_li[2] += 1
            
            if chr == " ":
                check_li[3] += 1
        
        print(*check_li)

    except:
        break


