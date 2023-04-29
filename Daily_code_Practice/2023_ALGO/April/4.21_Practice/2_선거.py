import sys
from collections import deque
input = sys.stdin.readline

picture = int(input())
student_count = int(input())
student_li = list(map(int, input().split()))
result = []
picture_li = []


for i in range(student_count):
    check = True
    picture_li = sorted(picture_li, key=lambda x:(x[0], x[1]))
    picture_li = deque(picture_li)
    n = len(picture_li)
    
    for j in range(n):
        if picture_li[j][2] == student_li[i]:
            check = False
            num_ = picture_li[j][0]
            idx = picture_li[j][1]
            del picture_li[j]
            break

    if check == False:
        picture_li.append([num_+ 1, idx, student_li[i]])
    else:
        if n == picture:
            picture_li.popleft()
            picture_li.append([1, i, student_li[i]])
        else:
            picture_li.append([1, i, student_li[i]])



for i in range(len(picture_li)):
    result.append(picture_li[i][2])

result.sort()

print(*result)