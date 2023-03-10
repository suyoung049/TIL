import sys
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

n, k = map(int, input().split())

num_li = list(range(1, n+1))
stack = []

i = 1

while True:
    if len(num_li) == 0:
        break

    if i < k:
        a = num_li.pop(0)
        num_li.append(a)
        i += 1

    elif i == k:
        a = num_li.pop(0)
        stack.append(a)
        i = 1
    

print('<', end='')
for i in range(n):
    if i == n-1: 
        print(f'{stack[i]}',  end='')
    else:
        print(f'{stack[i]}, ',  end='')
print('>',  end='')
