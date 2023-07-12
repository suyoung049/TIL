import sys

sys.stdin = open("21_input.txt", "r")
input = sys.stdin.readline
A, B = map(int, input().split())
set_A = set(list(map(int, input().split())))
set_B = set(list(map(int, input().split())))
union = (set_A & set_B)  # {2, 4}
diff_A = (set_A - union) # {1}
diff_B = (set_B - union) #  {3, 5, 6}
count_ = len(diff_A) + len(diff_B)
print(count_) # A 와 B의 대칭차집합이 구해집니다.




