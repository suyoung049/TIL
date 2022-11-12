import sys
sys.stdin = open('3_input.txt', 'r')

T = int(input())

for test_case in range(1, T +1):
    (s_1, s_2) = (0, 0)
    text_1, text_2 = input().split()

    if len(text_1) < len(text_2):
        text_1 = text_2
        text_2 = text_1    
    
    
    if text_1 == text_2:
        print('yes')
    
    else:
        x = len(text_1)

        for i in range(1, (x//2)+1):
            s = text_1[0:i]
            count = int(x/i)

            if (s*count == text_1):
                s_1 = s
                break
        if s_1 == text_2:
            print('yes')
        
        else:
        
            x_2 = len(text_2)

            for i in range(1, (x_2//2)+1):
                s = text_2[0:i]
                count = int(x_2/i)

                if (s*count == text_2):
                    s_2 = s
                    break

            if s_1 and s_2:
                if s_1 == s_2:
                    print('yes')
                else:
                    print('no')
            
            else:
                print('no')
            
            

    
