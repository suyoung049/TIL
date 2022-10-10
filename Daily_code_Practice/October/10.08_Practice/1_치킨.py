chicken = 1081
cupon = 0
eat = 0


while True:
    a = chicken//10
    b = chicken % 10
    eat += a
    chicken = a+b

    if chicken < 10:
        break

print(eat)

    
