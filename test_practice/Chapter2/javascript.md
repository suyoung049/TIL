### 기초 문법

####  변수 선언

```javascript
let num = 10   // 변수를 선언할 때는 앞에 let을 쓴다.
console.log(num)

let num = 20
num

num = 2
num

let num1 = 1
let num2 = num1

console.log(num1, num2) // 1 1 

```



#### 자료형과 기본 연산

##### 숫자열

- 변수에 저장된 값에 연산을 한 후 다시 그 값을 저장

```javascript
let a = 5
a = a + 3 // 5에 3을 더한 값을 다시 a에 저장
console.log(a) // 8

a += 1 // 줄여 쓸 수도 있다. 8에 1을 더해 9를 a에 저장. 사칙연산 다 가능하다.

// 증감연산자
a++ // 1을 더한 값을 다시 a에 저장
a-- // 1을 뺀 값을 다시 a에 저장
```



##### 문자열

- 모든 알파벳을 대문자로 바꾸기

```javascript
let myname = 'jungle'

myname.toUpperCase() // JUNGLE
```

- 이메일 주소에서 도메인만 추출하기

```javascript
let myemail = 'test@gmail.com'

let result = myemail.split('@') //['test', 'gmail.com']

result[0]
result[1]

let result2 = result[1].split('.') //['gmail', 'com']

result2[0] // gmail -> 우리가 알고 싶었던 것
result2[1] // com

// 한 줄로 쓸 수도 있다.
myemail.split('@')[1].split('.')[0]
```

- 특정 문자를 다른 문자로 바꾸기

```javascript
let txt = '서울시-마포구-망원동'
let names = txt.split('-'); // ['서울시','마포구','망원동']
let result = names.join('>'); // '서울시>마포구>망원동'
```



##### 불(Boolean) 자료형

- 불 자료형에는 논리 연산자를 이용할 수 있습니다.

```javascript
let a = 4 > 2  // true
!a             // false    NOT 연산자로 참을 거짓으로, 거짓을 참으로 바꿔준다.

let b = 2!=2   // false

a && b         // false    AND 연산자로 모두 참이어야 참을 반환한다.
a || b         // true     OR 연산자로 둘 중 하나만 참이면 참이다.
```



##### 리스트와 딕셔너리

- 리스트

```javascript
let a_list = []            // 빈 리스트를 선언. 변수 이름은 아무것이나 가능!

// 또는,

let b_list = [1,2,'hey',3] // 로 선언 가능. 
                           // 서로 다른 자료형의 요소를 섞어서 가질 수 있음.

b_list[1]                  // 2 를 출력. index는 0부터 시작
b_list[2]                  // 'hey'를 출력
b_list[2] = 5              // 값 수정
b_list                     // [1, 2, 5, 3]
// 리스트에 요소 넣기
b_list.push('헤이')
b_list                     // [1, 2, 5, 3, "헤이"] 를 출력

// 리스트의 길이 구하기
b_list.length              // 5를 출력
```

- 리스트는 다른 리스트를 요소로 가질 수 있습니다.

```javascript
let a_list = [1, 4, 2, [3, 1]]

a_list.length       // 4
a_list[3]           // [3, 1]
a_list[3][1]        // 1

let b_list = [4, 1, 0]
a_list.push(b_list) 
a_list              // [1, 4, 2, [3, 1], [4, 1, 0]]
a_list.length       // 5

// 리스트와 리스트를 이어붙이고 싶다면
let c_list = a_list.concat(b_list)
c_list              // [1, 4, 2, [3, 1], [4, 1, 0], 4, 1, 0]
a_list              // [1, 4, 2, [3, 1], [4, 1, 0]] 변하지 않음
```

- 딕셔너리

```javascript
names = [{'name':'bob','age':20},{'name':'carry','age':38}]

// names[0]['name']의 값은? 'bob'
// names[1]['name']의 값은? 'carry'

new_name = {'name':'john','age':7}
names.push(new_name)

// names의 값은? [{'name':'bob','age':20},{'name':'carry','age':38},{'name':'john','age':7}]
// names[2]['name']의 값은? 'john'
```

- 딕셔너리들을 요소로 갖는 리스트로 만들 수 있습니다. 비슷한 형태의 자료를 정리할 때 유용

```javascript
names = [{'name':'bob','age':20},{'name':'carry','age':38}]

// names[0]['name']의 값은? 'bob'
// names[1]['name']의 값은? 'carry'

new_name = {'name':'john','age':7}
names.push(new_name)

// names의 값은? [{'name':'bob','age':20},{'name':'carry','age':38},{'name':'john','age':7}]
// names[2]['name']의 값은? 'john'
```



#### 반복문

```javascript
for (let i = 0; i < 100; i++) {
	console.log(i);
}
```



- 딕셔너리를 요소로 갖는 리스트와 함께 쓰이면 더욱 강력

```javascript
let scores = [
  	{'name':'철수', 'score':90},
	  {'name':'영희', 'score':85},
	  {'name':'민수', 'score':70},
    {'name':'형준', 'score':50},
    {'name':'기남', 'score':68},
    {'name':'동희', 'score':30},
]

// 각 사람의 기록 출력
for (let i = 0 ; i < scores.length ; i++) {
	  console.log(scores[i])
}

// 점수가 70 미만인 사람의 이름 출력
for (let i = 0 ; i < scores.length ; i++) {
    let score = scores[i]
	  if (score['score'] < 70) {
		    console.log(score['name']);
	}
}
```
