class person:

    # 사람이라면 이름을 가지고 있다.
    # 인스턴스를 만들 때는 이름 정보를 받아서 하고 싶다.

    def __init__(self,name):
        # 개별 인스턴스에 각각 name 속성을 지정
        self.name = name

        # self : 호출하는 인스턴스를 파이썬 내부적으로 전달해줌
    def greeting(self):
        print(f'안녕하세요. {self.name}입니다')

# 인스턴스 만들때
jimin = person('지민')
jimin.greeting()

iu = person('지은')
iu.greeting()
