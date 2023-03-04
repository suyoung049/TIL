import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

# 한수는 1의 자리일때는 한수로 인정, 2자리일때도 자리수의 공차가 1개 존재하기때문에 2자리수 모두 한수로 인정

def han(n):
    count_ = 0
    for i in range(1, n+1):
        if i < 100:
            count_ += 1
        else:
            str_i = str(i)
            if int(str_i[0]) - int(str_i[1]) == int(str_i[1]) - int(str_i[2]):
                count_ += 1
    
    return count_

n = int(input())
print(han(n))





