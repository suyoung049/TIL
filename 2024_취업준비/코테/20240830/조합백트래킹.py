

n, m = 4, 2

rs = []

check = [False] * (n+1)
def recu(num_):
    global n, m, rs, check
    if num_ == m:
        print(' '.join(map(str, rs)))
        return

    for j in range(1,n+1):
        if check[j] == False:
            check[j] = True
            rs.append(j)
            recu(num_+1)
            check[j] = False
            rs.pop()

recu(0)

def solution(list, check):
    if not check in list:
        return True
print(solution([1,1,1], 0))