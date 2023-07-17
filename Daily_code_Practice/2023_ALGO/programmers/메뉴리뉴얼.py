from itertools import combinations
from collections import Counter

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]

result = []

for course_num in course:
    course_name = []
    for food in orders:
        for i in combinations(sorted(food), course_num):
            course_name.append(''.join(i))
        
    
    menue = Counter(course_name)

    if len(menue) !=0:
        max_menue = max(menue.values())

        for chose_menue, num_ in menue.items():
            if max_menue>= 2 and num_ == max_menue:
                result.append(chose_menue)

result.sort()
print(result)
     


 
 