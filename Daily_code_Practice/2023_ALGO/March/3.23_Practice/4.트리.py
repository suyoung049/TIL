import sys
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

def toPost_order(pre_order, in_order):
    if len(pre_order) == 0:
        return

    elif len(pre_order) == 1:
        print(pre_order[0], end=' ')
        return
    
    root_index = in_order.index(pre_order[0])

    left_in = in_order[0:root_index]
    left_pre = pre_order[1:len(left_in) + 1]
    toPost_order(left_pre, left_in)

    right_in = in_order[root_index+1:]
    right_pre = pre_order[len(left_pre) + 1:]
    toPost_order(right_pre, right_in)

    print(pre_order[0], end=' ')

T = int(input())

for _ in range(T):
    n = int(input())

    pre_order = list(map(int, input().split()))
    in_order = list(map(int, input().split()))

    toPost_order(pre_order, in_order)
    print()


