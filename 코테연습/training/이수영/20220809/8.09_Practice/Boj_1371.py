import sys

sys.stdin = open("1371_input.txt", "r")

text = sys.stdin.read()

chr_list = [0] *26 # a 부터 z 까지 수 (97~ 122)

for chr_ in text:
    if chr_.islower(): # 소문자만 탐색 개행이나 빈칸은 생략
        chr_list[ord(chr_)-97] += 1   # a의 아스키코드가 97부터 시작
for i in range(len(chr_list)):
    if chr_list[i] == max(chr_list):
        print(chr(97+i), end ='') # 나오는 문자의 수가 겹쳐도 index로 조절하기 때문에 
                                  # a, b, c 순으로 출력 