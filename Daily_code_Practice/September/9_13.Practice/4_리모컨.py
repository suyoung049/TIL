import sys
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

chenal = int(input())
button = abs(100-chenal)    # 리모컨을 +, - 만으로 만드는 버튼 수 
n = int(input())           # 고장난 버튼이 있을 때만


if n:
    broken = set(input().split())
else:
    broken = set()


for num_ in range(1000001):               
    for x in str(num_):
        if x in broken:             # 만약 눌러야할 버튼이 고장이 나있다면 멈춤
            break
    else:
        button = min(button, len(str(num_)) + abs(num_-chenal))   # +,- 한 경우와 버튼을 누른디 
                                                                  # +, -를 누른팀중 최소 시간 지정

print(button)