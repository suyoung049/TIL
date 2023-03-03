import sys
sys.stdin = open('7_input.txt', 'r')


num_ = int(input())
print(f'쓰고 싶은 문장 {num_}')


for i in range(1,10):
    print(str(num_) + ' ' + '*' ' ' + str(i) + ' ' + '=' + ' ' + str(num_ * i))
   

