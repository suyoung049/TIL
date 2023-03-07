import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
check = [False] * n


answer = sys.maxsize
def result():
    global answer

    our_team = 0
    vs_team = 0

    for i in range(n):
        for j in range(n):
            if check[i] and check[j]:
                our_team += matrix[i][j]
            
            if not check[i] and not check[j]:
                vs_team += matrix[i][j]
    
    answer = min(answer, abs(our_team - vs_team))
    return
        

def recu(num_):
    if num_ == n:
        result()
        return
    check[num_] = True
    recu(num_+1)
    check[num_] = False
    recu(num_+1)
                
recu(0)
print(answer)