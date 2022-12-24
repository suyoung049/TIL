id_pw = ["rabbit04", "98761"]
db = [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]
check = False

for data in db:
    
    if id_pw[0] == data[0]:
        check = True
        if id_pw[1] == data[1]:

            print('login')
            break
        
        else:
            print("wrong pw")
            break
    
    else:
        continue

if check == False:
    print('fail')
        


        
