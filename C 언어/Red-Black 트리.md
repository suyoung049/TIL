## Red-Black 트리

### Red-Black 트리

- 이진 탐색 트리(BST)의 한 종류
- 스스로 균형(balancing) 잡는 트리
- BST의 worst case의 단점을 개선
  - 모든 노드는 red 혹은 black



### Red-Black 트리 속성

- #1 모든 노드는 red 혹은 black

- #2 루트 노드는 black

##### nil 노드란?

1. 존재하지 않음을 의미하는 노드
2. 자녀가 없을 때 자녀를 nil 노드로 표기
3. 값이 있는 노드와 동등하게 취급

4. RB 트리에서 leaf 노드는 nil 노드

- #3 모든 nil(leaf)노드는 black

-  #4 (red의 자녀들은 black) or (red가 연속적으로 존재 할 수 없다.)

- #5  black height : 임의의 노드에서 자손 nil 노드들 까지 가는 경로들의 black 수는 같다(자기 자신은 카운트 제외)



##### 색을 바꾸면서도 속성 유지

- RB 트리가 #5 속성을 만족하고 있고 두자녀가 같은 색을 가질 때 부모와 두 자녀의 색을 바꿔줘도 속성은 그대로 유지 된다.
  - #5 속성: 임의의 노드에서 자손 nil 노드들 까지 가는 경로들의 black 수는 같다

##### RB 트리는 어떻게 균형을 잡는가?

- 삽입 /삭제 시 주로 #4, # 5를 위반하며 이들을 해결하려고 주고를 바꾸다 보면 자연스럽게 트리의 균형이 잡히게 된다.
  - #4 노드가 red라면 자녀들은 black
  - #5 임의의 노드에서 자손 nil 노드들 까지 가는 경로들의 black 수는 같다.



### Red - Black 트리 삽입 방식

0.  삽입 전 RB 트리 속성 만족한 상태
1.  삽입 방식은 일반적인 BST와 동일
2.  삽입 후 RB 트리 위반 여부 확인
3.  RB 트리 속성을 위반했다면 재조정
4.  RB 트리 속성을 다시 만족



- insert(50)
  - 노드를 삽입할 때 두 nil 노드의 색은 black으로 고정한다 그러면 자연스럽게 #3 속성을 만족
    - #3 모든 nil 노드는 black
  - Red-Black 트리 #2 속성 위반 루트 노드를 balck으로 바꾸면 해결
    - #2 루트 노드는 black



- insert(20)
  - Red-Black 트리의 모든 속성을 만족
    - 왜 새로 삽입하는 노드는 red 인가?
    - 삽입후에도 #5 속성을 만족하기 위해
      - #5 : 임의의 노드에서 자손 nil 노드들가지 가는 경로들의 black 수는 같다.
  - 이제부터 nil 노드를 표기하지 않아도 삽입되는 노드는 nil 노드가 두 개 있고 nil 노드는 black임을 기억해 주세요



##### case.3 해결하기

- 할아버지한테 가는 경로가 일직선

- 삽입된 red 노드가 부모의 왼쪽 자녀 & 부모도 red고 할아버지의 왼쪽자녀 & 삼촌(=부모의 형제)은 black이라면

  부모와 할아버지의 색을 바꾼 후 할아버지 기준으로 오른쪽(왼쪽)으로 회전

- insert(10)
  - red가 한쪽으로 몰려 있으니 red 하나를 반대편으로 옮겨준다
  - 구조를 바꾸면서도 BST의 특징을 유지시키는 방법은 회전이다.
  - #4 속성 위반을 해결하기 위해 red 하나를 넘겨야 하는데 BST 특징 또한 유지하면서 넘기려면 회전을 사용해야 한다
    - #4 노드가 red라면 자녀들은 black
  - 20과 50의 색을 바꿔 준다
  - 50을 기준으로 오른쪽으로 회전한다



##### case.2 해결하기

- 할아버지 한테 가는 경로가 꺾여 있음

- 삽입된 red 노드가 부모의 오른쪽 자녀 & 부모도 red고 할아버지의 왼쪽 자녀 & 삼촌(=부모의 형제)은 black이라면 부모를 기준으로 왼쪽으로 회전한 뒤 case.3의 방식으로 해결 (오른쪽 왼쪽을 바꿔도 성립)

- insert(40)

  - #4 속성 위반을 해결하기 위해 red 하나를 넘겨야 하는데 BST 특징 또한 유지하면서 넘기려면 회전을 사용해야 한다

    회전을 어떻게 사용할지가 관건이다.

  - case.3 과 살짝 다른점은 삽입된 노드를 기준으로 할아버지 까지의 경로가 꺾였다는 점
  - 꺾인 부분을 펴줘서 case.3과 같은 형태로 만들면 case.3과 같은 방식으로 해결 가능
  - 20 기준으로 왼쪽으로 회전한다
  - 40과 50의 색을 바꾼다
  - 50 기준으로 오른쪽으로 회전한다

##### case.1 해결하기

- 삽입된 red 노드의 부모도 red & 삼촌(=부모의 형제)도 red라면 부모와 삼촌을 black으로 바꾸고 할아버지를 red로 바꾼 뒤 할아버지에서 다시 확인을 시작한다.

- insert(30)
  - red가 한 쪽으로 몰려 있지 않아서 옮길 수 가 없다.
  - 10과 50을 black으로 바꾸고 20을 red로 바꾸면 된다.



##### Red-Black 트리 예제

![레드 블랙 트리 예제](C:\Users\holho\OneDrive\DeskTop\레드 블랙 트리 예제.png)



### Red-Black Tree 삭제

