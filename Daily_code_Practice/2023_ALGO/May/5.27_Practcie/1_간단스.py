import sys
sys.stdin = open("1_input.txt", "r")


word = input()
n = int(input())

for i in range(len(word)):
    if i+1 == n:
        print(word[i])