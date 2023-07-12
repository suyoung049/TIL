
import sys

sys.stdin = open("input_1204.txt", "r")
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    num_ = map(int, (input().split()))
    student_list = [0] * 101
    for i in num_:
        student_list[i] += 1
    max_score = 0
    for j in range(0, len(student_list)):
        if student_list[j] >= max_score:
            max_index = j
            max_score = student_list[j]
    print(f'#{test_case} {max_index}')
   
    print(f'#{test_case} {student_list.index(max(student_list))}')
   # 이방법은 간단히 최빈수를 구할수 있지만 여러 수 일때 큰 수를 구 할 수 없다.
           
           