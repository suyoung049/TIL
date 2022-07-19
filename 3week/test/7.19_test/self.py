class person:
    # 생성자! 인스턴스가 생성될대 어떤한 작업!
    def __init__(self, name):
        self.name = name 
        
    # 그 인스턴스의 이름을 name으로 해주세요


# person 클래스의 인스턴스 iu를 생성
iu = person('아이유')
print(iu.name)
jimin = person('지민')
print(jimin.name)