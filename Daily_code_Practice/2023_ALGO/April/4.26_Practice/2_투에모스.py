import sys
sys.stdin = open("2_input.txt", "r")
n = int(input())


toemos = [0, 0, 1, 1, 0]

if n <= 4:
    print(toemos[n])
check = True

for i in range(2, 61):
    if 2**i < n <= 2**(i+1):
        check = False
        
        count_ = 0
        while True:
            # 여기 로직이 잘못되어있음
            n = n - 2**i
            count_ += 1

            if 0< n <= 4:
                if toemos[n] == 0:
                    if count_ % 2 == 0:
                        print(0)
                        break
                    else:
                        print(1)
                        break
                else:
                    if count_ % 2 == 0:
                        print(1)
                        break
                    else:
                        print(0)
                        break
            i -= 1
    
    if check == False:
        break


