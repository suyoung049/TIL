n, k = 8, 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]


class Node:
    def __init__(self, idx:int, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.idx = idx

def solution(n, k, cmd):
    answer = ['X'] * n
    root = Node(idx=-1)
    node = root
    for i in range(n):
        node.next = Node(idx = i, prev=node)
        node = node.next
    node = root
    for i in range(k+1):
        node = node.next

    stack = []
    
    for cd in cmd:
        if cd[0] == "D":
            x = int(cd.split()[1])
            for _ in range(x):
                node = node.next
        elif cd[0] == "U":
            x = int(cd.split()[1])
            for _ in range(x):
                node = node.prev
        elif cd == "C":
            prev = node.prev
            next = node.next
            stack.append(node)
            prev.next = next
            if next:
                next.prev = prev
                node = node.next
            else:
                node = node.prev
        elif cd == "Z":
            reCover = stack.pop()
            prev = reCover.prev
            next = reCover.next
            prev.next = reCover
            if next:
                next.prev = reCover
    node = root
    answer_li = []
    for i in range(n):
        if node.next:
            node = node.next
            answer_li.append(node.idx)
    for idx in answer_li:
        answer[idx] = "O"
    return "".join(answer)

solution(n, k, cmd)