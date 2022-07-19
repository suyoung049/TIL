# 얕은 복사
a = [1, 2, 3]
b = a
b[0] = 'hi'

# a를 출력 [1, 2, 3]
print(a)
# b를 출력['hi', 2, 3]
print(b)

# list 형변환 결과 : 사실은 list고 사실은 값도 같지만 다른 메모리 주소 결과를 받아냄
c = [3, 4, 5]
d = list(c)
d[0] = 'hi'

# 슬라이싱 
e = [4, 5, 6]
f = e[::]
f[0] = 'hi'

# 깊은 복사
a = [[1,2], 2, 3]
b = list(a)
b[0][0] = 'hi'

print(a) #[['hi', 2], 2, 3]
print(b) #[['hi', 2], 2, 3]

import copy
c = [[1, 2], 2, 3]
d = copy.deepcopy(c)
d[0][0] = 'hi'
print(a)
print(b)