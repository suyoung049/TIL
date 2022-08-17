import sys

sys.stdin = open('1_input.txt', 'r')

T = int(input())

month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]



for test_case in range(1, T+1):
    data = input()
    result = [data[:4]]
    print(f'#{test_case}', end = ' ')
    if int(data[4:6]) in month:
        result.append(data[4:6])
    else:
        print('-1')
        continue
    if -1 <= int(data[6:]) <= day[int(data[4:6])-1]:
        result.append(data[6:])
    else:
        print('-1')
        continue
    print('/'.join(result))