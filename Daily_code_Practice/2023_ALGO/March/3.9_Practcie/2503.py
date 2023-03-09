import sys
from itertools import permutations
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

num = list(permutations([1,2,3,4,5,6,7,8,9], 3))

for _ in range(n):
    test, a, b = map(int, input().split())
    test_num = str(test)
    remove_num = 0

    for i in range(len(num)):
        s_count = b_count = 0
        i -= remove_num

        for j in range(3):
            check_num = int(test_num[j])

            if check_num in num[i]:
                if j == num[i].index(check_num):
                    s_count += 1
                else:
                    b_count += 1

        if s_count != a or b_count != b:
            num.remove(num[i])
            remove_num += 1


print(len(num))

