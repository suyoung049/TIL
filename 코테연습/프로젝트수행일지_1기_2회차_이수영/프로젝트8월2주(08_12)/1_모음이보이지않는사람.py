import sys

sys.stdin = open("_모음이보이지않는사람.txt")

word = {
    'a':'', 
    'e':'', 
    'i':'', 
    'o':'', 
    'u':''}

T = int(input())

for test_case in range(1, T+1):
    text = input()
    for chr_ in text:
        if chr_ in word:
            text = text.replace(chr_, word[chr_])
    print(f'#{test_case} {text}')

    # 모음을 딕셔너리로 정리하고 입력값안에 딕셔너리가 존재하면 빈칸으로
    # raplace하는 방식으로 코드를 작성하였습니다.