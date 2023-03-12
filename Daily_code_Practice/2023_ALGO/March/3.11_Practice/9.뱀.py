import sys
sys.stdin = open('9_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

def pprint(list_):
    for row in list_:
        print(row)


