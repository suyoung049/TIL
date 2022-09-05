import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

T = int(input())

for test_case in range(1, T+1):
    count = 0
    
    text = list(map(int, input().strip()))
    data = [0] * len(text)

    for i in range(len(text)):
        if data[i] != text[i]:
            if data[i] == 0:
                value = 1
            
            else:
                value = 0
        
            for j in range(i, len(text)):
                data[j] = value
            count += 1

        if text == data:
            break

    print(f'#{test_case} {count}')

   