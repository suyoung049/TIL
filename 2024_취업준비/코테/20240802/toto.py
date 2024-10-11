todo_list, finished = ["problemsolving", "practiceguitar", "swim", "studygraph"], [True, False, True, False]

def solution(todo_list, finished):
    answer = []
    for i in range(len(todo_list)):
        if (not finished[i]):
            answer.append(todo_list[i])
    print(answer)
    return answer


solution(todo_list, finished)