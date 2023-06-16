def solution(answers):
    student_1 = [1,2,3,4,5]
    student_2 = [2,1,2,3,2,4,2,5]
    student_3 = [3,3,1,1,2,2,4,4,5,5]
    
    a = int(10000/len(student_1))
    b = int(10000/len(student_2))
    c = int(10000/len(student_3))
    
   
    student_1 = student_1 * a
    student_2 = student_2 * b
    student_3 = student_3 * c
    
    coun = 0
    a_1, a_2, a_3 = 0, 0, 0
    
    for i in answers:
        if i == student_1[coun]:
            a_1 += 1
        if i == student_2[coun]:
            a_2 += 1
        if i == student_3[coun]:
            a_3 += 1
        coun += 1
    
    point = [a_1, a_2, a_3]
        
    answer = []
    if max(point) == point[0]:
        answer.append(1)
    if max(point) == point[1]:
        answer.append(2)
    if max(point) == point[2]:
        answer.append(3)
    return answer