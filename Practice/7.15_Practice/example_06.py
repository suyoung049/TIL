N = 10 
answer = [] # .append 메서드는 튜플에서 사용불가 리스트로 변경이 필요하다
for number in range(N + 1):
    answer.append(number * 2)

print(answer)