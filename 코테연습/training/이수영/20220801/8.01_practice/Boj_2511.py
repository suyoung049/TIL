import sys

sys.stdin = open("2511_input.txt", "r") 

a_card = list(map(int, input().split()))
b_card = list(map(int, input().split()))
a_bord = 0
b_bord = 0
history = 'D'

for i in range(10):
    if a_card[i] > b_card[i]:
        a_bord += 3
        history = 'A'
    if a_card[i] < b_card[i]:
        b_bord += 3
        history = 'B'
    if a_card[i] == b_card[i]:
        a_bord += 1
        b_bord += 1
if a_bord > b_bord:
    print(a_bord, b_bord)
    print('A')
if a_bord < b_bord:
    print(a_bord, b_bord)
    print('B')
if a_bord == b_bord:
    if history == 'A':
        print(a_bord, b_bord)
        print('A')
    if history == 'B':
        print(a_bord, b_bord)
        print('B')
    if history == 'D':
        print(a_bord, b_bord)
        print('D')      
    