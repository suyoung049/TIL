import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
save = {}

list_ = list(map(int, input().split()))

sr_list = sorted(list(set(list_))) # 자기보다 작은수의 개수가 압축 수 이므로 오름차순 정렬
                                   # 중복은 제거
for i in range(len(sr_list)):     # 중복은 제거 되고 오름차순된 리스트의 길이만큼
    save[sr_list[i]] = i          # 딕셔너리에 Key 값은 자기자신 value 값은 index를 저장해준다.

for i in range(n):
    print(save[list_[i]], end = ' ')  # 딕셔너리에서 해당 value 값 index가 압축 되는 수 