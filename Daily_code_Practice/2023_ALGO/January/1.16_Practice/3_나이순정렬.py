import sys
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

man = []

for _ in range(n):
    age, name = input().split()
    age = int(age)
    man.append((age,name))

man = sorted(man, key=lambda x:x[0])

for i in man:
    print(*i)