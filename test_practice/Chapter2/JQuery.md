## jQuery

### jQuery란?

HTML 요소들을 조작하는 편리한 JavaScript 라이브러리

- JavaScript와 다른 특별한 소프트웨어가 아니라 미리 작성된 코드를 모아둔 것
- 직접 JS 코드를 작성하여 모든 기능을 구현할 수도 있지만, 이 경우에 코드가 복잡하고, 개발환경과 다른 브라우저에서 잘 작동을 안하는 등 브라우저 간 호환성을 직접 고려해야하는 등의 문제가 있기 때문에 전문 개발자가 작성한 라이브러리를 가져와서 사용하면 편합니다.
- **대신, 쓰기 전에 임포트를 해주어야합니다.**



### 자주 쓰는 jQuery

#### input 박스의 값 가져오기

- 값을 가져오기 원하는 input 태그에 id를 부여해야 합니다. 
- 아래 코드를 개발자도구 콘솔창에 입력합니다.

```javascript
// id 값이 post-url인 곳을 가리키고, val()로 값을 가져온다.
let url = $('#post-url').val();
url // input 박스 안에 적혀있는 내용이 출력된다.
```

- input 박스에 적혀있는 글을 바꾸고 싶다면 아래와 같은 코드를 쓸 수 있다.

```javascript
$('#post-url').val("새 글입니다.");
```



#### div 숨기기/보이기

```javascript
// id 값이 post-box인 곳을 가리키고, hide()로 안보이게 한다.(=css의 display 값을 none으로 바꾼다)
$('#post-box').hide();

// show()로 보이게 한다.(=css의 display 값을 block으로 바꾼다)
$('#post-box').show();
```



####  CSS의 속성 값 가져오기

```javascript
$('#post-box').hide();
$('#post-box').css('display');

$('#post-box').show();
$('#post-box').css('display');
```



#### 태그 내 텍스트 입력하기

```javascript
let btn_text = $('#btn-posting-box').text(); 
btn_text         // '포스팅박스 열기'가 출력된다.
$('#btn-posting-box').text('포스팅박스 닫기');
```



#### 태그 내 html 입력하기

- 아래 코드를 실행하여 카드들 뒤에 텍스트를 넣습니다.

```javascript
$('#cards-box').append("추가 텍스트");
```

- 버튼을 추가

```javascript
let temp_html = `<button>추가 버튼</button>`;
$('#cards-box').append(temp_html);
```



- 카드 추가

```javascript
// 주의: 홑따옴표(')가 아닌 backtick(`)으로 감싸야 합니다.
// 숫자 1번 키 왼쪽의 버튼을 누르면 backtick(`)이 입력됩니다.
// backtick을 사용하면 문자 중간에 Javascript 변수를 삽입할 수 있습니다.
let img_url = 'https://cdn.vox-cdn.com/thumbor/Pkmq1nm3skO0-j693JTMd7RL0Zk=/0x0:2012x1341/1200x800/filters:focal(0x0:2012x1341)/cdn.vox-cdn.com/uploads/chorus_image/image/47070706/google2.0.0.jpg';
let link_url = 'https://google.com/';
let title = '제목 - 구글';
let desc = '구글에 대한 설명이 여기에 들어간다.';
let comment = '여기는 개인적인 코멘트가 들어간다.';

let temp_html = `<div class="card">
                    <img class="card-img-top"
                        src="${img_url}"
                        alt="Card image cap">
                    <div class="card-body">
                        <a href="${link_url}" class="card-title">${title}</a>
                        <p class="card-text">${desc}</p>
                        <p class="card-text comment">${comment}</p>
                    </div>
                </div>`;
$('#cards-box').append(temp_html);
```



#### 페이지 로딩이 완료되면 실행하기

```javascript
<script>

$(document).ready(function(){
	alert('페이지가 로딩되었습니다.')
});

</script>
```

