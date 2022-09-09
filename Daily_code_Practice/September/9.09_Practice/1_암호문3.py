import sys
sys.stdin = open('1_input.txt', 'r')
for test_case in range(1, 11):
    origin_len = int(input())
    origin_list = list(map(int, input().split()))

    command_len = int(input())
    command_list = input().split()
    
    i = 0

    while i < len(command_list):
        if command_list[i] == 'I':
            x = int(command_list[i+1])
            y = int(command_list[i+2])

            number_list = command_list[i+3: i+3+y]  # [3, 8]
            for number in number_list[::-1]:
                origin_list.insert(x, int(number))
        
        if command_list[i] == 'D':

            x = int(command_list[i+1])
            y = int(command_list[i+2])

            for _ in range(y):
                del(origin_list[x])

        

        if command_list[i] == 'A':

            y = int(command_list[i+1])

            num_list = command_list[i+2: i+2+y]

            for num_ in num_list:
                origin_list.append(int(num_))
        
        i = i +1 
    
    print(f'#{test_case}', *origin_list[:10])

    



