from itertools import combinations
orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]


def solution(orders, course):
    answer = []
    for c in course:
        course_li = []
        for order in orders:
            for i in combinations(order, c):
                course_li.append("".join(sorted(i)))
        
        count_dict = count_course(course_li)
        sorted_dict = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
        if sorted_dict:
            max_num = sorted_dict[0][1]
        if max_num != 1:
            for sor in sorted_dict:
                if sor[1] == max_num:
                    answer.append(sor[0])
                else:
                    break
    return sorted(answer)

def count_course(course_li):
    count_dict = dict()
    for menu in course_li:
        if count_dict.__contains__(menu):
            count_dict[menu] += 1
        else:
            count_dict[menu] = 1
    return count_dict 

solution(orders, course)