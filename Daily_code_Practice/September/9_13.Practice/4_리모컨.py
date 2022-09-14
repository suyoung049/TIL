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


for num_ in range(1000001):     # 큰 수에서 부터 하나하나씩 목표 채널의 차이에서 최소값을 비교          
    for x in str(num_):
        if x in broken:    # 만약 눌러야할 버튼이 고장이 나있다면 멈춤
            break
    else:
        button = min(button, len(str(num_)) + abs(num_-chenal))   # +,- 한 경우와  버튼을 누른 다음 +, -를 한 경우중 최소값을 출력

print(button)