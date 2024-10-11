my_strings, parts = ["progressive", "hamburger", "hammer", "ahocorasick"], [[0, 4], [1, 2], [3, 5], [7, 7]]

def solution(my_strings, parts):
    answer = ''
    for idx in range(len(parts)):
        part = my_strings[idx][parts[idx][0]: parts[idx][1] + 1]
        answer += part
   
    return answer

solution(my_strings, parts)