👉 GET, POST 방식 여러 방식([링크](https://developer.mozilla.org/ko/docs/Web/HTTP/Methods))이 존재하지만 우리는 가장 많이 쓰이는 GET, POST 방식에 대해 다루겠습니다.  

* GET        →      통상적으로! 데이터 조회(Read)를 요청할 때                           예) 영화 목록 조회                  →     데이터 전달 : URL 뒤에 물음표를 붙여 key=value로 전달                  →     예: google.com?q=북극곰 
* POST     →      통상적으로! 데이터 생성(Create), 변경(Update), 삭제(Delete) 요청 할 때                           예) 회원가입, 회원탈퇴, 비밀번호 수정                  →     데이터 전달 : 바로 보이지 않는 HTML body에 key:value 형태로 전달

#### GET POST 요청에서 클라이언트의 데이터를 받는 방법

##### GET 요청 API 코드

```python
@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give')
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})
```



##### GET 요청 확인 Ajax 코드

```javascript
$.ajax({
    type: "GET",
    url: "/test?title_give=봄날은간다",
    data: {},
    success: function(response){
       console.log(response)
    }
  })
```



#####  POST 요청 API 코드

````python
```python
@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})
```
````



##### POST 요청 확인 Ajax 코드

````javascript
```python
@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})
```
````



pip install beautifulsoup4
