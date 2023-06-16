import sys
sys.stdin = open("2_input.txt", "r")


num_ = input()
coun_ = 0

if len(num_) == 1:
    print(coun_)
    if int(num_) % 3 == 0:
        print('YES')

    else:
        print("NO")
else:
    while True:
        sum_ = 0
        for i in num_:
            sum_ += int(i)
        
        coun_ += 1
        
        if len(str(sum_)) == 1:
            break
        
        else:
            num_ = str(sum_)

    print(coun_)

    if sum_ % 3 == 0:
        print('YES')

    else:
        print("NO")



