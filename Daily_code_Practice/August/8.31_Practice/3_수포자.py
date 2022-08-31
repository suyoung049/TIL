def solution(answers):

    student_1 = [1, 2, 3, 4, 5]
    student_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    list_count_1 = int(10000 / len(student_1))
    list_count_2 = int(10000 / len(student_2))
    list_count_3 = int(10000 / len(student_3))

    student_1 = student_1 * list_count_1
    student_2 = student_2 * list_count_2
    student_3 = student_3 * list_count_3

    # print(student_3)

    index = 0 

    result_count_1 = 0 
    result_count_2 = 0 
    result_count_3 = 0 

    for i in answers:
        if i == student_1[index]:
            result_count_1 += 1 
        if i == student_2[index]:
            result_count_2 += 1 
        if i == student_3[index]:
            result_count_3 += 1 
        index += 1 

    # print(result_count_1)
    # print(result_count_2)
    # print(result_count_3)

    result_point = [result_count_1, result_count_2, result_count_3 ]

    result = []

    if max(result_point) == result_point[0]:
        result.append(1)
    if max(result_point) == result_point[1]:
        result.append(2)
    if max(result_point) == result_point[2]:
        result.append(3)

    return result


