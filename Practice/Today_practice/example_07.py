number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1             # 들여쓰기가 제대로 되지 않아서 count가 제대로 되지 않음

print(total/count)  #'//' 몫을 나타내는 기호 '/'로 변경해주어야 한다.