import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())

def pprint(list_):
    for row in list_:
        print(row)

origin = [list(map(int, input().strip())) for _ in range(n)]

change = [list(map(int, input().strip())) for _ in range(n)] 


pprint(origin)
pprint(change)