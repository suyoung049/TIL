n = 4
def solution(n):
    num_list = []
    answer = hanoi(1, 3, n, num_list)
    print(answer)
    return answer

def hanoi(one, three, n, num_list):
    if (n == 1):
        num_list.append([one, three])
        return
    
    hanoi(one, 6-one-three, n-1, num_list)
    num_list.append([one,three])
    hanoi(6-one-three,three,n-1,num_list)

    return num_list

solution(n)