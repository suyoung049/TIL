import sys

sys.stdin = open("_퍼펙트셔플.txt")
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    card = list(input().split())
    shuffle = (N)//2
    shuffle_list = []
    print(f'#{test_case}', end = ' ')
    if N % 2 != 0:
        card_pop = card.pop(shuffle)
        for i in range (0, shuffle):
            shuffle_list.append(card[i])
            shuffle_list.append(card[i+shuffle])
        shuffle_list.append(card_pop)
    else:
        for i in range (0, shuffle):
            shuffle_list.append(card[i])
            shuffle_list.append(card[i+shuffle])
    print(*shuffle_list)
    




    
       
            