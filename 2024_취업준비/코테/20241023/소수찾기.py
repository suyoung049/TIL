numbers = "1231"

def solution(numbers):
    answer = 0
    num_list = list(numbers)
    length = len(num_list)
    check = [False for _ in range(length)]
    num = []
    candidate = set()
    for i in range(1,length+1):
        dfs(0, i, length, check, candidate, num, num_list)

    for number in candidate:
        if number == 1:
            continue
        if check_num(number):
            answer += 1
    return answer

def dfs(n, k, length, check, candidate, num, num_list):
    if n == k:
        result = ""
        for str_num in num:
            result += str_num 
        candidate.add(int(result))
        return

    for i in range(length):
        if check[i] == False:
            check[i] = True
            num.append(num_list[i])
            dfs(n+1, k, length, check, candidate, num, num_list)
            num.pop()
            check[i] = False

def check_num(num):
    check = []
    for k in range(1, int(num**0.5) + 1):
        if num % k == 0:
            check.append(k)
            check.append(num//k)
    if len(check) == 2:
        return True
    else:
        return False



print(solution(numbers))