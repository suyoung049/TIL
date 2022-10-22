import sys
sys.stdin = open('3_input.txt', 'r')


T = int(input())

for test_case in range(1, T+1):
    card = input()
    dec = len(card)//3
   
    s = []
    d = []
    h = []
    c = []

    for i in range(dec):
        card_n = card[(3*i):(3*(i+1))]
        num_ = card_n[-2:]
        num_ = int(num_)
        if card_n[0] == 'S':
            if num_ not in s:
                s.append(num_)
            else:
                s.append('error')
        if card_n[0] == 'D':
            if num_ not in d:
                d.append(num_)
            else:
                d.append('error')        
        if card_n[0] == 'H':
            if num_ not in h:
                h.append(num_)
            else:
                h.append('error')        
        if card_n[0] == 'C':
            if num_ not in c:
                c.append(num_)
            else:
                c.appned('error')
                
    print(f'#{test_case}', end = ' ')
    
    if ('error' in s) or ('error' in d) or ('error' in h) or ('error' in c):
        print('ERROR')
    else:
        print(13-len(s), 13-len(d), 13-len(h), 13-len(c))
    
        
   

        
