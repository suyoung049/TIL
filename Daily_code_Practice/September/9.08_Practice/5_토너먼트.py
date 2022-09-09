import sys
sys.stdin = open('5_input.txt', 'r')

T = int(input())

for test_case in range(1,T+1):


    winner = []

    n = int(input())

    n = (2**n)

    people = list(map(int, input().split()))
    score = 0
    while len(people) > 1:
        for i in range(0,len(people),2):
            if people[i] > people[i+1]:
                winner.append(people[i])

            else:
                winner.append(people[i+1])

            score += abs(people[i] - people[i+1])

        people = winner
        winner = []
    print(f'#{test_case} {score}')



