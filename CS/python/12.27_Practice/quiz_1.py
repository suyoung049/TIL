siet = 'http://google.com'

passowrd = siet[7:]

passowrd = passowrd[:-4]

passowrd = passowrd[:3] + str(len(passowrd)) + str(passowrd.count("e")) + "!"

print(passowrd)

url = 'http://naver.com'
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]
