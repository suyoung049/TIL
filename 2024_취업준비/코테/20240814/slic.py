my_str, n = "abc1Addfggg4556b", 6
def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str), n):
        answer.append(my_str[i:i+6])

    return answer

solution(my_str, n)