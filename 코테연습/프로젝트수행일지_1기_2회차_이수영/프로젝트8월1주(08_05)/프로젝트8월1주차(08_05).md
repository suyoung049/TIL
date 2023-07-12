## 후기 작성

저번과 마찬가지로 알고리즘 자체가 어려운 문제들이 아니라서 접근 자체는 올바르게 한거 같은데 코드상으로 구현에서 막혀서 시간도 부족하고 1문제밖에 풀 지 못하였습니다. 

- 민석이의과체체크하기

이 문제는 어렵지 않게 해결 하였습니다.

- 조교의 성적 매기기

```python
import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())

N, M = map(int, input().split())
score_list =[]
for _ in range(N):
    a, b, c = map(int, input().split())
    score = (a * 0.35) + (b * 0.45) + (c * 0.2)
    score_list.append(score)
    sor_score_list = sorted(score_list)
for i in range(len(sor_score_list)):
    if i < N//10:
        score_list.replace(sor_score_list[i], 'D0')
print(score_list)
```

점수들을 중간, 기말, 수행으로 종합 점수를 구한 후 sorted로 정렬까지 진행하였는데 이 점수들을 등급으로 바꾸는 코드에서 막혀서 진행 할 수 없었습니다.

- 암호생성기

```python
import sys

sys.stdin = open("_암호생성기.txt")

N = int(input())
code = list(map(int, input().split()))

for j in range(1, 6):       
        code.append(code.pop(0)-int(j))
       
       
```

암호 생성기 같은 경우는 while 문으로 사이클을 구현해 보려 했는데 break가 걸리지 않고 계속 돌아가는 문제가 있어서 풀지 못하였습니다.

- 파리 퇴치

```python
import sys

sys.stdin = open("_파리퇴치.txt")
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    sum_list = []
    
    for i in range(N-M):
        for j in range(N-M):
            sum_ = matrix[i][j] + matrix[i][j+1] + matrix[i+1][j] + matrix[i+1][j+1]
            sum_list.append(sum_)
    print(max(sum_list))

```

위의 코드는 (2 * 2) 파리채까지만 구할수 있고 (3 * 3), (5 * 5), (7 * 7) 큰 파리채는 구할 수 없어서 그 부분에서 막혔습니다.

- 어디에단어가들어갈수있을까

```python
import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")
T = int(input())

N, M = map(int, input().split())
matrix = [list(input().split()) for _ in range(N)]
print(matrix)
a, b = 0, 0
lenth_a = 0
lenth_b = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == '1':
            lenth_a += 1
        else:
            lenth_a == 0
        if lenth_a == 3:
            a += 1

        if matrix[j][i] == '1':
            lenth_b += 1
        else:
            lenth_b == 0
        if lenth_b == 3:
            b += 1
print(a, b)
```

이 문제는 저번에 실습 문제랑 비슷한 유형이라 같은 방법으로 코드를 작성했는데 올바른 대답이 나오지 않아 

디버깅 하는 과정에서 시간 종료 하였습니다.

무언가 계속 답답한 모의고사였습니다. 조금만 더하면 풀 수 있을거 같은데 계속 마지막 단추를 풀지 못하는 것 같은 문제가 연속적으로 나와서 더 답답하였습니다. 한 문제 밖에 풀지 못하였지만 말그대로 모의고사니깐 기죽지 않고 열심히 해보겠습니다.  실전에서 잘하면 되니깐 화이팅!!