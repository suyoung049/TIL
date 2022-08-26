import sys
sys.stdin = open('2_input.txt', 'r')

decode = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
      'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
      '0','1','2','3','4','5','6','7','8','9','+','/'
      ]

T = int(input())

for test_case in range(1, T+1):
    word = list(input())
    value = ''                     # 주어진 문장을 2진수로 저장하기 위한 공간
    for i in range(len(word)):
        num_ = decode.index(word[i])
        bin_num = str(bin(num_)[2:])   # 2진수로 변환시에 앞에 '0b' 가 붙으므로 앞에 2자리 제거

        while len(bin_num) < 6 :        # 앞의 수를 없앤 후에 0을 더해가며 6자리 bit(6) 생성
            bin_num = '0' + bin_num
        value += bin_num              # value에 전부 저장

    result = ''

    for j in range(len(word) *6 // 8):          #입력받은 문자열에 6을 곱하고 8을 나눈 다음 
        data = int(value[j*8 : j*8+8],2)         # 인덱싱 되는 bit(8)를 10진수로 변환
        result += chr(data)                     # 10진수를 아스키코드를 사용 문자로 변환
    print(f'#{test_case} {result}')
    
   