import sys
sys.stdin = open('5_나이순정렬.txt')

N = int(input())

people = []

for _ in range(N):
    k, v =  input().split()
    people.append([k,v])
sr_people = sorted(people, key = lambda x:int(x[0]))
for i in sr_people:
    print(*i)