n = int(input())
a = input().split()

for i in range(n):     # 0부터 n-1 까지
    a[i] = int(a[i])  # range 쓸 때, 형변환 방법

d =[]
for i in range(24):   # [0, 0, 0, 0, 0, 0 , ....]과 같이 24개의 정수 값 0을 추가
    d.append(0)       #각 값은 d[0], d[1], d[2], d[3]...d[22], d[23]

for i in range(n):     # 번호를 부를 때마다, 그 번호에 대한 카운트 1씩 증가
    d[a[i]] += 1

for i in range(1, 24):       #카운트한 값을 공백을 두고 출력
    print(d[i], end =' ')

d = []              #어떤 데이터 목록(list) 을 순서대로 저장하기 위해 아무것도 없는 리스트 변수 만들기
d.append()  #d 리스트의 마지막에 원하는 값을 추가(append)해 넣음 
d[a[i]] += 1     #2중 리스트 참조 : 만약 a[i]의 값이 1이었다면? d[1] += 1 이 실행되는 것이다. 1번 카운트 1개 증가..