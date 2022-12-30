from random import*
users = range(1, 21)
list_ = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
lsit_ = list(users)

shuffle(list_)

checken = sample(list_,1)

coffie = sample(list_,3)

while True:
    if checken in coffie:
        coffie = sample(list_, 3)
    
    else:
        break

print(checken)
print(coffie)

winners = sample(lsit_, 4)

print('{}' .format(winners[0]))