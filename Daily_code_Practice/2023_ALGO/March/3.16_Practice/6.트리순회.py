import sys
sys.stdin = open('6_input.txt', 'r')
input = sys.stdin.readline

n = int(input())


tree = {}
for _ in range(n):
    data, left_node, right_node = input().split()
    if left_node == '.':
        left_node = None
    if right_node == '.':
        right_node = None
    tree[data] = [data, left_node, right_node]


# 전위 순회
def pre_order(node):
    print(node[0], end='')
    if node[1] != None:
        pre_order(tree[node[1]])
    if node[2] != None:
        pre_order(tree[node[2]])
# 중위 순회
def in_order(node):
    if node[1] != None:
        in_order(tree[node[1]])
    print(node[0], end='')
    if node[2] != None:
        in_order(tree[node[2]])

# 후위 순회
def post_order(node):
    if node[1] != None:
        post_order(tree[node[1]])

    if node[2] != None:
        post_order(tree[node[2]])

    print(node[0], end='') 

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])