0. 삭제 전 RB 트리 속성 만족한 상태
1. 삭제 방식은 일반적인 BST와 동일
2. 삭제 후 RB 트리 속성 위반 여부 확인
3. RB 트리 속성을 위반 했다면 재조정
4. RB 트리 속성을 다시 만족



** successor : 노드의 오른쪽에서 가장 작은 값

##### RB 트리에서 노드를 삭제할 때 어떤 색이 삭제되는지가 속성 위반 여부를 확인할 때 매우 중요

- 삭제하려는 노드의 자녀가 없거나 하나라면 삭제되는 색 = 삭제되는 노드의 색

- 삭제 하려는 노드의 자녀가 둘이라면 삭제되는 색 = 삭제되는 노드의 successor의 색

  

#### 속성 위반 여부 확인은 삭제되는 색을 통해

- 삭제하려는 노드의 자녀가 없거나 하나라면 삭제되는 색은 삭제되는 노드의 색
- 삭제하려는 노드의 자녀가 둘이라면 삭제되는 색은 삭제 되는 노드의 successor의 색

##### 삭제되는 색이 RED라면 어떤 속성도 위반하지 않는다

##### 삭제된 색이 BLACK이라면 # 2, # 4, # 5 속성을 위반 할 수 있다,



##### 삭제되는 색이 black일 때 # 2 위반 해결하기

- 루트 노드를 black으로 바꾸면 된다

##### 나머지 경우 삭제 되는 색이 black일 때 특수한 상황을 제외하면 #5 속성을 항상 위반하게 된다. 

- 삭제되는 색이 black이고 #5 위반일 때 extra black 부여
  - #5 속성을 다시 만족시키기 위해 삭제된 색의 위치를 대체한 노드에 extra black을 부여한다.
  - extra black의 역활 : 경로에서 black 수를 카운트 할 때 extra black은 하나의 black으로 카운트 된다.
  - black이 삭제 되었으므로 #5 속성을 위반했고 extra black을 부여해서 #5 속성을 다시 만족시켜야 한다.
  - doubly black : extra black이 부여된 black 노드
- 삭제 후 연결된 노드의 색이 red 일때 마찬가지로 exrta black 부여
  - red-and-black : extra black이 부여된 red 노드
- 삭제되는 색이 black이고 # 5 위반일때, 
  - extra black을 부여받은 노드는 doubly black이 되거나 red-and-black이 된다.



##### extra black 부여 후 red-and-black 해결하기

- red-and-black을 black으로 바꾸면 해결

##### extra black 부여 후 doubly black 해결하기

- extra black을 부여했더니 double black 노드가 생겼다면 결국 extra black을 어떻게 없앨 것인지가 관건
- doubly black의 extra black을 없애는 방법은 총 네가지 case로 분류됨
  - doubly black의 오른쪽 형제가 black &  그 형제의 오른쪽 자녀가 red일 때 
    - 그 red를 doubly black 위로 옮기고 옮긴 red로 extra black을 전달해서 red-and-black으로 만들면 red-and-black을 black으로 바꿔서 해결 
    - 오른쪽 형제는 부모의 색으로, 오른쪽 형제의 오른쪽 자녀는 black으로, 부모는 black으로 바꾼 후에 부모의 기준으로 왼쪽으로 회전하면 해결(오른쪽 왼쪽 바꿔도 성립)
  - doubly black의 오른쪽 형제가 black & 그 형제의 왼쪽 자녀가 red & 그 형제의 오른쪽 자녀는 black일 때
    - doubly black의 형제의 오른쪽 자녀를 red(자신과 부모 노드의 색을 교환후 부모를 기준으로 오른쪽 회전 )가 되게 만들어서 이후엔 case.4를 적용
  - doubly black의 형제가 black & 그 형제의 두 자녀 모두 black일 때
    - doubly black과 그 형제의 black을 모아서 부모에게 전달 해서 부모가 extra black을 해결하도록 위임한다.
  - doubly black의 형제가 red 일 때
    - doubly black의 형제를 black으로 만든 후 case 2, 3, 4 중에 하나로 해결
    - 부모와 형제의 색을 바꾸고 부모를 기준으로 왼쪽으로 회전한 뒤 doubly black을 기준으로 case 2, 3, 4중에 하나로 해결



#### 정리

##### 삭제되는 색이 black일 때 # 5 위반 해결하기

- 삭제되는 색이 black일 때 삭제되는 색이 있던 위치를 대체한 노드에 extra black을 부여한다
- 대체한 노드가 red-and-black이 되었다면 black으로 바꿔주면 끝
- 대체한 노드가 doubly black이 되었다면 case 1, 2, 3, 4 중에 하나로 해결



#### red-black tree 구현 이유

red-black 트리가 왜 필요 할까?

우선 순위 큐 보다 조금 더 복잡한 구조 

추가, 삭제가 조금더 유용하게 하기 위해 트리가 balance를 유지하기 위해 ,

blance를 맞추지 않으면 O(n)까지 증가 blance를 맞추면 O(logn)으로 줄어든다.

물론 삽입, 삭제하는 부분도 O(logn)으로 맞추어야 한다.

assert 사용도 디버깅 가능 



calloc 과 malloc의 차이 초기화의 차이만 있는가?

구조체가 다름(calloc의 argument(type, 개수)) malloc은 bus 오류가 난다.



```c
git clone --bare https://github.com/SWJungle/${project_name}.git
cd ${project_name}.git
# 아래 교육생 repository는 GitHub미리 만들어 놓아야 함
git push --mirror https://github.com/${교육생ID}/${project_name}.git
cd ..
rm -rf ${project_name}.git
git clone https://github.com/${교육생ID}/${project_name}.git
```

