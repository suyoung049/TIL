n = 626331

con_ = 0

answer = 0

while True:

    if n == 1:
        break

    if con_ > 500:
        break

    elif n % 2 == 0:
        n = n//2
        con_ += 1

    elif n % 2 != 0:
        n = (n*3) + 1
        con_ += 1



    

if con_ == 0:
    answer = 0

elif con_ == 501:
    answer = -1

else:
    answer = con_

print(answer)
