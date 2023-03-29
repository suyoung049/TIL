import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline


def topo_order(pre_order, in_order):
    if len(pre_order) == 0:
        return

    elif len(pre_order) == 1:
        print(pre_order[0], end=' ')
        return
    

    root_idx = in_order.index(pre_order[0])

    right_in = in_order[0:root_idx]
    right_pre = pre_order[1:root_idx+1]
    topo_order(right_pre, right_in)

    left_in = in_order[root_idx+1:]
    left_pre = pre_order[len(right_pre)+1:]
    topo_order(left_pre, left_in)

    print(pre_order[0], end=' ') 



T = int(input())
for _ in range(T):
    n = int(input())
    pre_order = list(map(int, input().split()))
    in_order = list(map(int, input().split()))

    topo_order(pre_order, in_order)
    print()