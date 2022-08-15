import sys

sys.stdin = open("10989_input.txt", "r")
n = int(sys.stdin.readline())
num_list = [0]* 10001
for i in range(n):
    num_list[int(sys.stdin.readline())] += 1  # 숫자가 있으면 리스트의 값이
                                              # 1씩 추가된다.
for j in range(10001):
    if num_list[j] != 0:
        for k in range(num_list[j]):  # 여러개의 숫자가 입력 되었을때
            print(j)                   # 동시 출력 하기 위한 반복문
       